# 上游候选试跑短名单

核验时间：2026-11-22T12:40:13.675696+00:00（UTC）。本轮试跑 40 个候选（每轮上限 40 个），还有 442 个等待首次试跑。
待审构建 506 个：自动收录通道 137 个，试跑但不收录 369 个；未登记仓库的 3 个文件只列出、不下载执行（见 UPDATES.md）。
试跑与已审阅构建使用同一隔离容器，VeneraX 与 Venera-Next 各跑一次；「通过」指核心阅读链路通过，不代表其他能力可用。

## 已排入自动收录（下一轮开始时再次复核并写入清单）

| key | 名称 | 现有版本 → 新版本 | 仓库 |
| --- | --- | --- | --- |
| xkcd | xkcd 中文 | 首次收录 → 1.0.2 | handahao666-boop/venera_comic_source |
| bh3 | 《崩坏3》IP站 | 首次收录 → 1.0.2 | handahao666-boop/venera_comic_source |
| zazhimi | 杂志迷 | 首次收录 → 1.0.2 | handahao666-boop/venera_comic_source |
| terrahistoricus | 泰拉记事社 | 首次收录 → 1.0.1 | handahao666-boop/venera_comic_source |
| namicomi | NamiComi 中文 | 首次收录 → 1.0.0 | handahao666-boop/venera_comic_source |
| toomics | Toomics 玩漫（繁中） | 首次收录 → 1.0.0 | handahao666-boop/venera_comic_source |
| mikagogo | 米卡插画 | 首次收录 → 1.0.0 | handahao666-boop/venera_comic_source |
| comick | comick | 1.2.0 → 1.3.0 | LX7kM9/venera-configs |
| gravuregalaxy | GravureGalaxy | 首次收录 → 2.0.1 | LX7kM9/venera-configs |
| lanraragi | Lanraragi | 1.2.0 → 1.2.1 | Magentadots/venera-configs |
| guixiu_pic | 闺秀网 | 首次收录 → 1.2.0 | meaninglesslyy/venera-config |
| boylove | 香香腐宅 | 首次收录 → 1.0.0 | sy0sy0/V |

## 自动收录观察期

新构建连续被订阅选中满 7 天且不少于 24 轮才算稳定；此前旧构建留在清单里照常巡检，新构建失败时订阅自动选回旧构建。

| key | 新版本 | 旧版本 | 本轮订阅选中 | 连续选中轮数 | 起算时间 |
| --- | --- | --- | --- | --- | --- |
| ManHuaGui | 1.2.3 | 1.2.1 | 新构建 | 1 | 2026-11-22T12:40:13.675696+00:00 |
| cxc | 1.0.4 | 1.0.3 | 新构建 | 1 | 2026-11-22T12:40:13.675696+00:00 |
| hcomic | 1.0.1 | 1.0.0 | 新构建 | 1 | 2026-11-22T12:40:13.675696+00:00 |
| jm | 1.9.3 | 1.9.2 | 新构建 | 1 | 2026-11-22T12:40:13.675696+00:00 |
| mycomic | 1.2.0 | 1.1.0 | 新构建 | 1 | 2026-11-22T12:40:13.675696+00:00 |
| nhentai | 1.1.1 | 1.1.0 | 新构建 | 1 | 2026-11-22T12:40:13.675696+00:00 |

