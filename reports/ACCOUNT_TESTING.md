# 账号巡检与 Actions Secrets

绅士漫画浏览器可登录、旧源接口仍失败的原因，以及最终域名和滑块验证差异，见 [绅士漫画登录诊断](WNACG_LOGIN.md)。

## 已接入的方式

凭据按站点分别保存在仓库 Settings → Secrets and variables → Actions 中，公开仓库只保存 Secret 名称、站点映射和已审阅源码哈希。原始密码文件不进入仓库、日志或 artifact。

定时及手动工作流都运行独立的 `account_patrol` job。每次重新获取最新 CLI 并安装其原始锁定依赖，校验客户端提交及文件哈希。随后每个站点、每个客户端各启动一个容器，只传入本站的 `PATROL_AUTH`，不传 GitHub 凭据和其他站点凭据。

账号与匿名巡检分别记录结果。主／扩展订阅仍只依据匿名 VeneraX 的当次结果，收录标准不变；Venera-Next 和账号结果均不能替代 X 的失败。

## 站点与 Secrets

| 站点 | 源 key | Secret 名称 | 执行范围 |
| --- | --- | --- | --- |
| 漫画柜 | ManHuaGui | PATROL_AUTH_MANHUAGUI | 白名单源码的账号登录及只读巡检 |
| 绅士漫画 | wnacg | PATROL_AUTH_WNACG | 同上；不将凭据交给“绅士会所”等不同站点 |
| 禁漫天堂 | jm | PATROL_AUTH_JM | 1.9.2；关闭 dailyCheckInTask |
| 包子漫画 | baozi | PATROL_AUTH_BAOZI | 白名单源码的账号登录及只读巡检 |
| 哔咔漫画 | picacg | PATROL_AUTH_PICACG | 同上 |
| 拷贝漫画 | copy_manga | PATROL_AUTH_COPY_MANGA | 同上；不自动交给其他同站别名 |
| 热辣漫画 | hot_manga | PATROL_AUTH_HOT_MANGA | 同上 |
| 奇漫屋 | qimanwu | PATROL_AUTH_QIMANWU | 已保存；当前审阅版本无 account.login，不注入 |
| 动漫屋 | dm5 | PATROL_AUTH_DM5 | 已保存；当前审阅版本无 account.login，不注入 |
| AGE动漫 | age_anime | PATROL_AUTH_AGE | 已保存；已审阅清单暂缺本站源 |
| 18ak 漫画 | 18ak | PATROL_AUTH_18AK | 已保存；已审阅清单暂缺本站源 |

可执行构建的完整哈希在 `monitor/accounts.json`。每站只选择已审阅的一个构建，避免为重复版本反复登录；仍分别在两套客户端环境巡检。新增源或切换账号构建需要更新白名单，不能凭相似显示名称分配密码。

每个 Secret 是只包含本站授权键的 JSON，以下仅为占位格式：

```json
{"jm":{"credentials":{"username":"在 Secret 中填写","password":"在 Secret 中填写"}}}
```

账号任务只接受 `credentials.username/password`，不允许 Secret 注入源码、覆盖固定样本或启用写操作。Cookie、Token 或验证码应按源的真实接口独立适配；账号密码不保证足以登录。

## 报告、隔离与限制

结果见 [中文账号报告](ACCOUNT_RESULTS.md) 和 `account-results.json`。只保留站点、固定源码哈希、客户端、固定输入、阶段状态和失败类别；删除阶段返回值及原始异常文本。即使源把密码放进返回值或异常，也不会原样进入公开报告。

不向 Actions 日志转发账号容器的 stdout/stderr；不上传网络 trace、Cookie、Token、`.patrol-state` 或源保存的数据。私有临时目录在每次容器结束后删除，源码单独只读挂载。不保存跨次会话，不需要管理仓库 Secrets 的写入令牌。

仅执行登录及只读能力，保持 mutations 关闭，不触发签到、评论、点赞、收藏增删或设置按钮。登录通过表示源的登录接口满足本次契约，不能单凭这一项宣称账号所有权限正常；核心阅读链路另行检查。

固定提交与哈希保证执行对象可追溯，不能把社区 JS 变成 Flutter 客户端或强安全沙箱。当前只向明确绑定且已审阅的站点源码分发本站凭据。

参考：[CLI 授权配置](https://github.com/Gandum2077/venera-patrol-cli#授权配置)、[GitHub Actions Secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)。
