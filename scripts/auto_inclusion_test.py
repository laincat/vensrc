import contextlib
from datetime import datetime, timedelta, timezone
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import cloud_audit as audit

CORE = ("source.load", "search.load", "comic.loadInfo", "comic.loadEp", "image.download", "image.decode")
STAGES = [{"path": path, "status": "passed"} for path in CORE]
PROFILES = {name: {"repository": f"client/{name}", "commit": letter * 40, "version": "1.0.0",
                   "scope": "fixture", "files": {"assets/init.js": letter * 64}}
            for name, letter in (("venerax", "1"), ("venera-next", "2"))}
SAMPLE = {"keyword": "漫画", "comicId": "1", "epId": "2"}
CHECKED = "2026-11-22T00:00:00+00:00"


def source(version, body='url = "https://www.example.com/list"', key="fixture"):
    return (f'class Fixture extends ComicSource {{\n    name = "测试源-{key}"\n    key = "{key}"\n'
            f'    version = "{version}"\n    minAppVersion = "1.0.0"\n    {body}\n}}\n').encode()


def build(data, repository="community/source", commit="b", file="fixture.js", **fields):
    digest = audit.sha(data)
    declared = audit.declared_fields(data.decode())
    return {"id": digest, "sha256": digest, "key": declared["key"], "name": declared["name"],
            "version": declared["version"], "minAppVersion": "1.0.0", "repository": repository,
            "fileName": file, "url": f"https://raw.githubusercontent.com/{repository}/{commit * 40}/{file}",
            "trackedBy": [repository], "priority": 0, **fields}


def record(candidate, profile, ok=True, **changes):
    identity = {**{name: PROFILES[profile][name] for name in ("repository", "commit", "version", "scope")},
                "name": profile, "bootstrapSha256": PROFILES[profile]["files"]["assets/init.js"]}
    stages = [{"path": "runtime.load", "status": "passed", "output": {"value": json.dumps(identity)}}]
    stages += STAGES if ok else STAGES[:-1] + [
        {"path": "image.decode", "status": "failed", "category": "image_decode_failed", "reason": "bad"}]
    return {"id": candidate["id"], "runtimeProfile": profile, "inputs": SAMPLE, "policy": audit.POLICY,
            "trialRun": "fixture-run", "networkHosts": ["m.example.com"], "accountCapabilities": [],
            "readSample": {"comicId": "1", "epId": "2"}, "readingSites": ["example.com"],
            "source": {"key": candidate["key"], "name": candidate["name"], "version": candidate["version"],
                       "sourceSha256": candidate["sha256"], "status": "passed" if ok else "failed",
                       "stages": stages, **changes}}


class Workspace:
    """临时仓库根目录：一份清单里的旧构建，加上两端客户端身份。"""

    def __init__(self, case):
        directory = tempfile.TemporaryDirectory()
        case.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.files = {}
        self.old_bytes = source("1.0.0")
        self.old = self.serve(build(self.old_bytes, sample=SAMPLE, officialKey=False, settings={},
                                    runtimeProfile="venerax", verifyProfiles=["venera-next"]), self.old_bytes)
        baseline = audit.official_policy()
        audit.save(self.root / "monitor/official-keys.json", baseline)
        audit.save(self.root / "monitor/upstreams.json", {
            "schemaVersion": 1, "repositories": ["community/source", "other/source"],
            "priorityRepositories": []})
        audit.save(self.root / "monitor/source-notes.json", {"schemaVersion": 1, "notes": {}})
        audit.save(self.root / "monitor/focus.json", {"schemaVersion": 1, "buildIds": []})
        audit.save(self.root / "monitor/accounts.json", {"schemaVersion": 1, "sites": []})
        audit.save(self.root / "monitor/clients.json", {"schemaVersion": 1, "profiles": PROFILES})
        for name in ("scripts/client_bridge.mjs", "scripts/prepare_client.py", "scripts/patrol-worker.c"):
            (self.root / name).parent.mkdir(parents=True, exist_ok=True)
            (self.root / name).write_text("fixture", encoding="utf-8")
        audit.save(self.root / "data/sources.lock.json", [])
        self.catalog([self.old])
        self.cli = {"commit": "c" * 40, "version": "fixture", "packageLockSha256": "d" * 64,
                    "clientProfiles": PROFILES,
                    "adapterSha256": {name: audit.sha((self.root / name).read_bytes()) for name in (
                        "scripts/client_bridge.mjs", "scripts/prepare_client.py", "scripts/patrol-worker.c", "monitor/clients.json")}}
        self.registered = audit.registered_repositories(audit.load(self.root / "monitor/upstreams.json"))
        self.exclusions = baseline
        for patcher in (patch.dict(audit.os.environ, AUDIT_RUN_URL="fixture-run"), patch.object(audit, "ROOT", self.root),
                        patch.object(audit, "request", side_effect=self.request)):
            patcher.start()
            case.addCleanup(patcher.stop)

    def serve(self, item, data):
        self.files[item["url"]] = data
        return item

    def candidate(self, version="1.0.1", body='url = "https://m.example.com/list"', **fields):
        data = source(version, body)
        # 每个候选一个独立的固定地址，互不覆盖。
        return self.serve(build(data, **{"commit": "e", "file": f"fixture-{audit.sha(data)[:8]}.js",
                                         **fields}), data)

    def request(self, url, api=False):
        return self.files[url]

    def catalog(self, items=None):
        if items is not None:
            audit.save(self.root / "monitor/catalog.json", {
                "schemaVersion": 1, "priorityRepositories": [], "sources": items})
        return audit.load(self.root / "monitor/catalog.json")

    def hosts(self, item):
        return audit.source_surface(self.files[item["url"]].decode())

    def gate(self, candidate):
        return audit.candidate_gate(candidate, self.catalog(), self.registered, self.exclusions, self.hosts)

    def payload(self, candidates=(), failing=(), records=None):
        return {"schemaVersion": 1, "checkedAt": CHECKED, "cli": self.cli,
                "catalogSha256": audit.sha((self.root / "monitor/catalog.json").read_bytes()),
                "records": records or [],
                "candidateRecords": [record(candidate, profile, (candidate["id"], profile) not in failing)
                                     for candidate in candidates for profile in audit.TRIAL_PROFILES]}

    def publish(self, payload, updates):
        with contextlib.redirect_stdout(io.StringIO()):
            audit.publish_candidates(payload, {"updates": [
                {"lane": "auto", **item} for item in updates]}, self.root)
        return (audit.load(self.root / "data/auto-inclusion.json"),
                audit.load(self.root / "data/candidate-results.json")["results"])

    def promote(self, now=None):
        with contextlib.redirect_stdout(io.StringIO()):
            return audit.promote(now)


