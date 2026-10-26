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
    assert.equal(source.version, "1.4.0");
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
  test(`${name}: 绅士漫画移动版首页、搜索、详情、连载分页及收藏结构回归`, async () => {
    process.env.VENERA_CLIENT_PROFILE = name;
    const globals = runtime.createVeneraRuntime();
    // 匿名真实页面提取的 DOM，标题和地址置换；收藏仅为结构用例，不代表会员实测。
    const entry = `<li><a class="ImgA" href="/photos-index-aid-397513.html">
      <img src="//covers.invalid/397513.webp"></a><a class="txtA">固定样本</a>
      <span class="info">2026-10-26, 131P</span></li>`;
    const list = `<div class="imgBox"><div class="Sub_H2"><span class="Title">最新上架</span>
      <a href="albums.html">更多</a></div><ul>${entry}
      ${entry.replace("/photos-index-aid-397513.html", "/link-index-aid-2.html")}
      ${entry.replace("/photos-index-aid-397513.html", "https://advert.invalid/")}
      </ul></div>`;
    const detail = `<div class="Introduct"><div id="comicName">固定样本</div>
      <div id="Cover"><img src="////covers.invalid/397513.webp"></div>
      <div class="sub_r"><a class="introName">投稿者</a><a href="/albums-index-cate-1.html">分类</a>
      <span class="date">131P · 收藏 1</span></div><div class="dv-desc-text">简介</div></div>`;
    const shelfTitle = "<title>我的書架-紳士漫畫移動版</title>";
    let shelf = shelfTitle + list;
    let detailBody = detail;
    const requests = [];
    globals.Network = { ...globals.Network, sendRequest: async (_method, url, headers) => {
      requests.push({ url, headers });
      let body = url.includes("users-") ? shelf
        : url.includes("photos-gallery-") ? String.raw`document.writeln("var imglist=[{url:\"//images.invalid/1.webp\",caption:\"[001]\"}];");`
        : url.includes("photos-index-") ? detailBody
        : (url.includes("favorite_ranking")
          ? `<div class="rand_rq"><div class="itemBox"><div class="itemImg">
            <a href="/photos-index-aid-397513.html"><img src="//covers.invalid/397513.webp"></a></div>
            <div class="itemTxt"><a class="title">固定样本</a><span class="date">日期</span></div></div></div>`
          : url.includes("/search/")
          ? list.replaceAll('</a><a class="txtA">固定样本</a>', '<span>固定样本</span></a>')
          : list) + `<div class="page"><span class="thispage">1</span>
          <a href="/albums-index-page-30.html">30</a><a href="/albums-index-page-2.html">後頁&gt;</a></div>`;
      if (url.includes("page-2-aid-390033")) body = detail +
        `<ul id="dv-ch-list"><li data-chid="398836"><a title="第 2 話">2</a></li></ul>`;
      return { status: 200, headers: {}, body: new TextEncoder().encode(body) };
    }};
    await installClientProfile(globals, runtime, runtimeImages);
    const code = await readFile(new URL("./wnacg.import.js", import.meta.url), "utf8");
    const source = runtime.loadVeneraConfigBySourceCode(code, globals, false);
    globals.__clientSourceLoaded(source);
    const home = await source.explore[0].load(1);
    assert.equal(home[0].comics[0].id, "397513");
    assert.equal(home[0].viewMore, "category:最新上架@/albums.html");
    const category = await source.categoryComics.load("最新", "/albums.html", [], 1);
    assert.equal(category.comics.length, 1);
    assert.equal(category.maxPage, 30);
    const search = await source.search.load("火影", [], 1);
    assert.equal(search.comics.length, 1);
    assert.equal(search.maxPage, 30);
    const ranking = await source.categoryComics.ranking.load("day", 1);
    assert.equal(ranking.comics.length, 1);
    assert.equal(ranking.maxPage, 30);
    const info = await source.comic.loadInfo("397513");
    assert.equal(info.title, "固定样本");
    assert.equal(info.cover, "https://covers.invalid/397513.webp");
    assert.equal(info.uploader, "投稿者");
    const thumbnails = await source.comic.loadThumbnails("397513", null);
    assert.deepEqual(thumbnails.thumbnails, ["https://images.invalid/1.webp"]);
    const favorites = await source.favorites.loadComics(1, null);
    assert.equal(favorites.comics.length, 1);
    assert.equal(favorites.comics[0].id, "397513");
    await assert.rejects(source.favorites.addOrDelFavorite("397513", null, false, undefined), /收藏编号/);
    shelf = shelfTitle + "<div class='imgBox'></div>";
    await assert.rejects(source.favorites.loadComics(1, null), /结构尚未识别/);
    shelf = shelfTitle + "<div class='imgBox'>尚未收藏</div>";
    assert.equal((await source.favorites.loadComics(1, null)).comics.length, 0);
    shelf = shelfTitle + list + "<div>您沒有權限，需要登錄</div>";
    await assert.rejects(source.favorites.loadComics(1, null), /会员会话未验证/);
    detailBody = detail + `<ul id="dv-ch-list"><li data-chid="357560"><a title="第 1 話">1</a></li></ul>
      <div id="dv-ch-more" data-total="2" data-limit="1"></div>`;
    const series = await source.comic.loadInfo("390033");
    assert.equal(series.chapters.size, 2);
    assert.deepEqual([...series.chapters.keys()], ["357560", "398836"]);
    assert.ok(requests.some(request => request.url.includes("page-2-aid-390033")));
    assert.ok(requests.filter(request => request.url.includes("users-"))
      .every(request => request.headers["cache-time"] === "no"));
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
