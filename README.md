# Vensrc

为 VeneraX 与 Venera-Next 整理、巡检社区漫画源。主订阅按 VeneraX 结果收录；Venera-Next 使用相同样本独立对照。

## 订阅

| 列表 | 固定地址 |
| --- | --- |
| 主订阅 | [index.json](https://github.com/laincat/vensrc/releases/latest/download/index.json) |
| 扩展订阅 | [extended.json](https://github.com/laincat/vensrc/releases/latest/download/extended.json) |

在客户端的漫画源仓库管理中添加订阅地址。两个地址是源列表，可同时添加；不要当成单个 JS 源导入。
[最新滚动 Release](https://github.com/laincat/vensrc/releases/latest)只上传以上两个 JSON，正文分别列出列表内每个源的名称、版本和来源仓库。

## 收录标准

- 核心阅读须在同一轮通过入口、详情、章节、图片下载和图片解码；跳过、未触发、缺凭据不算通过。
- 主订阅另要求整次巡检通过；扩展订阅可有其他能力失败或受限。
- 官方原版与转引排除。同 key 社区源必须严格高于官方版本，并独立通过巡检标准。
- 每份索引每个 key 只保留一个构建；固定样本、上游 Git 提交和源码 SHA-256 随巡检核对。

## 更新

GitHub Actions 每天香港时间 09:00 执行全量巡检、账号任务、浏览器诊断和 Release 校验。每轮从上游获取最新 `venera-patrol-cli`。页面能打开、账号登录成功或另一客户端通过，都不会替代阅读链路验证。

## 文档

- [订阅与版本规则](docs/订阅与版本规则.md)
- [巡检与自动化](docs/巡检与自动化.md)
- [双客户端结果](reports/CLIENT_RESULTS.md)
- [七个社区升级源与自用仓库](reports/FOCUS_RESULTS.md)
- [账号结果](reports/ACCOUNT_RESULTS.md) · [访问限制与人工验证](reports/ACCESS_RESULTS.md)
- [全量巡检报告](reports/RESULTS.md)
