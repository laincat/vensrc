# VeneraX、Venera-Next 与巡检工具的兼容范围

源码核对日期：2026-10-24（香港时间）。实际巡检状态以每次生成的 [客户端对照结果](CLIENT_RESULTS.md) 为准。

## 是否可以共用漫画源

两个 Fork 都继承原版的 `ComicSource`、`Comic`、`ComicDetails`、`Network`、`Convert`、图片加载回调和源列表格式。使用这些共同接口的源通常可以共用；不能由此保证全部源、所有版本和登录功能通用。

本次核对以下固定提交。它们对应核对时默认分支的源码版本；发行包和用户已安装版本需要另行核对。

| 项目 | 源码版本 | 固定提交 | 关键实现 |
| --- | --- | --- | --- |
| [VeneraX](https://github.com/Kyosee/VeneraX) | 2.3.6 | `a4e20b9f14061fd333e89ca31c6458571e7a7e00` | `assets/init.js`、`lib/foundation/js_engine.dart`、`lib/foundation/comic_source/parser.dart` |
| [Venera-Next](https://github.com/CyrilPeng/Venera-Next) | 1.18.0 | `47f7416cecc2dbbc97c7618f8dd53aa92f587601` | `assets/init.js`、`lib/foundation/js_engine.dart`、`lib/features/comic_source/parser.dart` |
| [venera-runtime](https://github.com/Gandum2077/venera-runtime) | npm 0.1.2 | 由每次最新 CLI 的 package-lock.json 锁定 | 默认 `APP.version` 为原版 1.6.3 |

两个客户端各自将应用版本注入 `APP.version`，各自用语义版本检查源的 `minAppVersion`。所以 `1.16.0` 在 Next 表示其版本门槛；X 的 `2.3.6` 数值更大，只能说明可以越过版本检查，不能证明实现了 Next 的全部能力。

已确认的差异包括：当前 Next 用 `__sourceRuntime` 和 `source_id` 校验源实例身份，并处理替换、回滚及异步回调生命周期；X 没有同样的身份桥接，另在解析源后修正源自带的 `isAppVersionAfter` 比较函数。遇到依赖这些差异的源，应分别测试。Node 巡检也不能替代 Flutter、QuickJS、WebView、平台网络栈、UI 及异步销毁的实测。

## BB-CHICKEN/venera-jm 1.9.2 的适配

上游声明最低版本 `1.16.0`，维护说明面向 Venera-Next。源 JS 保持固定提交、原始字节和最低版本，不替换为同 key 的旧版成功结果。

本仓库已把以下对照扩展到全部已审阅构建；JM 继续保留原来的固定样本：

- 首选环境为 VeneraX 2.3.6，按用户主要使用的客户端判断该构建是否具备收录资格。
- 同一源码、同一漫画 `1485211`、同一章节 `ep_1485211`、关键词“火影”，额外在 Next 1.18.0 环境复测。
- 两边都从各自提交下载原始 `assets/init.js`，与 `pubspec.yaml`、Dart 宿主及解析器一起核对 SHA-256；`APP.version` 使用同提交的真实源码版本，不覆盖旧 Runtime 的 `APP.version`。
- 网络、Cookie、源内本地状态、UTF-8、Base64、MD5、AES-ECB 及图片裁切／拼接由显式 `sendMessage` 桥接执行。Next 的存储消息核对实例身份。未实现的宿主消息报 `runtime_unsupported`，不返回伪成功。
- 图片修改用该客户端原始 `Image` 类调用真实图片后端，下载并解码正文图片；不以图片 URL 存在替代图片验证。
- 明确关闭 `dailyCheckInTask`，不提供账号、不签到、不发送评论、不修改网络收藏。源初始化中的公开域名与图片 CDN 刷新按原有逻辑执行。

适配测试覆盖最低版本拒绝、原版仍拒绝该源、Next 过期实例拒绝、HTTP 参数传递、真实 AES 解密，以及已知像素矩阵的切块重排。测试中的固定图片仅用于验证算法；源可用性仍必须通过实际网络巡检。

`monitor/clients.json` 保存客户端提交及接口文件哈希。客户端升级需要重新核对接口并更新锁定清单；不会只改一个版本号来接受新声明。

## 原版 CLI 能否兼容两个 Fork

截至本次核对，最新上游 `Gandum2077/venera-patrol-cli` 为 `dd6ded39844e56902d3880b1fc1c201a6d1d1fda`，依赖 `venera-runtime 0.1.2`。未经适配时，它提供原版 1.6.3 的 Node 运行环境，不能直接加载声明最低 1.16.0 的这个源，也没有完整的 VeneraX／Next 客户端模式。

本仓库每次巡检仍先获取上游默认分支最新 CLI，并使用其原始锁文件安装。随后添加本仓库透明记录哈希的客户端适配层，报告同时记录 CLI 提交、依赖锁、适配层哈希和客户端提交。因此“最新上游 CLI”和“本仓库接口适配”分别可追溯；不把适配归功于上游已经支持。

最新 CLI 的注入位置变化、依赖安装失败、客户端文件哈希不符或适配测试失败，均停止该次运行，不回退旧工具。巡检前再次核对上游 HEAD，确保本次工具仍是最新。

## 订阅怎么选

主／扩展订阅继续按原标准生成：主订阅要求核心阅读链路和整次执行通过；扩展订阅要求同次入口、详情、章节、图片下载和解码通过，其他能力允许失败或跳过。

`jm 1.9.2` 的主记录明确使用 VeneraX 环境，Next 对照另行保留；Next 成功不能替代 X 失败。该版本只有当次 X 核心通过才有收录资格。若它失败，同 key 的其他已审阅构建仍按各自当次结果参与选择；报告不会把旧版本结果写成 1.9.2 成功。

全部 316 个已审阅构建现均配置 `runtimeProfile: venerax`、`verifyProfiles: [venera-next]`，逐个执行两套客户端接口巡检。清单优先执行三个自用仓库；具体完成时间、核心链路及失败类别以 CLIENT_RESULTS.md 为准，不因进入执行清单就认定兼容。两个客户端使用同一份固定输入；源码字节和最低版本声明保持不变。订阅始终仅按 VeneraX 当次证据收录，Next 不参与替代选择。用户设备上的导入、实际阅读、账号与地区网络仍需客户端实测。

两个 Fork 当前源码都能保存多个源库，主／扩展索引可以同时添加。X 的索引解析及下载地址优先规则见固定提交的 `lib/pages/comic_source_page.dart`、`lib/foundation/comic_source_update_tasks.dart`；Next 的格式校验和来源关联见 `lib/features/comic_source/source_repositories.dart`。它们都优先读取非空 `url`，其次使用 `fileName`，与本订阅结构一致。

源更新路径也已经与原版不同：X 优先使用来源库解析出的下载 URL；Next 对已关联仓库的源重新读取该仓库索引，未关联时才回退源 JS 自带 URL。因此建议从添加后的订阅库内安装，并保留来源关联。此前仅依据原版得出的“更新只读取源 JS 自带 URL”不适用于这两份当前 Fork 源码。

## 全量接口与隔离账号任务

全量适配增加客户端原始 HTML 包装类及对应 Dart 消息桥接、HMAC、AES-CBC/CFB/OFB、随机数和 UUID。VeneraX 源解析后的 `isAppVersionAfter` 修正取自锁定且校验哈希的 Dart parser 脚本，不改写源 JS。未实现消息继续明确失败。两份客户端的 `HtmlNode.toElement` JS 消息拼写与 Dart 分支不同，按实际不兼容报告，不补造成功。

`compute` 只验证 Node 中函数计算与参数传递，不模拟 Flutter 隔离线程、实例销毁或平台调度。账号巡检使用独立 job；每个白名单源的每个客户端独立容器仅获得本站 Secret，不接收其他站点或 GitHub 发布凭据。公开产物删除所有返回值、原始异常和 trace，仅保留阶段状态、受信任标识、哈希及固定输入。匿名结果仍独立决定主／扩展订阅。
