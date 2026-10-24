import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const code = readFileSync(new URL("../sources/wnacg.js", import.meta.url), "utf8");

function fixture(response, domain = "www.wnacg.com") {
  const calls = [];
  let cookies = [{ name: "old_session", value: "test-only", domain }];
  const sandbox = {
    ComicSource: class { loadSetting() { return domain; } },
    Cookie: function (values) { Object.assign(this, values); },
    Network: {
      getCookies: async () => cookies,
      deleteCookies: async (url) => { calls.push(["delete", url]); cookies = []; },
      setCookies: async (url, values) => { calls.push(["set", url]); cookies = values; },
      get: async (url) => {
        calls.push(["get", url]);
        if (response instanceof Error) throw response;
        return response;
      },
    },
  };
  const source = vm.runInNewContext(`${code}\nnew Wnacg()`, sandbox);
  return { source, calls, cookies: () => cookies };
}

test("Cookie 验证仅接受会员页的明确登录标志，保留最低版本", async () => {
  const { source, calls, cookies } = fixture({
    status: 200, body: '<a href="/users-logout.html">退出</a>',
  });
  assert.equal(source.version, "1.1.0");
  assert.equal(source.minAppVersion, "1.0.0");
  assert.equal(source.account.login, undefined);
  assert.equal(source.account.loginWithWebview, undefined);
  assert.equal(await source.account.loginWithCookies.validate(["Cookie: session=test-only; flag=x=y"]), true);
  assert.equal(cookies().length, 2);
  assert.equal(cookies()[1].value, "x=y");
  assert.deepEqual(calls.filter(([operation]) => operation === "get"),
    [["get", "https://www.wnacg.com/users-index.html"]]);
});

test("匿名 HTTP 200、登录页、权限提示及 CF 页面均不能通过；失败恢复旧会话", async () => {
  for (const response of [
    { status: 200, body: '<a href="/users-login.html">登录</a>' },
    { status: 200, body: "紳士漫畫" },
    { status: 200, body: '<a href="/users-logout.html">退出</a>您沒有權限，需要登錄！' },
    { status: 403, body: '<a href="/users-logout.html">退出</a>' },
    { status: 403, headers: { "Cf-Mitigated": "challenge" }, body: "challenge" },
    { status: 200, body: '<script src="/cdn-cgi/challenge-platform/test"></script>' },
    new Error("test-only network failure"),
  ]) {
    const { source, cookies } = fixture(response);
    await assert.rejects(source.account.loginWithCookies.validate(["session=test-only"]));
    assert.equal(cookies()[0].name, "old_session");
  }
});

test("拒绝多行、重复 Cookie、Set-Cookie 和任意域名，且不发请求", async () => {
  for (const value of [
    "", "session=x\r\nInjected: x", "session=x; session=y", "session=x; Path=/",
    "session=x; Secure", "password", "session=contains space", "x".repeat(16385),
  ]) {
    const { source, calls } = fixture({ status: 200, body: "" });
    await assert.rejects(source.account.loginWithCookies.validate([value]));
    assert.equal(calls.length, 0);
  }
  const { source, calls } = fixture({}, "other.invalid");
  await assert.rejects(source.account.loginWithCookies.validate(["session=test-only"]));
  assert.equal(calls.length, 0);
});

test("备用域名仅接收本域会话；登出清理两个受支持域名", async () => {
  const { source, calls, cookies } = fixture({
    status: 200, body: '<a href="https://www.wnacg.ru/users-logout.html">退出</a>',
  }, "www.wnacg.ru");
  await source.account.loginWithCookies.validate(["session=test-only"]);
  assert.equal(cookies()[0].domain, "www.wnacg.ru");
  assert.ok(calls.every(([, url]) => url.startsWith("https://www.wnacg.ru")));
  await source.account.logout();
  assert.deepEqual(calls.slice(-2), [
    ["delete", "https://www.wnacg.com"], ["delete", "https://www.wnacg.ru"],
  ]);
});
