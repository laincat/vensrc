# 上游候选试跑短名单

核验时间：2026-11-27T08:35:44.179062+00:00（UTC）。本轮试跑 40 个候选（每轮上限 40 个），还有 69 个等待首次试跑。
待审构建 504 个：自动收录通道 107 个，试跑但不收录 397 个；未登记仓库的 3 个文件只列出、不下载执行（见 UPDATES.md）。
试跑与已审阅构建使用同一隔离容器，VeneraX 与 Venera-Next 各跑一次；「通过」指核心阅读链路通过，不代表其他能力可用。

## 已排入自动收录（下一轮开始时再次复核并写入清单）

| key | 名称 | 现有版本 → 新版本 | 仓库 |
| --- | --- | --- | --- |

## 自动收录观察期

新构建连续被订阅选中满 7 天且不少于 24 轮才算稳定；此前旧构建留在清单里照常巡检，新构建失败时订阅自动选回旧构建。

| key | 新版本 | 旧版本 | 本轮订阅选中 | 连续选中轮数 | 起算时间 |
| --- | --- | --- | --- | --- | --- |
| ManHuaGui | 1.2.3 | 1.2.1 | 新构建 | 14 | 2026-11-22T12:40:13.675696+00:00 |
| comick | 1.3.0 | 1.2.0 | 新构建 | 13 | 2026-11-22T13:00:58.753361+00:00 |
| cxc | 1.0.4 | 1.0.3 | 新构建 | 14 | 2026-11-22T12:40:13.675696+00:00 |
| hcomic | 1.0.1 | 1.0.0 | 新构建 | 14 | 2026-11-22T12:40:13.675696+00:00 |
| jm | 1.9.3 | 1.9.2 | 未选中新构建（保留旧构建） | 0 |  |
| lanraragi | 1.2.1 | 1.2.0 | 新构建 | 13 | 2026-11-22T13:00:58.753361+00:00 |
| mycomic | 1.2.0 | 1.1.0 | 未选中新构建（保留旧构建） | 0 |  |
| nhentai | 1.1.1 | 1.1.0 | 新构建 | 14 | 2026-11-22T12:40:13.675696+00:00 |

## 试跑通过、等待人工确认

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Komiic | Komiic | 1.0.6 | yelongyue197-svg/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| Komiic | Komiic | 1.0.7 | Magentadots/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| Komiic | Komiic | 1.1.1 | coldnighten/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| ManHuaGui | 漫画柜 | 1.2.2 | Magentadots/venera-configs | 版本 1.2.2 未严格高于清单现有版本 1.2.3 | 无 | 通过 | 通过 |
| ManHuaGui | 漫画柜 | 1.2.2 | nightcat3254/venera-sources | 版本 1.2.2 未严格高于清单现有版本 1.2.3 | 无 | 通过 | 通过 |
| ManHuaGui | 漫画柜 | 1.2.3 | lldaydayhappy/venera-sources | 版本 1.2.3 未严格高于清单现有版本 1.2.3 | 无 | 通过 | 通过 |
| baihehui | 百合会 | 1.0.0 | YongkeDet/venera-configs | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 通过 | 通过 |
| baihehui | 百合会 | 1.0.1 | Magentadots/venera-configs | 同 key 有更高版本的候选 1.0.2 | 无 | 通过 | 通过 |
| baihehui | 百合会 | 1.0.2 | LX7kM9/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| baihehui | 百合会 | 1.0.2 | maplessovo/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| baozi | 包子漫画 | 1.1.9 | maplessovo/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| baozi | 包子漫画 | 1.2.1 | handahao666-boop/venera_comic_source | 新增主机名：www.baozimh.com | www.baozimh.com | 通过 | 通过 |
| bh3 | 《崩坏3》IP站 | 1.0.2 | LX7kM9/venera-configs | 版本 1.0.2 未严格高于清单现有版本 1.0.2 | 无 | 通过 | 通过 |
| boylove | 香香腐宅 | 1.0.0 | YongkeDet/venera-configs | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 通过 | 通过 |
| bzmgcn | 包子漫画 | 1.1.1 | YUIRIKIiii/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| ccc | CCC追漫台 | 1.0.2 | nightcat3254/venera-sources | 版本 1.0.2 未严格高于清单现有版本 1.0.2 | 无 | 通过 | 通过 |
| ccc | CCC追漫台 | 1.0.9 | Junkrat9527/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| ccc | CCC追漫台 | 1.0.9 | LX7kM9/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| ccc | CCC追漫台 | 1.0.9 | lldaydayhappy/venera-sources | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |
| comick | comick | 1.3.0 | lldaydayhappy/venera-sources | 版本 1.3.0 未严格高于清单现有版本 1.3.0 | 无 | 通过 | 通过 |
| copy_manga | 拷贝漫画 | 1.4.8 | yuxuanmian/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| dm5 | 动漫屋 | 2.0.5 | LX7kM9/venera-configs | 版本 2.0.5 未严格高于清单现有版本 7.0.3 | 无 | 通过 | 通过 |
| dm5 | 动漫屋 | 7.0.2 | hgnbh/sw | 版本 7.0.2 未严格高于清单现有版本 7.0.3 | 无 | 通过 | 通过 |
| dongman | 咚漫漫画 | 1.0.0 | cattoldme/venera-configs | 不同 key 指向清单中已有的站点，待核对分区或语言版本 | 无 | 通过 | 通过 |
| dongman_la | 动漫啦 | 1.0.2 | hgnbh/sw | 版本 1.0.2 未严格高于清单现有版本 1.0.5 | 无 | 通过 | 通过 |
| dongman_la | 动漫啦 | 1.0.6 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| dumanwu | 读漫屋 | 17.0.0 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| ehentai | ehentai | 1.2.0 | coldnighten/venera-configs | 版本 1.2.0 未严格高于清单现有版本 1.2.0 | 无 | 通过 | 通过 |
| ehentai | ehentai | 1.2.0 | YongkeDet/venera-configs | 版本 1.2.0 未严格高于清单现有版本 1.2.0 | 无 | 通过 | 通过 |
| ehentai | ehentai | 1.2.1 | VComic-org/venera-comic-source | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |
| ehentai | ehentai | 1.2.1 | Magentadots/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| ehentai | ehentai | 1.2.1 | yuxuanmian/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| ehentai | ehentai | 1.2.4 | lldaydayhappy/venera-sources | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |
| ffppt | 飞翔漫画 | 1.0.1 | n3114576614-cell/N_venera_source | 版本 1.0.1 未严格高于清单现有版本 1.0.3 | 无 | 通过 | 通过 |
| ffppt | 飞翔漫画 | 1.0.2 | Junkrat9527/venera-sources | 版本 1.0.2 未严格高于清单现有版本 1.0.3 | 无 | 通过 | 通过 |
| ffppt | 飞翔漫画 | 1.0.8 | handahao666-boop/venera_comic_source | 新增主机名：dmlimg.youjieke.host、raw.githubusercontent.com | dmlimg.youjieke.host、raw.githubusercontent.com | 通过 | 通过 |
| ffppt | 飞翔漫画 | 1.1.1 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net、dmlimg.youjieke.host | cdn.jsdelivr.net、dmlimg.youjieke.host | 通过 | 通过 |
| gfmh | 古风漫画 | 1.3.1 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| globalcomix | GlobalComix 中文 | 1.0.0 | LX7kM9/venera-configs | 新 key 涉及凭据能力：cookie | 无 | 通过 | 通过 |
| globalcomix | GlobalComix 中文 | 1.0.0 | handahao666-boop/venera_comic_source | 新 key 涉及凭据能力：cookie | 无 | 通过 | 通过 |
| hot_manga | 热辣漫画 | 1.0.1 | Magentadots/venera-configs | 本仓库自建维护的源，不自动替换 | 无 | 通过 | 通过 |
| hot_manga | 热辣漫画 | 1.0.1 | nightcat3254/venera-sources | 本仓库自建维护的源，不自动替换 | 无 | 通过 | 通过 |
| isamanhua | 爱飒漫画 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 通过 | 通过 |
| isamanhua | 爱飒漫画 | 1.1.4 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| kanman | 看漫画 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 2.2.7 | 无 | 通过 | 通过 |
| kanman | 看漫画 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 2.2.7 | 无 | 通过 | 通过 |
| kuaikanmanhua | 快看漫画 | 1.0.0 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| laimanhua_split | 来漫画（分流） | 1.2.2 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| laimanhua_split | 来漫画（分流） | 1.2.2 | Junkrat9527/venera-sources | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| lanraragi | Lanraragi | 1.2.0 | coldnighten/venera-configs | 版本 1.2.0 未严格高于清单现有版本 1.2.1 | 无 | 通过 | 通过 |
| lanraragi | Lanraragi | 1.2.0 | VComic-org/venera-comic-source | 版本 1.2.0 未严格高于清单现有版本 1.2.1 | 无 | 通过 | 通过 |
| lanraragi | Lanraragi | 1.2.0 | YongkeDet/venera-configs | 版本 1.2.0 未严格高于清单现有版本 1.2.1 | 无 | 通过 | 通过 |
| lanraragi | Lanraragi | 1.2.3 | LX7kM9/venera-configs | 新增主机名：127.0.0.1 | 127.0.0.1 | 通过 | 通过 |
| lanraragi | Lanraragi | 1.2.3 | lldaydayhappy/venera-sources | 新增主机名：127.0.0.1、raw.githubusercontent.com | 127.0.0.1、raw.githubusercontent.com | 通过 | 通过 |
| legacy_1kkk | 极速漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| lizimh | 栗子漫画 | 1.2.4 | handahao666-boop/venera_comic_source | 版本 1.2.4 未严格高于清单现有版本 2.33.27 | 无 | 通过 | 通过 |
| lizimh | 栗子漫画 | 1.2.5 | LX7kM9/venera-configs | 版本 1.2.5 未严格高于清单现有版本 2.33.27 | 无 | 通过 | 通过 |
| manben | 漫本 | 1.0.1 | handahao666-boop/venera_comic_source | 版本 1.0.1 未严格高于清单现有版本 1.1.0 | 无 | 通过 | 通过 |
| manga51 | 51漫画 | 1.1.0 | meaninglesslyy/venera-config | 版本 1.1.0 未严格高于清单现有版本 1.2.0 | 无 | 通过 | 通过 |
| manga51 | 51漫画 | 1.3.0 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| manga51 | 51漫画 | 1.3.0 | Junkrat9527/venera-sources | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| manga_dex | MangaDex | 1.9.9 | LX7kM9/venera-configs | 新增凭据能力：accesstoken、authorization、loginrequiredmessage、refreshtoken | api.similarmanga.com、auth.mangadex.org | 通过 | 通过 |
| mangabz | Mangabz | 1.0.3 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net、image.mangabz.com | cdn.jsdelivr.net、image.mangabz.com | 通过 | 通过 |
| manhuagui | 漫画柜 | 1.2.2 | Zicheng0326/my-venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| manhuagui | 漫画柜 | 1.2.2 | YHQY-Dev/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| manhuaren | 漫画人 | 1.0.1 | nightcat3254/venera-sources | 版本 1.0.1 未严格高于清单现有版本 1.0.1 | 无 | 通过 | 通过 |
| manhuaren | 漫画人 | 1.0.1 | Taototo/venera-comic-sources | 版本 1.0.1 未严格高于清单现有版本 1.0.1 | 无 | 通过 | 通过 |
| manhuaren | 漫画人 | 2.0.0 | Junkrat9527/venera-sources | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| manhuaren | 漫画人 | 2.0.1 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| manhuashe | 漫画社 | 1.0.2 | LX7kM9/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 311s.com、cdn.jsdelivr.net、github.com、www.311s.com | 通过 | 通过 |
| manhuawu | 漫画屋 | 1.0.1 | LX7kM9/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | cdn.jsdelivr.net、github.com、m.mhua5.com、mhua5.com、www.mhua5.com | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.0.6 | maplessovo/venera-configs | 版本 1.0.6 未严格高于清单现有版本 1.1.3 | 无 | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.1.0 | coldnighten/venera-configs | 版本 1.1.0 未严格高于清单现有版本 1.1.3 | 无 | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.1.3 | lldaydayhappy/venera-sources | 版本 1.1.3 未严格高于清单现有版本 1.1.3 | 无 | 通过 | 通过 |
| mh160 | 漫画160 | 1.0.0 | handahao666-boop/venera_comic_source | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| mh160 | 漫画160 | 1.0.0 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| mhua5 | 漫画屋 | 1.1.0 | coldnighten/venera-configs | 新 key 涉及凭据能力：account、cookie、login、password | 无 | 通过 | 通过 |
| mhua5 | 漫画屋 | 2.3.3 | Ra1nbo-w/mhy-v | 新 key 涉及凭据能力：account、cookie、deletecookies、getcookies、loginwithcookies、loginwithwebview、setcookies | 无 | 通过 | 通过 |
| mikagogo | 米卡插画 | 1.0.0 | LX7kM9/venera-configs | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 通过 | 通过 |
| mkzhan | 漫客栈 | 1.0.1 | Zicheng0326/my-venera-sources | 版本 1.0.1 未严格高于清单现有版本 1.1.4 | 无 | 通过 | 通过 |
| mkzhan | 漫客栈 | 1.0.1 | YHQY-Dev/venera-sources | 版本 1.0.1 未严格高于清单现有版本 1.1.4 | 无 | 通过 | 通过 |
| mojoin | MOJOIN | 1.0.8 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| mxs | 漫小肆 | 1.0.1 | hgnbh/sw | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| mxs | 漫小肆 | 1.0.1 | Magentadots/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 通过 | 通过 |
| mycomic | MYCOMIC | 2.3.3 | Ra1nbo-w/mhy-v | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |
| namicomi | NamiComi 中文 | 1.0.0 | LX7kM9/venera-configs | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 通过 | 通过 |
| nhentai | nhentai | 1.1.1 | yuxuanmian/venera-configs | 版本 1.1.1 未严格高于清单现有版本 1.1.1 | 无 | 通过 | 通过 |
| nhentai | nhentai | 1.1.1 | VComic-org/venera-comic-source | 版本 1.1.1 未严格高于清单现有版本 1.1.1 | 无 | 通过 | 通过 |
| nhentai | nhentai | 1.1.2 | ChopDream/venera-source-hub | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |
| nhentai | nhentai | 2.0.0 | lldaydayhappy/venera-sources | 新增主机名：i.nhentai.net、raw.githubusercontent.com、t.nhentai.net | i.nhentai.net、raw.githubusercontent.com、t.nhentai.net | 通过 | 通过 |
| nnhanman | 鸟鸟韩漫 | 1.1.1 | meaninglesslyy/venera-config | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| nonhentai | NonHentai | 1.4.0 | LX7kM9/venera-configs | 新 key 涉及凭据能力：account、cookie、deletecookies、getcookies、login、loginwithcookies、loginwithwebview、setcookies | 无 | 通过 | 通过 |
| nonjm | Non禁天堂 | 1.9.6 | LX7kM9/venera-configs | 新 key 涉及凭据能力：account、authorization、cookie、deletecookies、login、password | 无 | 通过 | 通过 |
| pixiv | Pixiv 同人图 | 1.0.1 | hgnbh/sw | 版本 1.0.1 未严格高于清单现有版本 1.9.0 | 无 | 通过 | 通过 |
| rumanhua | 如漫画 | 2.4.1 | Junkrat9527/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| rumanhua | 如漫画 | 2.4.2 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| shonen_jump_plus | 少年ジャンプ＋ | 1.4.0 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| sixmh | 六漫画 | 1.0.1 | handahao666-boop/venera_comic_source | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 通过 |
| sunday_webry | サンデーうぇぶり | 1.0.1 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| tuku_cc | 图库漫画 | 1.0.2 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |
| wmanhua | W漫画 | 1.0.3 | handahao666-boop/venera_comic_source | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 通过 | 通过 |
| wmanhua | W漫画 | 1.0.4 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 通过 | 通过 |

