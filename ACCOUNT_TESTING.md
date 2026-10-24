# 账号巡检与 Actions Secrets

## 当前状态

GitHub Actions Secrets 可以保存站点用户名、密码、Cookie 或 Token。当前公开定时巡检**没有读取站点登录 Secret**；添加 Secret 只会保存凭据，不会自动启用登录。本轮所有报告均未使用账号。

最新 `venera-patrol-cli` 已支持通过 `PATROL_AUTH` 提供账号授权，但本仓库还需要接入独立的账号巡检任务、源白名单和按站点分配凭据，才能用于实际测试。不会把一份包含所有站点账号的 Secret 交给全部社区源。

## 可以准备的格式

进入本订阅仓库的 **Settings → Secrets and variables → Actions → New repository secret**，名称可使用 CLI 的标准名称 `PATROL_AUTH`，值为 JSON。下面全部是占位文字，需要在 GitHub 页面填写实际值；不要把真实值发在聊天、Issue、PR、公开配置或提交中。

```json
{
  "jm": {
    "credentials": {
      "username": "在 GitHub Secret 中填写用户名",
      "password": "在 GitHub Secret 中填写密码"
    }
  }
}
```

可以按相同格式增加其他站点条目。一级键是授权条目名，须与将来巡检配置的 `auth` 字段一致；不是任意填写网站显示名称。接入工作流时只提取本次选定站点的一项，传给对应源的巡检容器。

也可以分别保存每个站点的 Secret，减少维护时误用；具体名称应在接入工作流时统一。添加完成后，只需要告知 Secret 名称及对应站点，不需要也不应提供 Secret 值。

## 不同登录方式的范围

| 登录方式 | CLI 授权字段 | 条件 |
| --- | --- | --- |
| 用户名／密码 | `credentials.username`、`credentials.password` | 源实现 `account.login` |
| 源提供的 Cookie 登录表单 | `credentials.cookieValues` | 字段须与该源 `account.loginWithCookies.fields` 一致 |
| 浏览器导出的 Cookie | `credentials.cookies` | 保留正确的 URL、域、路径及安全属性，格式按 CLI 文档核对 |
| 浏览器 Token | `credentials.browserToken` | `dataKey` 必须是该源实际读取的字段 |
| 验证码、二步验证、交互式 WebView | 没有跨站统一的自动登录方式 | 账号密码可能不足，需要真实有效的 Cookie 或 Token；不能伪造成功页面作为登录证明 |

Cookie、Token 也属于登录凭据。账号登录应使用独立的手动任务，只执行明确选定且源码哈希已审阅的构建；测试真实登录、会话有效性和阅读权限。默认仍禁用签到、评论、点赞、收藏增删及设置按钮等写操作。

## 报告与隔离要求

账号任务应与公开匿名定时巡检分开，保留源码哈希、固定漫画样本及每次获取最新 CLI 的要求。每个容器仅获得该站点所需的凭据，不接收 GitHub 发布凭据。

公开报告仅记录脱敏后的阶段状态与故障类别，不发布用户名、密码、Cookie、Token、私有状态文件或原始追踪。会话持久化属于后续独立功能，不需要为一次登录测试额外提供管理仓库 Secrets 的令牌。

Secrets 的加密保存和日志遮蔽不使社区 JS 成为安全沙箱。账号巡检仍只执行经过审阅、固定提交且哈希匹配的源码；建议使用专门测试账号。

参考：[venera-patrol-cli 授权配置与登录方式](https://github.com/Gandum2077/venera-patrol-cli#授权配置)、[GitHub Actions Secrets 官方说明](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)。
