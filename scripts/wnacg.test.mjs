import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const code = readFileSync(new URL("../sources/wnacg.js", import.meta.url), "utf8");

function fixture(response, domain = "www.wnacg.com", selection = null) {
  const calls = [];
  const messages = [];
  const dialogs = [];
  const requestHeaders = [];
  const data = new Map();
  let clipboard = "";
  let cookies = [{ name: "old_session", value: "test-only", domain }];
  const sandbox = {
    APP: { webviewCookieCapture: true },
    ComicSource: class {
      loadSetting() { return domain; }
      loadData(key) { return data.get(key); }
      saveData(key, value) { data.set(key, value); }
      deleteData(key) { data.delete(key); }
    },
    Cookie: function (values) { Object.assign(this, values); },
    Convert: {
      decodeUtf8: (value) => new TextDecoder().decode(Array.isArray(value) ? Uint8Array.from(value) : value),
    },
    UI: {
      showMessage: (message) => messages.push(message),
      showDialog: (title, content) => dialogs.push([title, content]),
      showSelectDialog: async () => selection,
    },
    setClipboard: async (text) => { clipboard = text; },
    getClipboard: async () => clipboard,
    Network: {
      getCookies: () => cookies.filter((cookie) => {
        const candidate = String(cookie.domain || "").replace(/^\./, "");
        return !candidate || domain === candidate || domain.endsWith(`.${candidate}`);
      }),
      deleteCookies: async (url) => { calls.push(["delete", url]); cookies = []; },
      setCookies: async (url, values) => { calls.push(["set", url]); cookies = values; },
      get: async (url, headers) => {
        calls.push(["get", url]);
        requestHeaders.push(headers);
        if (response instanceof Error) throw response;
        return response;
      },
    },
  };
  const source = vm.runInNewContext(`${code}\nnew Wnacg()`, sandbox);
  return {
    app: sandbox.APP,
    source, calls, cookies: () => cookies, messages, dialogs, requestHeaders, data,
    clipboard: () => clipboard,
    setClipboard: (text) => { clipboard = text; },
  };
}

test("Cookie 验证仅接受会员页的明确登录标志，网页登录只在会员中心成立", async () => {
  const { source, calls, cookies } = fixture({
    status: 200, body: '<a href="/users-logout.html">退出</a>',
  });
  assert.equal(source.version, "1.3.3");
  assert.equal(source.minAppVersion, "1.3.4");
  assert.equal(source.account.login, undefined);
  assert.equal(source.account.loginWithWebview.url, "https://www.wnacg.com/users-login.html");
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-index.html", "我的空間 紳士漫畫"), true);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-index.html", "您沒有權限，需要登錄！"), false);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-index.html", ""), false);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-users_fav.html", "我的空间 紳士漫畫"), true);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://evil.invalid/users-index.html", "用戶中心 紳士漫畫"), false);
  assert.equal(await source.account.loginWithCookies.validate(["Cookie: session=test-only; flag=x=y"]), true);
  assert.equal(cookies().length, 2);
  assert.equal(cookies()[1].value, "x=y");
  assert.deepEqual(calls.filter(([operation]) => operation === "get"),
    [["get", "https://www.wnacg.com/users-users_fav.html"]]);
});

test("获取 Cookie 先验证会员会话，再自动登录并复制到剪贴板", async () => {
  const { source, calls, messages, clipboard, cookies, data } = fixture({
    status: 200, body: '<a href="/users-logout.html">退出</a>',
  });
  cookies().push({ name: "shared", value: "parent-domain", domain: ".wnacg.com" });
  cookies().push({ name: "wrong", value: "other-domain", domain: ".wnacg.ru" });
  await source.settings.copyCookies.callback();
  assert.equal(data.get("account"), "ok");
  assert.equal(clipboard(), "old_session=test-only; shared=parent-domain");
  assert.ok(messages.every((message) => !message.includes("test-only")));
  assert.deepEqual(calls.filter(([operation]) => operation === "get"),
    [["get", "https://www.wnacg.com/users-users_fav.html"]]);
  const anonymous = fixture({ status: 200, body: '<a href="/users-login.html">登录</a>' }).source;
  await assert.rejects(anonymous.settings.copyCookies.callback(), /会员会话未验证/);
});

test("从剪贴板自动填入 Cookie，验证成功后登录并清空剪贴板", async () => {
  const { source, data, clipboard, cookies, messages, setClipboard } = fixture({
    status: 200, body: '<a href="/users-logout.html">退出</a>',
  });
  setClipboard("Cookie: session=copied; extra=x=y");
  await source.settings.importCookies.callback();
  assert.equal(data.get("account"), "ok");
  assert.equal(cookies().length, 2);
  assert.equal(clipboard(), "");
  assert.ok(messages.every((message) => !message.includes("copied")));
  const anonymous = fixture({ status: 200, body: '<a href="/users-login.html">登录</a>' });
  anonymous.setClipboard("session=copied");
  await assert.rejects(anonymous.source.settings.importCookies.callback(), /会员会话未验证/);
  assert.equal(anonymous.cookies()[0].name, "old_session");
});

