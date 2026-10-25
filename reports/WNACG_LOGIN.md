# 绅士漫画网页登录与客户端验证

核对日期：2026-10-25（香港时间）。独立源 `wnacg 1.3.2`，来源 `laincat/vensrc`。固定样本 `397513`、关键词“火影”、最低应用版本 `1.3.4` 保留。

## 更正此前结论

1.3.1 的源设置“获取 Cookie”只能读取 App 请求库已经保存的会话；“自动填入”读取剪贴板。这没有完成用户要求的“在 App 网页内完成登录后直接捕获会话”，也没有修复网页滑块被横滑返回抢走的问题。

VeneraX 原版已有 WebView Cookie 自动导入机制，不需要修改客户端即可在源识别到特定私有页后导入 Cookie 并标记登录。新增网页捕获按钮、关闭抢先触发的返回手势，以及等待 App 请求核验完成后再接受登录，才需要修改客户端。本项目当前按“不修改 VeneraX”推进，只使用原版支持的私有页触发方案。

## 参考实现和真实页面

核对 `Gandum2077/venera-configs` 的 `ai` 分支、提交 `cbde997745bb9891d2c53ae1c1265f34ba562384`（2026-10-24，`wnacg 1.0.12`）：

- 网页登录固定使用 `https://www.wnacg.com/users-login.html`，导入源时不读取尚未注册的设置。
- 登录后在站点里打开“我的收藏”，识别 `users-users_fav.html` 或 `users-index.html`，标题同时包含站点名和“我的空间／我的空間”。
- 排除空标题、登录、权限、滑块和 CF 挑战页面。成功回调保持同步，适应原版 VeneraX 不等待异步回调的行为。
- 账号请求固定到登录域名；备用阅读域名不能接收主域名的 Cookie。

本次用正常浏览器访问了未登录的 `users-users_fav.html`：页面标题为空，正文显示“您沒有權限，需要登錄”，没有退出登录链接。因此只看 URL、HTTP 200 或 Cookie 存在都会误判。

`BB-CHICKEN/venera-jm 1.9.2` 使用 JM 的 `/login` API，收到有效 `uid` 后登录；它没有 WebView 捕获或滑块手势处理。其会话管理可参考，但网络异常／5xx 返回 `true` 不能当作本次登录已验证。详细对照见 [客户端说明](../clients/venerax/README.md)。

## 1.3.2 的两种路径

| 路径 | 操作和状态 | 仍需验证 |
| --- | --- | --- |
| 原版 VeneraX／Venera-Next | 本人在 App 内网页登录、完成滑块，然后点站点内“我的收藏”。匹配真实私有页后，由客户端导入 Cookie，源保存原登录域名 | 这是 `browser_only`；App 读取收藏前还会请求会员页校验。按钮和横滑冲突没有因此得到修复 |
| 带本仓库补丁的 VeneraX | 页面加载后尝试自动捕获；网页顶部另有“获取 Cookie 并登录”。从原生 CookieManager 读取 HttpOnly Cookie，等待 App HTTP 校验，再持久化并关闭网页 | 需通过原生集成测试和本人设备的真实账号验收，不能仅凭源码或 CLI 宣称可用 |

两条路径均不要求从外部浏览器复制 Cookie。原版的触发操作是**网页内的“我的收藏”**，不要在未触发时直接点 App 左上角返回；普通返回不会同步会话。

`webLoginVerification` 单独记录：

- `browser_only`：私有页识别与 Cookie 导入完成，未冒充 App HTTP 权限验证。
- `http_verified`：App 请求 `users-users_fav.html`，确认本站退出登录链接且无权限提示、无 CF 挑战后才记录。

在 VeneraX 原版中，客户端先把 WebView Cookie 写入 App CookieJar，再调用源的同步成功回调，随后将账号标记为已登录。源无法控制这一原生导入时机，也不能自行添加 WebView 按钮或关闭 App 的返回手势。缺 Cookie、登录页、匿名页、5xx、网络故障或挑战页都不能作为新的服务端登录验证成功。

源设置中的 Cookie 导出和剪贴板导入保留为手动后备，不再把它们描述为网页内捕获。Cookie 不回显、不上传到 Actions 或报告。

## 客户端补丁与证据边界

补丁及固定基线见 [clients/venerax](../clients/venerax/README.md)。它禁用登录页的 App 横滑返回和 WebKit 前后导航手势，将拖动交给 WebView；增加捕获按钮；保留 Cookie 的 HttpOnly、有效期和路径；失败恢复原 App 会话，成功才返回。

`VeneraX 原生网页登录验证` 使用真实 iPhone 模拟器和 WKWebView，但账号来自明确标记的本地测试站点。它可以验证原生管线，不能冒充绅士漫画的真实账号／滑块验收。2026-10-25 首轮静态检查和 CookieJar 测试通过，首次 iOS 集成构建在 `Pods_Runner` 链接处失败，App 未启动；后续补丁构建任务依照“不修改 VeneraX”的要求取消。因此没有补丁版 WKWebView 集成结果，也没有生成测试包。

当前电脑没有 VeneraX 或手机镜像。用户设备上的滑块、真实账号登录、返回后的会话及重启持久化尚未验收。必须保留这个结论，不能用 CLI 阅读通过替代。

## 发布页和备用地址

- 内置 `www.wnacg.com`、`www.wnacg.ru`；发布页曾公布 `www.wn003.cfd`、`www.wn004.cfd`。
- 使用 `wnacg01.link` 和 `wnacg02.link`，距上次成功同步满 24 小时再刷新；设置页也可手动刷新。
- 只收录受限域名格式的 HTTPS 漫画地址；失败保留缓存，不把广告或发布页当漫画服务器。
- 切换阅读地址不搬运 Cookie；账号请求通过 `accountBaseUrl` 留在实际登录域名。登录标记清除后需重新确认会话。
- 发布页列出、浏览器能打开和登录交互模块存在均不等于可用性通过。访问结果见 [访问报告](ACCESS_RESULTS.md)。

## 云端巡检和源码追溯

每天 Actions 获取最新 CLI，以两个客户端的固定接口独立测试固定阅读样本。本站密码 Secret 不注入，浏览器 Cookie 不上传；Cookie 登录缺凭据、WebView 需交互、按钮未执行均按跳过记录，不算通过。阅读结果见 [客户端报告](CLIENT_RESULTS.md)，账号结果见 [账号报告](ACCOUNT_RESULTS.md)。

仅保留本仓库的独立 `wnacg`，不重新加入其他绅士漫画构建。参考源的版本、最低应用版本和更新 URL 不直接覆盖本项目设置。

源码提交：`abd2b560b7cc8b6acdcdb1e7ddfba3330d4a3a89`。

源码 SHA-256：`07c835c5d58545f088c35a3eae43fc65c1231436ded26a6857e1563223cbee81`。
