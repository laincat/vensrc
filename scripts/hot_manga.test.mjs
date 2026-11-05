import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const code = readFileSync(new URL("../sources/hot_manga.js", import.meta.url), "utf8");

/// 最小运行时：只实现这份源用到的 Network / loadSetting / saveData / loadData。
function fixture(routes) {
  const requests = [];
  const store = new Map();
  const settings = { apiHost: "api.2024manga.com", imageQuality: "h1500x" };
  const sandbox = {
    ComicSource: class {
      loadSetting(key) { return settings[key]; }
      loadData(key) { return store.get(key); }
      saveData(key, value) { store.set(key, value); }
      deleteData(key) { store.delete(key); }
    },
    Network: {
      get: async (url, headers) => {
        requests.push({ url, headers });
        for (const [pattern, response] of routes) {
          if (pattern.test(url)) {
            return typeof response === "function" ? response(url) : response;
          }
        }
        throw new Error(`未预期的请求：${url}`);
      },
    },
  };
  const source = vm.runInNewContext(`${code}\nnew HotManga()`, sandbox);
  return { source, requests, store, settings };
}

const json = (value) => ({ status: 200, body: JSON.stringify(value) });
/// 源码跑在 vm 沙箱里，深比较前先转成本 realm 的普通对象。
const plain = (value) => JSON.parse(JSON.stringify(value));
const ok = (results) => json({ code: 200, message: "请求成功", results });

const LIST = ok({
  total: 61, limit: 30, offset: 0,
  list: [
    { name: "藍色監獄", path_word: "bluelock", cover: "https://img/bluelock.jpg",
      author: [{ name: "金城宗幸", path_word: "金城宗幸" }, { name: "野村优介", path_word: "野村优介" }],
      theme: [{ name: "競技", path_word: "jingji" }] },
    { name: "缺字段作品" },
  ],
});

test("列表：过滤缺 ID 的条目，maxPage 由总数换算", async () => {
  const { source, requests } = fixture([[/\/api\/v3\/comics\?/, LIST]]);
  const page = await source.explore[0].load(1);
  assert.equal(page.comics.length, 1);
  assert.deepEqual(plain(page.comics[0]), {
    id: "bluelock", title: "藍色監獄", cover: "https://img/bluelock.jpg",
    subTitle: "金城宗幸 / 野村优介", description: "競技",
  });
  assert.equal(page.maxPage, 3);
  const url = requests[0].url;
  assert.match(url, /^https:\/\/api\.2024manga\.com\/api\/v3\/comics\?/);
  assert.match(url, /free_type=1/);
  assert.match(url, /limit=30/);
  assert.match(url, /offset=0/);
  assert.equal(requests[0].headers.platform, "3");
  assert.equal(requests[0].headers.webp, "1");

  const second = await source.explore[0].load(2);
  assert.equal(second.comics.length, 1);
  assert.match(requests[1].url, /offset=30/);
});

test("列表：接口没有总数时 maxPage 为 null（Venera 约定=不限页数）", async () => {
  const { source } = fixture([[/\/api\/v3\/comics\?/, ok({ list: [
    { name: "A", path_word: "a", cover: "https://img/a.jpg", author: [], theme: [] },
  ] })]]);
  const page = await source.explore[0].load(1);
  assert.equal(page.maxPage, null);
});

test("分类：主题与排序两种 param 走同一接口的不同参数", async () => {
  const { source, requests } = fixture([[/\/api\/v3\/comics\?/, LIST]]);
  await source.categoryComics.load("熱血", "rexue", [], 1);
  assert.match(requests[0].url, /theme=rexue/);
  assert.match(requests[0].url, /ordering=-datetime_updated/);
  await source.categoryComics.load("人氣最高", "-popular", [], 1);
  assert.doesNotMatch(requests[1].url, /theme=/);
  assert.match(requests[1].url, /ordering=-popular/);
  assert.equal(source.category.parts.length, 2);
  assert.equal(source.category.parts[0].categories.length, source.category.parts[0].categoryParams.length);
});

test("搜索：关键词走 search 接口；缓存过的作者名走 author 参数", async () => {
  const { source, requests, store } = fixture([
    [/\/api\/v3\/search\/comic\?/, ok({ total: 5, list: [
      { name: "熱血女兒", path_word: "rexue-nver", cover: "https://img/x.jpg", author: [], theme: [] },
    ] })],
    [/\/api\/v3\/comics\?/, LIST],
  ]);
  const byKeyword = await source.search.load("热血", [], 1);
  assert.equal(byKeyword.comics[0].id, "rexue-nver");
  assert.match(requests[0].url, /q=%E7%83%AD%E8%A1%80/);

  store.set("authorPaths", { "岸本斉史": "anbenqishi" });
  await source.search.load("岸本斉史", [], 1);
  assert.match(requests[1].url, /author=anbenqishi/);
  assert.doesNotMatch(requests[1].url, /search\/comic/);

  const empty = await source.search.load("   ", [], 1);
  assert.deepEqual(plain(empty), { comics: [], maxPage: 1 });
});

