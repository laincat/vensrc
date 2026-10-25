import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, readFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";

process.env.VENERA_RUNTIME_DATA_DIR = await mkdtemp(path.join(tmpdir(), "venera-bridge-"));
const { default: runtime } = await import("venera-runtime");
const { runtimeImages } = await import("venera-runtime/platform");
const { installClientProfile } = await import("./client_bridge.mjs");

for (const [name, version] of [["venerax", "2.3.6"], ["venera-next", "1.18.0"]]) {
  test(`${name}: 绅士漫画导入顺序及真实 bootstrap 的字节正文转换`, async () => {
    process.env.VENERA_CLIENT_PROFILE = name;
    const globals = runtime.createVeneraRuntime();
    const requests = [];
    let shelfBody = "<!doctype html><title>我的書架-紳士漫畫移動版</title><div>我的書架</div>";
    globals.Network = { ...globals.Network, sendRequest: async (...args) => {
      requests.push(args);
      return {
        status: 200, headers: {},
        body: new TextEncoder().encode(shelfBody),
      };
    }};
    await installClientProfile(globals, runtime, runtimeImages);
    const code = await readFile(new URL("./wnacg.import.js", import.meta.url), "utf8");
    const fixedUrl = 'url: "https://www.wnacg.com/users-login.html"';
    assert.ok(code.includes(fixedUrl));
    // 重现 1.2.0 的导入错误；只在测试夹具中恢复提前读取设置的调用。
    const broken = code.replace(fixedUrl, 'url: source.loadSetting("domain")');
    const previous = runtime.loadVeneraConfigBySourceCode(broken, globals, false);
    assert.throws(() => globals.__clientSourceLoaded(previous),
      /Native source is unavailable during account configuration parsing/);
    delete globals.ComicSource.sources.wnacg;
    const source = runtime.loadVeneraConfigBySourceCode(code, globals, false);
    assert.doesNotThrow(() => globals.__clientSourceLoaded(source));
    assert.equal(source.version, "1.3.4");
    assert.equal(source.minAppVersion, "1.3.4");
    assert.equal(source.account.loginWithWebview.url, "https://www.wnacg.com/users-login.html");
    assert.equal(source.baseUrl, "https://www.wnacg.com");
    assert.equal(typeof source.settings.copyCookies.callback, "function");
    assert.equal(typeof source.settings.importCookies.callback, "function");
    assert.equal(typeof source.settings.loginStatus.callback, "function");
    assert.equal(source.account.loginWithWebview.checkStatus(
      "https://www.wnacg.com/users-users_fav.html", "我的書架-紳士漫畫移動版"), true);
    assert.equal(await source._checkSession(source.baseUrl), true);
    assert.equal(requests[0][1], "https://www.wnacg.com/users-users_fav.html");
    assert.equal(requests[0][2]["cache-time"], "no");
    shelfBody += "<div>您沒有權限，需要登錄</div>";
    await assert.rejects(source._checkSession(source.baseUrl), /会员会话未验证/);
  });
  test(`${name}: 发布页解析、备用发布页、每日同步及失败保留缓存`, async () => {
    process.env.VENERA_CLIENT_PROFILE = name;
    const globals = runtime.createVeneraRuntime();
    const requests = [];
    let unavailable = false;
    const html = `<title>紳士漫畫地址發布頁</title><ul>
      <li>紳士漫畫最新地址 <a href="https://www.wn003.cfd/">一</a></li>
      <li>紳士漫畫最新地址 <a href="https://www.wn004.cfd/">二</a></li>
      <li>紳士漫畫最新地址 <a href="https://www.wn005.cfd/">新</a>
        <a href="https://www.wn005.cfd/">重复</a>
        <a href="https://www.wn006.cfd.evil.invalid/">假</a>
        <a href="https://user@www.wn007.cfd/">凭据</a>
        <a href="http://www.wn008.cfd/">非 HTTPS</a>
        <a href="https://www.wn009.cfd:8080/">端口</a>
        <a href="https://www.wn010.cfd/path">非首页</a></li>
      <li>发布页 <a href="https://wnacg02.link/">发布页</a></li>
      <li>其他 <a href="https://www.wn011.cfd/">非地址栏</a></li></ul>`;
    globals.Network = { ...globals.Network, sendRequest: async (_method, url) => {
      requests.push(url);
      return url === "https://wnacg01.link/" || unavailable
        ? { status: 503, body: "" } : { status: 200, body: html };
    }};
    await installClientProfile(globals, runtime, runtimeImages);
    const code = await readFile(new URL("./wnacg.import.js", import.meta.url), "utf8");
    const source = runtime.loadVeneraConfigBySourceCode(code, globals, false);
    globals.__clientSourceLoaded(source);
    for (const key of ["mirrorCache", "activeDomain"]) await source.deleteData(key);
    assert.deepEqual(source._parseDomains(html),
      ["www.wn003.cfd", "www.wn004.cfd", "www.wn005.cfd"]);
    assert.throws(() => source._parseDomains("<title>Just a moment...</title>"), /标题不符/);
    assert.throws(() => source._parseDomains("<title>紳士漫畫地址發布頁</title>"), /没有可接受/);
    await source.init();
    assert.deepEqual(requests, ["https://wnacg01.link/", "https://wnacg02.link/"]);
    assert.ok(source._domains().includes("www.wn005.cfd"));
    assert.equal(source.loadData("activeDomain"), undefined);
    const checkedAt = source.loadData("mirrorCache").checkedAt;
    await source.init();
    assert.equal(requests.length, 2);
    unavailable = true;
    await assert.rejects(source._refreshDomains(), /两个发布页均未能同步/);
    assert.equal(source.loadData("mirrorCache").checkedAt, checkedAt);
    assert.ok(source._domains().includes("www.wn005.cfd"));
    for (const key of ["mirrorCache", "activeDomain"]) await source.deleteData(key);
  });
  test(`${name}: 真实 bootstrap、HTML、加密、版本检查与逐像素重排`, async () => {
    process.env.VENERA_CLIENT_PROFILE = name;
    const globals = runtime.createVeneraRuntime();
    const requests = [];
    globals.Network = { ...globals.Network, sendRequest: async (...args) => {
      requests.push(args);
      if (args[1].endsWith("/challenge"))
        return { status: 403, headers: { "Cf-Mitigated": "challenge" }, body: "fixture" };
      if (args[1].endsWith("/forbidden"))
        return { status: 403, headers: {}, body: "forbidden" };
      return { status: 200, headers: {}, body: "response" };
    }};
    await installClientProfile(globals, runtime, runtimeImages);
    assert.equal(globals.APP.version, version);
    assert.equal(runtime.APP.version, "1.6.3");
    const sourceCode = `class Fixture extends ComicSource {
      name="fixture"; key="fixture"; version="1.0.0"; minAppVersion="1.16.0";
      settings={dailyCheckInTask:{type:"switch",default:false}};
      isAppVersionAfter() { return false; }
    }`;
    const source = runtime.loadVeneraConfigBySourceCode(sourceCode, globals, false);
    globals.__clientSourceLoaded?.(source);
    assert.equal(source.isAppVersionAfter("1.16.0"), name === "venerax");
    if (name === "venerax") assert.equal(source.isAppVersionAfter("99.0.0"), false);
    const numericKey = runtime.loadVeneraConfigBySourceCode(
      sourceCode.replace('key="fixture"', 'key="18fixture"'), globals, false);
    assert.throws(() => globals.__clientSourceLoaded(numericKey),
      name === "venera-next" ? /key 18fixture is invalid/ : SyntaxError);
    assert.equal(source.loadSetting("dailyCheckInTask"), false);
    source.saveData("fixture", "value");
    assert.equal(source.loadData("fixture"), "value");
    if (name === "venera-next") {
      globals.ComicSource.sources.fixture = new globals.ComicSource();
      assert.throws(() => source.loadData("fixture"), /replaced/);
      globals.ComicSource.sources.fixture = source;
    }
    assert.throws(() => runtime.loadVeneraConfigBySourceCode(
      sourceCode.replace('minAppVersion="1.16.0"', 'minAppVersion="99.0.0"'),
      globals, false), /minAppVersion 99.0.0/);
    assert.throws(() => runtime.loadVeneraConfigBySourceCode(
      sourceCode, runtime.createVeneraRuntime(), false), /minAppVersion 1.16.0/);
    const bytes = globals.Convert["encode" + "Utf8"]("1234567890123456");
    assert.equal(globals.Convert.hexEncode(globals.Convert["m" + "d5"](bytes)),
      runtime.Convert.hexEncode(runtime.Convert["m" + "d5"](bytes)));
    const encrypted = runtime.Convert.encryptAesEcb(bytes, bytes);
    assert.equal(globals.Convert.decodeUtf8(globals.Convert.decryptAesEcb(encrypted, bytes)),
      "1234567890123456");
    const cbc = globals.Convert.encryptAesCbc(bytes, bytes, bytes);
    assert.equal(globals.Convert.decodeUtf8(globals.Convert.decryptAesCbc(cbc, bytes, bytes)),
      "1234567890123456");
    assert.equal(globals.Convert.hmacString(bytes, bytes, "sha256"),
      runtime.Convert.hmacString(bytes, bytes, "sha256"));
    const document = new globals.HtmlDocument('<main id="root"><p class="a">你好<b>x</b></p><p>next</p></main>');
    const paragraph = document.querySelector("p");
    assert.ok(paragraph instanceof globals.HtmlElement);
    assert.equal(paragraph.text, "你好x");
    assert.deepEqual(paragraph.attributes, { class: "a" });
    assert.equal(paragraph.children[0].localName, "b");
    assert.equal(paragraph.nextElementSibling.text, "next");
    assert.equal(document.getElementById("root").querySelectorAll("p").length, 2);
    assert.equal(paragraph.nodes[0].type, "text");
    assert.throws(() => paragraph.nodes[1].toElement(), /differs from Dart/);
    document.dispose();
    assert.throws(() => document.querySelector("p"), /unavailable/);
    assert.match(globals.createUuid(), /^[a-f0-9-]{36}$/);
    assert.equal(globals.randomInt(5, 6), 5);
    assert.equal(await globals.compute("(x,y) => x+y", 2, 3), 5);
    assert.throws(() => globals.compute(() => 1), /function string/);
    await globals.Network.post("https://fixture.invalid/", { Test: "header" }, "payload");
    assert.deepEqual(requests[0].slice(0, 2), ["POST", "https://fixture.invalid/"]);
    assert.equal(requests[0][3], "payload");
    await assert.rejects(globals.Network.get("https://fixture.invalid/challenge"),
      (error) => error.category === "anti_bot");
    assert.equal((await globals.Network.get("https://fixture.invalid/forbidden")).status, 403);
    const sharp = (await import("sharp")).default;
    const png = await sharp(Buffer.from([255, 0, 0, 0, 255, 0, 0, 0, 255]),
      { raw: { width: 1, height: 3, channels: 3 } }).png().toBuffer();
    const result = await globals.__modifyImage(png, `
      function modifyImage(image) {
        let res=Image.empty(1,3);
        for(let y=0;y<3;y++) res.fillImageRangeAt(0,y,image,0,2-y,1,1);
        return res;
      }`);
    const pixels = await sharp(Buffer.from(result)).removeAlpha().raw().toBuffer();
    assert.deepEqual([...pixels], [0, 0, 255, 0, 255, 0, 255, 0, 0]);
    assert.throws(() => new globals.Comic({ id: "1" }).noSuchMethod(), TypeError);
  });
}