class VersionAndHostTests(unittest.TestCase):
    def test_delegated_identity_requires_literal_config_and_exact_field(self):
        code = 'config = {"key":"fixture", "version":"1.0.2"};\nkey = this.config.key;\nversion = this.config.version;'
        self.assertEqual(audit.declared_fields(code), {"key": "fixture", "version": "1.0.2"})
        for changed in (code.replace('this.config.key;', 'this.config.key + suffix;'),
                        code.replace('};', '} || fallback;'), code.replace('"fixture"', 'compute()')):
            self.assertNotIn("key", audit.declared_fields(changed))

    def test_version_must_be_strictly_higher_and_comparable(self):
        for candidate, current, newer in (
            ("1.0.1", "1.0.0", True), ("1.10.0", "1.9.9", True), ("2.0.0", "1.99.99", True),
            ("1.0.0", "1.0.0", False), ("1.0.0", "1.0.1", False), ("1.9.0", "1.10.0", False),
            ("1.1", "1.0.0", False), ("1.0.1-beta", "1.0.0", False), ("v1.0.1", "1.0.0", False),
            ("1.0.1", "1.0", False), ("", "1.0.0", False), (None, "1.0.0", False),
        ):
            with self.subTest(candidate=candidate, current=current):
                self.assertEqual(audit.version_newer(candidate, current), newer)

    def test_hosts_are_read_from_urls_and_domain_literals_without_executing(self):
        code = r"""
            const api = "https://API.Example.com:8443/v1";
            const cdn = 'http://user@img.example.net/a.jpg';
            const ws = `wss://socket.example.org/`;
            const escaped = "https:\/\/escaped.example.io\/x";
            const hex = "\x68\x74\x74\x70\x73://hex.example.dev/";
            const templated = `https://${sub}.tail.example.com/${path}`;
            const dynamic = `https://${this.domain}/api`;
            const mirrors = ["mirror.example.cc", "10.0.0.8"];
            const noise = ["index.json", "cover.jpg", "JSON.parse", "comic.loadInfo", "div.title", "1.2.3"];
        """
        self.assertEqual(audit.source_hosts(code), {
            "api.example.com", "img.example.net", "socket.example.org", "escaped.example.io",
            "hex.example.dev", "tail.example.com", "mirror.example.cc", "10.0.0.8"})

    def test_www_and_m_prefixes_are_the_same_site_but_other_subdomains_are_new(self):
        known = {"www.example.com", "img.example.net"}
        self.assertEqual(audit.new_hosts({"m.example.com", "example.com", "www.example.com"}, known), [])
        self.assertEqual(audit.new_hosts({"api.example.com", "example.net", "evil.test"}, known),
                         ["api.example.com", "evil.test", "example.net"])
        # 只剥一层同站前缀，剥完也不能只剩顶级域。
        self.assertEqual(audit.new_hosts({"m.www.example.com", "www.com"}, known),
                         ["m.www.example.com", "www.com"])


