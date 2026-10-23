# Venera 漫画源复测摘要

生成时间：2026-10-23T09:04:30.547796+00:00（UTC）。
所有时间以证据中的时间戳为准；香港时间为 UTC+8。

- 盘点 261 个构建、260 个唯一 runtime key。
- 主索引 25 项；扩展索引 59 项。
- 已执行 525 次追加巡检。
- 其中显式固定漫画、章节 ID 的最终复测 179 次。
- 首轮未走通、本轮最新记录走通核心链路的构建有 23 个；不能将改善全部归因于关键词。
- 主索引要求同一次巡检通过入口、详情、章节、图片下载和解码，且无其他失败或跳过。
- 扩展索引同样要求核心链路通过，但其他能力可能失败或跳过。
- 同 key 只选一个构建；官方同 key 的社区替代构建会在锁定文件标识。
- 账号、地区、代理和用户设备可能改变结果；本记录不等于 Venera UI 导入和设备阅读验证。

## 主索引

| 源名称 | runtime key | 固定漫画 ID | 固定章节 ID |
| --- | --- | --- | --- |
| A漫 | `aman8` | `458778` | `dSIqcrthizgeTZxusEPu` |
| 布卡漫画 | `bukamh` | `wurenyichengweihuoyingweimubiaodenaruto` | `603211_208477` |
| CosplayTele | `cosplaytele` | `cinderella-crystal-wave-3` | `0` |
| 动漫屋 | `dm5` | `manhua-manbucangqiong` | `m938318` |
| 咚漫 | `dongman` | `2931` | `1` |
| 咚漫 | `dongmanmanhua` | `2914` | `10` |
| 飞翔漫画 | `ffppt` | `30027` | `0` |
| FoamGirl | `foamgirl` | `1839551` | `1` |
| GoDa漫画 | `goda` | `/manga/huoyingrenzhequancaiban-jiyingshe` | `5205@412417` |
| 瓜子漫画 | `guazi_manhua_v2` | `/comic.php?id=15663` | `1890870` |
| 绅士会所 | `hentaiclub` | `https://www.hentaiclub.net/r18/69677.html` | `0` |
| 嬉皮漫畫 | `hipmh` | `bToyOTM5NA-huan-ying-lian-ge-webtoon-4257-21966` | `bToyOTM5NC1jOjExMzAxNw-MjkzOTQ6MS4wMA` |
| 花咔漫画 | `huakacomic` | `6973d1f88370836c2a5c3f38` | `ep_69765b718370836c2a6c939f` |
| 快看漫画 | `kuaikan` | `766` | `744903` |
| 极速漫画 | `legacy_1kkk` | `http://www.1kkk.com/manhua18216/` | `https://m.1kkk.com/ch1-200037/` |
| 漫画人 | `manhuaren` | `https://www.manhuaren.com/manhua-manbucangqiong/` | `https://www.manhuaren.com/m969149/` |
| 漫蛙吧（图片修复版） | `manwaba_imagefix` | `58100` | `1135662` |
| 漫网 | `manwang` | `531963` | `192773` |
| 漫客栈 | `mkzhan` | `213560` | `750783` |
| 鸟鸟韩漫 | `nnhanman` | `huo-ying-ren-zhe-wu-ma-A-man-zuo-ai-jian-yu` | `/comic/huo-ying-ren-zhe-wu-ma-A-man-zuo-ai-jian-yu/chapter-61694.html` |
| 极速漫画 | `one_kkk` | `manhua55465` | `https://m.1kkk.com/ch15-969149/` |
| 311漫画 | `s311_com` | `/comic_91394.html` | `91394@2817951` |
| 神奇漫画 | `shenqimanhua` | `cmj5uq0j6smrlpv9p2tjdgn2s` | `cmj5uq0qhsn5spv9pr4uxbjlm` |
| 腾讯动漫 | `tencentcomics` | `643717` | `/ComicView/index/id/643717/cid/1` |
| X漫画 | `xmanhua` | `139` | `29396` |

## 扩展索引

