# Venera 可用源订阅索引

本仓库发布经过 Venera Runtime 和 venera-patrol-cli 有限样本巡检的社区漫画源索引。主要使用场景为 VeneraX；两个 Fork 的接口与验证范围见 [客户端兼容性](CLIENT_COMPATIBILITY.md)，中文结果、源名称和固定漫画／章节 ID 见 [复测摘要](RESULTS.md)。

## 订阅地址

| 订阅 | 地址 | 收录条件 |
| --- | --- | --- |
| 主订阅 | [index.json](https://raw.githubusercontent.com/laincat/venera-source-index/main/index.json) | 同次巡检的核心阅读链路及全部执行项通过 |
| 扩展订阅 | [extended.json](https://raw.githubusercontent.com/laincat/venera-source-index/main/extended.json) | 同次巡检的核心阅读链路通过，其他能力可能失败或跳过 |

在 VeneraX 的漫画源库管理中添加对应索引 URL，或在 Venera-Next 的漫画源仓库页添加；两者当前源码均支持保存多个库，可同时添加主、扩展订阅。较旧客户端若只有漫画源列表 URL 设置，则切换列表地址使用。主、扩展索引没有重复 key。这里的地址是源列表，不能当作单个 JS 源导入。

索引每项均提供 `url`，指向经过核验的上游固定 Git 提交。不会把 GitHub 的 HTML 页面地址当 JS 地址。源的名称、版本、最低应用版本、SHA-256 和固定巡检样本见 [锁定清单](sources.lock.json)。

列表持续更新与已安装源升级是两个步骤。当前核对的 VeneraX 优先使用来源库解析出的下载地址，Next 为已关联仓库的源读取仓库索引地址；从本订阅库安装并保留来源关联，才能沿用索引内固定提交的更新地址。未关联库、直接导入或旧版客户端可能回退到源 JS 自身的 `url`；部分社区源将它写成站点首页，此时升级可能失败，需要从列表提供的 JS 地址重新导入。本仓库没有改写上游脚本的 `url`。

## 通过的含义

核心链路要求在同一次 CLI 巡检中通过：搜索、发现或分类入口至少一个，随后是详情、章节、实际图片下载与图片解码。每源只抽查 1 页和 1 张正文图片，结果不代表所有漫画、所有章节、全部地区或全部账号功能。

主索引整次报告必须为 `passed`；扩展索引可能仍有搜索、分类、标签、评论、封面或账号等能力未通过。扩展源不是“完整可用”的承诺。索引中可能包含写真或图集源，名称保留上游标识。

没有提供账号凭据，不启用写操作。`source.load` 通过、核心阅读通过、Venera UI 导入成功、用户设备实际阅读成功是不同的验证范围。本索引已验证 CLI 和格式；未在用户设备验证 UI 导入与阅读。

某些社区版本沿用官方 key。锁定清单中的 `officialKey: true` 表示可能与已安装的官方同 key 源冲突或替换；不同 key 也可能是同一网站的别名。

## 更新安排

已迁移到 [GitHub Actions](https://github.com/laincat/venera-source-index/actions/workflows/patrol.yml)，按香港时间每周一 09:00（UTC 周一 01:00）运行，也可在 Actions 页面手动执行。修改巡检脚本或审阅清单后会自动触发。无需本机或 Codex 在线；GitHub 定时运行可能有延迟，以 Actions 记录为准。

**每次巡检前更新 venera-patrol-cli 到上游默认分支最新提交**，使用该提交的 `package-lock.json` 安装依赖并构建独立容器。巡检开始前再次核对上游 HEAD。获取、安装或报告格式检查失败时停止本次发布，不回退到缓存旧版。中文报告和 `audit-status.json` 记录 CLI 提交、版本、依赖锁 SHA-256、Node 版本和运行地址。

`jm 1.9.2` 另加载固定提交的 VeneraX 原始 JS bootstrap，并以相同固定样本对照 Venera-Next；版本取自各自真实 `pubspec.yaml`，不降低源最低版本、不修改旧 Runtime 版本。最新 CLI 加载的本仓库适配层、客户端源码哈希及逐阶段结果见 [客户端对照报告](CLIENT_RESULTS.md) 和 `client-results.json`。其他构建暂保留原版 Runtime 验证范围。

固定漫画与章节 ID 保存在 `monitor/catalog.json`；每个构建的 JS URL 固定到 Git 提交，下载字节 SHA-256 必须与已审阅清单完全相同。源码只在没有 GitHub 凭据、没有 Docker socket、源码只读的容器中运行；不提供账号，不启用 mutations。发布放在另一个有写权限的 job，重新核对清单哈希、源码哈希及主／扩展标准，只提交生成的 JSON、中文 CSV 和报告。

上游变更检测覆盖登记仓库及 GitHub 仓库搜索。新字节只下载、计算哈希和读取声明，不加载或执行；待审阅版本见 [上游变更报告](UPDATES.md) 和 `pending-updates.json`。维护者在 GitHub 审阅固定提交代码后，将对应构建加入 `monitor/catalog.json`，后续 Actions 会自动巡检并按结果收录。这一步不需要本机在线，也不会以自动扫描替代代码审阅。

最新复测核心链路失败时从对应订阅移除，不用旧成功结果冒充当前通过；全批核心失败或批量下载异常则停止发布，避免一次 runner 故障清空订阅。同 key 的不同构建分别巡检，最终优先选核心通过、整次通过的构建，再按自用仓库优先级及版本选择。失败构建仍保留在中文清单。

三个自用仓库作为重点跟踪对象：`hea784/venera-configs`、`BB-CHICKEN/venera-jm`、`handahao666-boop/venera_comic_source`。它们的逐构建结果在中文报告中单列；具体格式及客户端兼容性见 [自用源说明](OWN_SOURCES.md)。

## 报告与维护

- [中文巡检报告](RESULTS.md)：逐构建结果、固定样本的核心链路、主／扩展名单。
- [中文完整清单](sources.zh.csv)：源版本、样本输入、首个失败阶段及源码哈希。
- [账号巡检与 Secrets](ACCOUNT_TESTING.md)：可准备的凭据格式；当前匿名定时任务尚未接入账号 Secret。
- `audit-status.json`：本次执行环境、工具版本和 Actions 运行链接。
- Actions 的 `venera-patrol-results` artifact：结构化逐阶段证据及中文预览，保留 30 天；不上传原始 trace 或认证状态。
- `monitor/catalog.json`：已审阅源码及固定样本；不要通过修改 `minAppVersion` 或伪造通过阶段绕过兼容性问题。

已有源的固定样本变化也应在清单中审阅后提交，不因某本漫画临时不可读而自动替换成未记录的样本。仓库只发布元数据与报告，不发布漫画图片或上游 JS 镜像。

## 上游与范围

- [VeneraX（主要使用的客户端）](https://github.com/Kyosee/VeneraX)
- [Venera-Next（JM 同样本对照客户端）](https://github.com/CyrilPeng/Venera-Next)
- [Venera 官方索引](https://github.com/venera-app/venera-configs)
- [Venera 源格式](https://github.com/venera-app/venera/blob/master/doc/comic_source.md)
- [venera-patrol-cli](https://github.com/Gandum2077/venera-patrol-cli)

本仓库只发布索引、源码引用和审计摘要，不镜像漫画内容，也不修改或重新分发上游 JS。GitHub 未公开、未索引或尚未被搜索到的来源可能遗漏，不能声称已经穷尽全部漫画源。
