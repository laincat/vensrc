# VeneraX／Venera-Next 固定样本兼容清单

核验时间：2026-11-12T08:08:27.947965+00:00（UTC）。
最新上游 CLI 提交：`dd6ded39844e56902d3880b1fc1c201a6d1d1fda`；同时加载本仓库记录哈希的接口适配层。
全部已审阅源码逐个使用相同固定输入；VeneraX 为订阅选择依据，Next 为独立对照。
官方原版排除；社区同 key 版本必须严格高于官方，并独立满足本次核心阅读与主／扩展门槛。
结果为 Node 宿主上的真实客户端 JS 接口巡检，不代表 Flutter UI 或用户设备实测。
两边分时执行，差异也可能来自网络、限流或源站变化，不能全部归因于 Fork 接口。
账号巡检另见 ACCOUNT_RESULTS.md，不以账号通过替代匿名订阅收录标准。
完整阶段、输入和哈希保存在 ../data/client-results.json 与 ../data/sources.zh.csv。

## 全量统计

| 环境 | 报告构建数 | 核心阅读通过 | 整次通过 | 部分通过 | 失败 | 整源跳过 | 跳过阶段 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| venerax | 207 | 69 | 24 | 19 | 164 | 0 | 853 |
| venera-next | 207 | 68 | 24 | 19 | 164 | 0 | 854 |

跳过阶段、缺少凭据及未触发回调均不计入通过；核心通过只要求已说明的阅读链路。

## 三个自用仓库

- `hea784/venera-configs`：venerax 核心通过 9/20；venera-next 核心通过 8/20。
- `BB-CHICKEN/venera-jm`：venerax 核心通过 1/1；venera-next 核心通过 1/1。
- `handahao666-boop/venera_comic_source`：venerax 核心通过 23/37；venera-next 核心通过 22/37。

## 核心阅读结果不同的构建

共 1 个构建。两边分时执行；以下是结果差异，不自动归因为客户端代码。

| key | 版本 | 仓库 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- |
| comick | 1.2.0 | handahao666-boop/venera_comic_source | 通过 | 未通过 |

## 其他阶段结果差异

按阶段状态和类别对照，不比较耗时、返回正文和异常原文。“未出现”表示该环境报告没有此阶段，不能算通过。

| key | 版本 | 构建哈希（前12位） | 阶段 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- |
| comick | 1.2.0 | 8e775b238141 | comic.loadInfo | 通过 | 失败／请求超时 |
| comick | 1.2.0 | 8e775b238141 | comic.onClickTag | 失败／源配置错误；失败／源配置错误；通过；失败／源配置错误 | 跳过／缺少样本输入 |
| legacy_diya1 | 0.1.0 | 1d66772b6af5 | search.load | 失败／请求超时 | 失败／网络错误 |
| legacy_manmankan | 0.1.0 | e650efd029f2 | search.load | 失败／请求超时 | 失败／TLS 错误 |
| qimanwu | 1.0.0 | 372767ebd004 | explore[12].load | 失败／源配置错误 | 失败／需要登录 |
| qimanwu | 1.0.0 | 372767ebd004 | explore[14].load | 失败／源配置错误 | 失败／需要登录 |
| qimanwu | 1.0.0 | 372767ebd004 | explore[1].load | 失败／源配置错误 | 失败／需要登录 |
| qimanwu | 1.0.0 | 372767ebd004 | explore[5].load | 失败／需要登录 | 失败／源配置错误 |
| qimanwu | 1.0.0 | 372767ebd004 | explore[6].load | 失败／源配置错误 | 失败／需要登录 |

## 逐构建对照

