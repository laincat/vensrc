# 上游候选试跑短名单

核验时间：2026-11-22T19:48:55.485679+00:00（UTC）。本轮试跑 40 个候选（每轮上限 40 个），还有 366 个等待首次试跑。
待审构建 489 个：自动收录通道 117 个，试跑但不收录 372 个；未登记仓库的 3 个文件只列出、不下载执行（见 UPDATES.md）。
试跑与已审阅构建使用同一隔离容器，VeneraX 与 Venera-Next 各跑一次；「通过」指核心阅读链路通过，不代表其他能力可用。

## 已排入自动收录（下一轮开始时再次复核并写入清单）

| key | 名称 | 现有版本 → 新版本 | 仓库 |
| --- | --- | --- | --- |
| pandadiu | Cosplay联盟 | 首次收录 → 1.2.3 | LX7kM9/venera-configs |
| twoimg_people | TWOIMG 美女 | 首次收录 → 1.1.1 | meaninglesslyy/venera-config |
| photo_deck_geinou_nude | Geinou Nude | 首次收录 → 0.1.4 | tide23333-max/venera-photo-sources |
| photo_deck_aitoda | Aitoda · Nao Kanzaki | 首次收录 → 0.1.3 | tide23333-max/venera-photo-sources |
| photo_deck_gravurelab | GravureLab | 首次收录 → 0.1.3 | tide23333-max/venera-photo-sources |
| photo_deck_idol_area | IDOL AREA | 首次收录 → 0.1.3 | tide23333-max/venera-photo-sources |
| photo_deck_gravia | Gravia | 首次收录 → 0.1.4 | tide23333-max/venera-photo-sources |
| rawdevart | Rawdevart | 首次收录 → 1.1.2 | yuyuyu529/venera |
| toonkor | 툰코 Toonkor | 首次收录 → 1.0.0 | yuyuyu529/venera |

## 自动收录观察期

新构建连续被订阅选中满 7 天且不少于 24 轮才算稳定；此前旧构建留在清单里照常巡检，新构建失败时订阅自动选回旧构建。

| key | 新版本 | 旧版本 | 本轮订阅选中 | 连续选中轮数 | 起算时间 |
| --- | --- | --- | --- | --- | --- |
| ManHuaGui | 1.2.3 | 1.2.1 | 新构建 | 3 | 2026-11-22T12:40:13.675696+00:00 |
| comick | 1.3.0 | 1.2.0 | 新构建 | 2 | 2026-11-22T13:00:58.753361+00:00 |
| cxc | 1.0.4 | 1.0.3 | 新构建 | 3 | 2026-11-22T12:40:13.675696+00:00 |
| hcomic | 1.0.1 | 1.0.0 | 新构建 | 3 | 2026-11-22T12:40:13.675696+00:00 |
| jm | 1.9.3 | 1.9.2 | 新构建 | 3 | 2026-11-22T12:40:13.675696+00:00 |
| lanraragi | 1.2.1 | 1.2.0 | 新构建 | 2 | 2026-11-22T13:00:58.753361+00:00 |
| mycomic | 1.2.0 | 1.1.0 | 未选中新构建（保留旧构建） | 0 |  |
| nhentai | 1.1.1 | 1.1.0 | 新构建 | 3 | 2026-11-22T12:40:13.675696+00:00 |