## 试跑未通过

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4khd_24_21d7d1 | 4KHD 美图 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | www.4khd.com | 断在 source.load：源加载或版本不兼容：Invalid or unexpected token | 断在 source.load：源加载或版本不兼容：key 4khd_24_21d7d1 is invalid |
| Komiic | Komiic | 1.0.5 | VComic-org/venera-comic-source | 与清单现有源重名或属于已合并的 key | 无 | 断在 source.load：源加载或版本不兼容：Native source is unavailable during account configuration parsing | 断在 source.load：源加载或版本不兼容：Native source is unavailable during account configuration parsing |
| Komiic | Komiic | 1.0.8 | ZhiLin-Sam/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 断在 comic.loadEp：需要登录：Komiic 游客每日图片额度已用尽，请登录账号后重试（登录可恢复额度） |
| Komiic | Komiic | 1.1.0 | zakkida/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：源配置错误：[] is not a function | 断在 search.load：源配置错误：[] is not a function |
| Komiic | Komiic | 1.8.3 | lldaydayhappy/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadEp：需要登录：account 0 login failed | 断在 comic.loadEp：需要登录：account 0 login failed |
| Komiic | Komiic | 1.8.3 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadEp：需要登录：account 0 login failed | 断在 comic.loadEp：需要登录：account 0 login failed |
| Komiic | Komiic | 1.8.3 | Junkrat9527/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadEp：需要登录：account 0 login failed | 断在 comic.loadEp：需要登录：account 0 login failed |
| a_62_528fe9 | 漫客栈-A | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | comic.mkzhan.com | 断在 search.load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 search.load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| ac_qq | 腾讯动漫 | 1.0.1 | Angus-fw/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：腾讯动漫 未找到章节 | 断在 comic.loadInfo：源配置错误：腾讯动漫 未找到章节 |
| acg456 | ACG456 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.acg456.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| acgncc | ACGN漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、comic.acgn.cc | 断在 search.load：HTTP 错误：搜索失败: 500 | 断在 search.load：HTTP 错误：搜索失败: 500 |
| acgndog_external | 次元狗｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | www.acgndog.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| acqq | 腾讯漫画 | 1.0.0 | token1008/venera-cn-64bit | 新 key 涉及凭据能力：cookie | 无 | 断在 comic.loadInfo：源配置错误：Comic not found | 断在 comic.loadInfo：源配置错误：Comic not found |
| ao3 | AO3 同人图文 | 1.0.1 | hgnbh/sw | 自动收录通道，两端试跑未全部通过 | archiveofourown.org、blockquote.summary、blockquote.userstuff、cdn.jsdelivr.net、h2.title.heading、squidge.world | 断在 search.load：请求限流：Invalid status code: 429 | 断在 search.load：请求限流：Invalid status code: 429 |
| bainianmh | 百年漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：搜索失败: HTTP 401 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| bainianmh2 | 百年漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| banana | 香蕉漫画 | 1.0.4 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| banana_external | 香蕉漫画｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | xjdm168.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| baozi | 包子漫画 | 1.1.7 | YHQY-Dev/venera-sources | 版本 1.1.7 未严格高于清单现有版本 1.1.7 | 无 | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.1.7 | Zicheng0326/my-venera-sources | 版本 1.1.7 未严格高于清单现有版本 1.1.7 | 无 | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.1.7 | ChopDream/venera-source-hub | 版本 1.1.7 未严格高于清单现有版本 1.1.7 | 无 | 断在 comic.loadEp：反爬拦截：Cloudflare challenge requires browser verification | 断在 comic.loadEp：反爬拦截：Cloudflare challenge requires browser verification |
| baozi | 包子漫画 | 1.1.7 | fuluoydebende/venera-configs-fixed | 版本 1.1.7 未严格高于清单现有版本 1.1.7 | 无 | 断在 comic.loadEp：反爬拦截：Cloudflare challenge requires browser verification | 断在 comic.loadEp：反爬拦截：Cloudflare challenge requires browser verification |
| baozi | 包子漫画 | 1.1.7 | zhimouzhou/venera-manga-sources | 版本 1.1.7 未严格高于清单现有版本 1.1.7 | 无 | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.1.8 | nightcat3254/venera-sources | 新增主机名：cdn.jsdelivr.net、github.com | cdn.jsdelivr.net、github.com | 断在 comic.loadEp：反爬拦截：Cloudflare challenge requires browser verification | 断在 comic.loadEp：反爬拦截：Cloudflare challenge requires browser verification |
| baozi | 包子漫画 | 1.1.9 | YongkeDet/venera-configs | 新增主机名：www.baozimh.com | www.baozimh.com | 断在 comic.loadInfo：需要登录：Invalid status code: 403 | 断在 comic.loadInfo：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.0 | Magentadots/venera-configs | 新增主机名：baozimh.com、cdn.jsdelivr.net、cn.baozimh.com、www.baozimh.com | baozimh.com、cdn.jsdelivr.net、cn.baozimh.com、www.baozimh.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.1 | Junkrat9527/venera-sources | 新增主机名：as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.1 | lldaydayhappy/venera-sources | 新增主机名：as2.baozimh.com、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | as2.baozimh.com、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 1.2.3 | LX7kM9/venera-configs | 新增主机名：as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | as2.baozimh.com、cdn.jsdelivr.net、cn.baozimhcn.com、cn.bzmgcn.com、cn.dinnerku.com、cn.kukuc.co、cn.twmanga.com、cn.webmota.com、s1.bzcdn.net、s2.bzcdn.net、static-tw.bzmgcn.com、tw.baozimhcn.com、tw.bzmgcn.com、tw.dinnerku.com、tw.kukuc.co、tw.twmanga.com、tw.webmota.com | 断在 search.load：需要登录：Invalid status code: 403 | 断在 search.load：需要登录：Invalid status code: 403 |
| baozi | 包子漫画 | 2.3.3 | Ra1nbo-w/mhy-v | 新增凭据能力：getcookies、loginhost、loginwithcookies、loginwithwebview | cn.bzmgcn.com、cn.cnbzmg.com、cn.twbzmg.com、www.baozimh.com | 断在 source.load：源加载或版本不兼容：Native source is unavailable during account configuration parsing | 断在 source.load：源加载或版本不兼容：Native source is unavailable during account configuration parsing |
| baozi2 | 包子漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：搜索失败: 403 | 断在 search.load：需要登录：搜索失败: 403 |
| baozi_external | 包子漫画｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | baozimh.org | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| bilimanga | 哔哩哔哩漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.0 未严格高于清单现有版本 1.1.7 | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| bilimanga | 嗶哩漫畫 | 1.1.0 | n3114576614-cell/N_venera_source | 版本 1.1.0 未严格高于清单现有版本 1.1.7 | 无 | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification |
| bilimanga | 嗶哩漫畫 | 1.1.3 | hgnbh/sw | 版本 1.1.3 未严格高于清单现有版本 1.1.7 | 无 | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification |
| bilimanga | 嗶哩漫畫 | 1.2.0 | meaninglesslyy/venera-config | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification |
| bilimanga | 嗶哩漫畫 | 1.2.3 | handahao666-boop/venera_comic_source | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification |
| bilimanga | 哔哩漫画 | 1.6.2 | Junkrat9527/venera-sources | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification | 断在 image.download：反爬拦截：Cloudflare challenge requires browser verification |
| bilimanga | 哔哩漫画 | 2.2.1 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 image.download：反爬拦截：Image HTTP 403 | 断在 image.download：反爬拦截：Image HTTP 403 |
| bukamh | 布卡漫画 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.2.9 | 无 | 断在 search.load：需要登录：Invalid status: 403 | 断在 search.load：需要登录：Invalid status: 403 |
| bukamh | 布卡漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.0 未严格高于清单现有版本 1.2.9 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| bukamh | 布卡漫画 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.2.9 | 无 | 断在 search.load：需要登录：Invalid status: 403 | 断在 search.load：需要登录：Invalid status: 403 |
| buondua_15_095853 | Buondua图集 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | buondua.com | 断在 search.load：反爬拦截：HTTP 403 | 断在 search.load：反爬拦截：HTTP 403 |
| cartoonmad | CartoonMad | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.cartoonmad.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| chuixuemh | 吹雪漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.chuixue.net | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| chuiyao | 吹妖漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.chuiyao.com | 断在 search.load：HTTP 错误：搜索失败: 502 | 断在 search.load：HTTP 错误：搜索失败: 502 |
| colamanga | Colamanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.colamanga.com | 断在 search.load：HTTP 错误：搜索失败: 523 | 断在 search.load：HTTP 错误：搜索失败: 523 |
| comic_walker | カドコミ | 1.0.2 | hgnbh/sw | 同 key 有更高版本的候选 1.1.0 | 无 | 断在 image.decode：未执行 | 断在 image.decode：未执行 |
| comic_walker | カドコミ | 1.0.2 | token1008/venera-cn-64bit | 同 key 有更高版本的候选 1.1.0 | 无 | 断在 image.decode：未执行 | 断在 image.decode：未执行 |
| comic_walker | カドコミ | 1.0.2 | maplessovo/venera-configs | 同 key 有更高版本的候选 1.1.0 | 无 | 断在 image.decode：未执行 | 断在 image.decode：未执行 |
| comic_walker | カドコミ | 1.1.0 | coldnighten/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete |
| comic_walker | カドコミ | 1.3.2 | Junkrat9527/venera-sources | 新增主机名：comic-walker.com | comic-walker.com | 断在 image.decode：未执行 | 断在 image.decode：未执行 |
| comic_walker | カドコミ | 1.3.2 | LX7kM9/venera-configs | 新增主机名：comic-walker.com | comic-walker.com | 断在 image.decode：未执行 | 断在 image.decode：未执行 |
| comic_walker | カドコミ | 1.3.2 | lldaydayhappy/venera-sources | 新增主机名：comic-walker.com、raw.githubusercontent.com | comic-walker.com、raw.githubusercontent.com | 断在 image.decode：未执行 | 断在 image.decode：未执行 |
| comicabc | 無限動漫 | 1.0.0 | handahao666-boop/venera_comic_source | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadEp：源配置错误：原站圖片資料中沒有此章。 | 断在 comic.loadEp：源配置错误：原站圖片資料中沒有此章。 |
| comicbox_external | 污污漫画｜仅外部入口（18+） | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | www.comicbox.xyz | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| comicfury | Comic Fury 中文 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | comicfury.com、github.com、raw.githubusercontent.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| comicfury | Comic Fury 中文 | 1.0.0 | LX7kM9/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | cdn.jsdelivr.net、comicfury.com、github.com、www.comicfury.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| comick | comick | 1.2.1 | fuluoydebende/venera-configs-fixed | 版本 1.2.1 未严格高于清单现有版本 1.3.0 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| copy_manga | 拷贝漫画 | 1.4.4 | nightcat3254/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 1.4.4 | YongkeDet/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 1.4.4 | hea784/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 1.4.4 | maplessovo/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画M | 1.4.4 | zakkida/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 1.4.4 | zakkida/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 1.6.1 | Magentadots/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 1.6.1 | xiaoxingmian/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：請到官網更新最新APP(https://www.copy4000.com/download), 您或您身邊的人曾經下載過破解版本的拷貝漫畫，請下載安裝正版之後等待1小時，限制會自動解除。 | 断在 comic.loadInfo：源配置错误：請到官網更新最新APP(https://www.copy4000.com/download), 您或您身邊的人曾經下載過破解版本的拷貝漫畫，請下載安裝正版之後等待1小時，限制會自動解除。 |
| copy_manga | 拷贝漫画 | 1.6.13 | handahao666-boop/venera_comic_source | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：210：原站限制仍在等待中（剩余约 60分0秒），到期后重新加载；等待结束不代表服务器已确认恢复。原站提示：請到官網更新最新APP(https://www.copy4000.com/download), 您或您身邊的人曾經下載過破解版本的拷貝漫畫，請下載安裝正版之後等待1小時，限制會自動解除。 | 断在 comic.loadInfo：源配置错误：210：原站限制仍在等待中（剩余约 60分0秒），到期后重新加载；等待结束不代表服务器已确认恢复。原站提示：請到官網更新最新APP(https://www.copy4000.com/download), 您或您身邊的人曾經下載過破解版本的拷貝漫畫，請下載安裝正版之後等待1小時，限制會自動解除。 |
| copy_manga | 拷贝漫画 | 1.6.6 | ZhiLin-Sam/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| copy_manga | 拷贝漫画 | 2.3.1 | lldaydayhappy/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete |
| copy_manga | 拷贝漫画 | 2.3.1 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete |
| copy_manga | 拷贝漫画 | 2.3.3 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete | 断在 explore[0].load：前置能力未通过：Source setup or initialization did not complete |
| copy_manga_multi_accounts | 拷贝漫画M | 1.4.2 | hea784/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 comic.loadEp：网络错误：网络请求失败 | 断在 试跑未完成：候选请求地址无法核对 |
| copy_manga_multi_accounts | 拷贝漫画M | 1.4.2 | Magentadots/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：worker_crash：Worker exited before completion (1) | 断在 search.load：worker_crash：Worker exited before completion (1) |
| cosblay | CosBlay | 1.0.0 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、cn.cosblay.com、cosblay.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| cosplaytele | CosplayTele | 1.0.4 | maplessovo/venera-configs | 版本 1.0.4 未严格高于清单现有版本 1.7.0 | 无 | 断在 comic.loadEp：源配置错误：CosplayTele 未找到公开图片集 | 断在 comic.loadEp：源配置错误：CosplayTele 未找到公开图片集 |
| cosplaytele_25_190983 | CosplayTele | 0.2.0 | KadishJoey/venera-json | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadEp：HTTP 错误：HTTP 404 | 断在 comic.loadEp：HTTP 错误：HTTP 404 |
| cw_57_cc4798 | 包子漫画cw | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | cn.webmota.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| cycomic | 次元漫画 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.3 | 无 | 断在 search.load：需要登录：Invalid status: 403 | 断在 search.load：需要登录：Invalid status: 403 |
| cycomic | 次元漫画 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.3 | 无 | 断在 search.load：需要登录：Invalid status: 403 | 断在 search.load：需要登录：Invalid status: 403 |
| damotu | 大魔兔 | 0.7.1 | LX7kM9/venera-configs | 版本 0.7.1 未严格高于清单现有版本 1.0.0 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from /manhua/8302.htm | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from /manhua/8302.htm |
| dashumanhua | 大树漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.dashumanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| dashumanhua2 | 大树漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.dashumanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| dingmanhua | 丁漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.5 | 无 | 断在 comic.loadInfo：HTTP 错误：详情加载失败: 404 | 断在 comic.loadInfo：HTTP 错误：详情加载失败: 404 |
| dm5 | 动漫屋 | 0.2.0 | zhimouzhou/venera-manga-sources | 版本 0.2.0 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua-manbucangqiong | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua-manbucangqiong |
| dm5 | 动漫屋 | 0.2.0 | hea784/venera-configs | 版本 0.2.0 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua-manbucangqiong | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua-manbucangqiong |
| dm5 | 动漫屋 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadEp：HTTP 错误：Invalid status: 404 | 断在 comic.loadEp：HTTP 错误：Invalid status: 404 |
| dm5 | 动漫屋 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadEp：HTTP 错误：Invalid status: 404 | 断在 comic.loadEp：HTTP 错误：Invalid status: 404 |
| dm5 | 动漫屋 | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.1 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情没有返回章节 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情没有返回章节 |
| dm5 | 动漫屋 | 7.0.0 | n3114576614-cell/N_venera_source | 版本 7.0.0 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| dm5 | 动漫屋 | 7.0.1 | Magentadots/venera-configs | 版本 7.0.1 未严格高于清单现有版本 7.0.3 | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| dm5_comics | 动漫屋 | 0.2.2 | Meloon-dr/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：列表项缺少合法 ID、标题或封面 | 断在 search.load：需要登录：列表项缺少合法 ID、标题或封面 |
| dmzj | 动漫之家 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.dmzj.com | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| dogemanga | Dogemanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 同 key 有更高版本的候选 1.0.6 | cdn.jsdelivr.net、dogemanga.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| dogemanga | 漫画狗 | 1.0.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、dogemanga.com、www.dogemanga.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| dokiraw | Dokiraw | 1.0.2 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | dokiraw.guru、gcore.jsdelivr.net | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| dongman | 咚漫 | 1.0.8 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 image.download：请求超时：Network request failed: Request timed out after 10000ms | 通过 |
| dongman_la | 动漫啦 | 1.0.1 | n3114576614-cell/N_venera_source | 版本 1.0.1 未严格高于清单现有版本 1.0.5 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| dongman_la | 动漫啦 | 1.0.3 | Junkrat9527/venera-sources | 版本 1.0.3 未严格高于清单现有版本 1.0.5 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| dongmanla | 动漫啦 | 1.0.0 | YHQY-Dev/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| dongmanla | 动漫啦 | 1.0.0 | Zicheng0326/my-venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| dongmanla | 动漫啦 | 1.0.1 | token1008/venera-cn-64bit | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| dumanwu | 读漫屋 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| dumanwuorg | 读漫屋 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| dxmsk_bakamh_preload | 巴卡漫画（Inkveil预加载版） | 0.2.1 | dxmsk/Venera-Sources | 新 key 涉及凭据能力：account、cookie、getcookies、login、loginwithwebview、password | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| everiaclub | Everia Club | 1.1.0 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、everia.club、span.page-numbers.current、www.everia.club | 断在 search.load：阶段超时：Stage exceeded 20000ms; worker terminated | 断在 search.load：阶段超时：Stage exceeded 20000ms; worker terminated |
| fanbox_personal | FANBOX（个人订阅） | 0.1.1 | MQ9Reaper/venera-personal-sources | 新 key 涉及凭据能力：account、cookie、credentials、deletecookies、getcookies、login、loginwithcookies、loginwithwebview、setcookies | 无 | 断在 search.load：源配置错误：请粘贴 FANBOX 作者／帖子链接，或输入帖子 ID、@作者ID、creator:作者ID；暂不支持标题关键词搜索 | 断在 search.load：源配置错误：请粘贴 FANBOX 作者／帖子链接，或输入帖子 ID、@作者ID、creator:作者ID；暂不支持标题关键词搜索 |
| fantia_personal | Fantia（个人订阅） | 0.1.2 | MQ9Reaper/venera-personal-sources | 新 key 涉及凭据能力：account、cookie、credentials、deletecookies、getcookies、loginwithcookies、setcookies | 无 | 断在 search.load：源配置错误：请粘贴 Fantia 帖子链接、作者链接，或输入帖子 ID / fanclub:作者ID；暂不支持关键词搜索 | 断在 search.load：源配置错误：请粘贴 Fantia 帖子链接、作者链接，或输入帖子 ID / fanclub:作者ID；暂不支持关键词搜索 |
| favcomic | 喜漫漫画 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | github.com、raw.githubusercontent.com、www.favcomic.com | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| feixuemh | 飞雪漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.feixuemh.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| fmh | FMH漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、mh.fumanhua.net | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| gamersky | GamerSky | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | acg.gamersky.com、cdn.jsdelivr.net | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| goda | GoDa漫画 | 1.2.2 | nightcat3254/venera-sources | 同 key 有更高版本的候选 1.2.4 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| goda | GoDa漫画 | 1.2.2 | maplessovo/venera-configs | 同 key 有更高版本的候选 1.2.4 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| goda | GoDa漫画 | 1.2.2 | fuluoydebende/venera-configs-fixed | 新增主机名：godamanga.com | godamanga.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| goda | GoDa漫画 | 1.2.3 | token1008/venera-cn-64bit | 同 key 有更高版本的候选 1.2.4 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| goda | GoDa漫画 | 1.2.4 | lldaydayhappy/venera-sources | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| goda | GoDa漫画 | 1.2.4 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| guazimanhua | 瓜子漫画 | 1.0.1 | Ra1nbo-w/mhy-v | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：瓜子漫画网页请求失败：HTTP 403（https://www.guazimanhua.com/category.php?keyword=%5BREDACTED%5D&page=%5BREDACTED%5D | 断在 search.load：需要登录：瓜子漫画网页请求失败：HTTP 403（https://www.guazimanhua.com/category.php?keyword=%5BREDACTED%5D&page=%5BREDACTED%5D |
| guazimanhua | 瓜子漫画 | 1.0.4 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| guazimanhua | 瓜子漫画 | 1.0.4 | Junkrat9527/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| guazimanhua | 瓜子漫画 | 1.0.4 | ZhiLin-Sam/venera-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| gufengmh | 古风漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| guiluoli | 桂露莉漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.ymgjmh.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| guomanwang | 国漫网 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.guomanwang.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| hanhuaba | 韩话吧 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.hanhuaba.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| hanime1 | Hanime1.me | 2.4.0 | gallhall/venerav-configs | 自动收录通道，两端试跑未全部通过 | hanime1.me | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 source.load：源加载或版本不兼容：minAppVersion 2.0.0 is required |
| hanime1_comics | Hanime1 H漫画 | 1.2.1 | gallhall/venerav-configs | 自动收录通道，两端试跑未全部通过 | hanimeone.me、i2.nhentai.net、t2.nhentai.net | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| haoduoman | 好多漫画 | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、img.haoduoman.com、m.haoduoman.com、www.haoduoman.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| haoduoman2 | 好多漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.haoduoman.com | 断在 search.load：HTTP 错误：搜索失败: 400 | 断在 search.load：HTTP 错误：搜索失败: 400 |
| haokan_txt | 好看漫画 | 1.0.4 | LX7kM9/venera-configs | 版本 1.0.4 未严格高于清单现有版本 1.0.4 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| happy | 嗨皮漫画 | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| happy2 | 嗨皮漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| hciyuan_external | H次元｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | h-ciyuan.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| hentaiclub | 绅士会所 | 1.0.1 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| hhxxee | HHXXEE | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.hhxxee.com | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| hipmh | 嬉皮漫畫 | 1.0.6 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 image.download：请求超时：Network request failed: Request timed out after 10000ms | 断在 image.download：请求超时：Network request failed: Request timed out after 10000ms |
| hitomi | hitomi.la | 1.1.3 | zakkida/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) |
| hitomi | hitomi.la | 1.1.3 | nightcat3254/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) |
| hitomi | hitomi.la | 1.1.3 | Magentadots/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：HTTP 错误：404 | 断在 search.load：HTTP 错误：404 |
| hitomi | hitomi.la | 2.0.0 | lldaydayhappy/venera-sources | 新增主机名：ltn.gold-usergeneratedcontent.net、raw.githubusercontent.com、tn.gold-usergeneratedcontent.net | ltn.gold-usergeneratedcontent.net、raw.githubusercontent.com、tn.gold-usergeneratedcontent.net | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) |
| hitomi | hitomi.la | 2.0.0 | xiaoxingmian/venera-configs | 新增主机名：ltn.gold-usergeneratedcontent.net、tn.gold-usergeneratedcontent.net | ltn.gold-usergeneratedcontent.net、tn.gold-usergeneratedcontent.net | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) | 断在 comic.loadInfo：网络错误：Network request failed: Request budget exceeded (60) |
| hotmanga | 热辣漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.manga2024.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| ikanman | 爱看漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| ikanmantw | 爱看漫繁体 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、tw.manhuagui.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| ikmmh | 爱看漫 | 1.0.7 | Magentadots/venera-configs | 同 key 有更高版本的候选 3.0.1 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| ikmmh | 爱看漫 | 1.0.7 | nightcat3254/venera-sources | 同 key 有更高版本的候选 3.0.1 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| ikmmh | 爱看漫 | 1.0.8 | VComic-org/venera-comic-source | 新增主机名：raw.githubusercontent.com、ymcdnyfqdapp.ikmmh.com | raw.githubusercontent.com、ymcdnyfqdapp.ikmmh.com | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| ikmmh | 爱看漫 | 1.0.8 | yelongyue197-svg/venera-sources | 同 key 有更高版本的候选 3.0.1 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| ikmmh | 爱看漫 | 2.1.2 | Junkrat9527/venera-sources | 新增主机名：137syh.github.io | 137syh.github.io | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| ikmmh | 爱看漫 | 3.0.1 | lldaydayhappy/venera-sources | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 断在 search.load：需要登录：搜索失败：爱看漫反爬校验未通过（403）：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D | 断在 search.load：需要登录：搜索失败：爱看漫反爬校验未通过（403）：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D |
| ikmmh | 爱看漫 | 3.0.1 | Junkrat9527/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：需要登录：搜索失败：爱看漫反爬校验未通过（403）：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D | 断在 search.load：需要登录：搜索失败：爱看漫反爬校验未通过（403）：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D |
| ikmmh | 爱看漫 | 3.0.1 | LX7kM9/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：需要登录：搜索失败：爱看漫反爬校验未通过（403）：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D | 断在 search.load：需要登录：搜索失败：爱看漫反爬校验未通过（403）：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D |
| ikmmh_v2 | 爱看漫 | 3.0.1 | handahao666-boop/venera_comic_source | 新增主机名：raw.githubusercontent.com | raw.githubusercontent.com | 断在 search.load：需要登录：搜索失败：爱看漫拒绝了当前网络出口的地区（403）。请先用同一网络打开原站确认能正常访问，再刷新漫画源。地址：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D | 断在 search.load：需要登录：搜索失败：爱看漫拒绝了当前网络出口的地区（403）。请先用同一网络打开原站确认能正常访问，再刷新漫画源。地址：https://www.ikmmh.com/search?searchkey=%5BREDACTED%5D |
| jcomic | jcomic.net | 1.0.1 | nightcat3254/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 comic.loadEp：返回结构或样本不满足契约：章节没有返回非空图片列表 | 断在 search.load：请求超时：网络请求超时 |
| jisu_1kkk | 极速漫画 | 1.0.0 | token1008/venera-cn-64bit | 与清单现有源重名或属于已合并的 key | 无 | 断在 image.download：需要登录：Image HTTP 403 | 断在 image.download：需要登录：Image HTTP 403 |
| jisumanhua | 极速漫画 | 1.0.0 | handahao666-boop/venera_comic_source | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：需要登录：火影忍者特典漫画 已被列为限制漫画，其中有部份章节可能含有暴力、血腥、色情或不当的语言等内容，不适合未成年观众，为保护未成年人，我们将对 火影忍者特典漫画 进行屏蔽。如果你法定年龄已超过18岁。                                              请点击此处继续阅读！ | 断在 comic.loadInfo：需要登录：火影忍者特典漫画 已被列为限制漫画，其中有部份章节可能含有暴力、血腥、色情或不当的语言等内容，不适合未成年观众，为保护未成年人，我们将对 火影忍者特典漫画 进行屏蔽。如果你法定年龄已超过18岁。                                              请点击此处继续阅读！ |
| jisumh | 极速漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| jm | 禁漫天堂 | 1.4.1 | nightcat3254/venera-sources | 版本 1.4.1 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂 | 1.4.1 | hea784/venera-configs | 版本 1.4.1 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂（18+） | 1.4.1 | Taototo/venera-comic-sources | 版本 1.4.1 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadInfo：HTTP 错误：Invalid Status Code: 500 | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂 | 1.4.1 | maplessovo/venera-configs | 版本 1.4.1 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂 | 1.4.2 | ChopDream/venera-source-hub | 版本 1.4.2 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂 | 1.4.3 | yuxuanmian/venera-configs | 版本 1.4.3 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂 | 1.4.3 | lldaydayhappy/venera-sources | 版本 1.4.3 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jm | 禁漫天堂 | 1.4.3 | Magentadots/venera-configs | 版本 1.4.3 未严格高于清单现有版本 1.9.3 | 无 | 断在 search.load：HTTP 错误：Invalid Status Code: 404 | 断在 search.load：HTTP 错误：Invalid Status Code: 404 |
| jm | 禁漫天堂 | 1.4.3 | VComic-org/venera-comic-source | 版本 1.4.3 未严格高于清单现有版本 1.9.3 | 无 | 断在 comic.loadEp：源配置错误：Invalid Data | 断在 comic.loadEp：源配置错误：Invalid Data |
| jpm1234 | JPM1234 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.jpm1234.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| kalamanhua | 卡拉漫画 | 1.1.0 | yuyuyu529/venera | 新 key 涉及凭据能力：cookie | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| kanman | 看漫画 | 1.0.0 | token1008/venera-cn-64bit | 版本 1.0.0 未严格高于清单现有版本 2.2.7 | 无 | 断在 comic.loadEp：需要登录：本章暂无图片（可能已下架或需要付费/登录） | 断在 comic.loadEp：需要登录：本章暂无图片（可能已下架或需要付费/登录） |
| kanman | 看漫画 | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.1 未严格高于清单现有版本 2.2.7 | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| kavita | Kavita | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| klmanga | KLManga(生肉) | 1.0.0 | yuyuyu529/venera | 同 key 同版本有多个不同构建，需人工选择 | gcore.jsdelivr.net、klmanga.toys | 断在 comic.loadEp：源配置错误：图片解析接口返回非 JSON（可能被反爬拦截） | 断在 comic.loadEp：源配置错误：图片解析接口返回非 JSON（可能被反爬拦截） |
| klmanga | KL漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 同 key 同版本有多个不同构建，需人工选择 | cdn.jsdelivr.net、klmanga.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| klto9 | Klto9 | 1.0.3 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | gcore.jsdelivr.net、klto9.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| kmansin09 | K-Mansin (韩漫) | 1.0.2 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | gcore.jsdelivr.net、kmansin09.top | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| komga | Komga | 1.0.1 | zakkida/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：需要登录：Login expired | 断在 search.load：需要登录：Login expired |
| komga | Komga | 1.0.1 | Magentadots/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：源配置错误：Setting not found: default_username | 断在 search.load：源配置错误：Setting not found: default_username |
| komga | Komga | 1.0.1 | yelongyue197-svg/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情没有返回章节 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情没有返回章节 |
| komiic | Komiic | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、komiic.com、www.komiic.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| komiic2 | Komiic | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、komiic.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| komiic_cc | Komiic漫画 | 2.3.3 | Ra1nbo-w/mhy-v | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 断在 comic.loadEp：源配置错误：Daily image quota exceeded |
| kuaikan | 快看漫画 | 1.0.3 | Angus-fw/venera-configs | 新增凭据能力：account、cookie、deletecookies、login、loginh、loginwithwebview | kkmh.com | 断在 comic.loadInfo：需要登录：快看 请求失败: 403 https://www.kuaikanmanhua.com/v2/pweb/topic/766 | 断在 comic.loadInfo：需要登录：快看 请求失败: 403 https://www.kuaikanmanhua.com/v2/pweb/topic/766 |
| kuaikanmanhua | 快看漫画 | 1.0.0 | handahao666-boop/venera_comic_source | 与清单现有源重名或属于已合并的 key | 无 | 通过 | 断在 image.download：请求超时：Network request failed: Request timed out after 10000ms |
| legacy_51sami | 51漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| legacy_733so | 733漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 自动收录通道，两端试跑未全部通过 | www.733.so | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| legacy_comicun | 漫画联合国 | 0.1.0 | wuliaoe/venera-extra-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：源配置错误：没有解析到搜索结果（站点页面结构可能已更新） | 断在 search.load：源配置错误：没有解析到搜索结果（站点页面结构可能已更新） |
| legacy_damotu | 大魔兔 | 0.1.0 | wuliaoe/venera-extra-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：源配置错误：没有解析到搜索结果（站点页面结构可能已更新） | 断在 search.load：源配置错误：没有解析到搜索结果（站点页面结构可能已更新） |
| legacy_hbdsfj | 六漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| legacy_kanman | 看漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：源配置错误：没有解析到搜索结果（站点页面结构可能已更新） | 断在 search.load：源配置错误：没有解析到搜索结果（站点页面结构可能已更新） |
| legacy_taomanhua | 神漫画 | 0.1.0 | wuliaoe/venera-extra-sources | 自动收录通道，两端试跑未全部通过 | image.mhxk.com、m.taomanhua.com、mhpic.manhualang.com | 断在 search.load：TLS 错误：网络请求失败 | 断在 search.load：TLS 错误：网络请求失败 |
| lizimh | 栗子漫画 | 2.33.37 | Walter498/Walter | 新增凭据能力：loginofficialaccount、logintoken、password | t1.imge.store | 断在 search.load：DNS 错误：栗子接口暂不可用（域名解析失败或网络不可用），请稍后重试 | 断在 search.load：DNS 错误：栗子接口暂不可用（域名解析失败或网络不可用），请稍后重试 |
| m_37_824ad0 | 漫漫漫画-M | 0.2.0 | KadishJoey/venera-json | 不同 key 指向清单中已有的站点，待核对分区或语言版本 | 无 | 断在 search.load：HTTP 错误：HTTP 404 | 断在 search.load：HTTP 错误：HTTP 404 |
| m_47_c0f177 | 咚漫-M | 0.2.0 | KadishJoey/venera-json | 不同 key 指向清单中已有的站点，待核对分区或语言版本 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| magazinepocket | マガポケ Magazine Pocket | 1.0.1 | yuyuyu529/venera | 自动收录通道，两端试跑未全部通过 | api.pocket.shonenmagazine.com、gcore.jsdelivr.net、pocket.shonenmagazine.com | 断在 image.download：前置能力未通过：comic.onImageLoad did not pass | 断在 image.download：前置能力未通过：comic.onImageLoad did not pass |
| manben | 漫本 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.1.0 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| manben | 漫本 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.1.0 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| manga_dex | MangaDex | 1.2.1 | nightcat3254/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：Network response was not ok | 断在 search.load：需要登录：Network response was not ok |
| manga_dex | MangaDex | 1.9.4 | lldaydayhappy/venera-sources | 新增凭据能力：accesstoken、authorization、cookie、loginrequiredmessage、refreshtoken | api.similarmanga.com、auth.mangadex.org、git.nyne.dev、raw.githubusercontent.com | 断在 search.load：需要登录：HTTP 403 | 断在 search.load：需要登录：HTTP 403 |
| manga_dex | MangaDex | 1.9.4 | Junkrat9527/venera-sources | 新增凭据能力：accesstoken、authorization、cookie、loginrequiredmessage、refreshtoken | api.similarmanga.com、auth.mangadex.org、git.nyne.dev | 断在 search.load：需要登录：HTTP 403 | 断在 search.load：需要登录：HTTP 403 |
| mangabz | Mangabz | 0.2.0 | hea784/venera-configs | 版本 0.2.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from 142 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from 142 |
| mangabz | Mangabz | 0.2.0 | zhimouzhou/venera-manga-sources | 版本 0.2.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from 142 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from 142 |
| mangabz | Mangabz | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 search.load：需要登录：列表项缺少合法 ID、标题或封面 | 断在 search.load：需要登录：列表项缺少合法 ID、标题或封面 |
| mangabz | Mangabz | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mangabz | Mangabz | 1.0.0 | zakkida/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| mangabz | Mangabz | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 search.load：需要登录：列表项缺少合法 ID、标题或封面 | 断在 search.load：需要登录：列表项缺少合法 ID、标题或封面 |
| mangabz_72_18ed08 | Mangabz | 0.2.0 | KadishJoey/venera-json | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：HTTP 错误：HTTP 404 | 断在 comic.loadInfo：HTTP 错误：HTTP 404 |
| mangacopy | 拷貝漫畫 | 1.1.1 | YUIRIKIiii/venera-sources | 新 key 涉及凭据能力：account、authorization、cookie、loginwithcookies | 无 | 断在 comic.loadEp：源配置错误：該章節沒有下發圖片密鑰（contentKey 為空）。 站點要求登錄後才給密鑰：請在 漫畫源 → 拷貝漫畫 → 帳號 裏用 Cookie 登錄，再重新打開本章。 | 断在 comic.loadEp：源配置错误：該章節沒有下發圖片密鑰（contentKey 為空）。 站點要求登錄後才給密鑰：請在 漫畫源 → 拷貝漫畫 → 帳號 裏用 Cookie 登錄，再重新打開本章。 |
| mangacopy | MangaCopy | 1.4.5 | istayheart/my-venera-sources | 新 key 涉及凭据能力：account、authorization、login、password | 无 | 断在 comic.loadInfo：源配置错误：Setting not found: base_url | 断在 comic.loadInfo：源配置错误：Setting not found: base_url |
| mangadex | MangaDex | 1.2.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：API 请求失败: 403 | 断在 search.load：需要登录：API 请求失败: 403 |
| mangadex2 | MangaDex | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：需要登录：搜索失败: 403 | 断在 search.load：需要登录：搜索失败: 403 |
| mangaread | MangaRead | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| manhuadb | 漫画DB | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.manhua666.cc | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| manhuade_external | 漫画迷｜仅外部入口 | 1.0.0 | Meloon-dr/venera-sources | 自动收录通道，两端试跑未全部通过 | www.manhuade.com | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 | 断在 explore[0].load：返回结构或样本不满足契约：列表项缺少合法 ID、标题或封面 |
| manhuaguitw | 漫画柜繁体 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、tw.manhuagui.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| manhuapi | 漫画皮 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.4.2 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| manhuapi | 漫画皮 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.4.2 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| manhuatai | 漫画台 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.kanman.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| manhuauo_banana_v2 | 香蕉漫画 | 1.0.4 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| manhuawu | 漫画屋 | 1.0.1 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | github.com、raw.githubusercontent.com、www.mhua5.com | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：HTTP 错误：漫画屋页面请求失败，请稍后重试。 |
| manhuayu | 漫画鱼 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.manhuayu88.com | 断在 search.load：HTTP 错误：搜索失败: 400 | 断在 search.load：HTTP 错误：搜索失败: 400 |
| manwa | 漫蛙 | 1.0.0 | xiaoxingmian/venera-configs | 版本 1.0.0 未严格高于清单现有版本 1.1.6 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| manwa | 漫蛙 | 1.0.18 | yuxuanmian/venera-configs | 版本 1.0.18 未严格高于清单现有版本 1.1.6 | 无 | 断在 search.load：源配置错误：未找到搜索结果区域 | 断在 search.load：源配置错误：未找到搜索结果区域 |
| manwa | 漫蛙 | 1.1.6 | Zicheng0326/my-venera-sources | 版本 1.1.6 未严格高于清单现有版本 1.1.6 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| manwa_me | 漫蛙漫画 | 1.0.2 | shixuit/venera-next-manwa-me-source | 新 key 涉及凭据能力：account、cookie、deletecookies、loginwithcookies、loginwithwebview、setcookies | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| manwa_routes | 漫蛙漫画 | 2.3.3 | Ra1nbo-w/mhy-v | 自动收录通道，两端试跑未全部通过 | fuwbn.cc、manwa.me、manwark.cc、mwmissing1.cc、raw.githubusercontent.com | 断在 search.load：网络错误：漫蛙线路不可用：Error: Network request failed: Request with GET/HEAD method cannot have body.。请在源设置更新线路或打开走失页。 | 断在 search.load：源配置错误：漫蛙线路不可用：Error: 该地址不是已支持的漫蛙漫画站。。请在源设置更新线路或打开走失页。 |
| manwaba | 漫蛙吧 | 1.0.3 | zhimouzhou/venera-manga-sources | 版本 1.0.3 未严格高于清单现有版本 1.1.3 | 无 | 断在 image.decode：图片解码失败：Input buffer contains unsupported image format | 断在 image.decode：图片解码失败：Input buffer contains unsupported image format |
| manwaba | 漫蛙吧 | 1.0.3 | VComic-org/venera-comic-source | 版本 1.0.3 未严格高于清单现有版本 1.1.3 | 无 | 断在 image.decode：图片解码失败：Input buffer contains unsupported image format | 断在 image.decode：图片解码失败：Input buffer contains unsupported image format |
| manwaba | 漫蛙吧 | 1.0.3 | zakkida/venera-sources | 版本 1.0.3 未严格高于清单现有版本 1.1.3 | 无 | 断在 image.decode：图片解码失败：Input buffer contains unsupported image format | 断在 image.decode：图片解码失败：Input buffer contains unsupported image format |
| manwang | 漫网 | 1.3.4 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| meitula | 美图乐 | 1.0.8 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、li.list-item.card、meitula.org、www.meitula.org | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| mh1234 | 漫画1234 | 1.0.1 | Junkrat9527/venera-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：源配置错误：Cannot read properties of null (reading 'attributes') | 断在 search.load：源配置错误：Cannot read properties of null (reading 'attributes') |
| mh1234 | 漫画1234 | 1.0.1 | zakkida/venera-sources | 新增主机名：gmh1234.com | gmh1234.com | 断在 search.load：网络错误：网络请求失败 | 断在 search.load：网络错误：网络请求失败 |
| mh1234 | 漫画1234 | 1.0.1 | zhimouzhou/venera-manga-sources | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| mh1234 | 漫画1234 | 1.0.1 | Magentadots/venera-configs | 同 key 同版本有多个不同构建，需人工选择 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| mh1234 | 漫画1234 | 1.4.3 | LX7kM9/venera-configs | 新增主机名：hqread.cc、m.wmh1234.com、mh1234.com、reader.hqread.cc、wmh1234.com、www.wmh1234.com | hqread.cc、m.wmh1234.com、mh1234.com、reader.hqread.cc、wmh1234.com、www.wmh1234.com | 断在 comic.loadInfo：源配置错误：未找到任何章节，页面结构可能已变化 | 断在 comic.loadInfo：源配置错误：未找到任何章节，页面结构可能已变化 |
| mh1234 | 漫画1234 | 1.4.3 | lldaydayhappy/venera-sources | 新增主机名：hqread.cc、m.wmh1234.com、mh1234.com、raw.githubusercontent.com、reader.hqread.cc、wmh1234.com、www.wmh1234.com | hqread.cc、m.wmh1234.com、mh1234.com、raw.githubusercontent.com、reader.hqread.cc、wmh1234.com、www.wmh1234.com | 断在 comic.loadInfo：源配置错误：未找到任何章节，页面结构可能已变化 | 断在 comic.loadInfo：源配置错误：未找到任何章节，页面结构可能已变化 |
| mh1234 | 漫画1234 | 2.0.2 | maplessovo/venera-configs | 新增主机名：m.wmh1234.com、reader.hqread.cc、wmh1234.com、www.wmh1234.com | m.wmh1234.com、reader.hqread.cc、wmh1234.com、www.wmh1234.com | 断在 comic.loadInfo：源配置错误：未找到章节列表，站点页面结构可能已经更新 | 断在 comic.loadInfo：源配置错误：未找到章节列表，站点页面结构可能已经更新 |
| mh160 | 漫画160 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mh18 | 18漫画 | 1.0.1 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| mh18 | 18漫画 | 1.0.1 | maplessovo/venera-configs | 新增凭据能力：account、deletecookies、loginwithwebview | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| mh36 | 36漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.36mh.org | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mh360 | 360漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| mh4399 | 4399漫画网 | 1.0.5 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 image.download：反爬拦截：Image HTTP 403 | 断在 image.download：反爬拦截：Image HTTP 403 |
| mh522 | 522漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.522manhua.com | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| mh57 | MH57 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.wuqimh.net | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| mh90 | 90漫画 | 0.3.9 | LX7kM9/venera-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 comic.loadInfo：源配置错误：HTML document is unavailable | 断在 comic.loadInfo：源配置错误：HTML document is unavailable |
| mh92 | 92漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| mheee_catalog | 漫自由 | 2.3.4 | Ra1nbo-w/mhy-v | 新 key 涉及凭据能力：account、cookie、deletecookies、login、loginwithwebview、password | 无 | 断在 comic.loadEp：源配置错误：漫自由只有 EPUB / MOBI 文件，不能分话阅读；请点「下载」→ 展开「归档」选卷下载。 | 断在 comic.loadEp：源配置错误：漫自由只有 EPUB / MOBI 文件，不能分话阅读；请点「下载」→ 展开「归档」选卷下载。 |
| mhkan | 漫画看 | 1.0.0 | YHQY-Dev/venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.1.7 | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| mhkan | 漫画看 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.1.7 | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| migudm | 咪咕动漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、migudm.cn | 断在 search.load：HTTP 错误：搜索失败: 502 | 断在 search.load：HTTP 错误：搜索失败: 502 |
| mkzhan | 漫客栈 | 1.0.0 | token1008/venera-cn-64bit | 版本 1.0.0 未严格高于清单现有版本 1.1.4 | 无 | 断在 comic.loadInfo：DNS 错误：网络请求失败 | 断在 comic.loadInfo：DNS 错误：网络请求失败 |
| mkzhan | 快看漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.0 未严格高于清单现有版本 1.1.4 | 无 | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mkzhanw | MKZHANW | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.mkzhan.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mumumh | 梦游漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.mumumh.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| mxqf | MX趣 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.mxshm.top | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| mycomic | MYCOMIC | 1.1.1 | LX7kM9/venera-configs | 版本 1.1.1 未严格高于清单现有版本 1.2.0 | 无 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 |
| mycomic | MYCOMIC | 1.1.1 | lldaydayhappy/venera-sources | 版本 1.1.1 未严格高于清单现有版本 1.2.0 | 无 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 |
| mycomic | MYCOMIC | 1.1.1 | maplessovo/venera-configs | 版本 1.1.1 未严格高于清单现有版本 1.2.0 | 无 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 |
| mycomic | MYCOMIC | 1.1.2 | Magentadots/venera-configs | 版本 1.1.2 未严格高于清单现有版本 1.2.0 | 无 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 |
| mycomic | MYCOMIC | 1.1.2 | ChopDream/venera-source-hub | 版本 1.1.2 未严格高于清单现有版本 1.2.0 | 无 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 | 断在 search.load：反爬拦截：Cloudflare 验证拦截：请在漫画源设置中点击「登录」，通过内置浏览器完成一次 Cloudflare 验证后即可正常使用。 |
| nhentai | nhentai | 1.1.1 | fuluoydebende/venera-configs-fixed | 版本 1.1.1 未严格高于清单现有版本 1.1.1 | 无 | 断在 search.load：HTTP 错误：Invalid Status Code: 400 | 断在 search.load：HTTP 错误：Invalid Status Code: 400 |
| nhentai | nhentai | 1.2.1 | yelongyue197-svg/venera-sources | 新增主机名：i4.nhentai.net | i4.nhentai.net | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| noymanga | NoyManga | 1.1.3 | hgnbh/sw | 版本 1.1.3 未严格高于清单现有版本 1.1.5 | 无 | 断在 search.load：需要登录：尚未登录 NoyManga：请先在源设置中点“登录”（会打开网页），完成后再点“连接测试”里的“测试”。无需手动提取令牌。 | 断在 search.load：需要登录：尚未登录 NoyManga：请先在源设置中点“登录”（会打开网页），完成后再点“连接测试”里的“测试”。无需手动提取令牌。 |
| noymanga | NoyManga | 1.1.6 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：需要登录：尚未登录 NoyManga：请在源设置中填写账号与密码登录（点账号菜单 → 登录）。 | 断在 search.load：需要登录：尚未登录 NoyManga：请在源设置中填写账号与密码登录（点账号菜单 → 登录）。 |
| one_kkk | 极速漫画 | 0.2.0 | hea784/venera-configs | 版本 0.2.0 未严格高于清单现有版本 2.0.0 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua55465 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua55465 |
| one_kkk | 极速漫画 | 0.2.0 | zhimouzhou/venera-manga-sources | 版本 0.2.0 未严格高于清单现有版本 2.0.0 | 无 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua55465 | 断在 comic.loadInfo：网络错误：Network request failed: Failed to parse URL from manhua55465 |
| personal_baozi | 包子 · 个人测试源 | 0.1.0-alpha.3 | hp5588/venera-sources | 版本或源码待核对：版本必须是三段数字，无法确认的版本不得作为官方升级版收录 | 无 | 通过 | 断在 source.load：源加载或版本不兼容：minAppVersion 1.18.1 is required |
| personal_copy | 拷贝 · 个人测试源 | 0.1.0-alpha.2 | hp5588/venera-sources | 版本或源码待核对：版本必须是三段数字，无法确认的版本不得作为官方升级版收录 | 无 | 通过 | 断在 source.load：源加载或版本不兼容：minAppVersion 1.18.1 is required |
| personal_manwame_normal | 漫蛙 · 个人测试源 | 0.1.0-alpha.2 | hp5588/venera-sources | 版本或源码待核对：版本必须是三段数字，无法确认的版本不得作为官方升级版收录 | 无 | 通过 | 断在 source.load：源加载或版本不兼容：minAppVersion 1.18.1 is required |
| photo_deck_danryoku | DANRYOKU | 0.1.6 | tide23333-max/venera-photo-sources | 自动收录通道，两端试跑未全部通过 | danryoku.com、en.girlstop.info、girlstop.info、me.girlstop.info、raw.githubusercontent.com、www.danryoku.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| photo_deck_everia_club | Everia Club | 0.2.4 | tide23333-max/venera-photo-sources | 新 key 涉及凭据能力：account、cookie、deletecookies、getcookies、login、loginwithwebview | 无 | 断在 image.download：网络错误：Network request failed: Cannot convert argument to a ByteString because the character at index 49 has a value of 21335 which is greater than 255. | 断在 image.download：网络错误：Network request failed: Cannot convert argument to a ByteString because the character at index 49 has a value of 21335 which is greater than 255. |
| photo_deck_girlstop | GirlStop | 0.1.4 | tide23333-max/venera-photo-sources | 新 key 涉及凭据能力：account、deletecookies、getcookies、login、loginwithwebview | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| photo_deck_v2ph | V2PH | 0.3.48 | tide23333-max/venera-photo-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| picacg | Picacg | 1.0.13 | yuxuanmian/venera-configs | 新增凭据能力：cookie | 无 | 断在 search.load：需要登录：Not logged in | 断在 source.load：源加载或版本不兼容：minAppVersion 2.0.0 is required |
| picacg | Picacg | 1.0.7 | fuluoydebende/venera-configs-fixed | 新增主机名：picacomic.com | picacomic.com | 断在 search.load：需要登录：Not logged in | 断在 search.load：需要登录：Not logged in |
| picacg | Picacg | 1.0.7 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：需要登录：Not logged in | 断在 search.load：需要登录：Not logged in |
| pixiv | Pixiv | 1.9.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.loadNext：需要登录：Login expired | 断在 search.loadNext：需要登录：Login expired |
| pixiv_token | Pixiv | 0.3.35 | gallhall/venerav-configs | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：源配置错误：Not logged in: refresh_token is empty | 断在 source.load：源加载或版本不兼容：minAppVersion 2.0.0 is required |
| private_hmanwu | 韩漫屋（18+） | 1.1.2 | Taototo/venera-comic-sources | 新 key 涉及凭据能力：account、authorization、login、password | 无 | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| project_gutenberg | Project Gutenberg | 5.0.0 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、gutenberg.org、www.gutenberg.org、www.w3.org | 断在 search.load：HTTP 错误：HTTP 503 | 断在 search.load：HTTP 错误：HTTP 503 |
| pufeimh | 扑飞漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.pufei.cc | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| qimanwu | 奇漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 search.load：需要登录：搜索失败: 403 | 断在 search.load：需要登录：搜索失败: 403 |
| qimiaomh | 奇妙漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 与清单现有源重名或属于已合并的 key | 无 | 断在 search.load：TLS 错误：网络请求失败 | 断在 search.load：TLS 错误：网络请求失败 |
| qq_comic_official | 腾讯动漫（正版） | 2.0.0 | Junkrat9527/venera-sources | 新 key 涉及凭据能力：account、cookie、deletecookies、login、loginrequiredmessage、loginwithwebview | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| qq_comic_official | 腾讯动漫（正版） | 2.1.0 | LX7kM9/venera-configs | 新 key 涉及凭据能力：account、cookie、deletecookies、login、loginrequiredmessage、loginsuccess、loginsuccessmarker、loginwithwebview | 无 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| qq_comic_official_v1 | 腾讯动漫（正版） | 1.0.3 | ZhiLin-Sam/venera-sources | 自动收录通道，两端试跑未全部通过 | m.ac.qq.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| rawkuma | Rawkuma 生肉 | 1.0.0 | yuyuyu529/venera | 版本 1.0.0 未严格高于清单现有版本 1.1.0 | 无 | 断在 search.load：反爬拦截：Rawkuma 取 nonce 失败：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Rawkuma 取 nonce 失败：Cloudflare challenge requires browser verification |
| rawkuma | Rawkuma | 1.1.3 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：反爬拦截：Rawkuma 请求失败：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Rawkuma 请求失败：Cloudflare challenge requires browser verification |
| relamanhua | 熱辣漫畫 | 1.0.0 | handahao666-boop/venera_comic_source | 自动收录通道，两端试跑未全部通过 | api.manga2026.xyz、github.com、m.2024manga.com、raw.githubusercontent.com | 断在 comic.loadEp：源配置错误：該章需要在原站取得閱讀權限。 | 断在 comic.loadEp：源配置错误：該章需要在原站取得閱讀權限。 |
| remenmanhua | 热门漫画 | 1.0.0 | Zicheng0326/my-venera-sources | 版本 1.0.0 未严格高于清单现有版本 1.0.0 | 无 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| roum27 | 肉漫屋 | 1.1.0 | coldnighten/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、roum28.xyz | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| roumh | Rou韩漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.roumh.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| rumanhua | 入漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.rumanhua2.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| sfacg | SF轻小说 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、mm.sfacg.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| sfacg_manhua | SF漫画 | 1.0.2 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| sisimanhua | 思思漫画 | 2.7.0 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 image.download：HTTP 错误：Image HTTP 404 | 断在 image.download：HTTP 错误：Image HTTP 404 |
| soraraw | SoraRaw | 1.1.0 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、i.mangaraw.lat、soraraw.com、soraraw.net、www.soraraw.com、www.soraraw.net | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| source_26_c5541c | 腾讯漫画 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | m.ac.qq.com | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 | 断在 comic.loadInfo：返回结构或样本不满足契约：详情缺少标题或封面 |
| source_33_05aedf | 漫畫櫃 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | tw.manhuagui.com | 断在 search.load：HTTP 错误：HTTP 404 | 断在 search.load：HTTP 错误：HTTP 404 |
| source_56_3ebb0b | 漫蛙🌐🔞 | 0.2.0 | KadishJoey/venera-json | 自动收录通道，两端试跑未全部通过 | manwa.me | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：返回结构或样本不满足契约：当前关键词或列表为空，需复核样本或解析规则 |
| sources_hub | 漫画源聚合与全量导入器 | 1.0.0 | Magentadots/venera-configs | 自动收录通道，两端试跑未全部通过 | appcn.baozimh.com、bakamh.com、biccam.com、cdn.jsdelivr.net、cn.bzmgcn.com、mycomic.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| tooopen | 美图公社 | 1.0.6 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 161.248.86.5、cdn.jsdelivr.net、desk.tooopen.com、imgfzone.tooopen.com、tooopen.com、www.desk.tooopen.com、www.tooopen.com | 断在 search.load：源配置错误：网络请求超时，请重试 | 断在 comic.loadEp：源配置错误：未找到图片。 |
| trendszine | 风流杂志 | 1.1.0 | meaninglesslyy/venera-config | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、trendszine.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| ttkmh | 天天看漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.ttkmh.com | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| u17 | 有妖气 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、u17.com | 断在 search.load：DNS 错误：网络请求失败 | 断在 search.load：DNS 错误：网络请求失败 |
| vomic | vomic | 1.2.2 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 comic.loadEp：需要登录：vomic漫需要登录后才能阅读：请在 [漫画源] -> [vomic漫] -> [登录] 中使用邮箱账号登录 | 断在 comic.loadEp：需要登录：vomic漫需要登录后才能阅读：请在 [漫画源] -> [vomic漫] -> [登录] 中使用邮箱账号登录 |
| wmanhua | W漫画 | 1.0.2 | Junkrat9527/venera-sources | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| wmanhua | W漫画 | 1.0.3 | coldnighten/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：需要登录：当前关键词或列表为空，需复核样本或解析规则 |
| xmanhua2 | X漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、xmanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| yandere | yande.re | 5.0.0 | LX7kM9/venera-configs | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：请求超时：网络请求超时 | 断在 search.load：请求超时：网络请求超时 |
| yemancomic | 野蛮漫画 | 0.1.2 | hea784/venera-configs | 版本 0.1.2 未严格高于清单现有版本 0.1.2 | 无 | 断在 search.load：需要登录：Request Error: 403 https://yemancomic.com/search?searchkey=%5BREDACTED%5D | 断在 search.load：需要登录：Request Error: 403 https://yemancomic.com/search?searchkey=%5BREDACTED%5D |
| yemancomic | 野蛮漫画 | 1.3.8 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：需要登录：Request Error: 403 https://yemancomic.com/search?searchkey=%5BREDACTED%5D | 断在 search.load：需要登录：Request Error: 403 https://yemancomic.com/search?searchkey=%5BREDACTED%5D |
| yibenmanhua | 一本漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.yibenmanhua.com | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 | 断在 search.load：反爬拦截：当前关键词或列表为空，需复核样本或解析规则 |
| yidan | 一耽女孩 | 1.0.0 | sy0sy0/V | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、szfwp.com、www.szfwp.com | 断在 comic.loadEp：需要登录：本章节已锁定，需要付费或会员才能阅读 | 断在 comic.loadEp：需要登录：本章节已锁定，需要付费或会员才能阅读 |
| ykmh | 优酷漫画 | 1.1.0 | lldaydayhappy/venera-sources | 自动收录通道，两端试跑未全部通过 | 无 | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| ykmh | 优酷漫画 | 1.1.0 | Junkrat9527/venera-sources | 新增主机名：cdn.jsdelivr.net | cdn.jsdelivr.net | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| ykmh | 优酷漫画 | 1.2.0 | LX7kM9/venera-configs | 新增主机名：cdn.jsdelivr.net、js.haotuyuk.top | cdn.jsdelivr.net、js.haotuyuk.top | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification | 断在 search.load：反爬拦截：Cloudflare challenge requires browser verification |
| youdm | 优动漫 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.udm123.com | 断在 search.load：TLS 错误：网络请求失败 | 断在 search.load：TLS 错误：网络请求失败 |
| yymanhua | YY漫画 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、m.yymanhua.com、www.yymanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| yymanhua2 | YY漫画备用 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 自动收录通道，两端试跑未全部通过 | cdn.jsdelivr.net、www.yymanhua.com | 断在 search.load：HTTP 错误：搜索失败: 404 | 断在 search.load：HTTP 错误：搜索失败: 404 |
| zaimanhua | 再漫画 | 1.2.6 | lldaydayhappy/venera-sources | 新增主机名：raw.githubusercontent.com、www.zaimanhua.com、zaimanhua.com | raw.githubusercontent.com、www.zaimanhua.com、zaimanhua.com | 断在 comic.loadInfo：源配置错误：漫画不存在或已被删除 | 断在 comic.loadInfo：源配置错误：漫画不存在或已被删除 |
| zaimanhua | 再漫画 | 1.2.6 | LX7kM9/venera-configs | 新增主机名：www.zaimanhua.com、zaimanhua.com | www.zaimanhua.com、zaimanhua.com | 断在 comic.loadInfo：源配置错误：漫画不存在或已被删除 | 断在 comic.loadInfo：源配置错误：漫画不存在或已被删除 |

