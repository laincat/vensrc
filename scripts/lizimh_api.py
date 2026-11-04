"""查证栗子漫画（lizimh）当前接口域名，并判断源能不能用。

为什么需要它
------------
`lizimh` 源把接口地址写死在代码里（`static api` / `static apiFallback`），
2026-11-04 起两个地址一起 DNS 失效，源和巡检同时报 `dns_error`。官方 App 早就
不用这两个域名了：它启动时从对象存储取一段加密的自举配置，里面只有一个
`domain` 字段，接口域名换掉时官方只改这一段，源作者只能靠人肉发现。

这个工具复现了官方 App 的那一步：

1. 取自举配置（COS 上的匿名 JSON，内容是 AES-256-ECB 密文的 Base64）；
2. 用 App 内嵌的密钥解密，读出官方当前接口域名；
3. 按源的签名规则（`q2sIObYXCp2uBZgCNBlY93J3z67hK0wS` + 路径 + 时间戳的
   MD5 → `lzsign`）发真实请求，确认这个域名是不是真的能用。

于是"栗子源什么时候能恢复"变成一条命令：官方换域名后 `discover` 立刻能读到
新地址，`probe` 立刻能验证通过与否，不用等上游源作者发现、也不用抓包。

用法::

    python3 scripts/lizimh_api.py discover            # 官方当前接口域名
    python3 scripts/lizimh_api.py probe               # 自带候选地址逐个探测
    python3 scripts/lizimh_api.py probe --base https://ai.example.com
    python3 scripts/lizimh_api.py discover --json

退出码：discover 读到域名即 0；probe 只要有一个候选通过就是 0，全部失败为 1。
"""

import argparse
import base64
import hashlib
import json
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

# 官方 App（com.jy.zyds）libapp.so 里的自举配置地址与解密密钥。
BOOTSTRAP_URL = (
    "https://lz-1382057604.cos.ap-hongkong.myqcloud.com/"
    "5A6F4D2B7E9A1C3D8F0B2E4A6C8E0D2F4B6A8C0E2D4F6A8B0C2E4D6F8A0C2E4B.json"
)
BOOTSTRAP_KEY = b"f8d992c74b29491d8a3e3fd5f07389d8"

# 源里的应用协议常量，不是账号凭据；签名算法与此保持一致。
SIGN_PREFIX = "q2sIObYXCp2uBZgCNBlY93J3z67hK0wS"
UA = "Dart/3.5 (dart:io)"
# 源里写死的两个地址，留作对比基线。
SOURCE_HOSTS = ("http://ai.xajtl.com", "http://ai.qsmm.fun")
# 用来判断接口是否真的活着：三个公开只读端点。
PROBE_PATHS = ("/app/api/configv2", "/app/api/home/data")

_SBOX = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
]
_INV_SBOX = [0] * 256
for _i, _v in enumerate(_SBOX):
    _INV_SBOX[_v] = _i
_RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def _xtime(value):
    value <<= 1
    return (value ^ 0x1B) & 0xFF if value & 0x100 else value


def _mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a = _xtime(a)
        b >>= 1
    return result


def _expand_key(key):
    if len(key) not in (16, 24, 32):
        raise ValueError("AES key must be 16, 24 or 32 bytes")
    nk = len(key) // 4
    rounds = nk + 6
    words = [list(key[i:i + 4]) for i in range(0, len(key), 4)]
    for i in range(nk, 4 * (rounds + 1)):
        temp = list(words[i - 1])
        if i % nk == 0:
            temp = temp[1:] + temp[:1]
            temp = [_SBOX[b] for b in temp]
            temp[0] ^= _RCON[i // nk - 1]
        elif nk > 6 and i % nk == 4:
            temp = [_SBOX[b] for b in temp]
        words.append([a ^ b for a, b in zip(words[i - nk], temp)])
    return [sum(words[4 * r:4 * r + 4], []) for r in range(rounds + 1)]


def _decrypt_block(block, round_keys):
    """AES 单块解密；state 按列主序存放，索引为 4*col+row。"""

    def index(row, col):
        return 4 * col + row

    def add_key(state, key):
        return [a ^ b for a, b in zip(state, key)]

    state = add_key(block, round_keys[-1])
    for rnd in range(len(round_keys) - 2, -1, -1):
        shifted = [0] * 16
        for row in range(4):
            for col in range(4):
                shifted[index(row, (col + row) % 4)] = state[index(row, col)]
        state = [_INV_SBOX[b] for b in shifted]
        state = add_key(state, round_keys[rnd])
        if rnd:
            mixed = [0] * 16
            for col in range(4):
                a = state[4 * col:4 * col + 4]
                mixed[4 * col + 0] = _mul(a[0], 14) ^ _mul(a[1], 11) ^ _mul(a[2], 13) ^ _mul(a[3], 9)
                mixed[4 * col + 1] = _mul(a[0], 9) ^ _mul(a[1], 14) ^ _mul(a[2], 11) ^ _mul(a[3], 13)
                mixed[4 * col + 2] = _mul(a[0], 13) ^ _mul(a[1], 9) ^ _mul(a[2], 14) ^ _mul(a[3], 11)
                mixed[4 * col + 3] = _mul(a[0], 11) ^ _mul(a[1], 13) ^ _mul(a[2], 9) ^ _mul(a[3], 14)
            state = mixed
    return state


def aes_ecb_decrypt(ciphertext, key):
    """AES-ECB 解密原始字节；不处理填充，与宿主 Convert.decryptAesEcb 一致。"""
    if len(ciphertext) % 16:
        raise ValueError("ciphertext length must be a multiple of 16")
    round_keys = _expand_key(key)
    out = bytearray()
    for offset in range(0, len(ciphertext), 16):
        out += bytes(_decrypt_block(list(ciphertext[offset:offset + 16]), round_keys))
    return bytes(out)


def strip_pkcs7(data):
    if not data:
        return data
    pad = data[-1]
    if 1 <= pad <= 16 and data[-pad:] == bytes([pad]) * pad:
        return data[:-pad]
    return data


def domain_from_plaintext(raw):
    """从自举配置明文里取 `domain`；格式不对就抛 ValueError。"""
    text = strip_pkcs7(raw).decode("utf-8", "replace").strip()
    try:
        config = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"自举配置不是 JSON：{text[:120]!r}（{error}）") from error
    if not isinstance(config, dict):
        raise ValueError(f"自举配置不是对象：{text[:120]!r}")
    domain = str(config.get("domain") or "").strip()
    if not domain:
        raise ValueError(f"自举配置里没有 domain：{text[:120]!r}")
    return domain.rstrip("/")


