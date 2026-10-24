# 隔离账号巡检结果

核验时间：2026-10-24T02:35:11.922038+00:00（UTC）。
最新 CLI 提交：`dd6ded39844e56902d3880b1fc1c201a6d1d1fda`。
每个源只接收本站凭据；同一固定源码及样本分别在 VeneraX、Venera-Next 执行。
不发布用户名、密码、Cookie、Token、收藏内容、异常原文或原始追踪。
登录通过表示源登录接口满足本次契约；阅读链路独立判断，不代替匿名订阅的收录结果。
没有接入账号 Secret 的源、无登录接口的源及未登记站点均如实标记。
不启用签到、评论、点赞、收藏增删和设置按钮等写操作；不保存跨次会话。

| 站点 | key | 环境 | 登录 | 核心阅读 | 整次 | 首个失败类别 |
| --- | --- | --- | --- | --- | --- | --- |
| 漫画柜 | ManHuaGui | venerax | 通过 | 通过 | 部分通过 |  |
| 漫画柜 | ManHuaGui | venera-next | 通过 | 通过 | 部分通过 |  |
| 奇漫屋 | qimanwu | — | 已保存凭据；当前审阅版本未提供 account.login，未注入密码 | 未测试 | 跳过 |  |
| AGE动漫 | age_anime | — | 已保存凭据；当前已审阅清单无本站源 | 未测试 | 跳过 |  |
| 动漫屋 | dm5 | — | 已保存凭据；当前审阅版本未提供 account.login，未注入密码 | 未测试 | 跳过 |  |
| 绅士漫画 | wnacg | venerax | 失败 | 通过 | 失败 | 需要登录 |
| 绅士漫画 | wnacg | venera-next | 失败 | 通过 | 失败 | 需要登录 |
| 禁漫天堂 | jm | venerax | 通过 | 通过 | 部分通过 |  |
| 禁漫天堂 | jm | venera-next | 通过 | 通过 | 部分通过 |  |
| 包子漫画 | baozi | venerax | 通过 | 通过 | 失败 | 返回结构或样本不满足契约 |
| 包子漫画 | baozi | venera-next | 通过 | 通过 | 失败 | 返回结构或样本不满足契约 |
| 18ak 漫画 | 18ak | — | 已保存凭据；当前已审阅清单无本站源 | 未测试 | 跳过 |  |
| 哔咔漫画 | picacg | venerax | 通过 | 通过 | 部分通过 |  |
| 哔咔漫画 | picacg | venera-next | 通过 | 通过 | 部分通过 |  |
| 拷贝漫画 | copy_manga | venerax | 通过 | 未通过 | 失败 | 返回结构或样本不满足契约 |
| 拷贝漫画 | copy_manga | venera-next | 通过 | 未通过 | 失败 | 返回结构或样本不满足契约 |
| 热辣漫画 | hot_manga | venerax | 通过 | 通过 | 失败 | 源配置错误 |
| 热辣漫画 | hot_manga | venera-next | 通过 | 通过 | 失败 | 源配置错误 |

固定源码哈希、客户端提交、依赖锁和样本输入见 account-results.json。
Actions：https://github.com/laincat/venera-source-index/actions/runs/40054649606
