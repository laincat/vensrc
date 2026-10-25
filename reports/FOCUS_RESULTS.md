# 社区替代源与自用仓库重点复测

核验时间：2026-10-25T06:50:06.522714+00:00（UTC）；CLI：`dd6ded39844e56902d3880b1fc1c201a6d1d1fda`。
VeneraX 为订阅依据，Venera-Next 单独对照；固定样本、最低应用版本与源码哈希保持不变。
表内“核心／整次”分别表示阅读链路和报告总状态。登录只采用完全相同构建的独立账号任务证据。
未执行、跳过、缺少凭据和未触发回调均不计通过；两边分时执行的差异也可能来自源站或网络。

## 七个社区替代构建

固定跟踪原先恢复的七个构建；本轮失败或未被选中时仍在此列出，不以其他版本替换证据。

| key | 版本／官方基线 | 来源仓库 | 订阅 | VeneraX 核心／整次 | Next 核心／整次 | X 登录 | Next 登录 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baozi | 1.1.7／1.1.6 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 通过 | 通过 |
| ccc | 1.0.2／1.0.1 | zakkida/venera-sources | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| jm | 1.9.2／1.4.0 | BB-CHICKEN/venera-jm | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 通过 | 通过 |
| manhuaren | 1.0.1／1.0.0 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manwaba | 1.1.3／1.0.2 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| shonen_jump_plus | 1.2.0／1.1.1 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ykmh | 1.0.7／1.0.0 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |

## hea784/venera-configs

| key | 版本／官方基线 | 来源仓库 | 订阅 | VeneraX 核心／整次 | Next 核心／整次 | X 登录 | Next 登录 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Komiic | 1.0.3／1.0.3 | venera-app/venera-configs | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ManHuaGui | 1.2.1／1.2.1 | handahao666-boop/venera_comic_source | 未收录 | 通过／部分通过 | 通过／部分通过 | 通过 | 通过 |
| baozi | 1.1.6／1.1.6 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ccc | 1.0.1／1.0.1 | venera-app/venera-configs | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| comic_walker | 1.0.1／1.0.1 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| comick | 1.2.0／1.2.0 | handahao666-boop/venera_comic_source | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| copy_manga | 1.4.3／1.4.3 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| copy_manga_multi_accounts | 1.4.1／1.4.1 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| dm5 | 0.2.0／无 | hea784/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ehentai | 1.2.0／1.1.8 | venera-app/venera-configs | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| goda | 1.2.1／1.2.1 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| happy | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| hcomic | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| hitomi | 1.1.2／1.1.2 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| hot_manga | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 通过／失败 | 通过／失败 | 通过 | 通过 |
| ikmmh | 1.0.6／1.0.6 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| jcomic | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| jm | 1.4.1／1.4.0 | hea784/venera-configs | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| jm | 1.4.0／1.4.0 | venera-app/venera-configs | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| kavita | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| komga | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| lanraragi | 1.2.0／1.1.0 | venera-app/venera-configs | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manga_dex | 1.2.0／1.2.0 | venera-app/venera-configs | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mangabz | 0.2.0／无 | hea784/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manhuaren | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manwaba | 1.0.3／1.0.2 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mh1234 | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mh18 | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mxs | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mycomic | 1.1.0／1.1.0 | handahao666-boop/venera_comic_source | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| nhentai | 1.1.0／1.1.0 | venera-app/venera-configs | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| one_kkk | 0.2.0／无 | hea784/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| picacg | 1.0.6／1.0.6 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 通过 | 通过 |
| shonen_jump_plus | 1.1.1／1.1.1 | venera-app/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| yemancomic | 0.1.2／无 | hea784/venera-configs | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ykmh | 1.0.0／1.0.0 | venera-app/venera-configs | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| zaimanhua | 1.0.2／1.0.2 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |

## BB-CHICKEN/venera-jm

| key | 版本／官方基线 | 来源仓库 | 订阅 | VeneraX 核心／整次 | Next 核心／整次 | X 登录 | Next 登录 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| jm | 1.9.2／1.4.0 | BB-CHICKEN/venera-jm | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 通过 | 通过 |

## handahao666-boop/venera_comic_source

| key | 版本／官方基线 | 来源仓库 | 订阅 | VeneraX 核心／整次 | Next 核心／整次 | X 登录 | Next 登录 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GfmhApp | 1.3.0／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| Komiic | 1.0.8／1.0.3 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ManHuaGui | 1.2.1／1.2.1 | handahao666-boop/venera_comic_source | 未收录 | 通过／部分通过 | 通过／部分通过 | 通过 | 通过 |
| baihehui | 1.0.0／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| baozi | 1.1.7／1.1.6 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 通过 | 通过 |
| bilimanga | 1.1.7／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ccc | 1.0.1／1.0.1 | handahao666-boop/venera_comic_source | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| comic_walker | 1.0.1／1.0.1 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| comick | 1.2.0／1.2.0 | handahao666-boop/venera_comic_source | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| copy_manga | 1.6.6／1.4.3 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 通过 | 通过 |
| cxc | 1.0.3／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| dm5 | 7.0.3／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| dongman_la | 1.0.5／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| dongmanmanhua | 1.0.6／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ffppt | 1.0.3／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| goda | 1.2.1／1.2.1 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| guazimanhua | 1.0.4／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| hipmh | 1.0.1／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ikmmh_v2 | 3.0.0／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| laimanhua_split | 1.2.1／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manga51 | 1.2.0／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manga_dex | 1.1.1／1.2.0 | handahao666-boop/venera_comic_source | 未收录 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mangabz | 1.0.0／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manhuaren | 1.0.1／1.0.0 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manhuauo_banana_v2 | 1.0.3／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manwaba | 1.1.3／1.0.2 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| manwang | 1.2.0／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mh4399 | 1.0.3／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mojoin_v2 | 1.0.7／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| mycomic | 1.1.0／1.1.0 | handahao666-boop/venera_comic_source | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| noymanga | 1.1.5／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| qq_comic_official_v1 | 1.0.3／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| rawkuma | 1.1.0／无 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| rumanhua_fixed_v15 | 1.2.8／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| sfacg_manhua | 1.0.0／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| shonen_jump_plus | 1.2.0／1.1.1 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| sunday_webry | 1.0.0／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| tuku_cc | 1.0.1／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| webtoons_zh_hant | 1.0.0／无 | handahao666-boop/venera_comic_source | 未收录 | 通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| wmanhua | 1.0.1／无 | handahao666-boop/venera_comic_source | 主订阅 | 通过／通过 | 通过／通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| ykmh | 1.0.7／1.0.0 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| zaimanhua | 1.0.2／1.0.2 | handahao666-boop/venera_comic_source | 未收录 | 未通过／失败 | 未通过／失败 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |
| zerobyw33 | 1.2.0／无 | handahao666-boop/venera_comic_source | 扩展订阅 | 通过／部分通过 | 通过／部分通过 | 未对该构建执行账号巡检 | 未对该构建执行账号巡检 |

## 完整证据

- [客户端逐阶段对照](CLIENT_RESULTS.md)
- [账号登录失败、未验证与跳过项](ACCOUNT_RESULTS.md)
- [反爬与人工验证](ACCESS_RESULTS.md)
- [源码哈希及固定样本](../data/sources.lock.json)
- [全部已审阅构建](../monitor/catalog.json)

巡检 Actions：https://github.com/laincat/vensrc/actions/runs/40169611812