def parse_bootstrap(payload):
    """把自举配置解成接口域名；输入是文本或字节。"""
    if isinstance(payload, bytes):
        payload = payload.decode("ascii", "strict")
    raw = aes_ecb_decrypt(base64.b64decode(payload.strip(), validate=True), BOOTSTRAP_KEY)
    return domain_from_plaintext(raw)


def signed_path(target, timestamp=None):
    """按源的规则补默认参数、加 `lzsign` 与 `t`。"""
    head, _, query = str(target).partition("?")
    parts = [item for item in query.split("&") if item]
    parts = [item for item in parts if item.split("=")[0] not in ("lzsign", "t")]

    def add_default(name, value):
        if not any(item.split("=")[0] == name for item in parts):
            parts.append(f"{name}={quote(str(value), safe='')}")

    if head in ("/app/api/home/data", "/app/api/configv2"):
        add_default("packname", "com.jy.zyds")
        add_default("appsign256", "")
    if head == "/app/api/configv2":
        add_default("platform", "ios")
    stamp = str(int(time.time()) if timestamp is None else timestamp)
    if not (len(stamp) == 10 and stamp.isdigit()):
        raise ValueError("Invalid API timestamp")
    digest = hashlib.md5((SIGN_PREFIX + head + stamp).encode("utf-8")).hexdigest()
    parts += [f"lzsign={digest}", f"t={stamp}"]
    return f"{head}?{'&'.join(parts)}"


def request(url, timeout=25):
    req = Request(url, headers={"Accept": "application/json", "User-Agent": UA})
    with urlopen(req, timeout=timeout) as response:
        return response.status, response.read()


def probe(base, paths=PROBE_PATHS, timeout=25):
    """对候选域名发真实签名请求，返回逐端点结果。"""
    base = base.rstrip("/")
    results = []
    for path in paths:
        url = base + signed_path(path)
        try:
            status, body = request(url, timeout)
            payload = body[:200].decode("utf-8", "replace")
            results.append({"path": path, "status": status,
                            "ok": status == 200 and body.lstrip()[:1] in (b"{", b"["),
                            "body": payload})
        except HTTPError as error:
            results.append({"path": path, "status": error.code, "ok": False,
                            "body": error.read(200).decode("utf-8", "replace")})
        except (URLError, TimeoutError, OSError) as error:
            results.append({"path": path, "status": None, "ok": False,
                            "body": f"{type(error).__name__}: {error}"})
    return {"base": base, "ok": any(item["ok"] for item in results), "results": results}


def discover(timeout=25):
    with urlopen(Request(BOOTSTRAP_URL, headers={"User-Agent": UA}), timeout=timeout) as resp:
        return parse_bootstrap(resp.read())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["discover", "probe", "self-test"])
    parser.add_argument("--base", action="append", default=[],
                        help="额外探测的接口地址（可重复）")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args(argv)

    if args.command == "self-test":
        from lizimh_api_test import main as run_tests
        return run_tests()

    if args.command == "discover":
        try:
            domain = discover()
        except Exception as error:  # noqa: BLE001 - 诊断工具直接把原因报出来
            print(f"自举配置读取失败：{type(error).__name__}: {error}", file=sys.stderr)
            return 1
        report = {"bootstrap": BOOTSTRAP_URL, "domain": domain,
                  "matches_source": domain in SOURCE_HOSTS}
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.json
              else f"官方当前接口域名：{domain}")
        return 0

    candidates = []
    try:
        candidates.append(discover())
    except Exception as error:  # noqa: BLE001
        print(f"自举配置读取失败：{type(error).__name__}: {error}", file=sys.stderr)
    candidates += args.base + list(SOURCE_HOSTS)
    seen, ordered = set(), []
    for item in candidates:
        if item and item not in seen:
            seen.add(item)
            ordered.append(item)
    reports = [probe(base) for base in ordered]
    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        for item in reports:
            head = "可用" if item["ok"] else "不可用"
            print(f"{head}  {item['base']}")
            for step in item["results"]:
                print(f"    {step['status']}  {step['path']}  {step['body'][:80]}")
    return 0 if any(item["ok"] for item in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
