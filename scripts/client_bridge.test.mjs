import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";

process.env.VENERA_RUNTIME_DATA_DIR = await mkdtemp(path.join(tmpdir(), "venera-bridge-"));
const { default: runtime } = await import("venera-runtime");
const { runtimeImages } = await import("venera-runtime/platform");
const { installClientProfile } = await import("./client_bridge.mjs");

for (const [name, version] of [["venerax", "2.3.6"], ["venera-next", "1.18.0"]]) {
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
