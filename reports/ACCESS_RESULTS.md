# 反爬、网络限制与人工处理清单

来源巡检时间：2026-10-26T06:01:14.056897+00:00（UTC）。
anti_bot 表示检测到人机验证或反爬特征，未单凭 403 就认定 Cloudflare。
auth_required 也可能是权限、地区或站点拒绝，不能据此认定密码错误。
正常浏览器可访问不代表 CLI 阅读链路通过，本报告不修改主／扩展订阅。

## 处理顺序

1. 先使用源已提供的公开 API、域名刷新及正常请求头，避免重复登录或高频重试。
2. VeneraX 出现验证窗口时，在该窗口完成正常验证；验证后保持相同网络及浏览器身份再重试。
3. 需要点击、人机题或二步验证时由本人处理；不配置验证码代解服务。
4. GitHub runner 无法复用本机浏览器身份。若云端持续受限，需要站点允许的访问方式、站点监控白名单，或独立且出口稳定的远程验证环境；不会假报通过。
5. 429 应降低请求频率并尊重 Retry-After；地区限制与账号权限单独核对。

## 正常浏览器对照

仅对已审阅的公开首页或登录页做无账号诊断；不提交密码、不提取或发布 Cookie。
Actions 使用无界面 Chromium；其 IP、浏览器身份和 VeneraX WebView 不同，结果分别记录。
登录页能打开不表示登录成功；登录页同时出现登录表单与滑块模块时，单列人工交互要求。

| key | 公开页面 | 浏览器结果 | 观察到 CF challenge 响应头 | 登录交互验证模块 |
| --- | --- | --- | --- | --- |
| bakamh | https://bakamh.com/ | 仍需人工验证 | 是 | 未观察到 |
| rawkuma | https://rawkuma.net/ | 仍需人工验证 | 是 | 未观察到 |
| weebcentral | https://weebcentral.com/ | 仍需人工验证 | 是 | 未观察到 |
| nhentai | https://nhentai.net/ | 仍需人工验证 | 是 | 未观察到 |
| wnacg | https://www.wnacg.com/users-login.html | 浏览器可取得页面 | 否／未观察到 | 观察到滑块模块 |
| wnacg_ru | https://www.wnacg.ru/users-login.html | 浏览器可取得页面 | 否／未观察到 | 观察到滑块模块 |
| wnacg_003 | https://www.wn003.cfd/users-login.html | 浏览器可取得页面 | 否／未观察到 | 观察到滑块模块 |
| wnacg_004 | https://www.wn004.cfd/users-login.html | 浏览器网络失败 | 否／未观察到 | 未观察到 |
| wnacg_page1 | https://wnacg01.link/ | 未确认取得正常内容 | 否／未观察到 | 未观察到 |
| wnacg_page2 | https://wnacg02.link/ | 未确认取得正常内容 | 否／未观察到 | 未观察到 |

## 需要本人验证的站点

- `bakamh`（https://bakamh.com）：Actions 正常浏览器等待后仍出现验证，需本人在 VeneraX 验证窗口处理并在同环境重试。
- `rawkuma`（https://rawkuma.net）：Actions 正常浏览器等待后仍出现验证，需本人在 VeneraX 验证窗口处理并在同环境重试。
- `weebcentral`（https://weebcentral.com）：Actions 正常浏览器等待后仍出现验证，需本人在 VeneraX 验证窗口处理并在同环境重试。
- `nhentai`（https://nhentai.net）：Actions 正常浏览器等待后仍出现验证，需本人在 VeneraX 验证窗口处理并在同环境重试。
- `wnacg`（https://www.wnacg.com/users-login.html）：登录页加载滑块验证模块，需本人完成交互；这与 CF 挑战分别记录，未执行账号登录。
- `wnacg_ru`（https://www.wnacg.ru/users-login.html）：登录页加载滑块验证模块，需本人完成交互；这与 CF 挑战分别记录，未执行账号登录。
- `wnacg_003`（https://www.wn003.cfd/users-login.html）：登录页加载滑块验证模块，需本人完成交互；这与 CF 挑战分别记录，未执行账号登录。

