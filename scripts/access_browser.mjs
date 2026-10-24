import { readFile, writeFile } from "node:fs/promises";
import { chromium } from "@playwright/test";

const [input, output] = process.argv.slice(2);
const targets = JSON.parse(await readFile(input, "utf8")).targets;
const browser = await chromium.launch({ headless: true });
const results = [];
try {
  for (const target of targets) {
    const url = new URL(target.url);
    if (url.protocol !== "https:" || url.pathname !== "/" || url.search || url.username)
      throw new Error("Only reviewed HTTPS origins are allowed");
    const context = await browser.newContext();
    const page = await context.newPage();
    let challengeHeader = false;
    let navigationStatus = null;
    page.on("response", (response) => {
      if (response.request().isNavigationRequest() && response.frame() === page.mainFrame())
        navigationStatus = response.status();
      if (response.url().startsWith(url.origin + "/") &&
          response.headers()["cf-mitigated"] === "challenge") challengeHeader = true;
    });
    await context.route("**/*", (route) => ["image", "media", "font"].includes(
      route.request().resourceType()) ? route.abort() : route.continue());
    const result = { key: target.key, origin: url.origin, status: "network_failed" };
    try {
      const response = await page.goto(target.url, { waitUntil: "domcontentloaded", timeout: 30000 });
      result.httpStatus = response?.status() ?? null;
      for (let attempt = 0; attempt < 4; attempt++) {
        result.httpStatus = navigationStatus ?? result.httpStatus;
        const body = await page.locator("body").innerText({ timeout: 5000 });
        const challenge = /checking your browser|just a moment|verify (?:that )?you are human|security verification|请完成人机验证/i.test(
          await page.title() + "\n" + body) ||
          await page.locator('iframe[src*="challenges.cloudflare.com"]').count() > 0;
        const hasContent = body.length >= 200 && await page.locator("a[href]").count() >= 3;
        if (new URL(page.url()).origin !== url.origin) {
          result.status = "redirect_unconfirmed";
          break;
        }
        if (!challenge && hasContent && Number.isInteger(result.httpStatus) &&
            result.httpStatus >= 200 && result.httpStatus < 400) {
          result.status = "browser_accessible";
          break;
        }
        if (challenge || challengeHeader) result.status = "manual_verification_required";
        else if (result.httpStatus >= 400) result.status = "http_blocked";
        else result.status = "content_unconfirmed";
        // 只等待正常浏览器脚本执行；不点击验证码、不使用识别或代解服务。
        if (attempt < 3 && result.status === "manual_verification_required")
          await page.waitForTimeout(3000);
        else break;
      }
      result.cloudflareHeaderObserved = challengeHeader;
    } catch {
      // 不发布页面文本、原始错误、Cookie 或浏览器存储。
    } finally {
      await context.close();
    }
    results.push(result);
    console.log(`浏览器公开访问诊断：${target.key} ${result.status}`);
  }
} finally {
  await browser.close();
}
await writeFile(output, JSON.stringify({
  schemaVersion: 1, browserCliCommit: process.env.BROWSER_CLI_COMMIT, results,
}, null, 2) + "\n");
