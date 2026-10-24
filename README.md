# Vensrc

Venera + source：以 VeneraX 为主、同时对照 Venera-Next 的社区漫画源订阅与巡检项目。

本仓库发布经过 Venera Runtime 和 venera-patrol-cli 有限样本巡检的社区漫画源索引。主要使用场景为 VeneraX；两个 Fork 的接口与验证范围见 [客户端兼容性](reports/CLIENT_COMPATIBILITY.md)，中文结果、源名称和固定漫画／章节 ID 见 [复测摘要](reports/RESULTS.md)。

## 订阅地址

| 订阅 | 地址 | 收录条件 |
| --- | --- | --- |
| 主订阅 | [index.json](https://github.com/laincat/vensrc/releases/latest/download/index.json) | 同次巡检的核心阅读链路及全部执行项通过 |
| 扩展订阅 | [extended.json](https://github.com/laincat/vensrc/releases/latest/download/extended.json) | 同次巡检的核心阅读链路通过，其他能力可能失败或跳过 |

[最新 Release](https://github.com/laincat/vensrc/releases/latest)严格只提供 `index.json` 和 `extended.json` 两个附件。下载地址固定，快照标签可以变化；两个附件下载回读与 SHA-256 校验通过后才删除旧版，最终只保留一个 Release。哈希写入 Release 正文，中文报告和完整证据保留在仓库。分支上的备用地址为 [主索引](https://raw.githubusercontent.com/laincat/vensrc/main/subscriptions/index.json) 和 [扩展索引](https://raw.githubusercontent.com/laincat/vensrc/main/subscriptions/extended.json)。

在 VeneraX 的漫画源库管理中添加对应索引 URL，或在 Venera-Next 的漫画源仓库页添加；两者当前源码均支持保存多个库，可同时添加主、扩展订阅。较旧客户端若只有漫画源列表 URL 设置，则切换列表地址使用。主、扩展索引没有重复 key。这里的地址是源列表，不能当作单个 JS 源导入。

索引每项均提供 `url`，指向经过核验的上游固定 Git 提交。不会把 GitHub 的 HTML 页面地址当 JS 地址。源的名称、版本、最低应用版本、SHA-256 和固定巡检样本见 [锁定清单](data/sources.lock.json)。

列表持续更新与已安装源升级是两个步骤。当前核对的 VeneraX 优先使用来源库解析出的下载地址，Next 为已关联仓库的源读取仓库索引地址；从本订阅库安装并保留来源关联，才能沿用索引内固定提交的更新地址。未关联库、直接导入或旧版客户端可能回退到源 JS 自身的 `url`；部分社区源将它写成站点首页，此时升级可能失败，需要从列表提供的 JS 地址重新导入。本仓库没有改写上游脚本的 `url`。

## 通过的含义

核心链路要求在同一次 CLI 巡检中通过：搜索、发现或分类入口至少一个，随后是详情、章节、实际图片下载与图片解码。每源只抽查 1 页和 1 张正文图片，结果不代表所有漫画、所有章节、全部地区或全部账号功能。

主索引整次报告必须为 `passed`；扩展索引可能仍有搜索、分类、标签、评论、封面或账号等能力未通过。扩展源不是“完整可用”的承诺。索引中可能包含写真或图集源，名称保留上游标识。

匿名订阅巡检不提供账号凭据。独立账号任务只向白名单源分发本站 Secret，见 [脱敏账号报告](reports/ACCOUNT_RESULTS.md)；两类任务均不启用写操作。`source.load` 通过、核心阅读通过、Venera UI 导入成功、用户设备实际阅读成功是不同的验证范围。本索引已验证 CLI 和格式；未在用户设备验证 UI 导入与阅读。

本订阅排除直接来自 `venera-app/venera-configs` 的官方原版和转引。社区源沿用官方 key 时，**版本必须严格高于官方版本基线**，再按原有主／扩展巡检标准收录；同版、低版和无法比较的版本继续排除。不同 key 按原标准审核，不因版本数字较大就自动通过。

版本按三段数字逐段比较，例如 `1.10.0 > 1.9.9`，不使用字符串排序。官方 `jm` 基线为 `1.4.0`，BB-CHICKEN `1.9.2` 满足版本门槛，是否进入主／扩展订阅仍取决于本轮真实巡检。锁定清单对这类社区替代源记录 `officialVersion`，便于核对比较依据。

索引条目的 `description` 用于注明来源仓库，例如 `引用源：JunQianNuo/venera-sources`。BB-CHICKEN `jm` 1.9.2 的短注释直接摘自该构建对应的 [上游 CHANGELOG](https://github.com/BB-CHICKEN/venera-jm/blob/a266ff026e08e6c5f17516664ffc0b90c91164a1/CHANGELOG.md)，通过收录条件时同样保留该备注。

官方版本及其依据的官方索引提交、原始字节哈希见 [官方版本基线](data/official-exclusions.json)。每轮检测读取官方最新索引，追加 key 并提高基线；历史基线不降低。Release 发布前再次读取官方最新索引，如果某个已选社区版不再严格高于官方，即阻止发布，待按新基线重新生成。

本订阅的主、扩展索引内部仍合计每个 key 只选择一个构建；同 key 的高版本社区源可与官方库同时出现在可选来源中，安装后作为该 key 的替代版本使用。VeneraX 按 key 检查已安装源，Next 在同一仓库存在多个同 key 条目且无法按原 URL 唯一匹配时报告歧义，因此不把不同版本全部堆入同一订阅。不同 key 仍可能是同一网站的别名。

## 更新安排

已迁移到 [GitHub Actions](https://github.com/laincat/vensrc/actions/workflows/patrol.yml)，按香港时间每天 09:00（UTC 01:00）运行，也可在 Actions 页面手动执行。修改巡检脚本或审阅清单后会自动触发。无需本机或 Codex 在线；GitHub 定时运行可能有延迟，以 Actions 记录为准。

完整巡检成功后执行访问诊断；诊断报告发布成功后，[滚动 Release 工作流](https://github.com/laincat/vensrc/actions/workflows/release.yml)核对同轮的索引、客户端、账号与访问证据，再生成附件。发布器先创建草稿，上传并下载两个订阅附件逐一核对 SHA-256；通过后才设为最新并清理旧 Release 和对应标签。上传或校验失败时保留上一次完整的公开 Release，不把缺失或跳过的结果计为通过。相同附件快照重跑会复用同一标签。

Release 附件白名单严格为 `index.json`、`extended.json`；不打包原始追踪、账号状态、账号结果 JSON、本地密码文件、Cookie 或 Token。不会镜像上游 JS 或漫画内容。

**每次巡检前更新 venera-patrol-cli 到上游默认分支最新提交**，使用该提交的 `package-lock.json` 安装依赖并构建独立容器。巡检开始前再次核对上游 HEAD。获取、安装或报告格式检查失败时停止本次发布，不回退到缓存旧版。中文报告和 `data/audit-status.json` 记录 CLI 提交、版本、依赖锁 SHA-256、Node 版本和运行地址。

全部已审阅构建均加载固定提交的 VeneraX 原始 JS bootstrap，并以完全相同的固定输入逐个对照 Venera-Next；三个自用仓库优先执行。版本取自各自真实 `pubspec.yaml`，不降低源最低版本、不修改旧 Runtime 版本。订阅仅按 VeneraX 本次结果收录，Next 成功不能替代 X 失败。适配层、客户端源码哈希及逐阶段结果见 [客户端兼容清单](reports/CLIENT_RESULTS.md) 和 `data/client-results.json`。

固定漫画与章节 ID 保存在 `monitor/catalog.json`；每个构建的 JS URL 固定到 Git 提交，下载字节 SHA-256 必须与已审阅清单完全相同。源码只在没有 GitHub 凭据、没有 Docker socket、源码只读的容器中运行；匿名容器不提供账号；账号容器只获得本站凭据，临时会话在运行后删除；均不启用 mutations。发布放在另一个有写权限的 job，重新核对清单哈希、源码哈希及主／扩展标准，只提交生成的 JSON、中文 CSV 和报告。

上游变更检测覆盖登记社区仓库及 GitHub 仓库搜索，官方仓库只作为版本基线的元数据依据，不进入候选列表。新字节只下载、计算哈希和读取声明，不加载或执行；待审阅版本见 [上游变更报告](reports/UPDATES.md) 和 `data/pending-updates.json`。维护者在 GitHub 审阅固定提交代码后，将对应构建加入 `monitor/catalog.json`，后续 Actions 会自动巡检并按结果和版本门槛收录。这一步不需要本机在线，也不会以自动扫描替代代码审阅。

最新复测核心链路失败时从对应订阅移除，不用旧成功结果冒充当前通过；全批核心失败或批量下载异常则停止发布，避免一次 runner 故障清空订阅。同 key 的不同构建分别巡检，先过滤官方原版及未高于官方的社区构建，再优先选核心通过、整次通过的构建，最后按自用仓库优先级及版本选择。失败构建仍保留在中文清单。

三个自用仓库作为重点跟踪对象：`hea784/venera-configs`、`BB-CHICKEN/venera-jm`、`handahao666-boop/venera_comic_source`。它们的逐构建结果在中文报告中单列；具体格式及客户端兼容性见 [自用源说明](reports/OWN_SOURCES.md)。

## 目录与依赖自动化

根目录保留 README 和 Git 配置；`subscriptions/` 保存两份订阅，`reports/` 保存中文说明及报告，`data/` 保存锁定清单、CSV 和结构化证据，`monitor/` 保存已审阅源码、固定样本和账号白名单，`scripts/` 保存生成器及测试。

参考 laincat/AwesomePyKit 与 laincat/Rules 的方式，Dependabot 每天香港时间 09:00 检查 GitHub Actions 依赖，minor／patch 分组合并，major 留待人工审阅。独立 CI 检查 Python 测试、跳过项门槛、发布保护及最新 CLI 上的双客户端接口；合并脚本只接受 Dependabot 已验证签名的提交，并复核 PR 当前提交与所有检查。缺失、失败或跳过的必要 CI 不会自动合并，合并后显式触发新一轮 CI 和全量巡检。

上游 CLI 每轮重新获取最新版本，不由 Dependabot 锁定；没有新增无对应清单的 pip／npm 自动更新配置。

## 报告与维护

- [七个社区替代源与自用仓库重点结果](reports/FOCUS_RESULTS.md)：按固定构建列出双客户端、账号登录及本轮订阅去向。
- [中文巡检报告](reports/RESULTS.md)：逐构建结果、固定样本的核心链路、主／扩展名单。
- [中文完整清单](data/sources.zh.csv)：VeneraX 主环境的源版本、样本输入、首个失败阶段及源码哈希。
- [双客户端中文清单](data/client-compatibility.zh.csv)：每个构建在 VeneraX 与 Venera-Next 的独立结果；[对照报告](reports/CLIENT_RESULTS.md)单列全量统计、核心阅读差异及逐阶段状态差异。
- [反爬与人工处理清单](reports/ACCESS_RESULTS.md)：独立 Actions 的正常浏览器对照、仍需本人验证的站点和全部受限阶段；不会改变订阅资格。
- [账号巡检与 Secrets](reports/ACCOUNT_TESTING.md)：按站点隔离的 Secrets、源码白名单与脱敏规则；[账号结果](reports/ACCOUNT_RESULTS.md)单列登录失败、未验证／跳过项和全部失败阶段，独立于匿名订阅。
- `data/audit-status.json`：本次执行环境、工具版本和 Actions 运行链接。
- Actions 的 `venera-patrol-results` artifact：结构化逐阶段证据及中文预览，保留 30 天；不上传原始 trace 或认证状态。
- `monitor/catalog.json`：已审阅源码及固定样本；不要通过修改 `minAppVersion` 或伪造通过阶段绕过兼容性问题。

已有源的固定样本变化也应在清单中审阅后提交，不因某本漫画临时不可读而自动替换成未记录的样本。仓库只发布元数据与报告，不发布漫画图片或上游 JS 镜像。

## 上游与范围

- [VeneraX（主要使用的客户端）](https://github.com/Kyosee/VeneraX)
- [Venera-Next（全量同样本对照客户端）](https://github.com/CyrilPeng/Venera-Next)
- [Venera 官方索引](https://github.com/venera-app/venera-configs)
- [Venera 源格式](https://github.com/venera-app/venera/blob/master/doc/comic_source.md)
- [venera-patrol-cli](https://github.com/Gandum2077/venera-patrol-cli)

本仓库只发布索引、源码引用和审计摘要，不镜像漫画内容，也不修改或重新分发上游 JS。GitHub 未公开、未索引或尚未被搜索到的来源可能遗漏，不能声称已经穷尽全部漫画源。

## Cloudflare 等访问限制

适配层按两套客户端真实拦截器识别 `403` 加 `cf-mitigated: challenge`，明确报告反爬验证；普通 403 不自动认定为 Cloudflare 或密码错误。客户端的 Flutter WebView 验证、Cookie 与浏览器身份同步不能用 Node 版本号替代。

[反爬诊断工作流](https://github.com/laincat/vensrc/actions/workflows/access.yml)在完整巡检成功后执行，也可手动触发。它使用最新 CLI 锁定的浏览器依赖，对已审阅的 4 个公开首页和绅士漫画的 2 个公开登录页执行无账号的正常浏览器诊断，只等待页面自身脚本、不点击验证码；结果与真实阅读链路分开。浏览器可访问不使 CLI 失败的源自动进入订阅。绅士漫画的最终域名、站点自建滑块及旧源登录流程差异见 [专项诊断](reports/WNACG_LOGIN.md)。

需要人工时，优先在 VeneraX 自带验证窗口完成正常验证，再在相同网络环境重试。通行 Cookie 不能保证从本机搬到 GitHub runner 后仍有效；长期云端受限需要站点允许的访问方式或出口稳定的独立远程验证环境。未部署此类远程环境，不依赖本机恢复在线来维持基础定时巡检。