## 自动通道写入前复核未通过

| key | 名称 | 版本 | 仓库 | 未自动收录的原因 | 新增主机名 | VeneraX | Venera-Next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hachiraw | Hachiraw | 1.1.1 | YUIRIKIiii/venera-sources | 试跑访问新增主机名：i4.hachiraw.win、p16-sg.tiktokcdn.com | 无 | 通过 | 通过 |
| manga1000 | Manga1000 | 1.1.0 | yuyuyu529/venera | 不同 key 的详情请求指向清单已有站点 | gcore.jsdelivr.net、hachiraw.win | 通过 | 通过 |
| manhuaren | 漫画人 | 2.0.0 | lldaydayhappy/venera-sources | 试跑访问新增主机名：manhua1033zjcdn26.cdndm5.com、mhfm9us.cdndm5.com | 无 | 通过 | 通过 |
| manhuashe | 漫画社 | 1.0.2 | handahao666-boop/venera_comic_source | 不同 key 的详情请求指向清单已有站点 | github.com、raw.githubusercontent.com、www.311s.com | 通过 | 通过 |
| manwaba | 漫蛙吧 | 1.1.4 | Magentadots/venera-configs | 试跑访问新增主机名：52.128.238.250、manwauu.cc | 无 | 通过 | 通过 |
| mwuu | 漫蛙漫画 | 1.2.0 | Angus-fw/venera-configs | 不同 key 的详情请求指向清单已有站点 | cdn.jsdelivr.net、manwari.cc、mwuu.cc | 通过 | 通过 |
| photo_deck_4khd | SZZS / 4KHD | 0.1.7 | tide23333-max/venera-photo-sources | 不同 key 的详情请求指向清单已有站点 | 4khd.com、en.girlstop.info、girlstop.info、i0.wp.com、img.4khd.com、me.girlstop.info、pic.4khd.com、raw.githubusercontent.com、szzs.uuss.uk、www.4khd.com | 通过 | 通过 |
| pic12345 | 美女图库 | 1.0.1 | meaninglesslyy/venera-config | 两端实际阅读样本不一致 | cdn.jsdelivr.net、m.pic12345.net | 通过 | 通过 |
| private_myhl | 魅影画廊 | 1.0.2 | Taototo/venera-comic-sources | 试跑访问新增主机名：tk3.myhl005.sbs | 无 | 通过 | 通过 |
