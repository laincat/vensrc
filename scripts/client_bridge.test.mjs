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
  test(`${name}: 真实 bootstrap、最低版本、存储身份、HTTP、解密与逐像素重排`, async () => {
    process.env.VENERA_CLIENT_PROFILE = name;
    const globals = runtime.createVeneraRuntime();
    const requests = [];
    globals.Network = { ...globals.Network, sendRequest: async (...args) => {
      requests.push(args);
      return { status: 200, headers: {}, body: "response" };
    }};
    await installClientProfile(globals, runtime, runtimeImages);
    assert.equal(globals.APP.version, version);
    assert.equal(runtime.APP.version, "1.6.3");
    const sourceCode = `class Fixture extends ComicSource {
      name="fixture"; key="fixture"; version="1.0.0"; minAppVersion="1.16.0";
      settings={dailyCheckInTask:{type:"switch",default:false}};
    }`;
    const source = runtime.loadVeneraConfigBySourceCode(sourceCode, globals, false);
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
    await globals.Network.post("https://fixture.invalid/", { Test: "header" }, "payload");
    assert.deepEqual(requests[0].slice(0, 2), ["POST", "https://fixture.invalid/"]);
    assert.equal(requests[0][3], "payload");
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
