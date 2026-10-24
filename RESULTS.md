# Venera 漫画源云端巡检报告

核验时间：2026-10-24T10:48:31.425820+08:00（香港时间）。
巡检工具：`Gandum2077/venera-patrol-cli` 1.0.0，提交 `dd6ded39844e56902d3880b1fc1c201a6d1d1fda`。
依赖锁 SHA-256：`7ea394a32e59776dfb39647d0434c106283ae3f275e7329b694f660b771974de`。
本次审阅清单：316 个构建；主索引 **28** 项，扩展索引 **59** 项。

固定漫画及章节、源码字节哈希和 CLI 提交均保留。主索引必须同次通过入口、详情、章节、图片下载与解码，且整次报告为 passed；扩展索引要求相同核心链路通过，其他能力可有失败或跳过。旧成功结果不代替新失败。

GitHub 托管 runner 的网络与用户设备不同；未在用户设备验证导入或阅读。全部已审阅构建使用已核验的 VeneraX 原始 bootstrap，逐个以相同样本对照 Venera-Next。订阅仅按 VeneraX 本次结果选择；Next 成功不替代 X 失败。适配范围见 CLIENT_COMPATIBILITY.md，客户端对照复测见 CLIENT_RESULTS.md。

## 三个自用仓库

- `hea784/venera-configs`：已审阅构建 38 个，核心链路通过 17 个。
- `BB-CHICKEN/venera-jm`：已审阅构建 1 个，核心链路通过 1 个。
- `handahao666-boop/venera_comic_source`：已审阅构建 43 个，核心链路通过 28 个。

## 逐构建结果

