# 上游候选试跑短名单

核验时间：2026-11-22T12:14:24.881250+00:00（UTC）。本轮试跑 40 个候选（每轮上限 40 个），还有 472 个等待首次试跑。
待审构建 512 个：自动收录通道 143 个，试跑但不收录 369 个；未登记仓库的 3 个文件只列出、不下载执行（见 UPDATES.md）。
试跑与已审阅构建使用同一隔离容器，VeneraX 与 Venera-Next 各跑一次；「通过」指核心阅读链路通过，不代表其他能力可用。

## 已排入自动收录（下一轮开始时再次复核并写入清单）

| key | 名称 | 现有版本 → 新版本 | 仓库 |
| --- | --- | --- | --- |
| jm | 禁漫天堂 | 1.9.2 → 1.9.3 | BB-CHICKEN/venera-jm |
| mycomic | MYCOMIC | 1.1.0 → 1.2.0 | coldnighten/venera-configs |
| cxc | CxC | 1.0.3 → 1.0.4 | LX7kM9/venera-configs |
| ManHuaGui | 漫画柜 | 1.2.1 → 1.2.3 | LX7kM9/venera-configs |
| hcomic | H-Comic | 1.0.0 → 1.0.1 | Magentadots/venera-configs |
| nhentai | nhentai | 1.1.0 → 1.1.1 | Magentadots/venera-configs |

## 自动收录观察期

新构建连续被订阅选中满 7 天且不少于 24 轮才算稳定；此前旧构建留在清单里照常巡检，新构建失败时订阅自动选回旧构建。

| key | 新版本 | 旧版本 | 本轮订阅选中 | 连续选中轮数 | 起算时间 |
| --- | --- | --- | --- | --- | --- |

## 试跑通过、等待人工确认

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 试跑未通过

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4khd_24_21d7d1 | 4KHD 美图 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | www.4khd.com | 断在 source.load：源加载或版本不兼容：Invalid or unexpected token | 断在 source.load：源加载或版本不兼容：key 4khd_24_21d7d1 is invalid |
| a_62_528fe9 | 漫客栈-A | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | comic.mkzhan.com | 断在 search.load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 search.load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| acg456 | ACG456 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.acg456.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| comic_walker | カドコミ | 1.1.0 | coldnighten/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete |
| comicfury | Comic Fury 中文 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | comicfury.com、github.com、raw.githubusercontent.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| copy_manga_multi_accounts | 拷贝漫画M | 1.4.2 | hea784/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 试跑未完成：候选请求地址无法核对 | 断在 试跑未完成：候选请求地址无法核对 |
| favcomic | 喜漫漫画 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | github.com、raw.githubusercontent.com、www.favcomic.com | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| goda | GoDa漫画 | 1.2.4 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| happy | 嗨皮漫画 | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| jcomic | jcomic.net | 1.0.1 | nightcat3254/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 comic.loadEp：返回结构或样本不满足契约：章节没有返回非空图片列表 | 断在 comic.loadEp：返回结构或样本不满足契约：章节没有返回非空图片列表 |
| kavita | Kavita | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| manga_dex | MangaDex | 1.2.1 | nightcat3254/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：Network response was not ok | 断在 search.load：需要登录：Network response was not ok |
| manhuauo_banana_v2 | 香蕉漫画 | 1.0.4 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| manhuawu | 漫画屋 | 1.0.1 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | github.com、raw.githubusercontent.com、www.mhua5.com | 断在 comic.loadEp：请求超时：网络请求超时 | 通过 |
| mh18 | 18漫画 | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| picacg | Picacg | 1.0.7 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：Not logged in | 断在 search.load：需要登录：Not logged in |
| pixiv | Pixiv | 1.9.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.loadNext：需要登录：Login expired | 断在 search.loadNext：需要登录：Login expired |
| relamanhua | 熱辣漫畫 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | api.manga2026.xyz、github.com、m.2024manga.com、raw.githubusercontent.com | 断在 comic.loadEp：源配置错误：該章需要在原站取得閱讀權限。 | 断在 comic.loadEp：源配置错误：該章需要在原站取得閱讀權限。 |
| yandere | yande.re | 4.9.4 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| ykmh | 优酷漫画 | 1.1.0 | lldaydayhappy/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |

## 自动通道写入前复核未通过

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baozi | 包子漫画 | 1.1.8 | handahao666-boop/venera_comic_source | 试跑访问新增主机名：cn.twbzmg.com、cn.webmota.com、s1.bzcdn.net | 无 | 通过 | 通过 |
| bh3 | 《崩坏3》IP站 | 1.0.2 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | comic.bh3.com、github.com、raw.githubusercontent.com | 通过 | 通过 |
| comick | comick | 1.3.0 | LX7kM9/venera-configs | 试跑状态不满足主／扩展标准 | 无 | 通过 | 通过 |
| lanraragi | Lanraragi | 1.2.1 | Magentadots/venera-configs | 试跑状态不满足主／扩展标准 | 无 | 通过 | 通过 |
| manhuaren | 漫画人 | 2.0.0 | lldaydayhappy/venera-sources | 试跑访问新增主机名：manhua1033zjcdn26.cdndm5.com、mhfm9us.cdndm5.com | 无 | 通过 | 通过 |
| manhuashe | 漫画社 | 1.0.2 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | github.com、raw.githubusercontent.com、www.311s.com | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.1.4 | Magentadots/venera-configs | 试跑访问新增主机名：52.128.238.250、manwauu.cc | 无 | 通过 | 通过 |
| mikagogo | 米卡插画 | 1.0.0 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | github.com、mikagogo.com、raw.githubusercontent.com | 通过 | 通过 |
| namicomi | NamiComi 中文 | 1.0.0 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | api.namicomi.com、github.com、namicomi.com、raw.githubusercontent.com、uploads.namicomi.com | 通过 | 通过 |
| private_myhl | 魅影画廊 | 1.0.2 | Taototo/venera-comic-sources | 试跑访问新增主机名：tk3.myhl005.sbs | 无 | 通过 | 通过 |
| terrahistoricus | 泰拉记事社 | 1.0.1 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | comic.hypergryph.com、github.com、raw.githubusercontent.com | 通过 | 通过 |
| toomics | Toomics 玩漫（繁中） | 1.0.0 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | github.com、global.toomics.com、raw.githubusercontent.com | 通过 | 通过 |
| xkcd | xkcd 中文 | 1.0.2 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | github.com、raw.githubusercontent.com、xkcd.tw | 通过 | 通过 |
| zazhimi | 杂志迷 | 1.0.2 | handahao666-boop/venera_comic_source | 源码声明的 key 与候选不一致 | android2026.zazhimi.net、github.com、raw.githubusercontent.com、www.zazhimi.net | 通过 | 通过 |
