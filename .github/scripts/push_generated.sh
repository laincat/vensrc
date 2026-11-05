#!/usr/bin/env bash
# 提交已暂存的生成结果并推到 main：冲突时以本轮生成结果为准，失败退避重试。
#
# 为什么需要它：巡检（patrol.yml）与反爬诊断（access.yml）是两个独立工作流，
# 都会把生成文件写回 main。两边各自的 `git pull --rebase` 一旦撞车，就会在
# data/、reports/、subscriptions/ 上产生冲突，把已经跑完的巡检判红
# （2026-11-04 13:23 就因此失败）。这里把推送收敛成一个步骤：先 fetch 再
# rebase，冲突时保留本轮生成的版本（rebase 的 -X theirs），推送失败则退避重试。
set -euo pipefail

message="${1:?用法: push_generated.sh <提交说明>}"
attempts="${PUSH_ATTEMPTS:-5}"
credential='!gh auth git-credential'

if git diff --cached --quiet; then
  echo "没有需要提交的变更"
  exit 0
fi

git commit -m "$message"

for attempt in $(seq 1 "$attempts"); do
  git -c credential.helper="$credential" fetch --quiet origin main
  # 本提交只含脚本生成物，冲突时以本轮结果为准。
  git -c credential.helper="$credential" pull --rebase -X theirs --quiet origin main
  if git -c credential.helper="$credential" push --quiet origin HEAD:main; then
    echo "已推送 $(git rev-parse --short HEAD)（第 $attempt 次尝试）"
    exit 0
  fi
  echo "第 $attempt 次推送失败，退避后重试" >&2
  sleep $((attempt * 5))
done

echo "连续 $attempts 次推送失败，保留本地提交 $(git rev-parse --short HEAD)" >&2
exit 1