| 源名称 | key | 仓库 | 版本 | 巡检环境 | 核心链路 | 整次状态 | 首个失败／跳过 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 漫画160 | 160_53_6c28df | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| ◯ 177漫画 | 177_75_d9f4ef | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 18漫畫(国内可) | 18_11_31f9fe | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 18真人图集 | 18_12_5158bf | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| ◯ 18H | 18h_73_868382 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 崩坏3漫画 | 3_31_7d315c | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 4KHD 美图 | 4khd_24_21d7d1 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 733动漫 | 733_2 | zhimouzhou/venera-manga-sources | 0.1.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 8色摄影 | 8_23_b711ea | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 無限動漫 | 8comic | zakkida/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 92漫画 | 92_60_af6181 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 |
| 古风漫画 | GfmhApp | handahao666-boop/venera_comic_source | 1.3.0 | venerax | 通过 | 通过 |  |
| Komiic | Komiic | handahao666-boop/venera_comic_source | 1.0.8 | venerax | 未完整通过 | 失败 | explore[0].load：返回结构或样本不满足契约 |
| Komiic | Komiic | venera-app/venera-configs | 1.0.3 | venerax | 通过 | 失败 | explore[0].load：返回结构或样本不满足契约 |
| Komiic | Komiic | l233333333/venera-sources | 1.0.2 | venerax | 通过 | 失败 | explore[0].load：返回结构或样本不满足契约 |
| 漫画柜 | ManHuaGui | handahao666-boop/venera_comic_source | 1.2.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 新漫画-A | a_43_e3f585 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 一本漫画-A | a_49_189b7b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| A漫🔞 | a_54_aaf8eb | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| 漫客栈-A | a_62_528fe9 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 腾讯动漫 | ac_qq | Angus-fw/venera-configs | 1.0.1 | venerax | 通过 | 部分通过 | comic.link.linkToId：缺少样本输入 |
| 腾讯漫画 | acqq | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：源配置错误 |
| 爱漫岛 | aiman | Junkrat9527/venera-sources | 2.3.6 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| A漫 | aman8 | Junkrat9527/venera-sources | 1.0.0 | venerax | 通过 | 通过 |  |
| Asura Scans | asura_scans | Micqiyue/venera-sources | 1.3.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| 百合会 | baihehui | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 百合会 | baihehui | Junkrat9527/venera-sources | 1.0.2 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 巴卡漫画 | bakamh | Magentadots/venera-configs | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 香蕉漫画 | banana | Junkrat9527/venera-sources | 1.0.4 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 包子漫画 | baozi | handahao666-boop/venera_comic_source | 1.1.7 | venerax | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 |
| 包子漫画 | baozi | venera-app/venera-configs | 1.1.6 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 包子漫画 | baozi | l233333333/venera-sources | 1.1.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 包子漫画（修订版） | baozi_fixed | JunQianNuo/venera-sources | 1.1.3 | venerax | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 |
| 包子漫画（重制版） | baozi_recode | Micqiyue/venera-sources | 1.1.7 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| BatCave.biz | batcavebiz | F22822/22822 | 1.0.5 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 嗶哩漫畫 | bilimanga | handahao666-boop/venera_comic_source | 1.1.7 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 哔哩漫画 | bilimanga | Junkrat9527/venera-sources | 1.6.2 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 布卡漫画 | bukamh | Junkrat9527/venera-sources | 1.2.9 | venerax | 通过 | 通过 |  |
| Buon Dua | buondua | meaninglesslyy/venera-config | 1.2.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| Buondua图集 | buondua_15_095853 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| CCC追漫台 | ccc | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| CCC追漫台 | ccc | venera-app/venera-configs | 1.0.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| CCC追漫台 | ccc | zakkida/venera-sources | 1.0.2 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| Cosplay啦 | ciyuandao | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 |
| カドコミ | comic_walker | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 未完整通过 | 失败 | init：需要登录 |
| カドコミ | comic_walker | venera-app/venera-configs | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| カドコミ | comic_walker | zakkida/venera-sources | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| comick | comick | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 |
| comick | comick | l233333333/venera-sources | 1.1.1 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 拷贝漫画 | copy_manga | handahao666-boop/venera_comic_source | 1.6.6 | venerax | 未完整通过 | 失败 | explore[0].load：源配置错误 |
| 拷贝漫画 | copy_manga | venera-app/venera-configs | 1.4.3 | venerax | 未完整通过 | 失败 | explore[0].load：源配置错误 |
| 拷贝漫画 | copy_manga | zakkida/venera-sources | 1.4.4 | venerax | 未完整通过 | 失败 | explore[0].load：源配置错误 |
| 拷贝漫画(多账号) | copy_manga_multi_accounts | venera-app/venera-configs | 1.4.1 | venerax | 未完整通过 | 失败 | explore[0].load：源配置错误 |
| CosplayTele | cosplaytele | meaninglesslyy/venera-config | 1.7.0 | venerax | 通过 | 通过 |  |
| CosplayTele | cosplaytele_25_190983 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadEp：HTTP 错误 |
| 包子漫画cw | cw_57_cc4798 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| CxC | cxc | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 通过 | 部分通过 | account.loginWithCookies.validate：未提供账号凭据 |
| 次元漫画 | cycomic | Junkrat9527/venera-sources | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 大魔兔 | damotu | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 |
| 顶漫画 | dingmanhua | Angus-fw/venera-configs | 1.0.5 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 |
| 动漫屋 | dm5 | hea784/venera-configs | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 动漫屋 | dm5 | handahao666-boop/venera_comic_source | 7.0.3 | venerax | 通过 | 通过 |  |
| 咚漫 | dongman | Junkrat9527/venera-sources | 1.0.8 | venerax | 未完整通过 | 失败 | image.download：请求超时 |
| 动漫啦 | dongman_la | handahao666-boop/venera_comic_source | 1.0.5 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 |
| 动漫啦 | dongman_la | Junkrat9527/venera-sources | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 动漫啦 | dongmanla | token1008/venera-cn-64bit | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 咚漫 | dongmanmanhua | handahao666-boop/venera_comic_source | 1.0.6 | venerax | 通过 | 通过 |  |
| 堆堆漫画 | duiduiman | cheyou001/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 读漫屋 | dumanwu1 | zhimouzhou/venera-manga-sources | 0.4.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| ehentai | ehentai | venera-app/venera-configs | 1.2.0 | venerax | 通过 | 失败 | explore[2].loadNext：返回结构或样本不满足契约 |
| ehentai | ehentai | yelongyue197-svg/venera-sources | 1.1.8 | venerax | 通过 | 失败 | comic.archive.getArchives：需要登录 |
| Everia图集 | everia_14_efa23b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 810114 漫画源 | ex_810114_xyz | xuzhen2905-pixel/venera-source | 1.0.0 | venerax | 未完整通过 | 失败 | explore[0].load：返回结构或样本不满足契约 |
| ExHentai (fangliding 镜像) | ex_fangliding | zakkida/venera-sources | 1.2.0 | venerax | 未完整通过 | 失败 | search.loadNext：反爬拦截 |
| 飞翔漫画 | ffppt | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 通过 | 通过 |  |
| 飞翔漫画 | ffppt | Junkrat9527/venera-sources | 1.0.2 | venerax | 通过 | 通过 |  |
| FoamGirl | foamgirl | meaninglesslyy/venera-config | 1.2.1 | venerax | 未完整通过 | 失败 | explore[1].load：反爬拦截 |
| 4KHD | fourkhd | meaninglesslyy/venera-config | 2.0.7 | venerax | 通过 | 通过 |  |
| 4KHD Cosplay | fourkhd_cosplay | 6678670jsy/venera-sources | 2.0.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 |
| G站漫画 | g_67_c20b96 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 古风漫画 | gfmh | Junkrat9527/venera-sources | 1.3.1 | venerax | 未完整通过 | 失败 | image.download：HTTP 错误 |
| GMANHUA | gmanhua_59_ee9658 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| GoDa漫画 | goda | handahao666-boop/venera_comic_source | 1.2.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 瓜子漫画 | guazi_manhua_v2 | ChenTeea/veneresource | 1.0.1 | venerax | 通过 | 通过 |  |
| 瓜子漫画 | guazimanhua | handahao666-boop/venera_comic_source | 1.0.4 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| 瓜子漫画 | guazimanhua | Junkrat9527/venera-sources | 1.0.4 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| 国漫吧 | guoman8 | token1008/venera-cn-64bit | 1.0.2 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| Hachiraw | hachiraw | YUIRIKIiii/venera-sources | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 花火漫画 | hanabimanga | xiaoxingmian/venera-configs | 1.0.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 好看漫画 | haokan_txt | Junkrat9527/venera-sources | 1.0.4 | venerax | 通过 | 通过 |  |
| 嗨皮漫画 | happy | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| H-Comic | hcomic | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 部分通过 | comic.link.linkToId：缺少样本输入 |
| 绅士会所 | hentaiclub | meaninglesslyy/venera-config | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 嬉皮漫畫 | hipmh | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 通过 |  |
| 嬉皮漫畫 | hipmh | Junkrat9527/venera-sources | 1.0.6 | venerax | 通过 | 通过 |  |
| hitomi.la | hitomi | venera-app/venera-configs | 1.1.2 | venerax | 未完整通过 | 失败 | categoryComics.load：网络错误 |
| hitomi.la | hitomi | zakkida/venera-sources | 1.1.3 | venerax | 未完整通过 | 失败 | categoryComics.load：网络错误 |
| 包子漫画（私人） | hj_baozi | Taototo/venera-comic-sources | 1.1.7 | venerax | 未完整通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 |
| 紳士漫畫（私人） | hj_wnacg | Taototo/venera-comic-sources | 1.0.7 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 热辣漫画 | hot_manga | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 |
| 花咔漫画 | huakacomic | xiaoxingmian/venera-configs | 1.0.0 | venerax | 通过 | 通过 |  |
| 爱看漫 | ikmmh | venera-app/venera-configs | 1.0.6 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 爱看漫 | ikmmh | yelongyue197-svg/venera-sources | 1.0.8 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 爱看漫 | ikmmh_v2 | handahao666-boop/venera_comic_source | 3.0.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 爱飒漫画 | isamanhua | YHQY-Dev/venera-sources | 1.0.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 |
| jcomic.net | jcomic | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadEp：返回结构或样本不满足契约 |
| 极速漫画 | jisu_1kkk | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | explore[17].load：HTTP 错误 |
| JJCOS | jjcos | meaninglesslyy/venera-config | 1.3.0 | venerax | 通过 | 部分通过 | search.onTagSuggestionSelected：缺少样本输入 |
| 禁漫天堂 | jm | hea784/venera-configs | 1.4.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 禁漫天堂 | jm | BB-CHICKEN/venera-jm | 1.9.2 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 禁漫天堂 | jm | venera-app/venera-configs | 1.4.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 |
| 禁漫天堂 | jm | yelongyue197-svg/venera-sources | 1.3.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 禁漫天堂X | jmx | Junkrat9527/venera-sources | 2.1.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 看漫画 | kanman | Junkrat9527/venera-sources | 2.2.7 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| Kavita | kavita | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| Kiutaku | kiutaku | meaninglesslyy/venera-config | 1.1.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| Komga | komga | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| Komga | komga | zakkida/venera-sources | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| Komiic漫画 | komiic_69_259947 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| Komiic 多账号 | komiic_multi | snowf14k3/venera-komiic-multi | 1.6.2 | venerax | 未完整通过 | 失败 | explore[0].load：返回结构或样本不满足契约 |
| 快看漫画 | kuaikan | cattoldme/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | image.download：请求超时 |
| 来漫画（分流） | laimanhua_split | handahao666-boop/venera_comic_source | 1.2.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 来漫画（分流） | laimanhua_split | Junkrat9527/venera-sources | 1.2.2 | venerax | 通过 | 失败 | search.load：反爬拦截 |
| Lanraragi | lanraragi | venera-app/venera-configs | 1.2.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 |
| Lanraragi | lanraragi | yelongyue197-svg/venera-sources | 1.1.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 |
| 特漫网站 | legacy_17te | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 |
| 极速漫画 | legacy_1kkk | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 通过 | 通过 |  |
| 27漫画 | legacy_2mzx | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 51漫画 | legacy_51sami | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 58漫画网 | legacy_58puxin | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 733漫画 | legacy_733so | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 85漫画网 | legacy_85iu | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 90漫画 | legacy_90mh | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 1359漫画网 | legacy_bdido | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 百年漫画 | legacy_bnmanhua | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 漫画联合国 | legacy_comicun | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 大魔兔 | legacy_damotu | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 蒂亚漫画 | legacy_diya1 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 好漫6 | legacy_haoman6 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 |
| 六漫画 | legacy_hbdsfj | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 冰氪漫画 | legacy_icekr | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 爱米推漫画 | legacy_imitui | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 看漫画 | legacy_kanman | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：源配置错误 |
| 漫画羊 | legacy_manhuayang | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 漫漫看漫画网 | legacy_manmankan | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 漫漫睇 | legacy_manmantai | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 漫画芯 | legacy_mhxin | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 |
| 奇妙漫画 | legacy_qimiaomh | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 |
| 奇热漫画 | legacy_qiremanhua | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 258漫画网 | legacy_shut123 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 搜动漫 | legacy_soudongman | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 神漫画 | legacy_taomanhua | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 |
| 13漫画网 | legacy_w13k | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 武侠漫画 | legacy_wuxiamh | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 360漫画 | legacy_xd5s | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 土豆漫画网 | legacy_xm124 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 |
| 六漫画 | liumanhua | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | explore[1].load：需要登录 |
| 漫漫漫画-M | m_37_824ad0 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 咚漫-M | m_47_c0f177 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫画台-M | m_50_2be8b8 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 |
| 知音漫客-M | m_51_4e1530 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 看漫画-M | m_52_1d77ca | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 神漫画-M | m_63_d6913d | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 |
| 漫本 | manben | Junkrat9527/venera-sources | 1.1.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| Manga18FX | manga18fx | meaninglesslyy/venera-config | 1.0.2 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| 51漫画 | manga51 | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 通过 |  |
| 51漫画 | manga51 | huajiaoshu520/venera-cimoc | 1.1.0 | venerax | 通过 | 部分通过 | comic.link.linkToId：缺少样本输入 |
| 51漫画 | manga51 | Junkrat9527/venera-sources | 1.3.0 | venerax | 通过 | 部分通过 | comic.getShareLink：缺少样本输入 |
| MangaDex | manga_dex | handahao666-boop/venera_comic_source | 1.1.1 | venerax | 通过 | 部分通过 | categoryComics.load：缺少样本输入 |
| MangaDex | manga_dex | venera-app/venera-configs | 1.2.0 | venerax | 通过 | 部分通过 | account.loginWithWebview.checkStatus：需要交互 |
| MangaDex | manga_dex | yelongyue197-svg/venera-sources | 1.1.0 | venerax | 通过 | 失败 | comic.loadComments：运行时不支持 |
| MANGA Plus | manga_plus | WEP-56/EZvenera-config | 1.0.2 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| Mangabz | mangabz | hea784/venera-configs | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadEp：源配置错误 |
| Mangabz | mangabz | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 通过 |  |
| Mangabz | mangabz | YHQY-Dev/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| Mangabz | mangabz_72_18ed08 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：HTTP 错误 |
| MangaForFree | mangaforfree | meaninglesslyy/venera-config | 0.7.4 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| MangaPill | mangapill | zakkida/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| MangaRead | mangaread_66_d1113a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| 178漫画网 | manhua178 | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 |
| 漫画吧网 | manhuaba | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫画皮 | manhuapi | Junkrat9527/venera-sources | 1.4.2 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫画人 | manhuaren | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 通过 |  |
| 漫画人 | manhuaren | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 通过 |  |
| 香蕉漫画 | manhuauo_banana_v2 | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 漫漫漫画 | manman | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：源配置错误 |
| 漫舍 | manshe | Micqiyue/venera-sources | 1.0.8 | venerax | 通过 | 失败 | comic.link.linkToId：返回结构或样本不满足契约 |
| 漫蛙 | manwa | YHQY-Dev/venera-sources | 1.1.6 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫蛙吧 | manwaba | handahao666-boop/venera_comic_source | 1.1.3 | venerax | 通过 | 失败 | categoryComics.load：HTTP 错误 |
| 漫蛙吧 | manwaba | venera-app/venera-configs | 1.0.3 | venerax | 未完整通过 | 失败 | categoryComics.load：HTTP 错误 |
| 漫蛙吧（图片修复版） | manwaba_imagefix | YongkeDet/venera-configs | 1.0.7 | venerax | 通过 | 通过 |  |
| 漫网 | manwang | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫网 | manwang | Junkrat9527/venera-sources | 1.3.4 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫画manga | mh03 | Magentadots/venera-configs | 1.0.1 | venerax | 通过 | 失败 | explore[0].load：需要登录 |
| 漫画1234 | mh1234 | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 漫画1234 | mh1234 | zakkida/venera-sources | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：网络错误 |
| 漫画1234（新版网站） | mh1234_fixed | JunQianNuo/venera-sources | 1.2.2 | venerax | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 |
| 18漫画 | mh18 | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 4399漫画网 | mh4399 | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 4399漫画网 | mh4399 | Junkrat9527/venera-sources | 1.0.5 | venerax | 未完整通过 | 失败 | image.download：反爬拦截 |
| 漫画看 | mhkan | Junkrat9527/venera-sources | 1.1.7 | venerax | 未完整通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 |
| 喵趣漫画 | miaoqu | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| MissKon图集 | misskon_13_4b2d17 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| Mitaku | mitaku | meaninglesslyy/venera-config | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadEp：反爬拦截 |
| 漫客栈 | mkzhan | Junkrat9527/venera-sources | 1.1.4 | venerax | 通过 | 通过 |  |
| MOJOIN | mojoin | Junkrat9527/venera-sources | 1.0.8 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 |
| MOJOIN | mojoin_v2 | handahao666-boop/venera_comic_source | 1.0.7 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 |
| momon:GA | momon_ga | ChopDream/venera-source-hub | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫小肆 | mxs | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| MYCOMIC | mycomic | handahao666-boop/venera_comic_source | 1.1.0 | venerax | 通过 | 失败 | categoryComics.ranking.load：返回结构或样本不满足契约 |
| naver | naver_28_e2315f | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 |
| nhentai | nhentai | venera-app/venera-configs | 1.1.0 | venerax | 通过 | 部分通过 | account.loginWithWebview.checkStatus：需要交互 |
| nhentai | nhentai | yelongyue197-svg/venera-sources | 1.2.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 鸟鸟韩漫 | nnhanman | meaninglesslyy/venera-config | 1.1.1 | venerax | 通过 | 通过 |  |
| 鳥鳥韓漫nnhanman5 | nnhanman5_10_f0cebd | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 鸟鸟韩漫 | nnhm | Junkrat9527/venera-sources | 1.3.0 | venerax | 通过 | 通过 |  |
| NoyACG | noyacg | zetriumyx/noyacg-source-venera | 1.4.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| NoyManga | noymanga | handahao666-boop/venera_comic_source | 1.1.5 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 极速漫画 | one_kkk | hea784/venera-configs | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 极速漫画 | one_kkk | Junkrat9527/venera-sources | 2.0.0 | venerax | 通过 | 通过 |  |
| Ososedki | ososedki | meaninglesslyy/venera-config | 1.1.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| Picacg | picacg | venera-app/venera-configs | 1.0.6 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| Pixiv | pixiv | Junkrat9527/venera-sources | 1.9.0 | venerax | 未完整通过 | 失败 | search.loadNext：需要登录 |
| 大人漫画（私人） | private_drmh3 | Taototo/venera-comic-sources | 1.0.0 | venerax | 通过 | 通过 |  |
| 魅影画廊（私人） | private_myhl | Taototo/venera-comic-sources | 1.0.1 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 奇漫屋 | qimanwu | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 腾讯动漫（正版） | qq_comic_official | Junkrat9527/venera-sources | 2.0.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| 腾讯动漫（正版） | qq_comic_official_v1 | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| Rawkuma | rawkuma | handahao666-boop/venera_comic_source | 1.1.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| Rawkuma | rawkuma | Junkrat9527/venera-sources | 1.1.3 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 热门漫画 | remenmanhua | YHQY-Dev/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 如漫画 | rumanhua | Junkrat9527/venera-sources | 2.4.1 | venerax | 通过 | 部分通过 | comic.decryptChapterImages：缺少样本输入 |
| 如漫画 | rumanhua2 | zhimouzhou/venera-manga-sources | 0.4.3 | venerax | 通过 | 失败 | explore[0].load：返回结构或样本不满足契约 |
| 如漫画 | rumanhua_fixed_v15 | handahao666-boop/venera_comic_source | 1.2.8 | venerax | 通过 | 部分通过 | comic.unpackJS：缺少样本输入 |
| 311漫画 | s311_com | Junkrat9527/venera-sources | 1.2.0 | venerax | 通过 | 通过 |  |
| SF漫画 | sf_27_eb0a9b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| SF漫画 | sfacg_manhua | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| SF漫画 | sfacg_manhua | Junkrat9527/venera-sources | 1.0.2 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 神奇漫画 | shenqimanhua | coldnighten/venera-configs | 1.1.1 | venerax | 通过 | 通过 |  |
| 少年ジャンプ＋ | shonen_jump_plus | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 失败 | search.load：反爬拦截 |
| 少年ジャンプ＋ | shonen_jump_plus | venera-app/venera-configs | 1.1.1 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 少年ジャンプ＋ | shonen_jump_plus | yelongyue197-svg/venera-sources | 1.1.3 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 思思漫画 | sisimanhua | YHQY-Dev/venera-sources | 1.0.0 | venerax | 通过 | 失败 | thumbnail.download：TLS 错误 |
| 漫画家📱⛅ | source_01_656cfe | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 包子漫画 | source_02_e3ec7f | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：HTTP 错误 |
| 污漫天堂🔞 | source_03_c97d34 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| ◯ 拷贝漫画 | source_05_1be182 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 再漫画 | source_06_b7b48e | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| ☄️ 最次元 | source_07_49effa | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 野蛮漫画 | source_08_fa018e | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | image.decode：图片解码失败 |
| 顶漫画 | source_09_fe41f7 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 绅士会所 | source_16_d622ad | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 魅影画廊 | source_17_b7ddde | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 紳士漫畫·国内直连 | source_18_986ee7 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadEp：返回结构或样本不满足契约 |
| 中国人能飞 | source_19_50ee2a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 紳士漫畫🔞🌐 | source_20_d2b98b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadEp：返回结构或样本不满足契约 |
| 鸟鸟韩漫·直连 | source_21_a16969 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 武芊漫画·直连 | source_22_2764a4 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 腾讯漫画 | source_26_c5541c | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 |
| 漫画联合国 | source_32_e5ebaf | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫畫櫃 | source_33_05aedf | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 特漫网 | source_34_0dc3b2 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 漫画人 | source_35_667a4f | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 咚漫 | source_36_d33fb7 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 动漫戏说 | source_38_17bca1 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 |
| 极速漫画 | source_39_7cc572 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 动漫啦 | source_40_5846eb | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 动漫屋 | source_41_b0c446 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫漫漫画 | source_42_481e60 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| 海猫吧 | source_43 | zhimouzhou/venera-manga-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 看漫畫 | source_44_fed97a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 |
| 漫畫狗 | source_45_d76464 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫本 | source_46_ac3286 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫画皮 | source_48_074d4f | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫画园漫画 | source_54 | zhimouzhou/venera-manga-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 |
| 聚合漫画屋 | source_55_082633 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 漫蛙🌐🔞 | source_56_3ebb0b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 仙漫网 | source_58_9bd332 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 拷贝漫画 | source_61_acb91b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 |
| 無限動漫 | source_64_2e309a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 龙王传说网 | source_65_8717b6 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| 漫画柜 | source_74_9820b5 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| サンデーうぇぶり | sunday_webry | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 失败 | search.load：反爬拦截 |
| 腾讯动漫 | tencent_comics | Junkrat9527/venera-sources | 1.1.3 | venerax | 未完整通过 | 失败 | comic.loadInfo：源配置错误 |
| 腾讯动漫 | tencentcomics | xiaoxingmian/venera-configs | 1.0.0 | venerax | 通过 | 失败 | explore[0].load：需要登录 |
| 图库漫画 | tuku_cc | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 失败 | explore[0].load：需要登录 |
| 图库漫画 | tuku_cc | Junkrat9527/venera-sources | 1.0.2 | venerax | 通过 | 失败 | explore[0].load：需要登录 |
| V2PH | v2ph | meaninglesslyy/venera-config | 1.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| vomic | vomic | LX7kM9/venera-configs | 1.2.1 | venerax | 未完整通过 | 失败 | comic.loadEp：需要登录 |
| ◯ 包子漫画web | web_70_6c33fc | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| WEBTOON | webtoon | cattoldme/venera-configs | 1.0.0 | venerax | 通过 | 通过 |  |
| webtoon移动版 | webtoon_71_d28205 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 |
| Webtoon_us | webtoon_us_68_3131e7 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| LINE WEBTOON | webtoons_zh_hant | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |
| LINE WEBTOON | webtoons_zh_hant | Junkrat9527/venera-sources | 1.0.1 | venerax | 通过 | 通过 |  |
| WeebCentral | weebcentral | yelongyue197-svg/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 |
| W漫画 | wmanhua | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 通过 |  |
| W漫画 | wmanhua | Junkrat9527/venera-sources | 1.0.2 | venerax | 通过 | 通过 |  |
| 紳士漫畫 | wnacg | venera-app/venera-configs | 1.0.6 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 紳士漫畫 | wnacg | yelongyue197-svg/venera-sources | 1.0.5 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| x漫画 | x_30_465fc5 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：HTTP 错误 |
| x漫画-M | x_m_29_6ee1ce | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| Xiutaku | xiutaku | meaninglesslyy/venera-config | 1.1.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 |
| X漫画 | xmanhua | Junkrat9527/venera-sources | 1.8.1 | venerax | 通过 | 通过 |  |
| yande.re | yandere | Junkrat9527/venera-sources | 4.9.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 |
| 野蛮漫画 | yemancomic | hea784/venera-configs | 0.1.2 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 野蛮漫画 | yemancomic | Junkrat9527/venera-sources | 1.3.8 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 优酷漫画 (修复版) | ykmh | handahao666-boop/venera_comic_source | 1.0.7 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 |
| 优酷漫画 | ykmh | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 失败 | categoryComics.load：源配置错误 |
| 优酷漫画 | ykmh | zakkida/venera-sources | 1.0.2 | venerax | 通过 | 失败 | categoryComics.load：源配置错误 |
| ◯ YYDS | yyds_04_86b037 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 |
| 再漫画 | zaimanhua | handahao666-boop/venera_comic_source | 1.0.2 | venerax | 未完整通过 | 失败 | comic.loadInfo：源配置错误 |
| zero搬运网 | zerobyw | Junkrat9527/venera-sources | 1.2.0 | venerax | 通过 | 部分通过 | account.loginWithWebview.checkStatus：需要交互 |
| zero搬运网 | zerobyw33 | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| zero搬运网 | zerobyw33 | meaninglesslyy/venera-config | 1.2.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 |
| 知音漫客 | zymk | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 |

