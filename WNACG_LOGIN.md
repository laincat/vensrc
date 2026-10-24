# 绅士漫画：浏览器可登录与源登录失败的差异

核对日期：2026-10-24（香港时间）。用户已确认正常浏览器可以登录；本报告不据 CLI 的 `auth_required` 断言账号或密码错误。

## 公开接口核对

| 项目 | 本次观察 |
| --- | --- |
| 用户提供的主域名 | `wnacg.com`、`wnacg.ru` |
| 用户提供的发布页 | `https://wnacg01.link/`，本次可取得 HTTP 200 |
| 两个主域名的登录提交地址 | 不带 `www` 的 `/users-check_login.html` 均以 HTTP 301 跳转到各自带 `www` 的相同路径 |
| 浏览器登录页 | `https://www.wnacg.com/users-login.html`、`https://www.wnacg.ru/users-login.html` |
| 表单 | POST `/users-check_login.html`；字段含 `normal`、`login_name`、`login_pass`、`remember_pass` |
| 新的交互流程 | 登录页加载 `/statics/js/slider-captcha.js`；脚本接管登录提交，先由本人完成滑块验证，再提交一次性 `slider_pass` |
| 与 Cloudflare 的关系 | 该模块是站点自建滑块，不能仅因登录失败就归为 CF 挑战 |

以上使用不含账号的公开 GET／HEAD 请求核对；没有提交密码、点击滑块或获取通行票据。浏览器诊断 Actions 另记录两个公开登录页的实际可访问性及滑块模块是否出现。

## 固定源与客户端适配的边界

已审阅源为官方 `wnacg 1.0.6`，固定提交 `a04e05591f7832f7166d6660546613c114d6738a`，JS 的 SHA-256 为 `545a6d818d012c1e5799d6aaf7ecd09798969acb840166ee7c56de6d02201df0`。

该源默认域名为 `wnacg.com`；`account.login` 只提交 `login_name`、`login_pass`，随后要求 JSON 的 `html` 包含“登錄成功”。源码没有取得或提交 `slider_pass` 的实现。即使 CLI 正确实现两个客户端的网络接口，也不会自动补上源本身缺失的交互登录流程。

本次将该构建的巡检设置固定为自定义域名 `www.wnacg.com`，先排除登录 POST 遇到 301 跳转的影响。浏览器／Fetch 对 POST 的 301 跳转可能改用 GET，因此不能把浏览器已经到达最终域名后的登录和源直接提交裸域名视为同一个请求。没有修改上游 JS、最低版本、成功判断或固定漫画样本。

域名设置修正后的实际结果见 `ACCOUNT_RESULTS.md`；公开登录页诊断见 `ACCESS_RESULTS.md`。需要滑块的项目继续记为未完成交互，不把页面可打开当作账号登录通过，也不使用代解或伪造票据。

## 用户侧处理

可以继续使用本人已成功登录的正常浏览器。VeneraX 中若该源支持自定义域名，可先设为 `www.wnacg.com` 或 `www.wnacg.ru`；这只修正地址跳转，不保证旧源可以完成新增的滑块。

让自动巡检取得真实登录成功，需要源提供可用的正常 WebView 登录接口或站点允许的认证接口，再分别核对 VeneraX 与 Venera-Next 的会话接入方式。当前固定源只有账号密码登录和登出接口，没有 Cookie／WebView 登录接口；本次未增加浏览器会话导入，也未把浏览器 Cookie 当作通用的 Actions 凭据。
