# VeneraX 原生网页登录补丁

此处保存客户端补丁和独立验证流程。基线固定为 VeneraX 2.3.7 的 `058451b03daae1c45ce9bab054251ebd5e36a03a`，补丁 SHA-256 见 `manifest.json`。这不是 VeneraX 上游已经发布的功能。

## 已确认的原版问题

- 原生网页只有“在浏览器中打开、复制链接、重载”，没有获取 Cookie 的入口。
- 普通返回只关闭网页，不同步会话。源设置中的 `Network.getCookies` 只能读取 App 请求库已保存的 Cookie，不能从仍打开的 WebView 直接取出 Cookie。
- 原流程依赖 URL／标题触发。站点登录后若跳到首页，或事件在跳转之前触发，便可能不执行会话同步。
- 原生解析器和页面均未等待 `onLoginSuccess` 返回的异步校验，页面会提前关闭。
- 登录页面使用默认 `AppPageRoute`，iOS 的 App 横滑返回识别器可能抢走网页滑块。

## 补丁流程

1. 源声明 `loginWithWebview.captureCookies`，且客户端提供 `APP.webviewCookieCapture`。
2. App 内登录页禁用 App 的横滑返回和 WebKit 前后导航手势，把拖动交给原生 WebView。
3. 网页加载、历史变化后尝试同步；右上方同时显示“获取 Cookie 并登录”，可主动重试。
4. 通过系统 CookieManager 读取同域 Cookie，包括 HttpOnly；不使用 `document.cookie`、剪贴板或外部浏览器。
5. 同步到 App 的 CookieJar，保存浏览器 User-Agent，等待源通过 App 请求会员页核验登录。
6. 验证通过才持久化账号和会话、关闭网页。验证失败保留网页，恢复旧 Cookie 的所有路径及原有账号数据。

除固定登录域名外的网页不能触发捕获。原版客户端不因只看到会员 URL 就被算作登录通过。Linux 的独立桌面 WebView 不包含在本补丁入口内。

## 验证边界

`VeneraX 原生网页登录验证` 是手动触发的 Actions，使用固定上游源码和已校验补丁，不读取漫画站账号或浏览器会话：

- Dart 静态检查与真实 SQLite CookieJar 的成功、失败、重启恢复测试。
- iPhone 模拟器上的真实 WKWebView：本地测试站点的横向滑块、匿名拒绝、HttpOnly Cookie 自动同步、App 侧 HTTP 验证、返回后持久化。
- 测试明确使用本地站点和测试数据，不能冒充绅士漫画真实账号登录或真实站点滑块通过。
- 通过后可生成未签名 iOS 测试包，保存在 Actions artifact。它不加入订阅 Release，安装仍需要本人签名。

当前电脑没有 VeneraX 或手机镜像窗口。用户设备的站点滑块、真实账号、网络绑定及 App 返回后会话仍需本人验证；未完成时不能把此功能报告为“实机已可用”。

仓库的 `subscriptions/` 仍按阅读证据生成；`venera-patrol-cli` 只能检查源接口，不能替代这些原生与实机验证。

## BB-CHICKEN 的参考范围

已核对 `BB-CHICKEN/venera-jm` 当前提交 `a266ff026e08e6c5f17516664ffc0b90c91164a1`，版本 1.9.2，文件 `recode-jm.js` 的 SHA-256 为 `e50a45d1c3b33198ab3a154335c31f4e689652106135dcc367334a3325b8be3d`。

该实现使用 `account.login` 调用 JM 的 `/login` API，取得 `uid` 后接受登录；`get/post` 遇到明确的会员失效响应才抛出 `Login expired`。它不提供 `loginWithWebview`、网页 Cookie 捕获按钮或滑块手势处理，因此不能用于证明原版 VeneraX 能完成绅士漫画的网页会话同步。

可参考其 App 请求会话管理、登录返回值核验及明确的失效处理。但 `_verifyLogin()` 在 5xx 和网络异常时返回 `true`，只能理解为暂不使原有状态失效，不能当作本次账号校验通过。当前补丁在这些情况下不接受新的登录成功，保留网页并恢复原 App 会话。