## 主索引

古风漫画、A漫、布卡漫画、CosplayTele、动漫屋、咚漫、飞翔漫画、4KHD、瓜子漫画、好看漫画、嬉皮漫畫、花咔漫画、极速漫画、51漫画、Mangabz、漫画人、漫蛙吧（图片修复版）、漫客栈、鸟鸟韩漫、鸟鸟韩漫、极速漫画、大人漫画（私人）、311漫画、神奇漫画、WEBTOON、LINE WEBTOON、W漫画、X漫画

## 扩展索引

Komiic、漫画柜、腾讯动漫、Asura Scans、包子漫画、包子漫画（修订版）、Buon Dua、CCC追漫台、Cosplay啦、comick、CxC、大魔兔、顶漫画、动漫啦、ehentai、4KHD Cosplay、瓜子漫画、Hachiraw、花火漫画、H-Comic、紳士漫畫（私人）、热辣漫画、爱飒漫画、JJCOS、禁漫天堂、禁漫天堂X、看漫画、Kiutaku、来漫画（分流）、Lanraragi、Manga18FX、MangaDex、MangaForFree、178漫画网、漫舍、漫蛙吧、漫画manga、漫画1234（新版网站）、MOJOIN、MOJOIN、漫小肆、MYCOMIC、nhentai、魅影画廊（私人）、如漫画、如漫画、如漫画、SF漫画、少年ジャンプ＋、思思漫画、サンデーうぇぶり、腾讯动漫、图库漫画、紳士漫畫、Xiutaku、优酷漫画 (修复版)、zero搬运网、zero搬运网、知音漫客
