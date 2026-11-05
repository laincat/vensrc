# Venera 漫画源云端巡检报告

核验时间：2026-11-05T09:50:51.917586+08:00（香港时间）。
巡检工具：`Gandum2077/venera-patrol-cli` 1.0.0，提交 `dd6ded39844e56902d3880b1fc1c201a6d1d1fda`。
依赖锁 SHA-256：`7ea394a32e59776dfb39647d0434c106283ae3f275e7329b694f660b771974de`。
本次审阅清单：207 个构建；主索引 **23** 项，扩展索引 **45** 项。

官方版本基线覆盖 **33** 个 key。官方仓库原版仅在「同一 key 没有社区构建」时作为唯一可用版本参与订阅，其余只保留诊断证据；社区同 key 构建仍需版本严格高于官方基线。同版、低版或版本无法比较均排除。
绅士漫画只保留 `laincat/vensrc` 独立维护版；其他来源不再巡检或收录。账号改为本人完成滑块后导入浏览器 Cookie，并以会员页的真实登录标志验证；缺少会话不计登录通过，详见 WNACG_LOGIN.md。
版本基线依据官方索引提交 `a04e05591f7832f7166d6660546613c114d6738a`，原始索引 SHA-256：`04f85e10db259bffe4384adaad05f17e576546667df31152e65ae915d4ea33ab`。按三段数字比较版本；后续检测追加 key 并提高官方版本基线，不降低历史基线，清单见 ../data/official-exclusions.json。

固定漫画及章节、源码字节哈希和 CLI 提交均保留。主索引必须同次通过入口、详情、章节、图片下载与解码，且整次报告为 passed；扩展索引要求相同核心链路通过，其他能力可有失败或跳过。旧成功结果不代替新失败。

订阅快照滚动发布到 Releases，仅有主订阅和扩展订阅两个附件；中文报告与完整证据保存在仓库 reports/、data/。最终只保留最新一版；附件校验不完整时保留上一版。

GitHub 托管 runner 的网络与用户设备不同；未在用户设备验证导入或阅读。全部已审阅构建使用已核验的 VeneraX 原始 bootstrap，逐个以相同样本对照 Venera-Next。订阅仅按 VeneraX 本次结果选择；Next 成功不替代 X 失败。适配范围见 CLIENT_COMPATIBILITY.md，客户端对照复测见 CLIENT_RESULTS.md。

## 三个自用仓库

- `hea784/venera-configs`：已审阅构建 21 个，核心链路通过 10 个。
- `BB-CHICKEN/venera-jm`：已审阅构建 1 个，核心链路通过 1 个。
- `handahao666-boop/venera_comic_source`：已审阅构建 37 个，核心链路通过 23 个。

## 高于官方版本的社区替代源

以下每个构建都严格高于所列官方版本，并通过本次核心阅读门槛；同 key 源在客户端作为替代版本使用。

| 名称 | key | 社区版本 | 官方版本 | 订阅 |
| --- | --- | --- | --- | --- |
| 包子漫画 | baozi | 1.1.7 | 1.1.6 | 扩展索引 |
| CCC追漫台 | ccc | 1.0.2 | 1.0.1 | 扩展索引 |
| 禁漫天堂 | jm | 1.9.2 | 1.4.0 | 扩展索引 |
| 漫画人 | manhuaren | 1.0.1 | 1.0.0 | 主索引 |
| 漫蛙吧 | manwaba | 1.1.3 | 1.0.2 | 扩展索引 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.2.0 | 1.1.1 | 扩展索引 |
| 优酷漫画 (修复版) | ykmh | 1.0.7 | 1.0.0 | 扩展索引 |

## 未进入订阅的官方原版与低版本构建

官方仓库原版仅在「同一 key 没有社区构建」时作为补充参与订阅；已有社区构建时只保留诊断证据。社区同 key 构建仍须版本严格高于官方基线，核心通过也不能豁免版本门槛。