## 试跑通过、等待人工确认

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ffppt | 飞翔漫画 | 1.0.8 | handahao666-boop/venera_comic_source | 新增主机名：dmlimg.youjieke.host、raw.githubusercontent.com | dmlimg.youjieke.host、raw.githubusercontent.com | 通过 | 通过 |
| wmanhua | W漫画 | 1.0.3 | handahao666-boop/venera_comic_source | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |

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
| baozi | 包子漫画 | 1.2.0 | Magentadots/venera-configs | 新增主机名：baozimh.com、cdn.jsdelivr.net、cn.baozimh.com、www.baozimh.com | baozimh.com、cdn.jsdelivr.net、cn.baozimh.com、www.baozimh.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.1 | Junkrat9527/venera-sources | 新增主机名：as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.1 | lldaydayhappy/venera-sources | 新增主机名：as2.baozimh.com、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | as2.baozimh.com、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.3 | LX7kM9/venera-configs | 新增主机名：as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
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
| hanime1_comics | Hanime1 H漫画 | 1.2.1 | gallhall/venerav-configs | 自动收录通道，两端试跑未全部通过 | hanimeone.me、i2.nhentai.net、t2.nhentai.net | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| haoduoman | 好多漫画 | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、img.haoduoman.com、m.haoduoman.com、www.haoduoman.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| haoduoman2 | 好多漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.haoduoman.com | 断在 search.load：HTTP 错误：搜索失败: 400 | 断在 search.load：HTTP 错误：搜索失败: 400 |
| happy | 嗨皮漫画 | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| hciyuan_external | H次元｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | h-ciyuan.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| hhxxee | HHXXEE | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.hhxxee.com | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| hotmanga | 热辣漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.manga2024.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| ikanmantw | 爱看漫繁体 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、tw.manhuagui.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| jcomic | jcomic.net | 1.0.1 | nightcat3254/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 comic.loadEp：返回结构或样本不满足契约：章节没有返回非空图片列表 | 断在 comic.loadEp：返回结构或样本不满足契约：章节没有返回非空图片列表 |
| jpm1234 | JPM1234 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.jpm1234.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| kavita | Kavita | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| klto9 | Klto9 | 1.0.3 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | gcore.jsdelivr.net、klto9.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| kmansin09 | K-Mansin (韩漫) | 1.0.2 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | gcore.jsdelivr.net、kmansin09.top | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| komiic | Komiic | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、komiic.com、www.komiic.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| komiic2 | Komiic | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、komiic.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| legacy_733so | 733漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 自动收录通道，两端试跑未全部通过 | www.733.so | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| legacy_taomanhua | 神漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 自动收录通道，两端试跑未全部通过 | image.mhxk.com、m.taomanhua.com、mhpic.manhualang.com | 断在 search.load：TLS 错误：网络请求失败 | 断在 search.load：TLS 错误：网络请求失败 |
| magazinepocket | マガポケ Magazine Pocket | 1.0.1 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | api.pocket.shonenmagazine.com、gcore.jsdelivr.net、pocket.shonenmagazine.com | 断在 image.download：前置能力未通过：comic.onImageLoad did not pass | 断在 image.download：前置能力未通过：comic.onImageLoad did not pass |
| manga_dex | MangaDex | 1.2.1 | nightcat3254/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：Network response was not ok | 断在 search.load：需要登录：Network response was not ok |
| mangakuro | MangaKuro | 1.0.3 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | gcore.jsdelivr.net、mangakuro.net | 断在 image.download：DNS 错误：网络请求失败 | 断在 image.download：DNS 错误：网络请求失败 |
| manhuadb | 漫画DB | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.manhua666.cc | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| manhuade_external | 漫画迷｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | www.manhuade.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| manhuaguitw | 漫画柜繁体 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、tw.manhuagui.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| manhuatai | 漫画台 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.kanman.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| manhuauo_banana_v2 | 香蕉漫画 | 1.0.4 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| manhuawu | 漫画屋 | 1.0.1 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | github.com、raw.githubusercontent.com、www.mhua5.com | 断在 comic.loadEp：请求超时：网络请求超时 | 通过 |
| manhuayu | 漫画鱼 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.manhuayu88.com | 断在 search.load：HTTP 错误：搜索失败: 400 | 断在 search.load：HTTP 错误：搜索失败: 400 |
| manwa_routes | 漫蛙漫画 | 2.3.3 | Ra1nbo-w/mhy-v | 自动收录通道，两端试跑未全部通过 | fuwbn.cc、manwa.me、manwark.cc、mwmissing1.cc、raw.githubusercontent.com | 断在 search.load：网络错误：漫蛙线路不可用：Error: Network request failed: Request with GET/HEAD method cannot have body.。请在源设置更新线路或打开走失页。 | 断在 search.load：源配置错误：漫蛙线路不可用：Error: 该地址不是已支持的漫蛙漫画站。。请在源设置更新线路或打开走失页。 |
| meitula | 美图乐 | 1.0.8 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、li.list-item.card、meitula.org、www.meitula.org | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| mh18 | 18漫画 | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| mh36 | 36漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.36mh.org | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mh522 | 522漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.522manhua.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| mh57 | MH57 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.wuqimh.net | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| migudm | 咪咕动漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、migudm.cn | 断在 search.load：HTTP 错误：搜索失败: 502 | 断在 search.load：HTTP 错误：搜索失败: 502 |
| mkzhanw | MKZHANW | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.mkzhan.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mumumh | 梦游漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.mumumh.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| mxqf | MX趣 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.mxshm.top | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| photo_deck_danryoku | DANRYOKU | 0.1.6 | tide23333-max/venera-photo-sources | 自动收录通道，两端试跑未全部通过 | danryoku.com、en.girlstop.info、girlstop.info、me.girlstop.info、raw.githubusercontent.com、www.danryoku.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| pic12345 | 美女图库 | 1.0.1 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.pic12345.net | 断在 image.download：网络错误：网络请求失败 | 断在 image.download：网络错误：网络请求失败 |
| picacg | Picacg | 1.0.7 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：Not logged in | 断在 search.load：需要登录：Not logged in |
| pixiv | Pixiv | 1.9.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.loadNext：需要登录：Login expired | 断在 search.loadNext：需要登录：Login expired |
| project_gutenberg | Project Gutenberg | 5.0.0 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、gutenberg.org、www.gutenberg.org、www.w3.org | 断在 search.load：HTTP 错误：HTTP 503 | 断在 search.load：HTTP 错误：HTTP 503 |
| pufeimh | 扑飞漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.pufei.cc | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| qq_comic_official_v1 | 腾讯动漫（正版） | 1.0.3 | ZhiLin-Sam/venera-sources | 自动收录通道，两端试跑未全部通过 | m.ac.qq.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| relamanhua | 熱辣漫畫 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | api.manga2026.xyz、github.com、m.2024manga.com、raw.githubusercontent.com | 断在 comic.loadEp：源配置错误：該章需要在原站取得閱讀權限。 | 断在 comic.loadEp：源配置错误：該章需要在原站取得閱讀權限。 |
| roum27 | 肉漫屋 | 1.1.0 | coldnighten/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、roum28.xyz | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| roumh | Rou韩漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.roumh.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| rumanhua | 入漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.rumanhua2.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| sfacg | SF轻小说 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、mm.sfacg.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| source_26_c5541c | 腾讯漫画 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | m.ac.qq.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| source_33_05aedf | 漫畫櫃 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | tw.manhuagui.com | 断在 search.load：HTTP 错误：HTTP 404 | 断在 search.load：HTTP 错误：HTTP 404 |
| source_56_3ebb0b | 漫蛙🌐🔞 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | manwa.me | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| sources_hub | 漫画源聚合与全量导入器 | 1.0.0 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | appcn.baozimh.com、bakamh.com、biccam.com、cdn.jsdelivr.net、cn.bzmgcn.com、mycomic.com | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| tooopen | 美图公社 | 1.0.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 161.248.86.5、cdn.jsdelivr.net、desk.tooopen.com、imgfzone.tooopen.com、tooopen.com、www.desk.tooopen.com、www.tooopen.com | 断在 search.load：源配置错误：网络请求超时，请重试 | 断在 comic.loadEp：源配置错误：未找到图片。 |
| trendszine | 风流杂志 | 1.1.0 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、trendszine.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| ttkmh | 天天看漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.ttkmh.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| u17 | 有妖气 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、u17.com | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| wuxian | 无限动漫 | 1.0.8 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 8comic.com、articles.onemoreplace.tw、cdn.jsdelivr.net、www.8comic.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| xmanhua2 | X漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、xmanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| yandere | yande.re | 4.9.4 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| yibenmanhua | 一本漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.yibenmanhua.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| yidan | 一耽女孩 | 1.0.0 | sy0sy0/V | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、szfwp.com、www.szfwp.com | 断在 comic.loadEp：需要登录：本章节已锁定，需要付费或会员才能阅读 | 断在 comic.loadEp：需要登录：本章节已锁定，需要付费或会员才能阅读 |
| ykmh | 优酷漫画 | 1.1.0 | lldaydayhappy/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| youdm | 优动漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.udm123.com | 断在 search.load：TLS 错误：网络请求失败 | 断在 search.load：TLS 错误：网络请求失败 |
| yymanhua | YY漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.yymanhua.com、www.yymanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| yymanhua2 | YY漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.yymanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |

