"""为最新 CLI 加载经过哈希核对的客户端 bootstrap；不改写漫画源或最低版本。"""

import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def prepare(directory):
    engine = directory / "src/engine.js"
    code = engine.read_text(encoding="utf-8")
    replacements = {
        'import { persistSourceData }': 'import { installClientProfile } from "../client_bridge.mjs";\nimport { persistSourceData }',
        "return { version: globals.APP.version };":
            "const client = await installClientProfile(globals, runtime, runtimeImages);\n"
            "        return client ? JSON.stringify(client) : { version: globals.APP.version };",
        "() => runtime.modifyImage(bytes, config.modifyImage)":
            "() => (globals.__modifyImage ?? runtime.modifyImage)(bytes, config.modifyImage)",
    }
    for old, new in replacements.items():
        if code.count(old) != 1:
            raise ValueError("最新 CLI 结构变化，适配钩子不再唯一；停止而非静默绕过")
        code = code.replace(old, new)
    engine.write_text(code, encoding="utf-8", newline="\n")
    shutil.copyfile(ROOT / "scripts/client_bridge.mjs", directory / "client_bridge.mjs")
    target = directory / "client-profiles"
    target.mkdir(exist_ok=True)
    shutil.copyfile(ROOT / "monitor/clients.json", target / "clients.json")
    return {
        name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        for name in ("scripts/client_bridge.mjs", "scripts/prepare_client.py", "monitor/clients.json")
    }


if __name__ == "__main__":
    print(json.dumps(prepare(Path(sys.argv[1]).resolve())))
