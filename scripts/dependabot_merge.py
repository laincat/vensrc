"""Merge verified Dependabot patch/minor PRs after the exact head passed CI.

This script runs from the default branch under workflow_run; PR code is never
checked out with the write token. Major or unrecognized metadata fails closed.
"""
import json
import os
import re
import subprocess
from pathlib import Path


def api(endpoint, method="GET", **fields):
    args = ["gh", "api", endpoint, "--method", method]
    for key, value in fields.items():
        args.extend(["-f", f"{key}={value}"])
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return json.loads(result.stdout) if result.stdout.strip() else None


def eligible_commits(commits):
    if not commits:
        return False
    for commit in commits:
        if (commit.get("author") or {}).get("login") != "dependabot[bot]":
            return False
        data = commit["commit"]
        if not data.get("verification", {}).get("verified"):
            return False
        metadata = re.search(r"(?m)^---\nupdated-dependencies:\n(.*?)^\.\.\.$",
                             data["message"], re.S)
        if not metadata:
            return False
        types = re.findall(r"(?m)^  update-type: (\S+)\s*$", metadata[1])
        dependencies = re.findall(r"(?m)^- dependency-name: ", metadata[1])
        if not types or len(types) != len(dependencies):
            return False
        if any(t not in {"version-update:semver-patch",
                         "version-update:semver-minor"} for t in types):
            return False
    return True


def main():
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    run = event["workflow_run"]
    repo = os.environ["GITHUB_REPOSITORY"]
    if (run["conclusion"] != "success"
            or run["event"] not in {"pull_request", "workflow_dispatch"}
            or run["head_repository"]["full_name"] != repo):
        return
    sha = run["head_sha"]
    prs = api(f"repos/{repo}/commits/{sha}/pulls?per_page=100")
    for candidate in prs:
        number = candidate["number"]
        pr = api(f"repos/{repo}/pulls/{number}")
        if (pr["state"] != "open" or pr["draft"]
                or pr["user"]["login"] != "dependabot[bot]"
                or pr["head"]["repo"]["full_name"] != repo
                or pr["head"]["sha"] != sha
                or pr["base"]["ref"] != event["repository"]["default_branch"]):
            continue
        commits = api(f"repos/{repo}/pulls/{number}/commits?per_page=100")
        if len(commits) >= 100 or not eligible_commits(commits):
            print(f"PR #{number}: major/unrecognized/unverified update; review required")
            continue
        checks = api(f"repos/{repo}/commits/{sha}/check-runs?per_page=100")
        if (not any(c.get("name") == "校验脚本、收录标准与发布保护"
                    and c["status"] == "completed" and c["conclusion"] == "success"
                    for c in checks["check_runs"]) or checks["total_count"] > 100
                or any(c["status"] != "completed"
                       or c["conclusion"] not in {"success", "skipped", "neutral"}
                       for c in checks["check_runs"])):
            print(f"PR #{number}: checks incomplete or failed")
            continue
        status = api(f"repos/{repo}/commits/{sha}/status")
        if status["total_count"] and status["state"] != "success":
            print(f"PR #{number}: commit status incomplete or failed")
            continue
        subprocess.run(["gh", "pr", "merge", str(number), "--repo", repo,
                        "--squash", "--delete-branch",
                        "--match-head-commit", sha], check=True)
        print(f"Merged PR #{number} after successful validation of {sha}")
        # GITHUB_TOKEN merges do not trigger push workflows. Dispatch the build
        # explicitly so the upgrade reaches the published output.
        subprocess.run(["gh", "workflow", "run", os.environ["POST_MERGE_WORKFLOW"],
                        "--repo", repo, "--ref", pr["base"]["ref"]], check=True)
        subprocess.run(["gh", "workflow", "run", "patrol.yml",
                        "--repo", repo, "--ref", pr["base"]["ref"]], check=True)


if __name__ == "__main__":
    main()
