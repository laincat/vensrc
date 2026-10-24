import { readFile } from "node:fs/promises";
import { createHash, randomUUID } from "node:crypto";

function unsupported(message) {
  throw Object.assign(new Error(message), { category: "runtime_unsupported" });
}

// 只执行固定提交的客户端接口；未知宿主消息直接失败。
export async function installClientProfile(globals, runtime, images) {
  const name = process.env.VENERA_CLIENT_PROFILE;
  if (!name) return null;
  const base = new URL("./client-profiles/", import.meta.url);
  const lock = JSON.parse(await readFile(new URL("clients.json", base), "utf8"));
  const profile = lock.profiles[name];
  if (!profile) unsupported(`Unknown client profile: ${name}`);
  const init = await readFile(new URL(`${name}/assets/init.js`, base));
  if (createHash("sha256").update(init).digest("hex") !== profile.files["assets/init.js"])
    throw new Error("Client bootstrap hash mismatch");
  const pubspec = await readFile(new URL(`${name}/pubspec.yaml`, base));
  if (createHash("sha256").update(pubspec).digest("hex") !== profile.files["pubspec.yaml"])
    throw new Error("Client pubspec hash mismatch");
  const version = pubspec.toString().match(/^version:\s*(\S+)/m)?.[1].split("+")[0];
  if (version !== profile.version) throw new Error("Client version differs from pubspec");
  const host = { ...globals };
  const config = runtime.configManager;
  const handles = new Map();
  const documents = new Map();
  let client, nextImage = 0;
  const addImage = (handle) => {
    const key = ++nextImage;
    handles.set(key, handle);
    return key;
  };
  const getImage = (key) => {
    if (!handles.has(key)) throw new Error("Unknown image handle");
    return handles.get(key);
  };
  function sourceFor(message) {
    const source = client.ComicSource.sources[message.key];
    if (!source) throw new Error("Source instance is unavailable");
    if (name === "venera-next" &&
        client.__sourceRuntime.identity(source) !== message.source_id)
      throw new Error("Source instance has been replaced or removed");
    return source;
  }
  function sendMessage(m) {
    switch (m.method) {
      case "html": {
        if (m.function === "parse") {
          if (documents.size >= 8) documents.delete(documents.keys().next().value);
          documents.set(m.key, { document: new host.HtmlDocument(m.data), nodes: new Map(), next: 0 });
          return;
        }
        if (m.function === "dispose") return documents.delete(m.key);
        const doc = documents.get(m.doc ?? m.key);
        if (!doc) throw new Error("HTML document is unavailable");
        const add = (node) => {
          if (node == null) return null;
          const id = ++doc.next;
          doc.nodes.set(id, node);
          return id;
        };
        const node = m.doc === undefined ? doc.document : doc.nodes.get(m.key);
        if (!node) throw new Error("HTML node is unavailable");
        switch (m.function) {
          case "querySelector": case "dom_querySelector": return add(node.querySelector(m.query));
          case "querySelectorAll": case "dom_querySelectorAll":
            return node.querySelectorAll(m.query).map(add);
          case "getElementById": return add(node.getElementById(m.id));
          case "getChildren": return node.children.map(add);
          case "getNodes": return node.nodes.map(add);
          case "getParent": return add(node.parent);
          case "getPreviousSibling": return add(node.previousElementSibling);
          case "getNextSibling": return add(node.nextElementSibling);
          case "node_to_element": return add(node.toElement());
          case "node_toElement":
            // 两份客户端的 JS 拼写与 Dart 分支不同，不掩盖客户端自身的不兼容。
            unsupported("Client HtmlNode.toElement message differs from Dart host");
            break;
          default: {
            const property = {
              getText: "text", node_text: "text", node_type: "type",
              getAttributes: "attributes", getInnerHTML: "innerHTML",
              getClassNames: "classNames", getId: "id", getLocalName: "localName",
            }[m.function];
            if (!property) unsupported(`Unimplemented HTML function: ${m.function}`);
            return node[property];
          }
        }
        break;
      }
      case "http": {
        const headers = { ...m.headers };
        if (!Object.keys(headers).some((key) => key.toLowerCase() === "user-agent"))
          headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36";
        return host.Network[m.bytes ? "fetchBytes" : "sendRequest"](
          m.http_method, m.url, headers, m.data, m.extra);
      }
      case "convert": {
        if (m.type === "hmac")
          return host.Convert[m.isString ? "hmacString" : "hmac"](m.key, m.value, m.hash);
        const method = {
          utf8: m.isEncode ? "encodeUtf8" : "decodeUtf8",
          gbk: m.isEncode ? "encodeGbk" : "decodeGbk",
          base64: m.isEncode ? "encodeBase64" : "decodeBase64",
          md5: "md5", sha1: "sha1", sha256: "sha256", sha512: "sha512",
          "aes-ecb": m.isEncode ? "encryptAesEcb" : "decryptAesEcb",
          "aes-cbc": m.isEncode ? "encryptAesCbc" : "decryptAesCbc",
          "aes-cfb": m.isEncode ? "encryptAesCfb" : "decryptAesCfb",
          "aes-ofb": m.isEncode ? "encryptAesOfb" : "decryptAesOfb",
          rsa: m.isEncode ? null : "decryptRsa",
        }[m.type];
        if (!method || typeof host.Convert[method] !== "function")
          unsupported(`Unimplemented conversion: ${m.type}`);
        if (m.type === "aes-cfb") return host.Convert[method](m.value, m.key, m.iv, m.blockSize);
        if (m.type === "aes-ofb") return host.Convert[method](m.value, m.key, m.blockSize);
        return host.Convert[method](m.value, m.key, m.iv);
      }
      case "load_setting": {
        const source = sourceFor(m);
        const value = config.getSetting(m.key, m.setting_key) ??
          source.settings?.[m.setting_key]?.default;
        if (value === undefined) throw new Error(`Setting not found: ${m.setting_key}`);
        return value;
      }
      case "load_data":
        sourceFor(m);
        return config.getData(m.key, m.data_key);
      case "save_data":
        sourceFor(m);
        if (m.data_key === "setting") throw new Error("setting is not allowed to be saved");
        return config.setData(m.key, m.data_key, m.data);
      case "delete_data":
        sourceFor(m);
        return config.deleteData(m.key, m.data_key);
      case "isLogged":
        sourceFor(m);
        return config.getData(m.key, "account") != null;
      case "cookie": {
        const method = { get: "getCookies", set: "setCookies", delete: "deleteCookies" }[m.function];
        if (!method) unsupported(`Unimplemented cookie function: ${m.function}`);
        return host.Network[method](m.url, m.cookies);
      }
      case "delay":
        return new Promise((resolve) => setTimeout(resolve, Math.max(0, m.time)));
      case "uuid": return randomUUID();
      case "random":
        return m.type === "int" ? Math.floor(Math.random() * (m.max - m.min)) + m.min :
          Math.random() * (m.max - m.min) + m.min;
      case "compute": {
        if (typeof m.function !== "string" || !Array.isArray(m.args))
          throw new TypeError("compute requires a function string and argument array");
        return Promise.resolve(new Function(...Object.keys(globals),
          `return (${m.function})(...arguments[arguments.length - 1]);`)(
          ...Object.values(globals), m.args));
      }
      case "getClipboard": case "setClipboard":
        unsupported("Interactive clipboard is unavailable");
        break;
      case "getLocale": return host.APP.locale;
      case "getPlatform": return process.platform === "win32" ? "windows" : process.platform;
      case "log": return host.log(m.level, m.title, m.content);
      case "UI":
        if (!["showMessage", "showLoading", "cancelLoading"].includes(m.function))
          unsupported(`Interactive UI is unavailable: ${m.function}`);
        return host.UI[m.function](m.id ?? m.message);
      case "image": {
        if (m.function === "emptyImage") return addImage(images.empty(m.width, m.height));
        const image = getImage(m.key);
        switch (m.function) {
          case "getWidth": return image.width;
          case "getHeight": return image.height;
          case "copyRange":
            return addImage(images.crop(image, m.x, m.y, m.width, m.height));
          case "copyAndRotate90": return addImage(images.rotate90(image));
          case "fillImageAt":
            handles.set(m.key, images.fill(image, m.x, m.y, getImage(m.image)));
            return;
          case "fillImageRangeAt": {
            const region = images.crop(getImage(m.image), m.srcX, m.srcY, m.width, m.height);
            handles.set(m.key, images.fill(image, m.x, m.y, region));
            return;
          }
          default: unsupported(`Unimplemented image function: ${m.function}`);
        }
      }
      default: unsupported(`Unimplemented host message: ${m.method}`);
    }
  }
  // 使用客户端原始 bootstrap；版本来自同一提交的 pubspec，不修改旧 APP。
  client = new Function("sendMessage", "appVersion", `${init.toString()}
return { Convert, Network, fetch, Comic, ComicDetails, Comment, ImageLoadingConfig,
  ComicSource, APP, UI, console, log, setTimeout, setInterval, Image, Cookie,
  HtmlDocument, HtmlElement, HtmlNode, createUuid, randomInt, randomDouble,
  compute, getClipboard, setClipboard,
  __sourceRuntime: typeof __sourceRuntime === "undefined" ? null : __sourceRuntime };`
  )(sendMessage, version);
  const { Image, __sourceRuntime, ...api } = client;
  Object.assign(globals, api);
  if (name === "venerax") {
    const parserPath = "lib/foundation/comic_source/parser.dart";
    const parser = await readFile(new URL(`${name}/${parserPath}`, base));
    if (createHash("sha256").update(parser).digest("hex") !== profile.files[parserPath])
      throw new Error("Client parser hash mismatch");
    const script = parser.toString().match(
      /\/\/ Fix broken isAppVersionAfter[\s\S]*?JsEngine\(\)\.runCode\("""([\s\S]*?)"""\);/)?.[1];
    if (!script) throw new Error("Client source hook is unavailable");
    globals.__clientSourceLoaded = (source) => {
      const actual = script.replaceAll("$_key", source.key);
      new Function("ComicSource", "APP", actual)(client.ComicSource, client.APP);
    };
  }
  globals.__modifyImage = async (bytes, script) => {
    try {
      const input = new Image(addImage(await images.decode(bytes)));
      const transform = new Function("Image", `${script}\nreturn modifyImage;`)(Image);
      const output = transform(input);
      if (!(output instanceof Image)) throw new Error("modifyImage must return an Image");
      return await images.encodePng(getImage(output.key));
    } finally {
      handles.clear();
    }
  };
  return { name, repository: profile.repository, commit: profile.commit, version,
    bootstrapSha256: profile.files["assets/init.js"],
    scope: profile.scope };
}