class LaneTests(unittest.TestCase):
    def setUp(self):
        self.space = Workspace(self)

    def test_known_key_from_registered_repository_with_higher_version_and_no_new_host_is_auto(self):
        verdict = self.space.gate(self.space.candidate())
        self.assertEqual((verdict["lane"], verdict["newHosts"]), ("auto", []))
        self.assertEqual(verdict["baseline"]["id"], self.space.old["id"])

    def test_new_host_or_unreadable_baseline_goes_to_trial_only(self):
        verdict = self.space.gate(self.space.candidate(
            body='url = "https://www.example.com/"; const stats = "https://collect.example.org/p"'))
        self.assertEqual((verdict["lane"], verdict["reason"], verdict["newHosts"]),
                         ("trial", "new_hosts", ["collect.example.org"]))
        candidate = self.space.candidate()
        del self.space.files[self.space.old["url"]]
        verdict = self.space.gate(candidate)
        self.assertEqual((verdict["lane"], verdict["reason"]), ("trial", "hosts_unknown"))

    def test_version_that_is_equal_lower_or_not_comparable_is_never_auto(self):
        for version in ("1.0.0", "0.9.9", "1.1", "2.0.0-beta", "latest"):
            with self.subTest(version=version):
                verdict = self.space.gate(self.space.candidate(version))
                self.assertEqual((verdict["lane"], verdict["reason"]), ("trial", "version"))
        # 清单里同 key 有多份时，必须高于每一份。
        newer = self.space.serve(build(source("1.5.0"), repository="other/source", commit="f",
                                       sample=SAMPLE), source("1.5.0"))
        self.space.catalog([self.space.old, newer])
        self.assertEqual(self.space.gate(self.space.candidate("1.2.0"))["reason"], "version")
        self.assertEqual(self.space.gate(self.space.candidate("1.5.1"))["lane"], "auto")

    def test_new_key_is_auto_and_unregistered_repository_is_listed_only(self):
        data = source("1.0.0", key="brand_new")
        fresh = self.space.serve(build(data, commit="e"), data)
        self.assertEqual((self.space.gate(fresh)["lane"], self.space.gate(fresh)["reason"]),
                         ("auto", "new_key"))
        outsider = self.space.candidate(repository="stranger/source")
        self.assertEqual(self.space.gate(outsider)["lane"], "listed")
        # 声称来自已登记仓库、地址却指向别处，同样不执行。
        self.assertEqual(self.space.gate({**outsider, "repository": "community/source"})["lane"], "listed")
        self.assertEqual(self.space.gate({**self.space.candidate(), "url": "https://example.com/a.js"})["lane"],
                         "listed")

    def test_official_and_wnacg_exclusions_still_apply_before_any_lane(self):
        key, version = next(iter(self.space.exclusions["versions"].items()))
        data = source(version, key=key)
        same = self.space.serve(build(data, commit="e"), data)
        self.space.catalog([self.space.old, {**self.space.old, "id": "9" * 64, "sha256": "9" * 64,
                                             "key": key, "version": "0.0.1"}])
        self.assertEqual(self.space.gate(same)["lane"], "excluded")
        data = source("9.9.9", key="wnacg")
        self.assertEqual(self.space.gate(self.space.serve(build(data, commit="e"), data))["lane"], "excluded")

    def test_self_maintained_source_is_not_replaced_automatically(self):
        self.space.catalog([{**self.space.old, "repository": audit.SELF_MAINTAINED}])
        verdict = self.space.gate(self.space.candidate())
        self.assertEqual((verdict["lane"], verdict["reason"]), ("trial", "self_maintained"))

    def test_only_one_candidate_per_key_enters_the_auto_lane(self):
        low, high = self.space.candidate("1.0.1"), self.space.candidate("1.0.2")
        fork = self.space.candidate("1.0.2", repository="other/source",
                                    body='url = "https://example.com/fork"')
        classify = lambda items: {item["id"]: verdict for item, verdict in zip(items, audit.classify_updates(
            items, self.space.catalog(), self.space.registered, self.space.exclusions,
            self.space.hosts).values())}
        verdicts = classify([low, high])
        self.assertEqual((verdicts[high["id"]]["lane"], verdicts[low["id"]]["reason"]), ("auto", "superseded"))
        # 同版本两份不同字节：与现有构建同仓库的那一份接替。
        verdicts = classify([low, high, fork])
        self.assertEqual((verdicts[high["id"]]["lane"], verdicts[fork["id"]]["reason"]), ("auto", "ambiguous"))
        # 分不出唯一一份时都交回人工。
        other = self.space.candidate("1.0.2", repository="other/source",
                                     body='url = "https://example.com/other"')
        verdicts = classify([fork, other])
        self.assertEqual({verdict["reason"] for verdict in verdicts.values()}, {"ambiguous"})

    def test_trial_queue_puts_auto_lane_first_and_respects_the_limit_and_retry_window(self):
        now = datetime.fromisoformat(CHECKED)
        updates = [{"id": f"{number:064x}", "key": f"k{number}", "version": "1.0.0", "lane": lane,
                    "reason": reason} for number, (lane, reason) in enumerate(
                        [("trial", "version"), ("trial", "new_key"), ("trial", "new_hosts"),
                         ("auto", "auto"), ("listed", "unregistered"), ("auto", "auto")])]
        ids = [item["id"] for item in updates]
        self.assertEqual(audit.select_trials(updates, {}, now), [ids[3], ids[5], ids[2], ids[1], ids[0]])
        self.assertEqual(audit.select_trials(updates, {}, now, limit=2), [ids[3], ids[5]])
        many = [{"id": f"{number:064x}", "key": f"k{number}", "version": "1.0.0", "lane": "trial",
                 "reason": "new_key"} for number in range(100)]
        self.assertEqual(len(audit.select_trials(many, {}, now)), audit.TRIAL_LIMIT)
        recent = (now - timedelta(days=1)).isoformat()
        old = (now - timedelta(days=4)).isoformat()
        results = {ids[3]: {"checkedAt": recent}, ids[5]: {"checkedAt": old}, ids[1]: {"checkedAt": old}}
        # 试过的要等重试期：自动通道 3 天，仅试跑通道 14 天；没试过的排在重试之前。
        self.assertEqual(audit.select_trials(updates, results, now), [ids[5], ids[2], ids[0]])


