# VeneraX／Venera-Next 固定样本对照结果

核验时间：2026-10-24T02:03:23.142990+00:00（UTC）。
最新上游 CLI 提交：`dd6ded39844e56902d3880b1fc1c201a6d1d1fda`；同时加载本仓库记录哈希的接口适配层。
结果为 Node 宿主上的真实客户端 JS 接口巡检，不代表 Flutter UI 或用户设备实测。

## Kyosee/VeneraX 2.3.6

- 源：`jm` 1.9.2；最低版本 `1.16.0`（保持原声明）。
- 客户端接口提交：`a4e20b9f14061fd333e89ca31c6458571e7a7e00`。
- 源码 SHA-256：`e50a45d1c3b33198ab3a154335c31f4e689652106135dcc367334a3325b8be3d`。
- 固定样本：`{"keyword": "火影", "comicId": "1485211", "epId": "ep_1485211"}`。
- 核心链路：通过；整次状态：部分通过。

| 阶段 | 状态 | 类别／说明 |
| --- | --- | --- |
| runtime.load | 通过 |  |
| source.load | 通过 |  |
| configuration.apply | 通过 |  |
| init | 通过 |  |
| configuration.capabilities | 通过 |  |
| account.login | 跳过 | Provide credentials.username and password |
| category | 通过 |  |
| settings | 通过 |  |
| search.load | 通过 |  |
| explore[0].load | 通过 |  |
| categoryComics.optionLoader | 通过 |  |
| categoryComics.load | 通过 |  |
| categoryComics.ranking.load | 通过 |  |
| favorites.loadFolders | 跳过 | 网络收藏需要已登录的账号 |
| favorites.loadComics | 跳过 | 网络收藏需要已登录的账号 |
| comic.loadInfo | 通过 |  |
| comic.loadEp | 通过 |  |
| comic.loadComments | 通过 |  |
| comic.loadChapterComments | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.idMatch | 通过 |  |
| comic.onImageLoad | 通过 |  |
| image.download | 通过 |  |
| comic.onImageLoad.modifyImage | 通过 |  |
| image.decode | 通过 |  |
| comic.onImageLoad.onLoadFailed | 跳过 | 图片已成功，未触发失败恢复回调 |
| comic.onThumbnailLoad | 通过 |  |
| thumbnail.download | 通过 |  |
| thumbnail.decode | 通过 |  |
| account.logout | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| favorites.addOrDelFavorite | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| favorites.addFolder | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| favorites.deleteFolder | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| comic._makeImageRetry | 跳过 | No automatic adapter; provide cases[path].args and expect |
| comic.likeComic | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| comic.sendComment | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| comic.sendChapterComment | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.refreshDomains.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.optimizeNodes.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.imageSpeedTest.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.dailyCheckIn.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |

## CyrilPeng/Venera-Next 1.18.0

- 源：`jm` 1.9.2；最低版本 `1.16.0`（保持原声明）。
- 客户端接口提交：`47f7416cecc2dbbc97c7618f8dd53aa92f587601`。
- 源码 SHA-256：`e50a45d1c3b33198ab3a154335c31f4e689652106135dcc367334a3325b8be3d`。
- 固定样本：`{"keyword": "火影", "comicId": "1485211", "epId": "ep_1485211"}`。
- 核心链路：通过；整次状态：部分通过。

| 阶段 | 状态 | 类别／说明 |
| --- | --- | --- |
| runtime.load | 通过 |  |
| source.load | 通过 |  |
| configuration.apply | 通过 |  |
| init | 通过 |  |
| configuration.capabilities | 通过 |  |
| account.login | 跳过 | Provide credentials.username and password |
| category | 通过 |  |
| settings | 通过 |  |
| search.load | 通过 |  |
| explore[0].load | 通过 |  |
| categoryComics.optionLoader | 通过 |  |
| categoryComics.load | 通过 |  |
| categoryComics.ranking.load | 通过 |  |
| favorites.loadFolders | 跳过 | 网络收藏需要已登录的账号 |
| favorites.loadComics | 跳过 | 网络收藏需要已登录的账号 |
| comic.loadInfo | 通过 |  |
| comic.loadEp | 通过 |  |
| comic.loadComments | 通过 |  |
| comic.loadChapterComments | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.onClickTag | 通过 |  |
| comic.idMatch | 通过 |  |
| comic.onImageLoad | 通过 |  |
| image.download | 通过 |  |
| comic.onImageLoad.modifyImage | 通过 |  |
| image.decode | 通过 |  |
| comic.onImageLoad.onLoadFailed | 跳过 | 图片已成功，未触发失败恢复回调 |
| comic.onThumbnailLoad | 通过 |  |
| thumbnail.download | 通过 |  |
| thumbnail.decode | 通过 |  |
| account.logout | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| favorites.addOrDelFavorite | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| favorites.addFolder | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| favorites.deleteFolder | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| comic._makeImageRetry | 跳过 | No automatic adapter; provide cases[path].args and expect |
| comic.likeComic | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| comic.sendComment | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| comic.sendChapterComment | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.refreshDomains.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.optimizeNodes.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.imageSpeedTest.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
| settings.dailyCheckIn.callback | 跳过 | 默认禁用写操作，且没有显式写操作用例 |