## 自动通道写入前复核未通过

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baozi | 包子漫画 | 1.1.8 | handahao666-boop/venera_comic_source | 试跑访问新增主机名：cn.twbzmg.com、cn.webmota.com、s1.bzcdn.net | 无 | 通过 | 通过 |
| manga1000 | Manga1000 | 1.1.0 | yuyuyu529/venera | 不同 key 的详情请求指向清单已有站点 | gcore.jsdelivr.net、hachiraw.win | 通过 | 通过 |
| manhuaren | 漫画人 | 2.0.0 | lldaydayhappy/venera-sources | 试跑访问新增主机名：manhua1033zjcdn26.cdndm5.com、mhfm9us.cdndm5.com | 无 | 通过 | 通过 |
| manhuashe | 漫画社 | 1.0.2 | handahao666-boop/venera_comic_source | 不同 key 的详情请求指向清单已有站点 | github.com、raw.githubusercontent.com、www.311s.com | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.1.4 | Magentadots/venera-configs | 试跑访问新增主机名：52.128.238.250、manwauu.cc | 无 | 通过 | 通过 |
| mwuu | 漫蛙漫画 | 1.2.0 | Angus-fw/venera-configs | 不同 key 的详情请求指向清单已有站点 | cdn.jsdelivr.net、manwari.cc、mwuu.cc | 通过 | 通过 |
| photo_deck_4khd | SZZS / 4KHD | 0.1.7 | tide23333-max/venera-photo-sources | 不同 key 的详情请求指向清单已有站点 | 4khd.com、en.girlstop.info、girlstop.info、i0.wp.com、img.4khd.com、me.girlstop.info、pic.4khd.com、raw.githubusercontent.com、szzs.uuss.uk、www.4khd.com | 通过 | 通过 |
| private_myhl | 魅影画廊 | 1.0.2 | Taototo/venera-comic-sources | 试跑访问新增主机名：tk3.myhl005.sbs | 无 | 通过 | 通过 |