CLI 检测到反爬的源 key：`aiman`、`bakamh`、`batcavebiz`、`bilimanga`、`ex_fangliding`、`foamgirl`、`goda`、`guoman8`、`hentaiclub`、`hj_baozi`、`legacy_733so`、`manhuaba`、`manhuapi`、`manwang`、`mh18`、`mh4399`、`miaoqu`、`mitaku`、`nhentai`、`ososedki`、`rawkuma`、`shonen_jump_plus`、`source_16_d622ad`、`source_19_50ee2a`、`source_45_d76464`、`source_48_074d4f`、`source_56_3ebb0b`、`source_65_8717b6`、`sunday_webry`、`v2ph`、`weebcentral`。
未纳入首页浏览器对照的源仍未完成人工验证；首页诊断成功也不代表正文接口通过。

## 逐构建处理清单

| 名称 | key | 版本 | 仓库 | 环境 | 核心阅读 | 受限阶段 | 类别／处理 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 百合会 | baihehui | 1.0.0 | handahao666-boop/venera_comic_source | venerax | 通过（其他能力受限） | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 包子漫画 | baozi | 1.1.6 | venera-app/venera-configs | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 嗶哩漫畫 | bilimanga | 1.1.7 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| カドコミ | comic_walker | 1.0.1 | handahao666-boop/venera_comic_source | venerax | 未通过 | init | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ehentai | ehentai | 1.2.0 | venera-app/venera-configs | venerax | 通过（其他能力受限） | comic.archive.getArchives | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| GoDa漫画 | goda | 1.2.1 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 爱看漫 | ikmmh | 1.0.6 | venera-app/venera-configs | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 爱看漫 | ikmmh_v2 | 3.0.0 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 香蕉漫画 | manhuauo_banana_v2 | 1.0.3 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫网 | manwang | 1.2.0 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 18漫画 | mh18 | 1.0.0 | venera-app/venera-configs | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 4399漫画网 | mh4399 | 1.0.3 | handahao666-boop/venera_comic_source | venerax | 未通过 | image.download；image.download；thumbnail.download | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| NoyManga | noymanga | 1.1.5 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Picacg | picacg | 1.0.6 | venera-app/venera-configs | venerax | 未通过 | search.load；categoryComics.load；categoryComics.ranking.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Rawkuma | rawkuma | 1.1.0 | handahao666-boop/venera_comic_source | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.1 | venera-app/venera-configs | venerax | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| サンデーうぇぶり | sunday_webry | 1.0.0 | handahao666-boop/venera_comic_source | venerax | 通过（其他能力受限） | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 图库漫画 | tuku_cc | 1.0.1 | handahao666-boop/venera_comic_source | venerax | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 野蛮漫画 | yemancomic | 0.1.2 | hea784/venera-configs | venerax | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；categoryComics.ranking.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Komiic | Komiic | 1.0.8 | handahao666-boop/venera_comic_source | venerax | 未通过 | comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| カドコミ | comic_walker | 1.0.1 | venera-app/venera-configs | venerax | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.2.0 | handahao666-boop/venera_comic_source | venerax | 通过（其他能力受限） | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 爱漫岛 | aiman | 2.3.6 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 百合会 | baihehui | 1.0.2 | Junkrat9527/venera-sources | venerax | 通过（其他能力受限） | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 巴卡漫画 | bakamh | 1.0.1 | Magentadots/venera-configs | venerax | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 香蕉漫画 | banana | 1.0.4 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 包子漫画 | baozi | 1.1.0 | l233333333/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 包子漫画（重制版） | baozi_recode | 1.1.7 | Micqiyue/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| BatCave.biz | batcavebiz | 1.0.5 | F22822/22822 | venerax | 未通过 | search.load；explore[0].load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 哔哩漫画 | bilimanga | 1.6.2 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| カドコミ | comic_walker | 1.0.1 | zakkida/venera-sources | venerax | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 次元漫画 | cycomic | 1.0.3 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；categoryComics.ranking.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ehentai | ehentai | 1.1.8 | yelongyue197-svg/venera-sources | venerax | 通过（其他能力受限） | comic.archive.getArchives | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ExHentai (fangliding 镜像) | ex_fangliding | 1.2.0 | zakkida/venera-sources | venerax | 未通过 | search.loadNext；explore[0].loadNext；explore[1].loadNext；categoryComics.ranking.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| FoamGirl | foamgirl | 1.2.1 | meaninglesslyy/venera-config | venerax | 未通过 | explore[1].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| GMANHUA | gmanhua_59_ee9658 | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 国漫吧 | guoman8 | 1.0.2 | token1008/venera-cn-64bit | venerax | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；explore[4].load；explore[5].load；explore[6].load；explore[7].load；explore[8].load；explore[9].load；explore[10].load；explore[11].load；explore[12].load；explore[13].load；explore[14].load；explore[15].load；explore[16].load；explore[1 | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 花火漫画 | hanabimanga | 1.0.0 | xiaoxingmian/venera-configs | venerax | 未通过 | comic.loadEp | 限流：降低频率并按站点要求延迟 |
| 绅士会所 | hentaiclub | 1.0.0 | meaninglesslyy/venera-config | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 包子漫画（私人） | hj_baozi | 1.1.7 | Taototo/venera-comic-sources | venerax | 未通过 | comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 爱看漫 | ikmmh | 1.0.8 | yelongyue197-svg/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 极速漫画 | jisu_1kkk | 1.0.0 | token1008/venera-cn-64bit | venerax | 未通过 | image.download；image.download | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Komga | komga | 1.0.1 | zakkida/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Komiic 多账号 | komiic_multi | 1.6.2 | snowf14k3/venera-komiic-multi | venerax | 未通过 | comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 733漫画 | legacy_733so | 0.1.0 | wuliaoe/venera-extra-sources | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 搜动漫 | legacy_soudongman | 0.1.0 | wuliaoe/venera-extra-sources | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 六漫画 | liumanhua | 1.0.0 | token1008/venera-cn-64bit | venerax | 未通过 | explore[1].load；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫本 | manben | 1.1.0 | Junkrat9527/venera-sources | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| MANGA Plus | manga_plus | 1.0.2 | WEP-56/EZvenera-config | venerax | 未通过 | search.load；categoryComics.load；categoryComics.ranking.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Mangabz | mangabz | 1.0.0 | YHQY-Dev/venera-sources | venerax | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫画吧网 | manhuaba | 1.0.0 | token1008/venera-cn-64bit | venerax | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；explore[4].load；explore[5].load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫画皮 | manhuapi | 1.4.2 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫网 | manwang | 1.3.4 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫画manga | mh03 | 1.0.1 | Magentadots/venera-configs | venerax | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 4399漫画网 | mh4399 | 1.0.5 | Junkrat9527/venera-sources | venerax | 未通过 | image.download；image.download | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 喵趣漫画 | miaoqu | 1.0.0 | token1008/venera-cn-64bit | venerax | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；explore[4].load；explore[5].load；explore[6].load；explore[7].load；explore[8].load；explore[9].load；explore[10].load；explore[11].load；explore[12].load；explore[13].load；explore[14].load；explore[15].load；explore[16].load；explore[1 | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| Mitaku | mitaku | 1.0.0 | meaninglesslyy/venera-config | venerax | 未通过 | comic.loadInfo | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| nhentai | nhentai | 1.2.1 | yelongyue197-svg/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| NoyACG | noyacg | 1.4.0 | zetriumyx/noyacg-source-venera | venerax | 未通过 | explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Ososedki | ososedki | 1.1.1 | meaninglesslyy/venera-config | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| Pixiv | pixiv | 1.9.0 | Junkrat9527/venera-sources | venerax | 未通过 | search.loadNext；explore[0].loadNext；explore[1].loadNext；explore[3].loadNext；explore[4].loadNext；explore[5].loadNext；explore[6].loadNext；categoryComics.load；categoryComics.ranking.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 奇漫屋 | qimanwu | 1.0.0 | token1008/venera-cn-64bit | venerax | 未通过 | explore[6].load；explore[12].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Rawkuma | rawkuma | 1.1.3 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.3 | yelongyue197-svg/venera-sources | venerax | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ☄️ 最次元 | source_07_49effa | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 绅士会所 | source_16_d622ad | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 中国人能飞 | source_19_50ee2a | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 咚漫 | source_36_d33fb7 | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 极速漫画 | source_39_7cc572 | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫畫狗 | source_45_d76464 | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫画皮 | source_48_074d4f | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫蛙🌐🔞 | source_56_3ebb0b | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 龙王传说网 | source_65_8717b6 | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 腾讯动漫 | tencentcomics | 1.0.0 | xiaoxingmian/venera-configs | venerax | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 图库漫画 | tuku_cc | 1.0.2 | Junkrat9527/venera-sources | venerax | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| V2PH | v2ph | 1.2.0 | meaninglesslyy/venera-config | venerax | 未通过 | search.load；categoryComics.load；comic.loadInfo | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| vomic | vomic | 1.2.1 | LX7kM9/venera-configs | venerax | 未通过 | comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| WEBTOON | webtoon | 1.0.0 | cattoldme/venera-configs | venerax | 未通过 | thumbnail.download | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| WeebCentral | weebcentral | 1.0.0 | yelongyue197-svg/venera-sources | venerax | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 野蛮漫画 | yemancomic | 1.3.8 | Junkrat9527/venera-sources | venerax | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；categoryComics.ranking.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ◯ YYDS | yyds_04_86b037 | 0.2.0 | KadishJoey/venera-json | venerax | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 百合会 | baihehui | 1.0.0 | handahao666-boop/venera_comic_source | venera-next | 通过（其他能力受限） | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 包子漫画 | baozi | 1.1.6 | venera-app/venera-configs | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 嗶哩漫畫 | bilimanga | 1.1.7 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| ehentai | ehentai | 1.2.0 | venera-app/venera-configs | venera-next | 通过（其他能力受限） | comic.archive.getArchives | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| GoDa漫画 | goda | 1.2.1 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 爱看漫 | ikmmh | 1.0.6 | venera-app/venera-configs | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 爱看漫 | ikmmh_v2 | 3.0.0 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 香蕉漫画 | manhuauo_banana_v2 | 1.0.3 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫网 | manwang | 1.2.0 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 18漫画 | mh18 | 1.0.0 | venera-app/venera-configs | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 4399漫画网 | mh4399 | 1.0.3 | handahao666-boop/venera_comic_source | venera-next | 未通过 | image.download；image.download；thumbnail.download | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| NoyManga | noymanga | 1.1.5 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Picacg | picacg | 1.0.6 | venera-app/venera-configs | venera-next | 未通过 | search.load；categoryComics.load；categoryComics.ranking.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Rawkuma | rawkuma | 1.1.0 | handahao666-boop/venera_comic_source | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.1 | venera-app/venera-configs | venera-next | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| サンデーうぇぶり | sunday_webry | 1.0.0 | handahao666-boop/venera_comic_source | venera-next | 通过（其他能力受限） | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 图库漫画 | tuku_cc | 1.0.1 | handahao666-boop/venera_comic_source | venera-next | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 野蛮漫画 | yemancomic | 0.1.2 | hea784/venera-configs | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；categoryComics.ranking.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.2.0 | handahao666-boop/venera_comic_source | venera-next | 通过（其他能力受限） | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 腾讯动漫 | ac_qq | 1.0.1 | Angus-fw/venera-configs | venera-next | 未通过 | comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 爱漫岛 | aiman | 2.3.6 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 百合会 | baihehui | 1.0.2 | Junkrat9527/venera-sources | venera-next | 通过（其他能力受限） | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 巴卡漫画 | bakamh | 1.0.1 | Magentadots/venera-configs | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 香蕉漫画 | banana | 1.0.4 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 包子漫画 | baozi | 1.1.0 | l233333333/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 包子漫画（重制版） | baozi_recode | 1.1.7 | Micqiyue/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| BatCave.biz | batcavebiz | 1.0.5 | F22822/22822 | venera-next | 未通过 | search.load；explore[0].load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 哔哩漫画 | bilimanga | 1.6.2 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| カドコミ | comic_walker | 1.0.1 | zakkida/venera-sources | venera-next | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 次元漫画 | cycomic | 1.0.3 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；categoryComics.ranking.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ehentai | ehentai | 1.1.8 | yelongyue197-svg/venera-sources | venera-next | 通过（其他能力受限） | comic.archive.getArchives | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ExHentai (fangliding 镜像) | ex_fangliding | 1.2.0 | zakkida/venera-sources | venera-next | 未通过 | search.loadNext；explore[0].loadNext；explore[1].loadNext；categoryComics.ranking.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| FoamGirl | foamgirl | 1.2.1 | meaninglesslyy/venera-config | venera-next | 未通过 | explore[1].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| GMANHUA | gmanhua_59_ee9658 | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 国漫吧 | guoman8 | 1.0.2 | token1008/venera-cn-64bit | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；explore[4].load；explore[5].load；explore[6].load；explore[7].load；explore[8].load；explore[9].load；explore[10].load；explore[11].load；explore[12].load；explore[13].load；explore[14].load；explore[15].load；explore[16].load；explore[1 | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 花火漫画 | hanabimanga | 1.0.0 | xiaoxingmian/venera-configs | venera-next | 未通过 | comic.loadEp | 限流：降低频率并按站点要求延迟 |
| 绅士会所 | hentaiclub | 1.0.0 | meaninglesslyy/venera-config | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 包子漫画（私人） | hj_baozi | 1.1.7 | Taototo/venera-comic-sources | venera-next | 未通过 | comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 爱看漫 | ikmmh | 1.0.8 | yelongyue197-svg/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 极速漫画 | jisu_1kkk | 1.0.0 | token1008/venera-cn-64bit | venera-next | 未通过 | image.download；image.download | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Komga | komga | 1.0.1 | zakkida/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Komiic 多账号 | komiic_multi | 1.6.2 | snowf14k3/venera-komiic-multi | venera-next | 未通过 | comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 733漫画 | legacy_733so | 0.1.0 | wuliaoe/venera-extra-sources | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 搜动漫 | legacy_soudongman | 0.1.0 | wuliaoe/venera-extra-sources | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 六漫画 | liumanhua | 1.0.0 | token1008/venera-cn-64bit | venera-next | 未通过 | explore[1].load；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫本 | manben | 1.1.0 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| MANGA Plus | manga_plus | 1.0.2 | WEP-56/EZvenera-config | venera-next | 未通过 | search.load；categoryComics.load；categoryComics.ranking.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Mangabz | mangabz | 1.0.0 | YHQY-Dev/venera-sources | venera-next | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫画吧网 | manhuaba | 1.0.0 | token1008/venera-cn-64bit | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；explore[4].load；explore[5].load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫画皮 | manhuapi | 1.4.2 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫网 | manwang | 1.3.4 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load；comic.loadInfo；comic.loadEp | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫画manga | mh03 | 1.0.1 | Magentadots/venera-configs | venera-next | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 4399漫画网 | mh4399 | 1.0.5 | Junkrat9527/venera-sources | venera-next | 未通过 | image.download；image.download | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 喵趣漫画 | miaoqu | 1.0.0 | token1008/venera-cn-64bit | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；explore[3].load；explore[4].load；explore[5].load；explore[6].load；explore[7].load；explore[8].load；explore[9].load；explore[10].load；explore[11].load；explore[12].load；explore[13].load；explore[14].load；explore[15].load；explore[16].load；explore[1 | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| Mitaku | mitaku | 1.0.0 | meaninglesslyy/venera-config | venera-next | 未通过 | comic.loadInfo | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| nhentai | nhentai | 1.2.1 | yelongyue197-svg/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| NoyACG | noyacg | 1.4.0 | zetriumyx/noyacg-source-venera | venera-next | 未通过 | explore[0].load；categoryComics.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Ososedki | ososedki | 1.1.1 | meaninglesslyy/venera-config | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| Pixiv | pixiv | 1.9.0 | Junkrat9527/venera-sources | venera-next | 未通过 | search.loadNext；explore[0].loadNext；explore[1].loadNext；explore[3].loadNext；explore[4].loadNext；explore[5].loadNext；explore[6].loadNext；categoryComics.load；categoryComics.ranking.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 奇漫屋 | qimanwu | 1.0.0 | token1008/venera-cn-64bit | venera-next | 未通过 | explore[12].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| Rawkuma | rawkuma | 1.1.3 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.3 | yelongyue197-svg/venera-sources | venera-next | 未通过 | search.load；explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ☄️ 最次元 | source_07_49effa | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 绅士会所 | source_16_d622ad | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 中国人能飞 | source_19_50ee2a | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 咚漫 | source_36_d33fb7 | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 极速漫画 | source_39_7cc572 | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 漫畫狗 | source_45_d76464 | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫画皮 | source_48_074d4f | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 漫蛙🌐🔞 | source_56_3ebb0b | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 龙王传说网 | source_65_8717b6 | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 腾讯动漫 | tencentcomics | 1.0.0 | xiaoxingmian/venera-configs | venera-next | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| 图库漫画 | tuku_cc | 1.0.2 | Junkrat9527/venera-sources | venera-next | 通过（其他能力受限） | explore[0].load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| V2PH | v2ph | 1.2.0 | meaninglesslyy/venera-config | venera-next | 未通过 | search.load；categoryComics.load；comic.loadInfo | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| vomic | vomic | 1.2.1 | LX7kM9/venera-configs | venera-next | 未通过 | comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| WEBTOON | webtoon | 1.0.0 | cattoldme/venera-configs | venera-next | 未通过 | thumbnail.download | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| WeebCentral | weebcentral | 1.0.0 | yelongyue197-svg/venera-sources | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；explore[2].load；categoryComics.load | 人机验证／反爬：先在 VeneraX 验证窗口处理，再同环境重试 |
| 野蛮漫画 | yemancomic | 1.3.8 | Junkrat9527/venera-sources | venera-next | 未通过 | search.load；explore[0].load；explore[1].load；categoryComics.load；categoryComics.ranking.load；comic.loadInfo；comic.loadEp | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |
| ◯ YYDS | yyds_04_86b037 | 0.2.0 | KadishJoey/venera-json | venera-next | 未通过 | search.load | 权限／访问拒绝：核对登录、会员权限和网络限制；不能断言密码错误 |

## 依据与边界

- VeneraX 固定源码：`lib/network/cloudflare.dart`；其验证窗口、Cookie 和请求头处理属于 Flutter 宿主，Node CLI 不具备相同的交互环境。
- [Cloudflare 官方识别方法](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/)：`cf-mitigated: challenge` 可确认挑战响应。
- [Cloudflare 官方通行说明](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/)：通行 Cookie 绑定访问者和设备，不能保证跨机器复用。
- [挑战限制](https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/)：不同 IP 发起挑战和完成验证可能导致循环。

浏览器诊断 Actions：https://github.com/laincat/vensrc/actions/runs/40277444450
