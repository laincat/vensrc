# Venera 可用源订阅索引

本仓库发布经过 Venera Runtime 和 venera-patrol-cli 有限样本巡检的社区漫画源索引。中文结果、源名称和固定漫画／章节 ID 见 [复测摘要](RESULTS.md)。

## 订阅地址

| 订阅 | 地址 | 收录条件 |
| --- | --- | --- |
| 主订阅 | [index.json](https://raw.githubusercontent.com/laincat/venera-source-index/main/index.json) | 同次巡检的核心阅读链路及全部执行项通过 |
| 扩展订阅 | [extended.json](https://raw.githubusercontent.com/laincat/venera-source-index/main/extended.json) | 同次巡检的核心阅读链路通过，其他能力可能失败或跳过 |

在 Venera 的漫画源列表 URL 设置中填入对应地址，再进入漫画源列表添加源。主、扩展索引没有重复 key；如需查看扩展源，可切换列表地址。这里的地址是源列表，不能当作单个 JS 源导入。

索引每项均提供 `url`，指向经过核验的上游固定 Git 提交。不会把 GitHub 的 HTML 页面地址当 JS 地址。源的名称、版本、最低应用版本、SHA-256 和固定巡检样本见 [锁定清单](sources.lock.json)。

## 通过的含义

核心链路要求在同一次 CLI 巡检中通过：搜索、发现或分类入口至少一个，随后是详情、章节、实际图片下载与图片解码。每源只抽查 1 页和 1 张正文图片，结果不代表所有漫画、所有章节、全部地区或全部账号功能。

主索引整次报告必须为 `passed`；扩展索引可能仍有搜索、分类、标签、评论、封面或账号等能力未通过。扩展源不是“完整可用”的承诺。索引中可能包含写真或图集源，名称保留上游标识。

没有提供账号凭据，不启用写操作。`source.load` 通过、核心阅读通过、Venera UI 导入成功、用户设备实际阅读成功是不同的验证范围。本索引已验证 CLI 和格式；未在用户设备验证 UI 导入与阅读。

某些社区版本沿用官方 key。锁定清单中的 `officialKey: true` 表示可能与已安装的官方同 key 源冲突或替换；不同 key 也可能是同一网站的别名。

## 更新安排

由本地维护任务每周一 09:00（香港时间）检查上游和 GitHub 新来源，调整关键词、复核固定漫画样本，再生成并发布索引。新代码先审阅后运行；更新失败不记为成功。维护机器需在线且工作区可访问，仓库自身没有定时运行器。

源码 URL 固定到已验证的提交；只有新版本复测并通过后才更新索引。最新复测核心链路失败时从对应订阅移除，不用旧成功结果冒充当前通过。公开文件的提交时间和摘要中的巡检时间可用于判断新鲜度。

## 上游与范围

- [Venera 官方索引](https://github.com/venera-app/venera-configs)
- [Venera 源格式](https://github.com/venera-app/venera/blob/master/doc/comic_source.md)
- [venera-patrol-cli](https://github.com/Gandum2077/venera-patrol-cli)

本仓库只发布索引、源码引用和审计摘要，不镜像漫画内容，也不修改或重新分发上游 JS。GitHub 未公开、未索引或尚未被搜索到的来源可能遗漏，不能声称已经穷尽全部漫画源。