## 试跑通过、等待人工确认

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 试跑未通过

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4khd_24_21d7d1 | 4KHD 美图 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | www.4khd.com | 断在 source.load：源加载或版本不兼容：Invalid or unexpected token | 断在 source.load：源加载或版本不兼容：key 4khd_24_21d7d1 is invalid |
| a_62_528fe9 | 漫客栈-A | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | comic.mkzhan.com | 断在 search.load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 search.load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| acg456 | ACG456 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.acg456.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| acgncc | ACGN漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、comic.acgn.cc | 断在 search.load：HTTP 错误：搜索失败: 500 | 断在 search.load：HTTP 错误：搜索失败: 500 |
| acgndog_external | 次元狗｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | www.acgndog.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| ao3 | AO3 同人图文 | 1.0.1 | hgnbh/sw | 自动收录通道，两端试跑未全部通过 | archiveofourown.org、blockquote.summary、blockquote.userstuff、cdn.jsdelivr.net、h2.title.heading、squidge.world | 断在 search.load：请求限流：Invalid status code: 429 | 断在 search.load：请求限流：Invalid status code: 429 |
| banana_external | 香蕉漫画｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | xjdm168.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| baozi_external | 包子漫画｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | baozimh.org | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| buondua_15_095853 | Buondua图集 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | buondua.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情没有返回章节 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情没有返回章节 |
| cartoonmad | CartoonMad | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.cartoonmad.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| chuixuemh | 吹雪漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.chuixue.net | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| chuiyao | 吹妖漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.chuiyao.com | 断在 search.load：HTTP 错误：搜索失败: 502 | 断在 search.load：HTTP 错误：搜索失败: 502 |
| colamanga | Colamanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.colamanga.com | 断在 search.load：HTTP 错误：搜索失败: 523 | 断在 search.load：HTTP 错误：搜索失败: 523 |
| comic_walker | カドコミ | 1.1.0 | coldnighten/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete |
| comicbox_external | 污污漫画｜仅外部入口（18+） | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | www.comicbox.xyz | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| comicfury | Comic Fury 中文 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | comicfury.com、github.com、raw.githubusercontent.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| copy_manga_multi_accounts | 拷贝漫画M | 1.4.2 | hea784/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 试跑未完成：候选请求地址无法核对 | 断在 试跑未完成：候选请求地址无法核对 |
| cosblay | CosBlay | 1.0.0 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、cn.cosblay.com、cosblay.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| cw_57_cc4798 | 包子漫画cw | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | cn.webmota.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| dashumanhua | 大树漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.dashumanhua.com | 断在 search.load：HTTP 错误：搜索失败: 500 | 断在 search.load：HTTP 错误：搜索失败: 500 |
| dashumanhua2 | 大树漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.dashumanhua.com | 断在 search.load：HTTP 错误：搜索失败: 500 | 断在 search.load：HTTP 错误：搜索失败: 500 |
| dmzj | 动漫之家 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.dmzj.com | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| dogemanga | 漫画狗 | 1.0.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、dogemanga.com、www.dogemanga.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| dokiraw | Dokiraw | 1.0.2 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | dokiraw.guru、gcore.jsdelivr.net | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| everiaclub | Everia Club | 1.1.0 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、everia.club、span.page-numbers.current、www.everia.club | 断在 search.load：阶段超时：Stage exceeded 20000ms; worker terminated | 断在 search.load：阶段超时：Stage exceeded 20000ms; worker terminated |
| favcomic | 喜漫漫画 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | github.com、raw.githubusercontent.com、www.favcomic.com | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| feixuemh | 飞雪漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.feixuemh.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| fmh | FMH漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、mh.fumanhua.net | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| gamersky | GamerSky | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | acg.gamersky.com、cdn.jsdelivr.net | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| goda | GoDa漫画 | 1.2.4 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| guiluoli | 桂露莉漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.ymgjmh.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| guomanwang | 国漫网 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.guomanwang.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| hanhuaba | 韩话吧 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.hanhuaba.com | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| hanime1 | Hanime1.me | 2.4.0 | gallhall/venerav-configs | 自动收录通道，两端试跑未全部通过 | hanime1.me | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 source.load：源加载或版本不兼容：minAppVersion 2.0.0 is required |
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
| copy_web_routes | 拷贝漫画 | 2.3.2 | Ra1nbo-w/mhy-v | 源码声明的 key 与候选不一致 | copy4000.com、raw.githubusercontent.com、www.copy4000.com、www.mangacopy.com | 通过 | 通过 |
| manhuaren | 漫画人 | 2.0.0 | lldaydayhappy/venera-sources | 试跑访问新增主机名：manhua1033zjcdn26.cdndm5.com、mhfm9us.cdndm5.com | 无 | 通过 | 通过 |
| manhuashe | 漫画社 | 1.0.2 | handahao666-boop/venera_comic_source | 不同 key 的详情请求指向清单已有站点 | github.com、raw.githubusercontent.com、www.311s.com | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.1.4 | Magentadots/venera-configs | 试跑访问新增主机名：52.128.238.250、manwauu.cc | 无 | 通过 | 通过 |
| private_myhl | 魅影画廊 | 1.0.2 | Taototo/venera-comic-sources | 试跑访问新增主机名：tk3.myhl005.sbs | 无 | 通过 | 通过 |