| 名称 | key | 版本 | 仓库 | 源码哈希（前12位） | VeneraX 核心／整次 | Next 核心／整次 | 首个失败（X；Next） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 古风漫画 | GfmhApp | 1.3.0 | handahao666-boop/venera_comic_source | a49d1e4b58fd | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 漫画柜 | ManHuaGui | 1.2.1 | handahao666-boop/venera_comic_source | a5bf6c633e0c | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 百合会 | baihehui | 1.0.0 | handahao666-boop/venera_comic_source | ba1520f9cad1 | 通过／失败 | 通过／失败 | search.load 需要登录；search.load 需要登录 |
| 包子漫画 | baozi | 1.1.7 | handahao666-boop/venera_comic_source | d589aabc779b | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 嗶哩漫畫 | bilimanga | 1.1.7 | handahao666-boop/venera_comic_source | dd8fd0160934 | 未通过／失败 | 未通过／失败 | image.download 反爬拦截；image.download 反爬拦截 |
| CCC追漫台 | ccc | 1.0.1 | handahao666-boop/venera_comic_source | d916f6ef74cd | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| カドコミ | comic_walker | 1.0.1 | handahao666-boop/venera_comic_source | 736c49789faf | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| comick | comick | 1.2.0 | handahao666-boop/venera_comic_source | 8e775b238141 | 通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| 拷贝漫画(多账号) | copy_manga_multi_accounts | 1.4.1 | venera-app/venera-configs | 1d8d8f855fed | 通过／失败 | 通过／失败 | comic.onClickTag 源配置错误；comic.onClickTag 源配置错误 |
| CxC | cxc | 1.0.3 | handahao666-boop/venera_comic_source | d6f5fbaff901 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 动漫屋 | dm5 | 7.0.3 | handahao666-boop/venera_comic_source | 7dee44268278 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 动漫啦 | dongman_la | 1.0.5 | handahao666-boop/venera_comic_source | c3c1e9989d8a | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 咚漫 | dongmanmanhua | 1.0.6 | handahao666-boop/venera_comic_source | 65df758f8643 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| ehentai | ehentai | 1.2.0 | venera-app/venera-configs | ef15f80d8090 | 通过／失败 | 通过／失败 | explore[2].loadNext 返回结构或样本不满足契约；explore[2].loadNext 返回结构或样本不满足契约 |
| 飞翔漫画 | ffppt | 1.0.3 | handahao666-boop/venera_comic_source | a0253ea74b06 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| GoDa漫画 | goda | 1.2.1 | handahao666-boop/venera_comic_source | dc94b8d5074e | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 嗨皮漫画 | happy | 1.0.0 | venera-app/venera-configs | 656f038a7b13 | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| H-Comic | hcomic | 1.0.0 | venera-app/venera-configs | 0490859b636c | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 嬉皮漫畫 | hipmh | 1.0.1 | handahao666-boop/venera_comic_source | c55ce0fca5fb | 未通过／失败 | 未通过／失败 | image.download 请求超时；image.download 请求超时 |
| hitomi.la | hitomi | 1.1.2 | venera-app/venera-configs | af174079e017 | 未通过／失败 | 未通过／失败 | categoryComics.load 网络错误；categoryComics.load 网络错误 |
| 爱看漫 | ikmmh_v2 | 3.0.0 | handahao666-boop/venera_comic_source | b911acf01818 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| jcomic.net | jcomic | 1.0.0 | venera-app/venera-configs | afd7dc75ac12 | 未通过／失败 | 未通过／失败 | comic.loadEp 返回结构或样本不满足契约；comic.loadEp 返回结构或样本不满足契约 |
| 禁漫天堂 | jm | 1.9.2 | BB-CHICKEN/venera-jm | e50a45d1c3b3 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| Kavita | kavita | 1.0.0 | venera-app/venera-configs | 65173ae4eb4a | 未通过／失败 | 未通过／失败 | search.load TLS 错误；search.load TLS 错误 |
| Komga | komga | 1.0.0 | venera-app/venera-configs | 2aa5b4e7d4b3 | 未通过／失败 | 未通过／失败 | search.load 源配置错误；search.load 源配置错误 |
| 来漫画（分流） | laimanhua_split | 1.2.1 | handahao666-boop/venera_comic_source | 3b82bcbae932 | 通过／失败 | 通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| Lanraragi | lanraragi | 1.2.0 | venera-app/venera-configs | b2bc20d13979 | 通过／失败 | 通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| 51漫画 | manga51 | 1.2.0 | handahao666-boop/venera_comic_source | c6fba1ceade9 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| Mangabz | mangabz | 1.0.0 | handahao666-boop/venera_comic_source | 4beecb5beefc | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 漫画人 | manhuaren | 1.0.1 | handahao666-boop/venera_comic_source | 568730c90b61 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 香蕉漫画 | manhuauo_banana_v2 | 1.0.3 | handahao666-boop/venera_comic_source | af540832b7f0 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 漫蛙吧 | manwaba | 1.1.3 | handahao666-boop/venera_comic_source | 5fc159d25409 | 通过／失败 | 通过／失败 | categoryComics.load HTTP 错误；categoryComics.load HTTP 错误 |
| 漫网 | manwang | 1.2.0 | handahao666-boop/venera_comic_source | 4520b8edb70b | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 漫画1234 | mh1234 | 1.0.0 | venera-app/venera-configs | 17d910952f7d | 未通过／失败 | 未通过／失败 | search.load 源配置错误；search.load 源配置错误 |
| 18漫画 | mh18 | 1.0.0 | venera-app/venera-configs | 88ba802dbc33 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 4399漫画网 | mh4399 | 1.0.3 | handahao666-boop/venera_comic_source | ffddebed57a8 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| MOJOIN | mojoin_v2 | 1.0.7 | handahao666-boop/venera_comic_source | ccfde1cd6784 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 漫小肆 | mxs | 1.0.0 | venera-app/venera-configs | da2c222eda82 | 通过／失败 | 通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| MYCOMIC | mycomic | 1.1.0 | handahao666-boop/venera_comic_source | 85432d15a15e | 通过／失败 | 通过／失败 | categoryComics.ranking.load 返回结构或样本不满足契约；categoryComics.ranking.load 返回结构或样本不满足契约 |
| nhentai | nhentai | 1.1.0 | venera-app/venera-configs | 0f68757f89d4 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| NoyManga | noymanga | 1.1.5 | handahao666-boop/venera_comic_source | 031fa44dd185 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| Picacg | picacg | 1.0.6 | venera-app/venera-configs | a404719b7f3f | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| Rawkuma | rawkuma | 1.1.0 | handahao666-boop/venera_comic_source | 9997666ded8b | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 如漫画 | rumanhua_fixed_v15 | 1.2.8 | handahao666-boop/venera_comic_source | 3727590e9d05 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| SF漫画 | sfacg_manhua | 1.0.0 | handahao666-boop/venera_comic_source | fa1533e0fb6a | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.2.0 | handahao666-boop/venera_comic_source | 22407b426ed6 | 通过／失败 | 通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| サンデーうぇぶり | sunday_webry | 1.0.0 | handahao666-boop/venera_comic_source | e0df66f216f9 | 通过／失败 | 通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 图库漫画 | tuku_cc | 1.0.1 | handahao666-boop/venera_comic_source | 235e01bc5009 | 通过／失败 | 通过／失败 | explore[0].load 需要登录；explore[0].load 需要登录 |
| W漫画 | wmanhua | 1.0.1 | handahao666-boop/venera_comic_source | 621a3e063f15 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 野蛮漫画 | yemancomic | 0.1.2 | hea784/venera-configs | 46ccc7b1b495 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 优酷漫画 (修复版) | ykmh | 1.0.7 | handahao666-boop/venera_comic_source | ae5fba5713b3 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 再漫画 | zaimanhua | 1.0.2 | handahao666-boop/venera_comic_source | 96b89df7bcda | 未通过／失败 | 未通过／失败 | comic.loadInfo 源配置错误；comic.loadInfo 源配置错误 |
| zero搬运网 | zerobyw33 | 1.2.0 | handahao666-boop/venera_comic_source | fec1f36630cc | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 漫画160 | 160_53_6c28df | 0.2.0 | KadishJoey/venera-json | 17b45905679d | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| ◯ 177漫画 | 177_75_d9f4ef | 0.2.0 | KadishJoey/venera-json | c657f535b6b8 | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 18漫畫(国内可) | 18_11_31f9fe | 0.2.0 | KadishJoey/venera-json | 3085316556d8 | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 18真人图集 | 18_12_5158bf | 0.2.0 | KadishJoey/venera-json | 94010a70c8ee | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| ◯ 18H | 18h_73_868382 | 0.2.0 | KadishJoey/venera-json | fc1a63d667cb | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 崩坏3漫画 | 3_31_7d315c | 0.2.0 | KadishJoey/venera-json | 019794eca2cf | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 733动漫 | 733_2 | 0.1.0 | zhimouzhou/venera-manga-sources | 54ce49133a98 | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 8色摄影 | 8_23_b711ea | 0.2.0 | KadishJoey/venera-json | c0abff98a26b | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 無限動漫 | 8comic | 1.0.0 | zakkida/venera-sources | 0c4b06ef4f91 | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 92漫画 | 92_60_af6181 | 0.2.0 | KadishJoey/venera-json | fd41125aa460 | 未通过／失败 | 未通过／失败 | source.load 源加载或版本不兼容；source.load 源加载或版本不兼容 |
| 新漫画-A | a_43_e3f585 | 0.2.0 | KadishJoey/venera-json | 3b7000a44ea8 | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| 一本漫画-A | a_49_189b7b | 0.2.0 | KadishJoey/venera-json | 3052015a1176 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| A漫🔞 | a_54_aaf8eb | 0.2.0 | KadishJoey/venera-json | 7dabfb81a70e | 未通过／失败 | 未通过／失败 | comic.loadInfo 返回结构或样本不满足契约；comic.loadInfo 返回结构或样本不满足契约 |
| 爱漫岛 | aiman | 2.3.6 | Junkrat9527/venera-sources | 18c0c8b32434 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| A漫 | aman8 | 1.0.0 | Junkrat9527/venera-sources | 2b16b80ed5cf | 通过／通过 | 通过／通过 | 无失败；无失败 |
| Asura Scans | asura_scans | 1.3.0 | Micqiyue/venera-sources | a852624ec250 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 巴卡漫画 | bakamh | 1.0.1 | Magentadots/venera-configs | 43e5d34767e7 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 包子漫画（修订版） | baozi_fixed | 1.1.3 | JunQianNuo/venera-sources | d5be7f79acce | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 包子漫画（重制版） | baozi_recode | 1.1.7 | Micqiyue/venera-sources | 8c8f381f4323 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| BatCave.biz | batcavebiz | 1.0.5 | F22822/22822 | 99e1a1e65c21 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 布卡漫画 | bukamh | 1.2.9 | Junkrat9527/venera-sources | 34424b843c05 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| Buon Dua | buondua | 1.2.0 | meaninglesslyy/venera-config | 2cba3e6205a4 | 通过／失败 | 通过／失败 | comic.idMatch 返回结构或样本不满足契约；comic.idMatch 返回结构或样本不满足契约 |
| CCC追漫台 | ccc | 1.0.2 | zakkida/venera-sources | c8db4ef9af1d | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| Cosplay啦 | ciyuandao | 1.0.0 | token1008/venera-cn-64bit | af736e8c7ac6 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| CosplayTele | cosplaytele | 1.7.0 | meaninglesslyy/venera-config | dd6e35d1a5b6 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 次元漫画 | cycomic | 1.0.3 | Junkrat9527/venera-sources | 3db355237cec | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 大魔兔 | damotu | 1.0.0 | token1008/venera-cn-64bit | 7a9137c49fbd | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 顶漫画 | dingmanhua | 1.0.5 | Angus-fw/venera-configs | 30b1a74acaa3 | 通过／失败 | 通过／失败 | comic.onClickTag 源配置错误；comic.onClickTag 源配置错误 |
| 堆堆漫画 | duiduiman | 1.0.0 | cheyou001/venera-sources | b7318fecaa07 | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| 读漫屋 | dumanwu1 | 0.4.3 | zhimouzhou/venera-manga-sources | ab1ccd248ea7 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| Everia图集 | everia_14_efa23b | 0.2.0 | KadishJoey/venera-json | 83c0e795960b | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 810114 漫画源 | ex_810114_xyz | 1.0.0 | xuzhen2905-pixel/venera-source | 9e66fbc18688 | 未通过／失败 | 未通过／失败 | explore[0].load 返回结构或样本不满足契约；explore[0].load 返回结构或样本不满足契约 |
| ExHentai (fangliding 镜像) | ex_fangliding | 1.2.0 | zakkida/venera-sources | 19fdc46bcfeb | 未通过／失败 | 未通过／失败 | search.loadNext 反爬拦截；search.loadNext 反爬拦截 |
| FoamGirl | foamgirl | 1.2.1 | meaninglesslyy/venera-config | b5191bbc6933 | 未通过／失败 | 未通过／失败 | explore[1].load 反爬拦截；explore[1].load 反爬拦截 |
| 4KHD | fourkhd | 2.0.7 | meaninglesslyy/venera-config | a0fc9199723d | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 4KHD Cosplay | fourkhd_cosplay | 2.0.0 | 6678670jsy/venera-sources | bd1374c61127 | 通过／失败 | 通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| G站漫画 | g_67_c20b96 | 0.2.0 | KadishJoey/venera-json | cc6fabe4d79b | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| GMANHUA | gmanhua_59_ee9658 | 0.2.0 | KadishJoey/venera-json | d87412d3bf9d | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 瓜子漫画 | guazi_manhua_v2 | 1.0.1 | ChenTeea/veneresource | 9191babe81a1 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 国漫吧 | guoman8 | 1.0.2 | token1008/venera-cn-64bit | b7c7b03cefb7 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| Hachiraw | hachiraw | 1.0.0 | YUIRIKIiii/venera-sources | bee58b154cb6 | 通过／失败 | 通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 花火漫画 | hanabimanga | 1.0.0 | xiaoxingmian/venera-configs | e8d71c02d79c | 未通过／失败 | 未通过／失败 | comic.loadEp 请求限流；comic.loadEp 请求限流 |
| 好看漫画 | haokan_txt | 1.0.4 | Junkrat9527/venera-sources | 88e1a9b1d513 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 绅士会所 | hentaiclub | 1.0.0 | meaninglesslyy/venera-config | 87985fef6ce6 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 包子漫画（私人） | hj_baozi | 1.1.7 | Taototo/venera-comic-sources | 6d037fb62050 | 未通过／失败 | 未通过／失败 | comic.loadEp 反爬拦截；comic.loadEp 反爬拦截 |
| 热辣漫画 | hot_manga | 1.0.1 | laincat/vensrc | 519ec86d7ad3 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 花咔漫画 | huakacomic | 1.0.0 | xiaoxingmian/venera-configs | 8f430535694c | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 爱看漫 | ikmmh | 1.0.6 | venera-app/venera-configs | a5382a807db1 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 爱飒漫画 | isamanhua | 1.0.0 | YHQY-Dev/venera-sources | 788af64ed6b0 | 通过／失败 | 通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| JJCOS | jjcos | 1.3.0 | meaninglesslyy/venera-config | 27a34128c375 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 禁漫天堂X | jmx | 2.1.0 | Junkrat9527/venera-sources | 670aadfa4101 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 看漫画 | kanman | 2.2.7 | Junkrat9527/venera-sources | dafac9381c69 | 通过／失败 | 通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| Kiutaku | kiutaku | 1.1.0 | meaninglesslyy/venera-config | f48424abde97 | 通过／失败 | 通过／失败 | comic.idMatch 返回结构或样本不满足契约；comic.idMatch 返回结构或样本不满足契约 |
| Komiic漫画 | komiic_69_259947 | 0.2.0 | KadishJoey/venera-json | 698670f557ce | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| Komiic 多账号 | komiic_multi | 1.6.2 | snowf14k3/venera-komiic-multi | 96036813d021 | 未通过／失败 | 未通过／失败 | comic.loadEp 需要登录；comic.loadEp 需要登录 |
| 快看漫画 | kuaikan | 1.0.0 | cattoldme/venera-configs | ad550aa4ecaf | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 特漫网站 | legacy_17te | 0.1.0 | wuliaoe/venera-extra-sources | 81fbbe889e77 | 未通过／失败 | 未通过／失败 | search.load 网络错误；search.load 网络错误 |
| 27漫画 | legacy_2mzx | 0.1.0 | wuliaoe/venera-extra-sources | 1678dfafbe50 | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 58漫画网 | legacy_58puxin | 0.1.0 | wuliaoe/venera-extra-sources | 90656b7133c4 | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 85漫画网 | legacy_85iu | 0.1.0 | wuliaoe/venera-extra-sources | ea29db842956 | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| 90漫画 | legacy_90mh | 0.1.0 | wuliaoe/venera-extra-sources | 5f366c77c1d9 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 1359漫画网 | legacy_bdido | 0.1.0 | wuliaoe/venera-extra-sources | 42f5b36dbd38 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 百年漫画 | legacy_bnmanhua | 0.1.0 | wuliaoe/venera-extra-sources | 7079da75071d | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 蒂亚漫画 | legacy_diya1 | 0.1.0 | wuliaoe/venera-extra-sources | 1d66772b6af5 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 网络错误 |
| 好漫6 | legacy_haoman6 | 0.1.0 | wuliaoe/venera-extra-sources | b9c37400249c | 未通过／失败 | 未通过／失败 | search.load 网络错误；search.load 网络错误 |
| 冰氪漫画 | legacy_icekr | 0.1.0 | wuliaoe/venera-extra-sources | f31f409699a0 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 爱米推漫画 | legacy_imitui | 0.1.0 | wuliaoe/venera-extra-sources | f301496fb91a | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 漫画羊 | legacy_manhuayang | 0.1.0 | wuliaoe/venera-extra-sources | a17452ca3352 | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 漫漫看漫画网 | legacy_manmankan | 0.1.0 | wuliaoe/venera-extra-sources | e650efd029f2 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load TLS 错误 |
| 漫漫睇 | legacy_manmantai | 0.1.0 | wuliaoe/venera-extra-sources | 0540caf28915 | 未通过／失败 | 未通过／失败 | search.load 源配置错误；search.load 源配置错误 |
| 漫画芯 | legacy_mhxin | 0.1.0 | wuliaoe/venera-extra-sources | ee90d24a3604 | 未通过／失败 | 未通过／失败 | search.load TLS 错误；search.load TLS 错误 |
| 奇妙漫画 | legacy_qimiaomh | 0.1.0 | wuliaoe/venera-extra-sources | 542169675a8b | 未通过／失败 | 未通过／失败 | search.load TLS 错误；search.load TLS 错误 |
| 奇热漫画 | legacy_qiremanhua | 0.1.0 | wuliaoe/venera-extra-sources | 091afce1a67e | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 258漫画网 | legacy_shut123 | 0.1.0 | wuliaoe/venera-extra-sources | b64072c59548 | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 搜动漫 | legacy_soudongman | 0.1.0 | wuliaoe/venera-extra-sources | 6734f0154be3 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 13漫画网 | legacy_w13k | 0.1.0 | wuliaoe/venera-extra-sources | 9052584cf9d6 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 武侠漫画 | legacy_wuxiamh | 0.1.0 | wuliaoe/venera-extra-sources | 1b4a8cc8c088 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 360漫画 | legacy_xd5s | 0.1.0 | wuliaoe/venera-extra-sources | 2e24a31a1745 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 土豆漫画网 | legacy_xm124 | 0.1.0 | wuliaoe/venera-extra-sources | 2e10f44aa7dc | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 六漫画 | liumanhua | 1.0.0 | token1008/venera-cn-64bit | aa7733f6ccfa | 未通过／失败 | 未通过／失败 | explore[1].load 需要登录；explore[1].load 需要登录 |
| 栗子漫画 | lizimh | 2.33.27 | Walter498/Walter | 12a149b918ec | 未通过／失败 | 未通过／失败 | search.load DNS 错误；search.load DNS 错误 |
| 漫画台-M | m_50_2be8b8 | 0.2.0 | KadishJoey/venera-json | 579f8c0a8613 | 未通过／失败 | 未通过／失败 | search.load TLS 错误；search.load TLS 错误 |
| 知音漫客-M | m_51_4e1530 | 0.2.0 | KadishJoey/venera-json | 6607bda2a387 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 看漫画-M | m_52_1d77ca | 0.2.0 | KadishJoey/venera-json | 5a5a1ed2667f | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 神漫画-M | m_63_d6913d | 0.2.0 | KadishJoey/venera-json | 61f0b72f8c80 | 未通过／失败 | 未通过／失败 | search.load TLS 错误；search.load TLS 错误 |
| 漫本 | manben | 1.1.0 | Junkrat9527/venera-sources | b75670e66801 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| Manga18FX | manga18fx | 1.0.2 | meaninglesslyy/venera-config | 2c6a2d86f30a | 通过／失败 | 通过／失败 | comic.idMatch 返回结构或样本不满足契约；comic.idMatch 返回结构或样本不满足契约 |
| MangaDex | manga_dex | 1.2.0 | venera-app/venera-configs | c8beb84262da | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| MANGA Plus | manga_plus | 1.0.2 | WEP-56/EZvenera-config | 7a29a3460780 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| MangaForFree | mangaforfree | 0.7.4 | meaninglesslyy/venera-config | 617657b4235f | 通过／失败 | 通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| MangaPill | mangapill | 1.0.0 | zakkida/venera-sources | ca1a4bec908a | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| MangaRead | mangaread_66_d1113a | 0.2.0 | KadishJoey/venera-json | 7e24ed7aa022 | 未通过／失败 | 未通过／失败 | comic.loadInfo 返回结构或样本不满足契约；comic.loadInfo 返回结构或样本不满足契约 |
| 178漫画网 | manhua178 | 1.0.0 | token1008/venera-cn-64bit | d7361f1ec912 | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| 漫画吧网 | manhuaba | 1.0.0 | token1008/venera-cn-64bit | 51636f60ed1f | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 漫画皮 | manhuapi | 1.4.2 | Junkrat9527/venera-sources | 65c2d5107a45 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 漫漫漫画 | manman | 1.0.0 | token1008/venera-cn-64bit | ed5cec30a0f1 | 未通过／失败 | 未通过／失败 | comic.loadInfo HTTP 错误；comic.loadInfo HTTP 错误 |
| 漫舍 | manshe | 1.0.8 | Micqiyue/venera-sources | e69d6f53b58b | 通过／失败 | 通过／失败 | comic.link.linkToId 返回结构或样本不满足契约；comic.link.linkToId 返回结构或样本不满足契约 |
| 漫蛙 | manwa | 1.1.6 | YHQY-Dev/venera-sources | 66e1ec3051ed | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 漫蛙吧（图片修复版） | manwaba_imagefix | 1.0.7 | YongkeDet/venera-configs | 7cd57c562c3c | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 漫画manga | mh03 | 1.0.1 | Magentadots/venera-configs | fb0043c114e1 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 漫画1234（新版网站） | mh1234_fixed | 1.2.2 | JunQianNuo/venera-sources | ae25ddf5e039 | 通过／失败 | 通过／失败 | categoryComics.load 返回结构或样本不满足契约；categoryComics.load 返回结构或样本不满足契约 |
| 漫画看 | mhkan | 1.1.7 | Junkrat9527/venera-sources | dbc378b662da | 未通过／失败 | 未通过／失败 | categoryComics.load 返回结构或样本不满足契约；categoryComics.load 返回结构或样本不满足契约 |
| 喵趣漫画 | miaoqu | 1.0.0 | token1008/venera-cn-64bit | 3453e17e6953 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| MissKon图集 | misskon_13_4b2d17 | 0.2.0 | KadishJoey/venera-json | 90fa4bdbe2aa | 未通过／失败 | 未通过／失败 | comic.loadInfo 返回结构或样本不满足契约；comic.loadInfo 返回结构或样本不满足契约 |
| Mitaku | mitaku | 1.0.0 | meaninglesslyy/venera-config | 775844ab98af | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 漫客栈 | mkzhan | 1.1.4 | Junkrat9527/venera-sources | 2988fe4b9c89 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| momon:GA | momon_ga | 1.0.1 | ChopDream/venera-source-hub | c70fb410eebe | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| naver | naver_28_e2315f | 0.2.0 | KadishJoey/venera-json | 61f35f1a3b45 | 未通过／失败 | 未通过／失败 | search.load 网络错误；search.load 网络错误 |
| 鳥鳥韓漫nnhanman5 | nnhanman5_10_f0cebd | 0.2.0 | KadishJoey/venera-json | 82c30a72ab8d | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 鸟鸟韩漫 | nnhm | 1.3.0 | Junkrat9527/venera-sources | f429d7718abd | 通过／通过 | 通过／通过 | 无失败；无失败 |
| NoyACG | noyacg | 1.4.0 | zetriumyx/noyacg-source-venera | 7ac204fad268 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 极速漫画 | one_kkk | 2.0.0 | Junkrat9527/venera-sources | 2ef9dbceeb23 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| Ososedki | ososedki | 1.1.1 | meaninglesslyy/venera-config | 9abac2acac99 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| Pixiv | pixiv | 1.9.0 | Junkrat9527/venera-sources | aeac0db633a5 | 未通过／失败 | 未通过／失败 | search.loadNext 需要登录；search.loadNext 需要登录 |
| 大人漫画（私人） | private_drmh3 | 1.0.0 | Taototo/venera-comic-sources | 16295397129c | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 魅影画廊（私人） | private_myhl | 1.0.1 | Taototo/venera-comic-sources | 9ac3e3a327b5 | 通过／失败 | 通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 奇漫屋 | qimanwu | 1.0.0 | token1008/venera-cn-64bit | 372767ebd004 | 未通过／失败 | 未通过／失败 | search.load 源配置错误；search.load 源配置错误 |
| 热门漫画 | remenmanhua | 1.0.0 | YHQY-Dev/venera-sources | e7f8f13fc036 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 311漫画 | s311_com | 1.2.0 | Junkrat9527/venera-sources | ec1cc9c7c3fe | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 神奇漫画 | shenqimanhua | 1.1.1 | coldnighten/venera-configs | 9c44e7c5e3fb | 通过／通过 | 通过／通过 | 无失败；无失败 |
| 思思漫画 | sisimanhua | 1.0.0 | YHQY-Dev/venera-sources | 938f9b2398c7 | 未通过／失败 | 未通过／失败 | image.download HTTP 错误；image.download HTTP 错误 |
| 漫画家📱⛅ | source_01_656cfe | 0.2.0 | KadishJoey/venera-json | 12beb03c326e | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 污漫天堂🔞 | source_03_c97d34 | 0.2.0 | KadishJoey/venera-json | 4c3549af4429 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| ◯ 拷贝漫画 | source_05_1be182 | 0.2.0 | KadishJoey/venera-json | 6b38e35fde75 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| ☄️ 最次元 | source_07_49effa | 0.2.0 | KadishJoey/venera-json | d9d3f92061a9 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 魅影画廊 | source_17_b7ddde | 0.2.0 | KadishJoey/venera-json | f48e06a4fa4d | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 中国人能飞 | source_19_50ee2a | 0.2.0 | KadishJoey/venera-json | 3d02227f24f6 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 鸟鸟韩漫·直连 | source_21_a16969 | 0.2.0 | KadishJoey/venera-json | 19d1c8a56868 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 武芊漫画·直连 | source_22_2764a4 | 0.2.0 | KadishJoey/venera-json | 16813b474367 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 漫画联合国 | source_32_e5ebaf | 0.2.0 | KadishJoey/venera-json | ca81e53b6b8f | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 特漫网 | source_34_0dc3b2 | 0.2.0 | KadishJoey/venera-json | 8f957e341ec1 | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| 动漫戏说 | source_38_17bca1 | 0.2.0 | KadishJoey/venera-json | 5d99c0c6d83b | 未通过／失败 | 未通过／失败 | search.load 网络错误；search.load 网络错误 |
| 海猫吧 | source_43 | 0.1.0 | zhimouzhou/venera-manga-sources | 824c7b68e175 | 未通过／失败 | 未通过／失败 | search.load 源配置错误；search.load 源配置错误 |
| 看漫畫 | source_44_fed97a | 0.2.0 | KadishJoey/venera-json | 3f5b1f5cdab5 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 漫畫狗 | source_45_d76464 | 0.2.0 | KadishJoey/venera-json | d14ca9af41fb | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 漫画园漫画 | source_54 | 0.1.0 | zhimouzhou/venera-manga-sources | ee0ff2b9b6a2 | 未通过／失败 | 未通过／失败 | search.load 源配置错误；search.load 源配置错误 |
| 聚合漫画屋 | source_55_082633 | 0.2.0 | KadishJoey/venera-json | 8074a7b28db5 | 未通过／失败 | 未通过／失败 | search.load 请求超时；search.load 请求超时 |
| 仙漫网 | source_58_9bd332 | 0.2.0 | KadishJoey/venera-json | 201220b9d521 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| 龙王传说网 | source_65_8717b6 | 0.2.0 | KadishJoey/venera-json | 74b88234b1bf | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 腾讯动漫 | tencentcomics | 1.0.0 | xiaoxingmian/venera-configs | 50a7268a0de3 | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| V2PH | v2ph | 1.2.0 | meaninglesslyy/venera-config | e78bf6e69d4a | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| vomic | vomic | 1.2.1 | LX7kM9/venera-configs | b9c3012e1500 | 未通过／失败 | 未通过／失败 | comic.loadEp 需要登录；comic.loadEp 需要登录 |
| ◯ 包子漫画web | web_70_6c33fc | 0.2.0 | KadishJoey/venera-json | 64183163b2d7 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| WEBTOON | webtoon | 1.0.0 | cattoldme/venera-configs | 1afbcd932087 | 未通过／失败 | 未通过／失败 | comic.loadInfo HTTP 错误；comic.loadInfo HTTP 错误 |
| webtoon移动版 | webtoon_71_d28205 | 0.2.0 | KadishJoey/venera-json | d5f87faf566e | 未通过／失败 | 未通过／失败 | search.load HTTP 错误；search.load HTTP 错误 |
| Webtoon_us | webtoon_us_68_3131e7 | 0.2.0 | KadishJoey/venera-json | 2501f63d2445 | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| LINE WEBTOON | webtoons_zh_hant | 1.0.1 | Junkrat9527/venera-sources | 18166b460991 | 通过／通过 | 通过／通过 | 无失败；无失败 |
| WeebCentral | weebcentral | 1.0.0 | yelongyue197-svg/venera-sources | 09e8a15ffde2 | 未通过／失败 | 未通过／失败 | search.load 反爬拦截；search.load 反爬拦截 |
| 紳士漫畫 | wnacg | 1.4.2 | laincat/vensrc | 86df16976e3d | 通过／部分通过 | 通过／部分通过 | 无失败；无失败 |
| Xiutaku | xiutaku | 1.1.0 | meaninglesslyy/venera-config | 1b4283f85946 | 通过／失败 | 通过／失败 | comic.idMatch 返回结构或样本不满足契约；comic.idMatch 返回结构或样本不满足契约 |
| X漫画 | xmanhua | 1.8.1 | Junkrat9527/venera-sources | ab5be6abb62f | 通过／通过 | 通过／通过 | 无失败；无失败 |
| yande.re | yandere | 4.9.3 | Junkrat9527/venera-sources | cada1c28f4ed | 未通过／失败 | 未通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
| ◯ YYDS | yyds_04_86b037 | 0.2.0 | KadishJoey/venera-json | 810c02550b8d | 未通过／失败 | 未通过／失败 | search.load 需要登录；search.load 需要登录 |
| 知音漫客 | zymk | 1.0.0 | token1008/venera-cn-64bit | 78a5f653f495 | 通过／失败 | 通过／失败 | search.load 返回结构或样本不满足契约；search.load 返回结构或样本不满足契约 |