class DiscoveryTests(unittest.TestCase):
    def test_discovery_sorts_lanes_without_downloading_unregistered_or_executing_anything(self):
        space = Workspace(self)
        audit.save(space.root / "monitor/upstreams.json", {
            "schemaVersion": 1, "repositories": ["community/source"], "priorityRepositories": []})
        upgrade, fresh = source("1.0.1"), source("1.0.0", key="brand_new")
        trees = {"noise/app": {"tree": [{"path": "README.md", "type": "blob"}]},
                 "real/sources": {"tree": [{"path": "a.js", "type": "blob"}]}}
        urls = []

        def request(url, api=False):
            urls.append(url)
            if "/commits" in url:
                return json.dumps([{"sha": "e" * 40}]).encode()
            if "/search/repositories" in url:
                return json.dumps({"items": [{"full_name": name, "pushed_at": "t1"} for name in (
                    "noise/app", "real/sources", "unknown/repo")]}).encode()
            if "/git/trees/" in url:
                return json.dumps(trees[url.split("/repos/")[1].split("/git/")[0]]).encode()
            if url.endswith("/HEAD/a.js"):
                return b"class A extends ComicSource {}"
            if url.endswith("/index.json"):
                return json.dumps([
                    {"name": "测试源", "key": "fixture", "fileName": "fixture.js"},
                    {"name": "新源", "key": "brand_new", "fileName": "new.js"},
                    {"name": "外部", "key": "outside", "fileName": "x.js",
                     "url": "https://raw.githubusercontent.com/stranger/repo/main/x.js"},
                ]).encode()
            return {"fixture.js": space.old_bytes if "b" * 40 in url else upgrade,
                    "new.js": fresh}[url.rsplit("/", 1)[1]]

        def discover():
            with patch.object(audit, "refresh_official_policy", return_value=space.exclusions), \
                    patch.object(audit, "request", side_effect=request), \
                    contextlib.redirect_stdout(io.StringIO()):
                audit.discover(space.root / "work")
            return audit.load(space.root / "work/artifact/discovery.json")

        result = discover()
        lanes = {item["key"]: (item["lane"], item["trial"]) for item in result["updates"]}
        self.assertEqual(lanes, {"fixture": ("auto", True), "brand_new": ("auto", True)})
        auto = next(item for item in result["updates"] if item["key"] == "fixture")
        self.assertEqual((auto["sha256"], auto["sample"], auto["baseline"]["version"]),
                         (audit.sha(upgrade), SAMPLE, "1.0.0"))
        self.assertEqual([(item["repository"], item["key"]) for item in result["unregistered"]],
                         [("stranger/repo", "outside")])
        self.assertFalse(any("stranger/repo" in url for url in urls))
        # 明显无关的仓库滤掉；判断不了的（unknown/repo 没有文件列表）保持现状。
        self.assertEqual([item["repository"] for item in result["newRepositories"]],
                         ["real/sources", "unknown/repo"])
        self.assertEqual([item["repository"] for item in result["filteredRepositories"]], ["noise/app"])
        self.assertEqual(audit.load(space.root / "monitor/catalog.json"), space.catalog())
        # 没有新提交的仓库沿用上一轮的判断，不再读文件列表；试过且未到重试期的候选不重复安排。
        audit.save(space.root / "data/pending-updates.json", result)
        audit.save(space.root / "data/candidate-results.json", {"results": {
            auto["id"]: {"checkedAt": datetime.now(timezone.utc).isoformat()}}})
        urls.clear()
        del trees["noise/app"], trees["real/sources"]
        result = discover()
        self.assertEqual([item["repository"] for item in result["filteredRepositories"]], ["noise/app"])
        self.assertFalse(any("noise/app" in url or "real/sources" in url for url in urls))
        self.assertEqual({item["key"]: item["trial"] for item in result["updates"]},
                         {"fixture": False, "brand_new": True})


