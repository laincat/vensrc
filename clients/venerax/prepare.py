"""固定 VeneraX 基线并应用已审阅补丁；不读取账号或 Actions Secrets。"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
patch = root / "webview-login.patch"
if hashlib.sha256(patch.read_bytes()).hexdigest() != manifest["patchSha256"]:
    raise SystemExit("客户端补丁哈希不匹配")
target = Path(sys.argv[1]).resolve()
if target.exists():
    raise SystemExit("请指定本轮独立且不存在的客户端目录")


def run(*args):
    subprocess.run(args, check=True)


run("git", "init", str(target))
run("git", "-C", str(target), "remote", "add", "origin",
    "https://github.com/" + manifest["repository"] + ".git")
run("git", "-C", str(target), "fetch", "--depth", "1", "origin", manifest["commit"])
run("git", "-C", str(target), "checkout", "--detach", "FETCH_HEAD")
run("git", "-C", str(target), "apply", "--check", str(patch))
run("git", "-C", str(target), "apply", str(patch))
print("已固定客户端基线和补丁哈希；尚未代表实机登录通过。")