test("详情：分组章节、作者索引与标签命名空间", async () => {
  const { source, requests, store } = fixture([
    [/\/api\/v3\/comic2\//, ok({
      comic: {
        uuid: "ea79f15a", name: "火影忍者特典", path_word: "huoyingrenzhetedian",
        cover: "https://img/naruto.jpg", brief: "  特典部分  ",
        status: { display: "已完結" }, region: { display: "日本" },
        datetime_updated: "2018-11-05",
        author: [{ name: "岸本斉史", path_word: "anbenqishi" }],
        theme: [{ name: "冒險", path_word: "maoxian" }],
      },
      groups: { default: { path_word: "default", name: "默認", count: 7 } },
    })],
    [/\/chapters\?/, ok({ total: 7, limit: 100, offset: 0, list: [
      { uuid: "09a0024c", name: "皆之书" }, { uuid: "189c0da4", name: "第二话" },
    ] })],
  ]);
  const info = await source.comic.loadInfo("huoyingrenzhetedian");
  assert.equal(info.title, "火影忍者特典");
  assert.equal(info.subId, "ea79f15a");
  assert.equal(info.description, "特典部分\n\n已完結 · 日本 · 更新於 2018-11-05");
  assert.deepEqual(plain(info.tags), { 作者: ["岸本斉史"], 標籤: ["冒險"] });
  // 「更新／狀態」不再作为标签命名空间暴露，从根上避免点标签报错。
  assert.deepEqual(plain(Object.keys(info.tags)).sort(), ["作者", "標籤"]);
  assert.deepEqual(plain(info.chapters["默認"]), { "09a0024c": "皆之书", "189c0da4": "第二话" });
  assert.equal(store.get("authorPaths")["岸本斉史"], "anbenqishi");
  assert.match(requests[1].url, /group\/default\/chapters/);
});

test("章节：图片按清晰度替换规格段，缺图直接报错", async () => {
  const { source, settings } = fixture([
    [/\/chapter\//, ok({ chapter: { contents: [
      { url: "https://sh.mangafunb.fun/h/x/1/h1500x.webp" },
      { url: "https://sh.mangafunb.fun/h/x/2/h1500x.webp" },
      { url: "" },
    ] } })],
  ]);
  const ep = await source.comic.loadEp("huoyingrenzhetedian", "09a0024c");
  assert.deepEqual(plain(ep.images), [
    "https://sh.mangafunb.fun/h/x/1/h1500x.webp",
    "https://sh.mangafunb.fun/h/x/2/h1500x.webp",
  ]);
  settings.imageQuality = "h800x";
  const small = await source.comic.loadEp("huoyingrenzhetedian", "09a0024c");
  assert.match(small.images[0], /h800x\.webp$/);

  const broken = fixture([[/\/chapter\//, ok({ chapter: { contents: [] } })]]);
  await assert.rejects(broken.source.comic.loadEp("a", "b"), /没有取到图片地址/);
});

test("点标签：作者与标签跳搜索，其余命名空间不返回（回归：不再抛错）", async () => {
  const { source } = fixture([]);
  assert.deepEqual(plain(source.comic.onClickTag("作者", "岸本斉史")),
    { action: "search", keyword: "岸本斉史" });
  assert.deepEqual(plain(source.comic.onClickTag("標籤", "冒險")),
    { action: "search", keyword: "冒險" });
  assert.deepEqual(plain(source.comic.onClickTag("标签", "冒險")),
    { action: "search", keyword: "冒險" });
  for (const namespace of ["更新", "狀態", "状态", "地区", "", undefined]) {
    assert.equal(source.comic.onClickTag(namespace, "x"), undefined, String(namespace));
  }
});

test("接口异常：状态码、非 JSON、业务码都要报出可读原因", async () => {
  const bad = fixture([[/\/api\/v3\/comics\?/, { status: 503, body: "" }]]);
  await assert.rejects(bad.source.explore[0].load(1), /状态码 503/);

  const html = fixture([[/\/api\/v3\/comics\?/, { status: 200, body: "<html>404</html>" }]]);
  await assert.rejects(html.source.explore[0].load(1), /不是 JSON/);

  const delisted = fixture([[/\/api\/v3\/comics\?/, json({ code: 210, message: "該作品已下架", results: {} })]]);
  await assert.rejects(delisted.source.explore[0].load(1), /該作品已下架/);
});

test("源声明：key、版本与接口标识保持可审阅", async () => {
  const { source } = fixture([]);
  assert.equal(source.key, "hot_manga");
  assert.equal(source.version, "1.0.1");
  assert.equal(source.minAppVersion, "1.6.0");
  assert.equal(source.comic.idMatch, undefined);
  assert.equal(source.account, undefined);
  assert.equal(source.explore.length, 4);
});