class TrialTests(unittest.TestCase):
    def setUp(self):
        self.space = Workspace(self)
        self.work = self.space.root / "work"
        self.sources, self.output = self.work / "source-bytes", self.work / "container"
        for folder in (self.sources, self.output, self.work / "artifact"):
            folder.mkdir(parents=True)
        self.metadata = {"commit": "c" * 40, "image": "venera-patrol:fixture"}
        self.commands = []
        for patcher in (
            patch.object(audit.os, "getuid", lambda: 1000, create=True),
            patch.object(audit.os, "getgid", lambda: 1000, create=True),
            patch.object(audit, "run", lambda *a, **k: SimpleNamespace(stdout="c" * 40 + "\tHEAD\n")),
            patch.object(audit.subprocess, "run", side_effect=self.docker),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)

    def docker(self, command, **options):
        self.commands.append(command)
        if command[:2] == ["docker", "kill"]:
            return SimpleNamespace(returncode=0)
        name = command[command.index("--config") + 1].split("/")[-1].split(".")[0]
        if "VENERA_CLIENT_PROFILE=venera-next" in command and getattr(self, "break_next", False):
            raise OSError("docker 不可用")
        mount = next(part for part in command if part.endswith(",target=/work"))
        output = Path(mount.split("source=", 1)[1].split(",target=", 1)[0])
        self.assertNotEqual(output, self.output)
        index = audit.load(output / f"{name}.index.json")
        self.assertEqual(len(index), 1)
        folder = output / f"reports/{name}/run"
        audit.save(folder / "report.json", {"schemaVersion": 1, "sources": [
            {"key": entry["key"], "name": "测试源", "version": "1.0.1",
             "sourceSha256": Path(entry["fileName"]).stem, "status": "passed", "stages": STAGES, "capabilities": []}
            for entry in index]})
        (folder / "source.trace.jsonl").write_text(json.dumps({"event": "http.request", "url": "https://example.com"}))
        return SimpleNamespace(returncode=0)

    def trial(self, updates, **options):
        audit.save(self.work / "artifact/discovery.json", {"updates": updates})
        with contextlib.redirect_stdout(io.StringIO()):
            return audit.trial_candidates(self.work, self.space.catalog(), self.metadata,
                                          self.sources, **options)

    def test_candidates_run_in_the_same_locked_down_container_with_the_existing_sample(self):
        known = {**self.space.candidate(), "trial": True}
        data = source("1.0.0", key="brand_new")
        fresh = {**self.space.serve(build(data, commit="e", file="new.js"), data), "trial": True}
        skipped = {**self.space.candidate("1.0.3"), "trial": False}
        records = self.trial([known, fresh, skipped])
        self.assertEqual(sorted((item["id"], item["runtimeProfile"]) for item in records), sorted(
            (item["id"], profile) for item in (known, fresh) for profile in audit.TRIAL_PROFILES))
        inputs = {item["id"]: item["inputs"] for item in records}
        self.assertEqual((inputs[known["id"]], inputs[fresh["id"]]), (SAMPLE, audit.DEFAULT_SAMPLE))
        self.assertFalse((self.sources / f"{skipped['id']}.js").exists())
        reviewed = audit.container_command(self.metadata, self.sources, self.output, 0, "venerax")
        for command in self.commands:
            for flag in ("--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges", "--no-env"):
                self.assertIn(flag, command)
            self.assertIn(f"type=bind,source={self.sources},target=/sources,readonly", command)
            self.assertFalse(any("TOKEN" in part or "docker.sock" in part for part in command))
            # 除了容器名和配置文件，隔离参数与已审阅构建完全相同。
            name = command[command.index("--name") + 1]
            profile = next(part for part in command if part.startswith("VENERA_CLIENT_PROFILE="))
            self.assertIn("PATROL_WORKER=/usr/local/bin/patrol-worker", command)
            self.assertIn("PATROL_WORKER=/usr/local/bin/patrol-worker", reviewed)
        mounts = [next(part for part in cmd if part.endswith(",target=/work")) for cmd in self.commands]
        self.assertEqual(len(set(mounts)), 4)

    def test_candidate_failures_stay_with_the_candidate_and_never_raise(self):
        good = {**self.space.candidate(), "trial": True}
        tampered = {**self.space.candidate("1.0.2"), "trial": True}
        self.space.files[tampered["url"]] = b"changed after discovery"
        unpinned = {**self.space.candidate("1.0.3"), "trial": True,
                    "url": "https://raw.githubusercontent.com/community/source/main/fixture.js"}
        self.break_next = True
        records = self.trial([good, tampered, unpinned])
        by_id = {}
        for item in records:
            by_id.setdefault(item["id"], {})[item["runtimeProfile"]] = item
        self.assertIn("source", by_id[good["id"]]["venerax"])
        self.assertIn("docker 不可用", by_id[good["id"]]["venera-next"]["error"])
        self.assertIn("SHA-256", by_id[tampered["id"]]["venerax"]["error"])
        self.assertIn("固定提交", by_id[unpinned["id"]]["venera-next"]["error"])
        self.assertEqual(len(self.commands), 2)

    def test_exhausted_time_budget_leaves_candidates_for_the_next_round(self):
        self.assertEqual(self.trial([{**self.space.candidate(), "trial": True}], budget=0), [])
        self.assertEqual(self.commands, [])