| 名称 | key | 选中构建版本 | 核心链路 | 排除原因 | 源备注 |
| --- | --- | --- | --- | --- | --- |
| 漫画柜 | ManHuaGui | 1.2.1 | 通过；仍排除 | 未高于官方版本基线 | 引用源：handahao666-boop/venera_comic_source |
| カドコミ | comic_walker | 1.0.1 | 未完整通过；排除 | 未高于官方版本基线 | 引用源：handahao666-boop/venera_comic_source |
| comick | comick | 1.2.0 | 通过；仍排除 | 未高于官方版本基线 | 引用源：handahao666-boop/venera_comic_source |
| GoDa漫画 | goda | 1.2.1 | 未完整通过；排除 | 未高于官方版本基线 | 引用源：handahao666-boop/venera_comic_source |
| MYCOMIC | mycomic | 1.1.0 | 通过；仍排除 | 未高于官方版本基线 | 引用源：handahao666-boop/venera_comic_source |
| 再漫画 | zaimanhua | 1.0.2 | 未完整通过；排除 | 未高于官方版本基线 | 引用源：handahao666-boop/venera_comic_source |

## 逐构建结果

| 源名称 | key | 仓库 | 版本 | 巡检环境 | 核心链路 | 整次状态 | 首个失败／跳过 | 收录处理 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 漫画160 | 160_53_6c28df | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| ◯ 177漫画 | 177_75_d9f4ef | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 18漫畫(国内可) | 18_11_31f9fe | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 18真人图集 | 18_12_5158bf | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| ◯ 18H | 18h_73_868382 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 崩坏3漫画 | 3_31_7d315c | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 733动漫 | 733_2 | zhimouzhou/venera-manga-sources | 0.1.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 8色摄影 | 8_23_b711ea | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 無限動漫 | 8comic | zakkida/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 92漫画 | 92_60_af6181 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | source.load：源加载或版本不兼容 | 按原有收录标准审核 |
| 古风漫画 | GfmhApp | handahao666-boop/venera_comic_source | 1.3.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 漫画柜 | ManHuaGui | handahao666-boop/venera_comic_source | 1.2.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 排除：未高于官方版本基线 |
| 新漫画-A | a_43_e3f585 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| 一本漫画-A | a_49_189b7b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| A漫🔞 | a_54_aaf8eb | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 爱漫岛 | aiman | Junkrat9527/venera-sources | 2.3.6 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| A漫 | aman8 | Junkrat9527/venera-sources | 1.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| Asura Scans | asura_scans | Micqiyue/venera-sources | 1.3.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 百合会 | baihehui | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 巴卡漫画 | bakamh | Magentadots/venera-configs | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 包子漫画 | baozi | handahao666-boop/venera_comic_source | 1.1.7 | venerax | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 高于官方 1.1.6；按原收录标准审核 |
| 包子漫画（修订版） | baozi_fixed | JunQianNuo/venera-sources | 1.1.3 | venerax | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 包子漫画（重制版） | baozi_recode | Micqiyue/venera-sources | 1.1.7 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| BatCave.biz | batcavebiz | F22822/22822 | 1.0.5 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 嗶哩漫畫 | bilimanga | handahao666-boop/venera_comic_source | 1.1.7 | venerax | 未完整通过 | 失败 | image.download：反爬拦截 | 按原有收录标准审核 |
| 布卡漫画 | bukamh | Junkrat9527/venera-sources | 1.2.9 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| Buon Dua | buondua | meaninglesslyy/venera-config | 1.2.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 | 按原有收录标准审核 |
| CCC追漫台 | ccc | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 排除：未高于官方版本基线 |
| CCC追漫台 | ccc | zakkida/venera-sources | 1.0.2 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 高于官方 1.0.1；按原收录标准审核 |
| Cosplay啦 | ciyuandao | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 | 按原有收录标准审核 |
| カドコミ | comic_walker | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 排除：未高于官方版本基线 |
| comick | comick | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 | 排除：未高于官方版本基线 |
| 拷贝漫画(多账号) | copy_manga_multi_accounts | venera-app/venera-configs | 1.4.1 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| CosplayTele | cosplaytele | meaninglesslyy/venera-config | 1.7.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| CxC | cxc | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 通过 | 部分通过 | account.loginWithCookies.validate：未提供账号凭据 | 按原有收录标准审核 |
| 次元漫画 | cycomic | Junkrat9527/venera-sources | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 大魔兔 | damotu | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 | 按原有收录标准审核 |
| 顶漫画 | dingmanhua | Angus-fw/venera-configs | 1.0.5 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 | 按原有收录标准审核 |
| 动漫屋 | dm5 | handahao666-boop/venera_comic_source | 7.0.3 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 动漫啦 | dongman_la | handahao666-boop/venera_comic_source | 1.0.5 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 | 按原有收录标准审核 |
| 咚漫 | dongmanmanhua | handahao666-boop/venera_comic_source | 1.0.6 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 堆堆漫画 | duiduiman | cheyou001/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| 读漫屋 | dumanwu1 | zhimouzhou/venera-manga-sources | 0.4.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| ehentai | ehentai | venera-app/venera-configs | 1.2.0 | venerax | 通过 | 失败 | explore[2].loadNext：返回结构或样本不满足契约 | 官方原版补充（无社区构建）；按原收录标准审核 |
| Everia图集 | everia_14_efa23b | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 810114 漫画源 | ex_810114_xyz | xuzhen2905-pixel/venera-source | 1.0.0 | venerax | 未完整通过 | 失败 | explore[0].load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| ExHentai (fangliding 镜像) | ex_fangliding | zakkida/venera-sources | 1.2.0 | venerax | 未完整通过 | 失败 | search.loadNext：反爬拦截 | 按原有收录标准审核 |
| 飞翔漫画 | ffppt | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| FoamGirl | foamgirl | meaninglesslyy/venera-config | 1.2.1 | venerax | 未完整通过 | 失败 | explore[1].load：反爬拦截 | 按原有收录标准审核 |
| 4KHD | fourkhd | meaninglesslyy/venera-config | 2.0.7 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 4KHD Cosplay | fourkhd_cosplay | 6678670jsy/venera-sources | 2.0.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| G站漫画 | g_67_c20b96 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| GMANHUA | gmanhua_59_ee9658 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| GoDa漫画 | goda | handahao666-boop/venera_comic_source | 1.2.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 排除：未高于官方版本基线 |
| 瓜子漫画 | guazi_manhua_v2 | ChenTeea/veneresource | 1.0.1 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 国漫吧 | guoman8 | token1008/venera-cn-64bit | 1.0.2 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| Hachiraw | hachiraw | YUIRIKIiii/venera-sources | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 花火漫画 | hanabimanga | xiaoxingmian/venera-configs | 1.0.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 按原有收录标准审核 |
| 好看漫画 | haokan_txt | Junkrat9527/venera-sources | 1.0.4 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 嗨皮漫画 | happy | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| H-Comic | hcomic | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 部分通过 | comic.link.linkToId：缺少样本输入 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 绅士会所 | hentaiclub | meaninglesslyy/venera-config | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 嬉皮漫畫 | hipmh | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 未完整通过 | 失败 | image.download：请求超时 | 按原有收录标准审核 |
| hitomi.la | hitomi | venera-app/venera-configs | 1.1.2 | venerax | 未完整通过 | 失败 | categoryComics.load：网络错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 包子漫画（私人） | hj_baozi | Taototo/venera-comic-sources | 1.1.7 | venerax | 未完整通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 热辣漫画 | hot_manga | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 花咔漫画 | huakacomic | xiaoxingmian/venera-configs | 1.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 爱看漫 | ikmmh | venera-app/venera-configs | 1.0.6 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 爱看漫 | ikmmh_v2 | handahao666-boop/venera_comic_source | 3.0.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 爱飒漫画 | isamanhua | YHQY-Dev/venera-sources | 1.0.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| jcomic.net | jcomic | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadEp：返回结构或样本不满足契约 | 官方原版补充（无社区构建）；按原收录标准审核 |
| JJCOS | jjcos | meaninglesslyy/venera-config | 1.3.0 | venerax | 通过 | 部分通过 | search.onTagSuggestionSelected：缺少样本输入 | 按原有收录标准审核 |
| 禁漫天堂 | jm | BB-CHICKEN/venera-jm | 1.9.2 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 高于官方 1.4.0；按原收录标准审核 |
| 禁漫天堂X | jmx | Junkrat9527/venera-sources | 2.1.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 按原有收录标准审核 |
| 看漫画 | kanman | Junkrat9527/venera-sources | 2.2.7 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| Kavita | kavita | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| Kiutaku | kiutaku | meaninglesslyy/venera-config | 1.1.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 | 按原有收录标准审核 |
| Komga | komga | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| Komiic漫画 | komiic_69_259947 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| Komiic 多账号 | komiic_multi | snowf14k3/venera-komiic-multi | 1.6.2 | venerax | 未完整通过 | 失败 | explore[0].load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 快看漫画 | kuaikan | cattoldme/venera-configs | 1.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 来漫画（分流） | laimanhua_split | handahao666-boop/venera_comic_source | 1.2.1 | venerax | 通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| Lanraragi | lanraragi | venera-app/venera-configs | 1.2.0 | venerax | 通过 | 失败 | search.load：HTTP 错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 特漫网站 | legacy_17te | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 | 按原有收录标准审核 |
| 27漫画 | legacy_2mzx | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 58漫画网 | legacy_58puxin | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 85漫画网 | legacy_85iu | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| 90漫画 | legacy_90mh | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 按原有收录标准审核 |
| 1359漫画网 | legacy_bdido | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 按原有收录标准审核 |
| 百年漫画 | legacy_bnmanhua | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 蒂亚漫画 | legacy_diya1 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 | 按原有收录标准审核 |
| 好漫6 | legacy_haoman6 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 | 按原有收录标准审核 |
| 冰氪漫画 | legacy_icekr | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 爱米推漫画 | legacy_imitui | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 漫画羊 | legacy_manhuayang | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 漫漫看漫画网 | legacy_manmankan | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 漫漫睇 | legacy_manmantai | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 漫画芯 | legacy_mhxin | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 | 按原有收录标准审核 |
| 奇妙漫画 | legacy_qimiaomh | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 | 按原有收录标准审核 |
| 奇热漫画 | legacy_qiremanhua | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 258漫画网 | legacy_shut123 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 搜动漫 | legacy_soudongman | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 13漫画网 | legacy_w13k | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 武侠漫画 | legacy_wuxiamh | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 360漫画 | legacy_xd5s | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 土豆漫画网 | legacy_xm124 | wuliaoe/venera-extra-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 六漫画 | liumanhua | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | explore[1].load：需要登录 | 按原有收录标准审核 |
| 栗子漫画 | lizimh | Walter498/Walter | 2.33.27 | venerax | 未完整通过 | 失败 | search.load：DNS 错误 | 按原有收录标准审核 |
| 漫画台-M | m_50_2be8b8 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 | 按原有收录标准审核 |
| 知音漫客-M | m_51_4e1530 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 看漫画-M | m_52_1d77ca | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 神漫画-M | m_63_d6913d | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：TLS 错误 | 按原有收录标准审核 |
| 漫本 | manben | Junkrat9527/venera-sources | 1.1.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| Manga18FX | manga18fx | meaninglesslyy/venera-config | 1.0.2 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 51漫画 | manga51 | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| MangaDex | manga_dex | venera-app/venera-configs | 1.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 官方原版补充（无社区构建）；按原收录标准审核 |
| MANGA Plus | manga_plus | WEP-56/EZvenera-config | 1.0.2 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| Mangabz | mangabz | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| MangaForFree | mangaforfree | meaninglesslyy/venera-config | 0.7.4 | venerax | 未完整通过 | 失败 | search.load：阶段超时 | 按原有收录标准审核 |
| MangaPill | mangapill | zakkida/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| MangaRead | mangaread_66_d1113a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 178漫画网 | manhua178 | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 | 按原有收录标准审核 |
| 漫画吧网 | manhuaba | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 漫画皮 | manhuapi | Junkrat9527/venera-sources | 1.4.2 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 漫画人 | manhuaren | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 通过 |  | 高于官方 1.0.0；按原收录标准审核 |
| 香蕉漫画 | manhuauo_banana_v2 | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 漫漫漫画 | manman | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：HTTP 错误 | 按原有收录标准审核 |
| 漫舍 | manshe | Micqiyue/venera-sources | 1.0.8 | venerax | 通过 | 失败 | comic.link.linkToId：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 漫蛙 | manwa | YHQY-Dev/venera-sources | 1.1.6 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 漫蛙吧 | manwaba | handahao666-boop/venera_comic_source | 1.1.3 | venerax | 通过 | 失败 | categoryComics.load：HTTP 错误 | 高于官方 1.0.2；按原收录标准审核 |
| 漫蛙吧（图片修复版） | manwaba_imagefix | YongkeDet/venera-configs | 1.0.7 | venerax | 通过 | 失败 | categoryComics.load：HTTP 错误 | 按原有收录标准审核 |
| 漫网 | manwang | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 漫画manga | mh03 | Magentadots/venera-configs | 1.0.1 | venerax | 通过 | 失败 | explore[0].load：需要登录 | 按原有收录标准审核 |
| 漫画1234 | mh1234 | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 漫画1234（新版网站） | mh1234_fixed | JunQianNuo/venera-sources | 1.2.2 | venerax | 通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 18漫画 | mh18 | venera-app/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 4399漫画网 | mh4399 | handahao666-boop/venera_comic_source | 1.0.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 漫画看 | mhkan | Junkrat9527/venera-sources | 1.1.7 | venerax | 未完整通过 | 失败 | categoryComics.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 喵趣漫画 | miaoqu | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| MissKon图集 | misskon_13_4b2d17 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：返回结构或样本不满足契约 | 按原有收录标准审核 |
| Mitaku | mitaku | meaninglesslyy/venera-config | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 漫客栈 | mkzhan | Junkrat9527/venera-sources | 1.1.4 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| MOJOIN | mojoin_v2 | handahao666-boop/venera_comic_source | 1.0.7 | venerax | 通过 | 部分通过 | comic.onImageLoad.onLoadFailed：本次成功路径未触发 | 按原有收录标准审核 |
| momon:GA | momon_ga | ChopDream/venera-source-hub | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 漫小肆 | mxs | venera-app/venera-configs | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 | 官方原版补充（无社区构建）；按原收录标准审核 |
| MYCOMIC | mycomic | handahao666-boop/venera_comic_source | 1.1.0 | venerax | 通过 | 失败 | categoryComics.ranking.load：返回结构或样本不满足契约 | 排除：未高于官方版本基线 |
| naver | naver_28_e2315f | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 | 按原有收录标准审核 |
| nhentai | nhentai | venera-app/venera-configs | 1.1.0 | venerax | 通过 | 部分通过 | account.loginWithWebview.checkStatus：需要交互 | 官方原版补充（无社区构建）；按原收录标准审核 |
| 鳥鳥韓漫nnhanman5 | nnhanman5_10_f0cebd | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 鸟鸟韩漫 | nnhm | Junkrat9527/venera-sources | 1.3.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| NoyACG | noyacg | zetriumyx/noyacg-source-venera | 1.4.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| NoyManga | noymanga | handahao666-boop/venera_comic_source | 1.1.5 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 极速漫画 | one_kkk | Junkrat9527/venera-sources | 2.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| Ososedki | ososedki | meaninglesslyy/venera-config | 1.1.1 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| Picacg | picacg | venera-app/venera-configs | 1.0.6 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 官方原版补充（无社区构建）；按原收录标准审核 |
| Pixiv | pixiv | Junkrat9527/venera-sources | 1.9.0 | venerax | 未完整通过 | 失败 | search.loadNext：需要登录 | 按原有收录标准审核 |
| 大人漫画（私人） | private_drmh3 | Taototo/venera-comic-sources | 1.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 魅影画廊（私人） | private_myhl | Taototo/venera-comic-sources | 1.0.1 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 奇漫屋 | qimanwu | token1008/venera-cn-64bit | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 按原有收录标准审核 |
| Rawkuma | rawkuma | handahao666-boop/venera_comic_source | 1.1.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 热门漫画 | remenmanhua | YHQY-Dev/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 如漫画 | rumanhua_fixed_v15 | handahao666-boop/venera_comic_source | 1.2.8 | venerax | 通过 | 部分通过 | comic.unpackJS：缺少样本输入 | 按原有收录标准审核 |
| 311漫画 | s311_com | Junkrat9527/venera-sources | 1.2.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| SF漫画 | sfacg_manhua | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 神奇漫画 | shenqimanhua | coldnighten/venera-configs | 1.1.1 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 少年ジャンプ＋ | shonen_jump_plus | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 失败 | search.load：反爬拦截 | 高于官方 1.1.1；按原收录标准审核 |
| 思思漫画 | sisimanhua | YHQY-Dev/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | image.download：HTTP 错误 | 按原有收录标准审核 |
| 漫画家📱⛅ | source_01_656cfe | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 污漫天堂🔞 | source_03_c97d34 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| ◯ 拷贝漫画 | source_05_1be182 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| ☄️ 最次元 | source_07_49effa | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 魅影画廊 | source_17_b7ddde | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 中国人能飞 | source_19_50ee2a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 鸟鸟韩漫·直连 | source_21_a16969 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 武芊漫画·直连 | source_22_2764a4 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 漫画联合国 | source_32_e5ebaf | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 特漫网 | source_34_0dc3b2 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| 动漫戏说 | source_38_17bca1 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：网络错误 | 按原有收录标准审核 |
| 海猫吧 | source_43 | zhimouzhou/venera-manga-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 按原有收录标准审核 |
| 看漫畫 | source_44_fed97a | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：请求超时 | 按原有收录标准审核 |
| 漫畫狗 | source_45_d76464 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 漫画园漫画 | source_54 | zhimouzhou/venera-manga-sources | 0.1.0 | venerax | 未完整通过 | 失败 | search.load：源配置错误 | 按原有收录标准审核 |
| 聚合漫画屋 | source_55_082633 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 仙漫网 | source_58_9bd332 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 龙王传说网 | source_65_8717b6 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| サンデーうぇぶり | sunday_webry | handahao666-boop/venera_comic_source | 1.0.0 | venerax | 通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| 腾讯动漫 | tencentcomics | xiaoxingmian/venera-configs | 1.0.0 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| 图库漫画 | tuku_cc | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 通过 | 失败 | explore[0].load：需要登录 | 按原有收录标准审核 |
| V2PH | v2ph | meaninglesslyy/venera-config | 1.2.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| vomic | vomic | LX7kM9/venera-configs | 1.2.1 | venerax | 未完整通过 | 失败 | comic.loadEp：需要登录 | 按原有收录标准审核 |
| ◯ 包子漫画web | web_70_6c33fc | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| WEBTOON | webtoon | cattoldme/venera-configs | 1.0.0 | venerax | 未完整通过 | 失败 | comic.loadInfo：HTTP 错误 | 按原有收录标准审核 |
| webtoon移动版 | webtoon_71_d28205 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：HTTP 错误 | 按原有收录标准审核 |
| Webtoon_us | webtoon_us_68_3131e7 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| LINE WEBTOON | webtoons_zh_hant | Junkrat9527/venera-sources | 1.0.1 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| WeebCentral | weebcentral | yelongyue197-svg/venera-sources | 1.0.0 | venerax | 未完整通过 | 失败 | search.load：反爬拦截 | 按原有收录标准审核 |
| W漫画 | wmanhua | handahao666-boop/venera_comic_source | 1.0.1 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 紳士漫畫 | wnacg | laincat/vensrc | 1.4.1 | venerax | 未完整通过 | 失败 | init：源配置错误 | 高于官方 1.0.6；按原收录标准审核 |
| Xiutaku | xiutaku | meaninglesslyy/venera-config | 1.1.0 | venerax | 通过 | 失败 | comic.idMatch：返回结构或样本不满足契约 | 按原有收录标准审核 |
| X漫画 | xmanhua | Junkrat9527/venera-sources | 1.8.1 | venerax | 通过 | 通过 |  | 按原有收录标准审核 |
| yande.re | yandere | Junkrat9527/venera-sources | 4.9.3 | venerax | 未完整通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |
| 野蛮漫画 | yemancomic | hea784/venera-configs | 0.1.2 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 优酷漫画 (修复版) | ykmh | handahao666-boop/venera_comic_source | 1.0.7 | venerax | 通过 | 失败 | comic.onClickTag：源配置错误 | 高于官方 1.0.0；按原收录标准审核 |
| ◯ YYDS | yyds_04_86b037 | KadishJoey/venera-json | 0.2.0 | venerax | 未完整通过 | 失败 | search.load：需要登录 | 按原有收录标准审核 |
| 再漫画 | zaimanhua | handahao666-boop/venera_comic_source | 1.0.2 | venerax | 未完整通过 | 失败 | comic.loadInfo：源配置错误 | 排除：未高于官方版本基线 |
| zero搬运网 | zerobyw33 | handahao666-boop/venera_comic_source | 1.2.0 | venerax | 通过 | 部分通过 | account.login：未提供账号凭据 | 按原有收录标准审核 |
| 知音漫客 | zymk | token1008/venera-cn-64bit | 1.0.0 | venerax | 通过 | 失败 | search.load：返回结构或样本不满足契约 | 按原有收录标准审核 |

## 主索引

古风漫画、A漫、布卡漫画、CosplayTele、动漫屋、咚漫、4KHD、瓜子漫画、好看漫画、花咔漫画、快看漫画、51漫画、Mangabz、漫画人、漫客栈、鸟鸟韩漫、极速漫画、大人漫画（私人）、311漫画、神奇漫画、腾讯动漫、LINE WEBTOON、X漫画

## 扩展索引

Asura Scans、百合会、包子漫画、包子漫画（修订版）、Buon Dua、CCC追漫台、Cosplay啦、拷贝漫画(多账号)、CxC、大魔兔、顶漫画、动漫啦、ehentai、4KHD Cosplay、Hachiraw、花火漫画、H-Comic、热辣漫画、爱飒漫画、JJCOS、禁漫天堂、禁漫天堂X、看漫画、Kiutaku、来漫画（分流）、Lanraragi、Manga18FX、178漫画网、漫舍、漫蛙吧、漫蛙吧（图片修复版）、漫画manga、漫画1234（新版网站）、MOJOIN、漫小肆、nhentai、魅影画廊（私人）、如漫画、少年ジャンプ＋、サンデーうぇぶり、图库漫画、Xiutaku、优酷漫画 (修复版)、zero搬运网、知音漫客