| 源名称 | runtime key | 状态 | 失败或未验证能力（最多列四项） |
| --- | --- | --- | --- |
| Komiic | `Komiic` | 失败 | account.login：未提供账号凭据；explore[0].load：返回结构或样本不满足契约；categoryComics.load：返回结构或样本不满足契约；categoryComics.ranking.load：返回结构或样本不满足契约 |
| 漫画柜 | `ManHuaGui` | 部分通过 | account.login：未提供账号凭据；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用；favorites.addOrDelFavorite：写操作未启用 |
| 腾讯漫画 | `acqq` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| 爱漫岛 | `aiman` | 部分通过 | account.loginWithCookies.validate：未提供账号凭据；favorites.loadFolders：未提供账号凭据；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| Asura Scans | `asura_scans` | 失败 | account.login：未提供账号凭据；favorites.loadFolders：未提供账号凭据；favorites.loadComics：未提供账号凭据；comic.idMatch：返回结构或样本不满足契约 |
| 百合会 | `baihehui` | 失败 | account.login：未提供账号凭据；search.load：需要登录；account.logout：写操作未启用；comic.link.idToLink：缺少测试输入 |
| 包子漫画（修订版） | `baozi_fixed` | 失败 | account.login：未提供账号凭据；categoryComics.load：返回结构或样本不满足契约；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| 哔哩漫画 | `bilimanga` | 部分通过 | account.loginWithWebview.checkStatus：interactive_required；account.logout：写操作未启用；comic.getShareLink：缺少测试输入 |
| CCC追漫台 | `ccc` | 部分通过 | account.login：未提供账号凭据；account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；favorites.loadComics：未提供账号凭据 |
| Cosplay啦 | `ciyuandao` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| CxC | `cxc` | 部分通过 | account.loginWithCookies.validate：未提供账号凭据；account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；account.logout：写操作未启用 |
| 次元漫画 | `cycomic` | 失败 | explore[1].load：返回结构或样本不满足契约；categoryComics.ranking.load：返回结构或样本不满足契约 |
| 大魔兔 | `damotu` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| 顶漫画 | `dingmanhua` | 失败 | comic.link.linkToId：缺少测试输入；comic.onClickTag：源配置错误；comic.onClickTag：源配置错误 |
| ehentai | `ehentai` | 失败 | account.loginWithCookies.validate：未提供账号凭据；account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；favorites.loadFolders：未提供账号凭据 |
| 瓜子漫画 | `guazimanhua` | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| 国漫吧 | `guoman8` | 失败 | explore[43].load：需要登录；comic.onImageLoad.onLoadFailed：not_triggered |
| Hachiraw | `hachiraw` | 失败 | search.load：返回结构或样本不满足契约；comic.idMatch：返回结构或样本不满足契约 |
| H-Comic | `hcomic` | 部分通过 | comic.link.linkToId：缺少测试输入 |
| 紳士漫畫（私人） | `hj_wnacg` | 部分通过 | account.login：未提供账号凭据；favorites.loadFolders：未提供账号凭据；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| 热辣漫画 | `hot_manga` | 失败 | account.login：未提供账号凭据；favorites.loadComics：未提供账号凭据；comic.onClickTag：源配置错误；comic.onClickTag：源配置错误 |
| 爱看漫 | `ikmmh` | 部分通过 | account.login：未提供账号凭据；favorites.loadComics：未提供账号凭据；comic.onImageLoad.onLoadFailed：not_triggered；account.logout：写操作未启用 |
| 爱看漫 | `ikmmh_v2` | 部分通过 | account.login：未提供账号凭据；favorites.loadComics：未提供账号凭据；comic.onImageLoad.onLoadFailed：not_triggered；account.logout：写操作未启用 |
| 爱飒漫画 | `isamanhua` | 失败 | search.load：HTTP 错误 |
| 极速漫画 | `jisu_1kkk` | 失败 | account.loginWithWebview.checkStatus：interactive_required；explore[17].load：HTTP 错误；comic.onImageLoad.onLoadFailed：not_triggered；account.logout：写操作未启用 |
| JJCOS | `jjcos` | 部分通过 | search.onTagSuggestionSelected：缺少测试输入；comic.onImageLoad.onLoadFailed：not_triggered；comic.onThumbnailLoad.onLoadFailed：unsupported_thumbnail |
| 禁漫天堂X | `jmx` | 部分通过 | account.login：未提供账号凭据；favorites.loadFolders：未提供账号凭据；favorites.loadComics：未提供账号凭据；comic.onImageLoad.onLoadFailed：not_triggered |
| 看漫画 | `kanman` | 失败 | search.load：返回结构或样本不满足契约；explore[0].onThumbnailLoad：缺少测试输入；categoryComics.onThumbnailLoad：缺少测试输入 |
| Kiutaku | `kiutaku` | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| 来漫画（分流） | `laimanhua_split` | 失败 | search.load：HTTP 错误；thumbnail.download：TLS 错误 |
| Lanraragi | `lanraragi` | 失败 | search.load：HTTP 错误；search.loadNext：HTTP 错误 |
| 51漫画 | `manga51` | 部分通过 | comic.link.linkToId：缺少测试输入 |
| MangaDex | `manga_dex` | 失败 | categoryComics.load：缺少测试输入；comic.loadComments：运行时不支持；comic.getComic：缺少测试输入；comic.getChapters：缺少测试输入 |
| 178漫画网 | `manhua178` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| 漫画吧网 | `manhuaba` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| 漫舍 | `manshe` | 失败 | comic.link.linkToId：返回结构或样本不满足契约 |
| 漫画manga | `mh03` | 失败 | explore[0].load：需要登录 |
| 漫画1234（新版网站） | `mh1234_fixed` | 失败 | account.loginWithWebview.checkStatus：interactive_required；categoryComics.load：返回结构或样本不满足契约；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| MOJOIN | `mojoin` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| MOJOIN | `mojoin_v2` | 部分通过 | comic.onImageLoad.onLoadFailed：not_triggered |
| 漫小肆 | `mxs` | 失败 | search.load：请求超时；settings.domainCheck.callback：写操作未启用 |
| 大人漫画（私人） | `private_drmh3` | 失败 | explore[0].load：请求超时；categoryComics.load：请求超时 |
| 魅影画廊（私人） | `private_myhl` | 失败 | search.load：返回结构或样本不满足契约 |
| 腾讯动漫（正版） | `qq_comic_official` | 部分通过 | account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| 如漫画 | `rumanhua` | 部分通过 | comic.decryptChapterImages：缺少测试输入；comic._findPackedExpr：缺少测试输入；comic._unquote：缺少测试输入；comic._parseK：缺少测试输入 |
| 如漫画 | `rumanhua2` | 失败 | explore[0].load：返回结构或样本不满足契约 |
| 如漫画 | `rumanhua_fixed_v15` | 部分通过 | comic.unpackJS：缺少测试输入 |
| SF漫画 | `sfacg_manhua` | 失败 | search.load：返回结构或样本不满足契约 |
| 思思漫画 | `sisimanhua` | 失败 | thumbnail.download：TLS 错误 |
| サンデーうぇぶり | `sunday_webry` | 失败 | search.load：反爬拦截 |
| 腾讯动漫 | `tencent_comics` | 部分通过 | account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| 图库漫画 | `tuku_cc` | 失败 | explore[0].load：需要登录 |
| 紳士漫畫 | `wnacg` | 部分通过 | account.login：未提供账号凭据；favorites.loadFolders：未提供账号凭据；favorites.loadComics：未提供账号凭据；account.logout：写操作未启用 |
| Xiutaku | `xiutaku` | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| yande.re | `yandere` | 失败 | account.login：未提供账号凭据；account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；search.load：返回结构或样本不满足契约 |
| 野蛮漫画 | `yemancomic` | 失败 | explore[1].load：返回结构或样本不满足契约；categoryComics.ranking.load：返回结构或样本不满足契约 |
| zero搬运网 | `zerobyw` | 失败 | account.loginWithWebview.checkStatus：interactive_required；account.loginWithWebview.onLoginSuccess：dependency_failed；search.load：请求超时；account.isLoggedIn：缺少测试输入 |
| zero搬运网 | `zerobyw33` | 失败 | account.login：未提供账号凭据；explore[0].load：请求超时；account.logout：写操作未启用；settings.refresh_domain.callback：写操作未启用 |
| 知音漫客 | `zymk` | 失败 | search.load：返回结构或样本不满足契约；comic.onImageLoad.onLoadFailed：not_triggered |

扩展源的全部限制见 `sources.lock.json` 的 `limitations`。未入选源和具体阶段见本地 `sources.zh.csv`；完整执行证据保存在本地审计目录。