class InclusionTests(unittest.TestCase):
    def test_new_key_reaches_extended_subscription_without_account_grant(self):
        data = source("1.0.0", key="new_reader")
        candidate = self.space.serve(build(data, commit="f"), data)
        plan = self.space.root / "monitor/accounts.json"
        before = plan.read_bytes()
        payload = self.space.payload([candidate])
        for result in payload["candidateRecords"]:
            result["inputs"] = audit.DEFAULT_SAMPLE
            result["source"]["status"] = "failed"
            result["source"]["stages"] += [{"path": "comic.onClickTag", "status": "failed"}]
        state, results = self.space.publish(payload, [candidate])
        self.assertIsNone(state["pending"][0]["replaces"])
        self.assertEqual(results[candidate["id"]]["outcome"], "queued")
        entry, = self.space.promote()["added"]
        self.assertIsNone(entry["autoIncluded"]["replaces"])
        self.assertEqual(entry["sample"], {**audit.DEFAULT_SAMPLE, "comicId": "1", "epId": "2"})
        for result in payload["candidateRecords"]:
            result["inputs"] = entry["sample"]
        self.assertEqual(before, plan.read_bytes())
        old_pair = [record(self.space.old, profile) for profile in audit.TRIAL_PROFILES]
        formal = self.space.payload(records=[old_pair[0], payload["candidateRecords"][0]])
        formal["clientRecords"] = [old_pair[1], payload["candidateRecords"][1]]
        audit.publish(formal, self.space.root)
        self.assertEqual([row["key"] for row in audit.load(self.space.root / "subscriptions/extended.json")], ["new_reader"])

    def test_credential_changes_dynamic_hosts_and_mixed_runs_are_held(self):
        candidate = self.space.candidate(body='url = "https://example.com"; account = {loginWithCookies: {}}')
        self.assertEqual(self.space.gate(candidate)["reason"], "credentials")
        for field, value in (("networkHosts", ["stats.elsewhere.test"]), ("networkHosts", []),
                             ("accountCapabilities", ["account.loginWithCookies.validate"]),
                             ("trialRun", "earlier-run")):
            with self.subTest(field=field, value=value):
                payload = self.space.payload([self.candidate])
                payload["candidateRecords"][1][field] = value
                state, results = self.space.publish(payload, [self.candidate])
                self.assertEqual(state["pending"], [])
                self.assertEqual(results[self.candidate["id"]]["outcome"], "rejected")

    def test_source_repository_is_verified_before_fetch(self):
        outsider = {**self.candidate, "url": self.candidate["url"].replace("community/source", "other/unregistered")}
        traversal = {**self.candidate, "url": self.candidate["url"].replace("/fixture-", "/%2e%2e/fixture-")}
        for candidate in (outsider, traversal):
            audit.request.reset_mock()
            state, _ = self.queue(candidate)
            self.assertFalse(state["pending"])
            audit.request.assert_not_called()

    def test_new_key_with_duplicate_site_or_different_reading_samples_is_held(self):
        data = source("1.0.0", key="new_reader")
        candidate = self.space.serve(build(data, commit="f"), data)
        for conflict in ("site", "sample", "account"):
            with self.subTest(conflict=conflict):
                payload = self.space.payload([candidate])
                for entry in payload["candidateRecords"]:
                    entry["inputs"] = audit.DEFAULT_SAMPLE
                if conflict == "site":
                    payload["records"] = [record(self.space.old, "venerax")]
                elif conflict == "sample":
                    payload["candidateRecords"][1]["readSample"] = {"comicId": "other"}
                else:
                    payload["candidateRecords"][1]["accountCapabilities"] = ["account.login"]
                state, results = self.space.publish(payload, [candidate])
                self.assertEqual(state["pending"], [])
                self.assertEqual(results[candidate["id"]]["outcome"], "rejected")

    def setUp(self):
        self.space = Workspace(self)
        self.candidate = self.space.candidate()

    def queue(self, candidate=None, **options):
        candidate = candidate or self.candidate
        return self.space.publish(self.space.payload([candidate], **options), [candidate])

    def test_publish_queues_only_after_rechecking_and_never_writes_the_catalog_itself(self):
        before = (self.space.root / "monitor/catalog.json").read_bytes()
        state, results = self.queue()
        self.assertEqual((self.space.root / "monitor/catalog.json").read_bytes(), before)
        pending, = state["pending"]
        self.assertEqual((pending["candidate"]["id"], pending["replaces"], pending["replacesVersion"]),
                         (self.candidate["id"], self.space.old["id"], "1.0.0"))
        self.assertEqual(results[self.candidate["id"]]["outcome"], "queued")
        report = (self.space.root / "reports/CANDIDATES.md").read_text(encoding="utf-8")
        self.assertIn("1.0.0 → 1.0.1", report)

    def test_publish_rejects_evidence_that_does_not_match_pinned_bytes_or_both_clients(self):
        candidate = self.candidate
        wrong_hash = self.space.payload([candidate])
        wrong_hash["candidateRecords"][0]["source"]["sourceSha256"] = "0" * 64
        wrong_version = self.space.payload([candidate])
        wrong_version["candidateRecords"][1]["source"]["version"] = "9.9.9"
        wrong_sample = self.space.payload([candidate])
        wrong_sample["candidateRecords"][0]["inputs"] = {"keyword": "别的"}
        wrong_client = self.space.payload([candidate])
        wrong_client["candidateRecords"][0]["source"]["stages"][0]["output"]["value"] = json.dumps(
            {"name": "venerax", "repository": "forged/client", "commit": "0" * 40, "version": "1",
             "scope": "x", "bootstrapSha256": "0" * 64})
        one_sided = self.space.payload([candidate])
        del one_sided["candidateRecords"][1]
        for name, payload, outcome in (
            ("执行哈希不符", wrong_hash, "rejected"), ("实际加载版本不符", wrong_version, "rejected"),
            ("样本被换", wrong_sample, "rejected"), ("客户端身份不符", wrong_client, "rejected"),
            ("缺一端记录", one_sided, "error"),
            ("Venera-Next 未通过", self.space.payload(
                [candidate], failing={(candidate["id"], "venera-next")}), "failed"),
            ("VeneraX 未通过", self.space.payload(
                [candidate], failing={(candidate["id"], "venerax")}), "failed"),
        ):
            with self.subTest(name):
                state, results = self.space.publish(payload, [candidate])
                self.assertEqual((state["pending"], results[candidate["id"]]["outcome"]), ([], outcome))
        failed = results[candidate["id"]]["profiles"]["venerax"]
        self.assertEqual((failed["core"], failed["breakAt"]), (False, "image.decode"))

    def test_publish_recomputes_the_lane_instead_of_trusting_discovery(self):
        cases = {
            "下载到的字节变了": self.space.candidate("1.0.2"),
            "实际新增主机名": self.space.candidate("1.0.3", body='url = "https://tracker.example.org/"'),
            "版本并不更高": self.space.candidate("1.0.0", body='url = "https://example.com/same"'),
            "仓库未登记": self.space.candidate("1.0.4", repository="stranger/source"),
            "声明的 key 不符": {**self.space.candidate("1.0.5"), "key": "other"},
        }
        self.space.files[cases["下载到的字节变了"]["url"]] = source("1.0.2", 'url = "https://evil.test/"')
        details = {}
        for name, candidate in cases.items():
            with self.subTest(name):
                state, results = self.queue(candidate)
                self.assertEqual((state["pending"], results[candidate["id"]]["outcome"]), ([], "rejected"))
                details[name] = results[candidate["id"]]["detail"]
        self.assertIn("tracker.example.org", details["实际新增主机名"])
        self.assertIn("SHA-256", details["下载到的字节变了"])

    def test_trial_only_lane_is_reported_with_break_point_and_new_hosts_but_never_queued(self):
        candidate = self.space.candidate(body='url = "https://tracker.example.org/"')
        update = {**candidate, "lane": "trial", "reason": "new_hosts", "detail": "新增主机名：tracker.example.org",
                  "newHosts": ["tracker.example.org"]}
        state, results = self.space.publish(self.space.payload([candidate]), [update])
        self.assertEqual((state["pending"], results[candidate["id"]]["outcome"]), ([], "passed"))
        state, results = self.space.publish(self.space.payload(
            [candidate], failing={(candidate["id"], "venerax")}), [update])
        report = (self.space.root / "reports/CANDIDATES.md").read_text(encoding="utf-8")
        self.assertIn("tracker.example.org", report)
        self.assertIn("断在 image.decode：图片解码失败", report)
        self.assertEqual(state["pending"], [])

    def test_promote_rechecks_then_writes_the_entry_marked_as_automatic_and_keeps_the_old_build(self):
        self.queue()
        summary = self.space.promote()
        catalog = audit.validate_catalog(self.space.catalog())
        old, new = catalog["sources"]
        self.assertEqual([entry["id"] for entry in summary["added"]], [self.candidate["id"]])
        self.assertEqual((new["id"], new["version"], new["url"], new["sample"], new["repository"]),
                         (self.candidate["id"], "1.0.1", self.candidate["url"], SAMPLE, "community/source"))
        self.assertEqual((new["runtimeProfile"], new["verifyProfiles"]), ("venerax", ["venera-next"]))
        self.assertEqual({name: new["autoIncluded"][name] for name in ("replaces", "replacesVersion", "cliCommit")},
                         {"replaces": old["id"], "replacesVersion": "1.0.0", "cliCommit": "c" * 40})
        self.assertEqual(old["rollbackFor"], new["id"])
        state = audit.load(self.space.root / "data/auto-inclusion.json")
        self.assertEqual((state["pending"], list(state["builds"])), ([], [new["id"]]))
        # 稳定之前删掉旧构建，清单校验直接失败。
        with self.assertRaisesRegex(AssertionError, "稳定前必须保留"):
            audit.validate_catalog({**catalog, "sources": [new]})
        with self.assertRaisesRegex(AssertionError, "回退标记"):
            audit.validate_catalog({**catalog, "sources": [old]})

    def test_promote_rejects_a_queue_entry_that_no_longer_verifies_and_leaves_the_catalog_alone(self):
        before = (self.space.root / "monitor/catalog.json").read_bytes()
        state_path = self.space.root / "data/auto-inclusion.json"
        self.queue()
        queued = state_path.read_bytes()

        def tamper(change):
            state = json.loads(queued)
            change(state["pending"][0])
            audit.save(state_path, state)

        cases = {
            "队列里的记录被改成失败": lambda entry: entry["records"]["venera-next"]["source"]["stages"].pop(),
            "队列里的哈希被换": lambda entry: entry["candidate"].update(id="0" * 64, sha256="0" * 64),
            "地址不再固定": lambda entry: entry["candidate"].update(
                url="https://raw.githubusercontent.com/community/source/main/fixture.js"),
        }
        for name, change in cases.items():
            with self.subTest(name):
                tamper(change)
                summary = self.space.promote()
                self.assertEqual((summary["added"], len(summary["rejected"])), ([], 1))
                self.assertEqual((self.space.root / "monitor/catalog.json").read_bytes(), before)
        with self.subTest("固定地址上的字节变了"):
            state_path.write_bytes(queued)
            self.space.files[self.candidate["url"]] = b"changed"
            self.assertEqual(self.space.promote()["added"], [])
        with self.subTest("清单在排队之后已经有了更高版本"):
            state_path.write_bytes(queued)
            self.space.files[self.candidate["url"]] = source("1.0.1", 'url = "https://m.example.com/list"')
            self.space.catalog([{**self.space.old, "version": "1.0.1"}])
            self.assertEqual(self.space.promote()["added"], [])
            self.assertEqual(audit.load(state_path)["pending"], [])


