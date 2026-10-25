import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const code = readFileSync(new URL("../sources/wnacg.js", import.meta.url), "utf8");

function fixture(response, domain = "www.wnacg.com", selection = null) {
  const calls = [];
  const messages = [];
  const data = new Map();
  let clipboard = "";
  let cookies = [{ name: "old_session", value: "test-only", domain }];
  const sandbox = {
    ComicSource: class {
      loadSetting() { return domain; }
      loadData(key) { return data.get(key); }
      saveData(key, value) { data.set(key, value); }
      deleteData(key) { data.delete(key); }
    },
    Cookie: function (values) { Object.assign(this, values); },
    UI: {
      showMessage: (message) => messages.push(message),
      showSelectDialog: async () => selection,
    },
    setClipboard: async (text) => { clipboard = text; },
    Network: {
      getCookies: async () => cookies.filter((cookie) => {
        const candidate = String(cookie.domain || "").replace(/^\./, "");
        return !candidate || domain === candidate || domain.endsWith(`.${candidate}`);
      }),
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
  return { source, calls, cookies: () => cookies, messages, clipboard: () => clipboard, data };
}

test("Cookie 验证仅接受会员页的明确登录标志，网页登录只在会员中心成立", async () => {
  const { source, calls, cookies } = fixture({
    status: 200, body: '<a href="/users-logout.html">退出</a>',
  });
  assert.equal(source.version, "1.3.0");
  assert.equal(source.minAppVersion, "1.3.4");
  assert.equal(source.account.login, undefined);
  assert.equal(source.account.loginWithWebview.url, "https://www.wnacg.com/users-login.html");
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-index.html", "用戶中心 紳士漫畫"), true);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-index.html", "您沒有權限，需要登錄！"), false);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://evil.invalid/users-index.html", "用戶中心 紳士漫畫"), false);
  assert.equal(await source.account.loginWithCookies.validate(["Cookie: session=test-only; flag=x=y"]), true);
  assert.equal(cookies().length, 2);
  assert.equal(cookies()[1].value, "x=y");
  assert.deepEqual(calls.filter(([operation]) => operation === "get"),
    [["get", "https://www.wnacg.com/users-index.html"]]);
});

test("获取 Cookie 先验证会员会话，再仅复制到剪贴板且不在界面显示", async () => {
  const { source, calls, messages, clipboard, cookies } = fixture({
    status: 200, body: '<a href="/users-logout.html">退出</a>',
  });
  cookies().push({ name: "shared", value: "parent-domain", domain: ".wnacg.com" });
  cookies().push({ name: "wrong", value: "other-domain", domain: ".wnacg.ru" });
  await source.settings.copyCookies.callback();
  assert.equal(clipboard(), "old_session=test-only; shared=parent-domain");
  assert.ok(messages.every((message) => !message.includes("test-only")));
  assert.deepEqual(calls.filter(([operation]) => operation === "get"),
    [["get", "https://www.wnacg.com/users-index.html"]]);
  const anonymous = fixture({ status: 200, body: '<a href="/users-login.html">登录</a>' }).source;
  await assert.rejects(anonymous.settings.copyCookies.callback(), /会员会话未验证/);
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
  const { source: invalid, calls } = fixture({}, "other.invalid");
  assert.throws(() => invalid.baseUrl, /请选择内置或发布页公布的绅士漫画域名/);
  await assert.rejects(invalid.account.loginWithCookies.validate(["session=test-only"]));
  assert.equal(calls.length, 0);
});

test("内置发布页备用地址；切换地址清除登录标记，且不迁移 Cookie", async () => {
  const { source, calls, data, cookies } = fixture({}, "www.wnacg.com", 2);
  data.set("account", "test-only");
  assert.ok(source._domains().includes("www.wn003.cfd"));
  assert.ok(source._domains().includes("www.wn004.cfd"));
  await source.settings.domain.callback();
  assert.equal(source.baseUrl, "https://www.wn003.cfd");
  assert.equal(data.has("account"), false);
  assert.equal(cookies()[0].domain, "www.wnacg.com");
  assert.equal(calls.length, 0);
  for (const selection of [null, -1, 99, "2", 0]) {
    const cancelled = fixture({}, "www.wnacg.com", selection);
    cancelled.data.set("account", "test-only");
    await cancelled.source.settings.domain.callback();
    assert.equal(cancelled.data.get("account"), "test-only");
    assert.equal(cancelled.data.has("activeDomain"), false);
  }
});

test("备用地址会话仅验证当前域名，拒绝其他域名的退出链接", async () => {
  for (const [href, valid] of [
    ["/users-logout.html", true],
    ["https://www.wn003.cfd/users-logout.html", true],
    ["https://www.wn004.cfd/users-logout.html", false],
    ["https://www.wn003.cfd.evil.invalid/users-logout.html", false],
  ]) {
    const { source } = fixture({ status: 200, body: `<a href="${href}">退出</a>` }, "www.wn003.cfd");
    if (valid) assert.equal(await source._checkSession(source.baseUrl), true);
    else await assert.rejects(source._checkSession(source.baseUrl));
  }
});

test("备用域名仅接收本域会话；登出清理主域名及缓存备用域名", async () => {
  const { source, calls, cookies } = fixture({
    status: 200, body: '<a href="https://www.wnacg.ru/users-logout.html">退出</a>',
  }, "www.wnacg.ru");
  assert.equal(source.account.loginWithWebview.url, "https://www.wnacg.com/users-login.html");
  await source.account.loginWithCookies.validate(["session=test-only"]);
  assert.equal(cookies()[0].domain, "www.wnacg.ru");
  assert.ok(calls.every(([, url]) => url.startsWith("https://www.wnacg.ru")));
  await source.account.logout();
  assert.deepEqual(calls.slice(-4), [
    ["delete", "https://www.wnacg.com"], ["delete", "https://www.wnacg.ru"],
    ["delete", "https://www.wn003.cfd"], ["delete", "https://www.wn004.cfd"],
  ]);
});