test("网页登录回调只保存已通过会员页校验的主域名会话", async () => {
  const good = fixture({ status: 200, body: '<a href="/users-logout.html">退出</a>' });
  good.data.set("activeDomain", "www.wnacg.ru");
  await good.source.account.loginWithWebview.onLoginSuccess();
  assert.equal(good.data.has("account"), false);
  assert.equal(good.data.get("activeDomain"), "www.wnacg.ru");
  assert.equal(good.source.accountBaseUrl, "https://www.wnacg.com");
  assert.equal(good.data.get("webLoginVerification"), "http_verified");

  const bad = fixture({ status: 200, body: '<a href="/users-login.html">登录</a>' });
  bad.data.set("account", "stale");
  await assert.rejects(bad.source.account.loginWithWebview.onLoginSuccess(), /会员会话未验证/);
  assert.equal(bad.data.get("account"), "stale");
  assert.equal(bad.cookies()[0].name, "old_session");
});

test("原版客户端按真实私有页触发同步 Cookie 导入，不把导入当 HTTP 验证", () => {
  const { source, app, data, messages } = fixture({});
  app.webviewCookieCapture = false;
  assert.equal(source.account.loginWithWebview.captureCookies, false);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-index.html", "用戶中心"), false);
  assert.equal(source.account.loginWithWebview.checkStatus(
    "https://www.wnacg.com/users-users_fav.html", "我的空间 紳士漫畫"), true);
  assert.equal(source.account.loginWithWebview.onLoginSuccess(), undefined);
  assert.equal(data.get("webLoginOrigin"), "https://www.wnacg.com");
  assert.equal(data.get("webLoginVerification"), "browser_only");
  assert.match(messages[0], /App 已接收网页 Cookie/);
  assert.doesNotMatch(messages[0], /test-only|old_session/);
  assert.equal(data.has("account"), false);
  assert.throws(() => source.account.loginWithWebview.onLoginSuccess(), /我的收藏/);
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

test("登录状态诊断不显示 Cookie 内容且不把本地标记当成会员验证", async () => {
  const good = fixture({ status: 200, body: '<a href="/users-logout.html">退出</a>' });
  good.source.explore[0].load = async () => [{ comics: [{}] }];
  good.source.comic.loadInfo = async (id) => {
    assert.equal(id, "397513");
    return { title: "fixture" };
  };
  good.data.set("account", "ok");
  await good.source.settings.loginStatus.callback();
  assert.equal(good.dialogs.length, 1);
  assert.match(good.dialogs[0][1], /会员页验证：通过/);
  assert.match(good.dialogs[0][1], /适用于会员页的 Cookie：1 项/);
  assert.doesNotMatch(good.dialogs[0][1], /test-only/);
  assert.doesNotMatch(good.dialogs[0][1], /old_session/);
  assert.match(good.dialogs[0][1], /首页解析：通过/);
  assert.match(good.dialogs[0][1], /固定漫画详情（397513）：通过/);
  assert.equal(good.data.get("webLoginVerification"), "http_verified");

  const bad = fixture({ status: 200, body: '<a href="/users-login.html">登录</a>' });
  bad.data.set("account", "ok");
  await bad.source.settings.loginStatus.callback();
  assert.match(bad.dialogs[0][1], /会员页验证：未通过/);
  assert.match(bad.dialogs[0][1], /仅表示本地登录标记/);
  assert.equal(bad.data.get("webLoginVerification"), undefined);
});

test("兼容 VeneraX 共享缓存的字节正文，且会员 GET 显式禁用缓存", async () => {
  const value = '<a href="/users-logout.html">退出</a>';
  for (const body of [value, new TextEncoder().encode(value), Array.from(new TextEncoder().encode(value))]) {
    const { source, requestHeaders } = fixture({ status: 200, body });
    assert.equal(await source._checkSession("https://www.wnacg.com"), true);
    assert.equal(requestHeaders[0]["cache-time"], "no");
  }
  const challenged = fixture({
    status: 403, body: new TextEncoder().encode('<script src="/cdn-cgi/challenge-platform/test"></script>'),
  });
  await assert.rejects(challenged.source._checkSession("https://www.wnacg.com"), /Cloudflare/);
});

test("诊断失败不展示异常原文，且能显示阅读与登录域名差异", async () => {
  const { source, dialogs, data } = fixture(new Error("sensitive-test-only"));
  data.set("webLoginOrigin", "https://www.wnacg.com");
  data.set("activeDomain", "www.wnacg.ru");
  data.set("webLoginVerification", "http_verified");
  await source.settings.loginStatus.callback();
  assert.match(dialogs[0][1], /阅读与登录域名不同/);
  assert.doesNotMatch(dialogs[0][1], /sensitive-test-only/);
  assert.equal(data.get("webLoginVerification"), "browser_only");
});

test("诊断区分会员权限、HTTP 状态与源解析异常，且不输出异常详情", () => {
  const { source } = fixture({});
  assert.equal(source._failureSummary("Invalid Status Code 403"), "HTTP 403");
  assert.equal(source._failureSummary("会员会话未验证"), "站点未确认会员权限");
  assert.match(source._failureSummary(new TypeError("sensitive-test-only")), /源解析错误/);
  assert.doesNotMatch(source._failureSummary(new TypeError("sensitive-test-only")), /sensitive/);
});