class RollbackTests(unittest.TestCase):
    def setUp(self):
        self.space = Workspace(self)
        candidate = self.space.candidate()
        self.space.publish(self.space.payload([candidate]), [candidate])
        self.space.promote(datetime.fromisoformat(CHECKED))
        self.old, self.new = self.space.catalog()["sources"]
        self.moment = datetime.fromisoformat(CHECKED)

    def round(self, new_ok=True, old_ok=True, hours=1):
        """跑一轮真实的 publish：订阅选择、稳定计数都走正式代码。"""
        self.moment += timedelta(hours=hours)
        catalog = self.space.catalog()
        records, clients = [], []
        for item in catalog["sources"]:
            ok = new_ok if item["id"] == self.new["id"] else old_ok
            for profile in audit.TRIAL_PROFILES:
                (records if profile == "venerax" else clients).append(record(item, profile, ok))
        payload = {**self.space.payload(records=records), "clientRecords": clients,
                   "checkedAt": self.moment.isoformat()}
        with contextlib.redirect_stdout(io.StringIO()):
            audit.publish(payload, self.space.root)
            audit.publish_candidates(payload, {"updates": []}, self.space.root)
        index = audit.load(self.space.root / "subscriptions/index.json")
        return index, audit.load(self.space.root / "data/auto-inclusion.json")["builds"].get(self.new["id"])

    def test_subscription_falls_back_to_the_old_build_while_the_new_one_fails(self):
        index, build = self.round()
        self.assertEqual([(row["version"], row["url"]) for row in index], [("1.0.1", self.new["url"])])
        self.assertEqual((build["passes"], build["selected"]), (1, True))
        index, build = self.round(new_ok=False)
        self.assertEqual([(row["version"], row["url"]) for row in index], [("1.0.0", self.old["url"])])
        self.assertEqual((build["passes"], build["since"], build["selected"]), (0, None, False))
        self.assertIn("未选中新构建", (self.space.root / "reports/CANDIDATES.md").read_text(encoding="utf-8"))
        # 观察期内不会移除旧构建。
        self.space.promote()
        self.assertEqual(len(self.space.catalog()["sources"]), 2)
        index, build = self.round()
        self.assertEqual([row["version"] for row in index], ["1.0.1"])
        self.assertEqual(build["passes"], 1)

    def test_old_build_is_removed_only_after_enough_consecutive_rounds_and_days(self):
        for _ in range(audit.STABLE_PASSES + 5):
            _, build = self.round()
        # 轮数够了，天数不够。
        self.assertFalse(build["stable"])
        self.space.promote()
        self.assertEqual(len(self.space.catalog()["sources"]), 2)
        _, build = self.round(hours=24 * audit.STABLE_DAYS)
        self.assertTrue(build["stable"])
        summary = self.space.promote()
        self.assertEqual([item["id"] for item in summary["retired"]], [self.old["id"]])
        remaining, = audit.validate_catalog(self.space.catalog())["sources"]
        self.assertEqual((remaining["id"], bool(remaining["autoIncluded"]["stableAt"])), (self.new["id"], True))
        self.assertEqual(audit.load(self.space.root / "data/auto-inclusion.json")["builds"], {})

    def test_days_alone_are_not_enough_and_a_failure_restarts_the_count(self):
        _, build = self.round()
        _, build = self.round(hours=24 * (audit.STABLE_DAYS + 1))
        self.assertEqual((build["passes"], build["stable"]), (2, False))
        for _ in range(audit.STABLE_PASSES):
            _, build = self.round()
        self.assertTrue(build["stable"])
        _, build = self.round(new_ok=False)
        self.assertEqual((build["passes"], build["stable"]), (0, False))
        self.space.promote()
        self.assertEqual(len(self.space.catalog()["sources"]), 2)

    def test_builds_referenced_by_focus_notes_or_accounts_are_kept_after_stability(self):
        audit.save(self.space.root / "monitor/accounts.json", {
            "schemaVersion": 1, "sites": [{"key": "fixture", "buildId": self.old["id"]}]})
        for _ in range(audit.STABLE_PASSES):
            self.round()
        self.round(hours=24 * audit.STABLE_DAYS)
        self.assertEqual(self.space.promote()["retired"], [])
        old, new = audit.validate_catalog(self.space.catalog())["sources"]
        self.assertNotIn("rollbackFor", old)
        self.assertTrue(new["autoIncluded"]["stableAt"])


if __name__ == "__main__":
    unittest.main()
