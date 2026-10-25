# 隔离账号巡检结果

核验时间：2026-10-25T05:39:17.679499+00:00（UTC）。
最新 CLI 提交：`dd6ded39844e56902d3880b1fc1c201a6d1d1fda`。
每个源只接收本站凭据；同一固定源码及样本分别在 VeneraX、Venera-Next 执行。
不发布用户名、密码、Cookie、Token、收藏内容、异常原文或原始追踪。
登录通过表示源登录接口满足本次契约；阅读链路独立判断，不代替匿名订阅的收录结果。
没有接入账号 Secret 的源、无登录接口的源及未登记站点均如实标记。
绅士漫画只测试 Cookie 登录接口的缺凭据处理；本站密码不再注入，本人在客户端导入会话并完成会员页校验前，登录保持未验证。
不启用签到、评论、点赞、收藏增删和设置按钮等写操作；不保存跨次会话。

跳过和未执行不计入登录、核心阅读或整次通过。登录拒绝不等同于密码错误。

## 登录失败项

本轮没有已执行且失败的登录接口；未执行项另列。

## 已核对的登录流程差异

- 绅士漫画：Vensrc 独立维护版 1.3.1；网页登录成功后自动验证并保存会话，支持获取 Cookie 与从剪贴板一键导入；发布页备用地址每日同步。Actions 不注入本站密码、不接收会话，缺凭据不算登录通过。详见 WNACG_LOGIN.md。

## 登录未验证／跳过项

- 奇漫屋（`qimanwu`）：已保存凭据；当前审阅版本未提供 account.login，未注入密码。
- AGE动漫（`age_anime`）：已保存凭据；当前已审阅清单无本站源。
- 动漫屋（`dm5`）：已保存凭据；当前审阅版本未提供 account.login，未注入密码。
- 绅士漫画／venerax：登录跳过，不计通过。
- 绅士漫画／venera-next：登录跳过，不计通过。
- 18ak 漫画（`18ak`）：已保存凭据；当前已审阅清单无本站源。

## 全部账号结果

| 站点 | key | 环境 | 登录 | 核心阅读 | 整次 | 全部失败阶段及类别 | 跳过阶段数 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 漫画柜 | ManHuaGui | venerax | 通过 | 通过 | 部分通过 | 无失败 | 3 |
| 漫画柜 | ManHuaGui | venera-next | 通过 | 通过 | 部分通过 | 无失败 | 3 |
| 奇漫屋 | qimanwu | — | 已保存凭据；当前审阅版本未提供 account.login，未注入密码 | 未测试 | 跳过 |  | 未执行 |
| AGE动漫 | age_anime | — | 已保存凭据；当前已审阅清单无本站源 | 未测试 | 跳过 |  | 未执行 |
| 动漫屋 | dm5 | — | 已保存凭据；当前审阅版本未提供 account.login，未注入密码 | 未测试 | 跳过 |  | 未执行 |
| 绅士漫画 | wnacg | venerax | 跳过 | 通过 | 部分通过 | 无失败 | 13 |
| 绅士漫画 | wnacg | venera-next | 跳过 | 通过 | 部分通过 | 无失败 | 13 |
| 禁漫天堂 | jm | venerax | 通过 | 通过 | 部分通过 | 无失败 | 13 |
| 禁漫天堂 | jm | venera-next | 通过 | 通过 | 部分通过 | 无失败 | 13 |
| 包子漫画 | baozi | venerax | 通过 | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 2 |
| 包子漫画 | baozi | venera-next | 通过 | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 2 |
| 18ak 漫画 | 18ak | — | 已保存凭据；当前已审阅清单无本站源 | 未测试 | 跳过 |  | 未执行 |
| 哔咔漫画 | picacg | venerax | 通过 | 通过 | 部分通过 | 无失败 | 6 |
| 哔咔漫画 | picacg | venera-next | 通过 | 通过 | 部分通过 | 无失败 | 6 |
| 拷贝漫画 | copy_manga | venerax | 通过 | 未通过 | 失败 | settings：返回结构或样本不满足契约；search.load：源配置错误；explore[0].load：源配置错误；categoryComics.load：源配置错误；favorites.loadComics：源配置错误 | 11 |
| 拷贝漫画 | copy_manga | venera-next | 通过 | 未通过 | 失败 | settings：返回结构或样本不满足契约；search.load：源配置错误；explore[0].load：源配置错误；categoryComics.load：源配置错误；favorites.loadComics：源配置错误 | 11 |
| 热辣漫画 | hot_manga | venerax | 通过 | 通过 | 失败 | comic.onClickTag：源配置错误；comic.onClickTag：源配置错误 | 2 |
| 热辣漫画 | hot_manga | venera-next | 通过 | 通过 | 失败 | comic.onClickTag：源配置错误；comic.onClickTag：源配置错误 | 2 |

固定源码哈希、客户端提交、依赖锁和样本输入见 ../data/account-results.json。
Actions：https://github.com/laincat/vensrc/actions/runs/40166204159
