# 上游变更与待审阅候选

检查时间：2026-11-05T01:40:59.766734+00:00（UTC）。
检查 70 个已登记仓库；发现 478 个未审阅源码构建。

新代码只下载计算哈希及读取声明字段，不通过 list、init 或巡检执行。维护者在 GitHub 审阅固定提交的 JS 后，把候选加入 monitor/catalog.json；后续 Actions 才会执行巡检并按主／扩展标准自动收录。

候选排除官方原版、转引，以及未严格高于官方版本的社区同 key 源；版本更高也必须审阅、巡检后才可收录。

## 源码变动

| 名称 | key | 版本 | 仓库 | 最低应用版本 | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| 爱看漫 | ikmmh | 2.1.2 | Junkrat9527/venera-sources | 1.0.0 | fdab1f9f87c055e33fdf069a744ef1ed60c1f421c4c85806b5e69412be9a6ee3 |
| vomic | vomic | 1.2.0 | 137syh/venera-syh | 1.5.0 | 525cf99fc99d62991069c3c01ecaff16b4044804ec451743ec7188af3f853846 |
| 漫蛙吧 | manwaba | 1.0.3 | zakkida/venera-sources | 1.4.0 | 6d85a9a18d2f44fb8b71ef598e6a74fb9de4b0ddd0260b3a6cb57fc05753f481 |
| 腾讯动漫 | ac_qq | 1.0.1 | Angus-fw/venera-configs | 1.0.0 | c36110d27ea41a64fdd9f1180bc3cf4b0936b0cdffa0fb30a14c5c8c64612236 |
| 漫蛙漫画 | mwuu | 1.2.0 | Angus-fw/venera-configs | 1.0.0 | 1cd62034164549749d971b15a7ac1e085c6d9b9bd721029038660d1635f1d49b |
| 快看漫画 | kuaikan | 1.0.3 | Angus-fw/venera-configs | 1.0.0 | a2a515bde9bb5c7b7c1b22417559e7d4db03e872523cef4053b9808c11cf93de |
| 腾讯动漫 | tencent_comics | 1.1.3 | Junkrat9527/venera-sources | 1.6.0 | e696aaf1b4fb36d0bc29591fc407854c89e43ff4280211233192eb66b45963ed |
| NoyManga | noymanga | 1.1.3 | hgnbh/sw | 1.6.0 | feffe371db3a294e17202041e2da0b0b021f1a0f810c3eaf55e79ab847cf0fde |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.2 | cattoldme/venera-configs | 1.2.1 | a3f346b5569d945c4953ef32dd017735ddf81ecc0b0e5929cb79de69ea59e848 |
| 咚漫漫画 | dongman | 1.0.0 | cattoldme/venera-configs | 1.6.0 | db829f439e27dc33c3ae3303646fa780efe7d2c37ee9c777df1f041d7631485d |
| 包子漫画 | baozi | 1.1.7 | ChopDream/venera-source-hub | 1.0.0 | 81214391b7fb95d8e632381d92f284e26939c4b465abed5a0cb324606564e1be |
| 禁漫天堂 | jm | 1.4.2 | ChopDream/venera-source-hub | 1.5.0 | 1b195b4ecd0bcbed61546d11761f6d0c8b027588564da7d28368f2f4645d5b16 |
| nhentai | nhentai | 1.1.2 | ChopDream/venera-source-hub | 1.0.0 | 9379d8441f42d06a7835cee6b21519ea8a951eb01c476402d00dce721ffeaec6 |
| MYCOMIC | mycomic | 1.1.2 | ChopDream/venera-source-hub | 1.4.6 | f35e2e7cb531f7591e81a5edf41ab6303880686f0009c7477f77154e9511f07f |
| Komiic | Komiic | 1.1.1 | coldnighten/venera-configs | 1.0.0 | 09745417a434adb03de541685c53a39340ec842b70ef193542b0273139f3a5ec |
| ehentai | ehentai | 1.2.0 | coldnighten/venera-configs | 1.5.3 | 5e84f24b495acc4564660ef4d99fe260626205ac71ad2aa14e9c18aa6c1c011e |
| 漫蛙吧 | manwaba | 1.1.0 | coldnighten/venera-configs | 1.4.0 | 1f86b7eac78866624f514a6c919a9780ce89b7ad1e8676863546c08a2f111ae5 |
| Lanraragi | lanraragi | 1.2.0 | coldnighten/venera-configs | 1.4.0 | 323a61b9905979c5e0ebd50fe7e119cb3bc67a62aa7d7bbdc57b70dc4c5ef9a1 |
| カドコミ | comic_walker | 1.1.0 | coldnighten/venera-configs | 1.6.0 | 926ea5a941994d321df046149a91220244ba710e3dde52356939d7af1d19d67a |
| 肉漫屋 | roum27 | 1.1.0 | coldnighten/venera-configs | 1.6.0 | 3745f74ccfa8b3b00b5199f2f3946f954bc94e02b9d0e80438e087053215b7e4 |
| W漫画 | wmanhua | 1.0.3 | coldnighten/venera-configs | 1.6.0 | e7dda68f4770edfad5e0bf4842c7e7ed2b0542112e72627bf67ee08716850446 |
| 漫画屋 | mhua5 | 1.1.0 | coldnighten/venera-configs | 1.6.0 | ca3190f8c8195047def754315cbc8c4ff8ec5a5a0f5ba31b1a62a96ac19ae378 |
| MYCOMIC | mycomic | 1.2.0 | coldnighten/venera-configs | 1.4.6 | 930d26974a5cfe42108b8634157c6a6425edaf3bbe20c73aca73469030db7abe |
| 乐成漫画 | lcmhx | 1.0.1 | coldnighten/venera-configs | 1.6.0 | 095a6b7f72176785c3460d536977a713722ae3dbf3eddbda7e0067e6f3bdcfd7 |
| 包子漫画 | baozi | 1.1.7 | fuluoydebende/venera-configs-fixed | 1.0.0 | dc8902797555ded67e74ea1ce7516b3f9824bfe56c5b6ae0fb6fb5e01a15d217 |
| Picacg | picacg | 1.0.7 | fuluoydebende/venera-configs-fixed | 1.0.0 | 878fb51af54a06f361ba31053852e80146c75065615bc3098202d83dc1585c77 |
| nhentai | nhentai | 1.1.1 | fuluoydebende/venera-configs-fixed | 1.0.0 | 921fe64a5b188abb56fecc56d3b1cb53ec9450ed67b68e554d4a3da63d597d99 |
| comick | comick | 1.2.1 | fuluoydebende/venera-configs-fixed | 1.4.0 | 698032e28a7498e6d2a33ef3dd99324d2dd4220e93363ab9ecb62b42ca70ab64 |
| 优酷漫画 | ykmh | 1.0.1 | fuluoydebende/venera-configs-fixed | 1.4.0 | 7510025f800dba6d44d424af2ab1b43f214d01e753ab9afbf92f11b405fe2ae3 |
| GoDa漫画 | goda | 1.2.2 | fuluoydebende/venera-configs-fixed | 1.4.0 | bf6e42a568824d063b32172dd733babb4643dab917097d21156f571aa4f4111f |
| Pixiv | pixiv_token | 0.3.35 | gallhall/venerav-configs | 2.0.0 | 81b538dcdbbdf438d0b06e0855d3cf9fcf792ff7447873e52e7073f7d8f7dcb8 |
| Hanime1.me | hanime1 | 2.4.0 | gallhall/venerav-configs | 2.0.0 | 75628a9e8392a0630b713cf443cccfd1c16347ff303420ec7f32702f5e8beafb |
| Hanime1 H漫画 | hanime1_comics | 1.2.1 | gallhall/venerav-configs | 1.0.0 | 729836e4e65b01161f5ba1f9998fdc1630d08dd6407e480f063d578cfa7ea7c7 |
| 包子漫画 | baozi | 1.1.8 | handahao666-boop/venera_comic_source | 1.0.0 | db40b64506f7002420eb5d6e23b3f7829a0fe3c6c36afff77991ec1097d78f25 |
| 拷贝漫画 | copy_manga | 1.6.6 | ZhiLin-Sam/venera-sources | 1.6.0 | 06ea2676323e40e980cb8f8fba2b53a70733e7cade267e0261763c55e6b30155 |
| 瓜子漫画 | guazimanhua | 1.0.4 | ZhiLin-Sam/venera-sources | 1.0.0 | b93ad63c5e0ac1a41c77ab95e7561f20718ad46228fb9b6b8fbb8196c3f56dc6 |
| Komiic | Komiic | 1.0.8 | ZhiLin-Sam/venera-sources | 1.0.0 | ad74a243c07ebc549254e75162fceb81097e6755054e1902ca81e0327370bd68 |
| 腾讯动漫（正版） | qq_comic_official_v1 | 1.0.3 | ZhiLin-Sam/venera-sources | 1.0.0 | fd53172968ebc576a69d8bda73b8e576589a28b469e84a46890692b93e1256b6 |
| W漫画 | wmanhua | 1.0.3 | handahao666-boop/venera_comic_source | 1.4.0 | 113b94d281f16f53877f75c18df909c2e0b3e3233746cb99ac7b3976e6cc0398 |
| LINE WEBTOON | webtoons_zh_hant | 1.0.0 | ZhiLin-Sam/venera-sources | 1.6.0 | d4bc4b0641af7533e2a7ca1bd358c099ce2844a57721f256b9e8c42a3664bfb6 |
| 栗子漫画 | lizimh | 1.2.4 | handahao666-boop/venera_comic_source | 1.2.2 | 51450326c6bff18d8fde7744aff9d822e2341908c4863fd7c48af28ce42f9ac7 |
| 动漫屋 | dm5 | 0.2.0 | zhimouzhou/venera-manga-sources | 1.6.0 | 0adf399b0eab25937f07a9b6b23c044b7ebee8b75f1d30dcd55a1a8a4a5a400a |
| Mangabz | mangabz | 0.2.0 | zhimouzhou/venera-manga-sources | 1.6.0 | ac1d497bfe0ba800b84ae3f5f5d4d0bf07dccd1174e8e24198cf5eadf00623b1 |
| 极速漫画 | one_kkk | 0.2.0 | zhimouzhou/venera-manga-sources | 1.6.0 | f71e0d2db4c2771915fd3916eefe1d73440f9cc2611829e300e9b920ff9bb569 |
| 禁漫天堂 | jm | 1.4.1 | hea784/venera-configs | 1.5.0 | 490504eb906339d352c86dc8afdd40a772ac775bcdddb4a2de2eb683db23a08f |
| AO3 同人图文 | ao3 | 1.0.1 | hgnbh/sw | 1.4.0 | fe73cde6653ee4ac991ea871a94ba5ecba381adb5db46b37996f34bf6e9bd125 |
| 嗶哩漫畫 | bilimanga | 1.1.3 | hgnbh/sw | 1.6.0 | 555e08f8d7dd2f0e8f95541dd644d0ccaf6e09309c41a979de00349ff8738c1a |
| カドコミ | comic_walker | 1.0.2 | hgnbh/sw | 1.6.0 | 7d965185909caf11829df04a20e74b6c57dee372a71a9a5528da3b165f48fa52 |
| 动漫屋 | dm5 | 7.0.2 | hgnbh/sw | 1.6.0 | 25f69ded59266a0ed04d69dfee08f147d5a45bd537e8f474142810dfa996af7e |
| 动漫啦 | dongman_la | 1.0.2 | hgnbh/sw | 1.4.0 | ae7055749e31d9718abdfb14787c753210395597ca3a54f0c3903f14cb2302bf |
| 飞翔漫画 | ffppt | 1.0.1 | n3114576614-cell/N_venera_source | 1.0.0 | b86d41220d3fcfafd0799ac569332adfc0978c5ac0509a08cf077b6f51853d3e |
| HentaiFox 系列 | hentaifox | 1.0.0 | hgnbh/sw | 1.4.0 | 1521fc63cea10c184d9e9bbf395500698ad5232259b6f991e594a631b9c1c694 |
| LOFTER 同人图文 | lofter | 1.0.1 | hgnbh/sw | 1.4.0 | e9e50018c6574d58d71f969ad429e9ba7f0924e08737f2fd88f6f101171c8db6 |
| 漫小肆 | mxs | 1.0.1 | hgnbh/sw | 1.5.0 | f7445609e82ce00ca5c40f0895a36857d47da646d44dd4e6e8c6d587a0da410e |
| Pixiv 同人图 | pixiv | 1.0.1 | hgnbh/sw | 1.4.0 | eb85deae9758c8d27e26c6b126a7383d046356e996f5f35170711eacd89aa8e4 |
| 如漫画 | rumanhua_fixed_v15 | 1.2.7 | hgnbh/sw | 1.0.0 | 8c0eaf511dc14b14abc85c8e565c900bbe3ed8296a8df5c61fc40022c6d65a3c |
| 优酷漫画 (修复版) | ykmh | 1.0.6 | yelongyue197-svg/venera-sources | 1.4.0 | f0b1979721bf81094772b4575c2cb1a6ebc774a58d4b3f3fa301a36b5a7d641f |
| 漫客栈 | mkzhan | 1.0.1 | YHQY-Dev/venera-sources | 1.0.0 | 4b8e222d01cd8860a57da0a1e08a894b1f2f1ebb362864ba1db50eb94baae87f |
| 布卡漫画 | bukamh | 1.0.0 | YHQY-Dev/venera-sources | 1.4.0 | 32402780e73a061ea0c60431fd8ca3ad0b9a24ea61c1d7d81891d7133fdb0b78 |
| 看漫画 | kanman | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 42ff5a70afda843fa9cc2cd12d8223dc6da3594b811fa7c4a0459794887c907f |
| 次元漫画 | cycomic | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 942f29bd9a6834d7a7d9f7a5a115b3ff1164f0990828f4eb9c2358ed354303d7 |
| 包子 · 个人测试源 | personal_baozi | 0.1.0-alpha.2 | hp5588/venera-sources | 1.18.1 | 2cc176d875df5403d0b36837ec92cba318525cd0160a8d0a7bdf9f24c99cf348 |
| 拷贝 · 个人测试源 | personal_copy | 0.1.0-alpha.2 | hp5588/venera-sources | 1.18.1 | 970460752771581cf49bf1252ec63191ebd3e01a6f16ef9505d27500cbcf3ae5 |
| 漫蛙 · 个人测试源 | personal_manwame_normal | 0.1.0-alpha.2 | hp5588/venera-sources | 1.18.1 | 8739d264f70a3ed7d150745da31f46fd16c2ee70603dbd016703105396236f5b |
| 51漫画 | manga51 | 1.1.0 | meaninglesslyy/venera-config | 1.6.0 | 5a505f80319071bddf6f0de2b1bc2f32d9153bcb7c5d11679e7c1fe88ab3221e |
| 嗶哩漫畫 | bilimanga | 1.2.0 | meaninglesslyy/venera-config | 1.6.0 | e21b7984e309e0a1b730d737da914834ce15908b59c45c0d4d2be2627cecbbe2 |
| 如漫画 | rumanhua | 1.0.0 | meaninglesslyy/venera-config | 1.6.0 | 017847c6901f8e491c28e6cb7b3da2a3475e6512b88374ecd41b7922dcca38a7 |
| zero搬运网 | zerobyw33 | 1.2.0 | meaninglesslyy/venera-config | 1.6.0 | 17b9a4ae12100e367b54c116d5ee9810a9520eacbf7ab46cf930fe6485dd2fe7 |
| Komiic | Komiic | 1.8.3 | Junkrat9527/venera-sources | 1.0.0 | d957a4de13948a967368975b43e947a3dc56cb094f02e4fa9b62f8339a5e678a |
| 百合会 | baihehui | 1.0.2 | LX7kM9/venera-configs | 1.4.0 | 356372e99f8b6836151cca6ddbd5bc46a8085cdc7ec06a91ea2442289e401758 |
| 香蕉漫画 | banana | 1.0.4 | LX7kM9/venera-configs | 1.0.0 | 8ed30b390d9c74c696d045f6067336a0a46e607764a4c7d76357c46585595515 |
| 包子漫画 | baozi | 1.2.1 | Junkrat9527/venera-sources | 1.0.0 | 0fe528ef087e092a2d57ec32f2d9414642987e07ceaced9973c6ecf8acb1cb40 |
| 包子漫画 | baozi | 1.1.7 | zhimouzhou/venera-manga-sources | 1.0.0 | ed698fbc58b216b0a22bc178947f56f637400629cd4a852bcda70b68b34349f3 |
| 哔哩漫画 | bilimanga | 1.6.2 | Junkrat9527/venera-sources | 1.6.0 | 0480d3d33192a99f19c458dc3248996988a73a4493b829a8ea0c15f3083e0a63 |
| CCC追漫台 | ccc | 1.0.9 | Junkrat9527/venera-sources | 1.6.0 | 062c6d3948d728e97d529330b0db07b102b259302571a0aeb2ec0e213b38b5b5 |
| カドコミ | comic_walker | 1.3.2 | Junkrat9527/venera-sources | 1.6.0 | 266cab4c1172866c25fb5b61f57f56502817b2c7dc14a707d67e5e8b1f3fdf0a |
| comick | comick | 1.3.0 | LX7kM9/venera-configs | 1.4.0 | 510fbc210f12ab0260d26b4b708c8d23582e11c68fad4d5f7a0aac820bc7d236 |
| 拷贝漫画 | copy_manga | 2.3.1 | LX7kM9/venera-configs | 1.6.0 | ea1f834157acd3787eade0a4c436f172b46e983f576e46142aa650574f373ca5 |
| 咚漫 | dongman | 1.0.8 | LX7kM9/venera-configs | 1.6.0 | a4e34d9681a48022640c072842dc37ccb4099fd1f9c04d8ab51cc38ebfa57669 |
| 动漫啦 | dongman_la | 1.0.1 | n3114576614-cell/N_venera_source | 1.0.0 | f3599e84cdebd39aa3cf752e0b97b015ea673917314572cf52e567d81a12daba |
| 动漫啦 | dongman_la | 1.0.3 | Junkrat9527/venera-sources | 1.0.0 | 3da97ede8f94cce6127313d582a8dda391d7b74d04bbb125e95c246010ee5ac5 |
| 动漫啦 | dongmanla | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 15a8e8970bd8142accb161272c6491082b193d8ceaad393025877effe63cf009 |
| ehentai | ehentai | 1.2.1 | VComic-org/venera-comic-source | 1.5.3 | 1aa135bfdba24d66eaea1cbd6c66eb4d6b7a97d62ffc8ef8361f2ce5eff6038b |
| 飞翔漫画 | ffppt | 1.0.2 | Junkrat9527/venera-sources | 1.0.0 | 9073ad30b4cbfd080f35154607610450db6a76fc56f1c4f1fb263c5502488318 |
| 古风漫画 | gfmh | 1.3.1 | LX7kM9/venera-configs | 1.6.0 | 2b372bbc3dba44150a359b7475080d6ab6b70ec4f26bf143c1597c60e8619e0d |
| GoDa漫画 | goda | 1.2.4 | LX7kM9/venera-configs | 1.4.0 | d560801cd543d9cec07d1098b46f9992276cde9e904c5a8ff431a678a2f3415e |
| 瓜子漫画 | guazimanhua | 1.0.4 | Junkrat9527/venera-sources | 1.0.0 | 3b47fd313cc99c887b6d2fca7d320b6df72f72e52c0b322fe74ff1f683c3c489 |
| 嬉皮漫畫 | hipmh | 1.0.6 | LX7kM9/venera-configs | 1.6.0 | 95a132f5468187e35cd9224cd0ae923ec544187a14a60d8bac376308218f2f1a |
| 爱看漫 | ikmmh | 3.0.1 | Junkrat9527/venera-sources | 1.0.0 | 78cc44bb2c9a69225a3446698005d3d33080dedb67ff9d9e7cc43052e14190f8 |
| 禁漫天堂 | jm | 1.4.3 | VComic-org/venera-comic-source | 1.5.0 | eb059a5ae6ad528bbcbfcfb2296a4b3945405bb5cab1faab326f1b374450d0b7 |
| 来漫画（分流） | laimanhua_split | 1.2.2 | Junkrat9527/venera-sources | 1.0.0 | ed9c0d8a088d31aa8b45d311a7280c35d4b971c728c74b9fe3eead94e08cbb9b |
| Lanraragi | lanraragi | 1.2.3 | LX7kM9/venera-configs | 1.4.0 | 55bc1f431f9e26af5a20a38cc26fc233595df10a00916ca519afc042f33ef8ad |
| 51漫画 | manga51 | 1.3.0 | Junkrat9527/venera-sources | 1.6.0 | edaebdf2b61473888cce47c9d2cf58cb0cfc49c6d2d2ae88bbba2314c851a82c |
| MangaDex | manga_dex | 1.9.4 | Junkrat9527/venera-sources | 1.4.0 | c1fda4f7542327ea9c35a485250b7f97ba51c65b831407a4f1474ee51728ae97 |
| Mangabz | mangabz | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 45ea62f02ef64fa0ad1f176fe125572b78d326060d06bf2964c7f8bc5dd63192 |
| 漫画柜 | manhuagui | 1.2.2 | YHQY-Dev/venera-sources | 1.4.0 | b7f7995704b42b31010edf007c6a069bef77d3a96d03b5dca2d3456c6e2b29a4 |
| 漫画人 | manhuaren | 2.0.0 | Junkrat9527/venera-sources | 1.6.0 | 5adc51fbd180f7f4b987d9f36c1f06951d3507a61def96385af2b72eb078508d |
| 漫蛙吧 | manwaba | 1.0.3 | zhimouzhou/venera-manga-sources | 1.4.0 | 2727adee5abf680436db5a962b460bd416bfdb3042c3e5b0256a595efe22323c |
| 漫网 | manwang | 1.3.4 | LX7kM9/venera-configs | 1.4.0 | f4864ddfe001645b8b3e05285cc037ed844ddaa95802ff3a8863b177d40f5fb9 |
| 漫画1234 | mh1234 | 1.4.3 | LX7kM9/venera-configs | 1.4.0 | a1d71934255b57ea7f7895a9bdedbfedceeda4fcdaec9aa765cd974792c985d5 |
| 漫画1234 | mh1234 | 1.0.1 | Junkrat9527/venera-sources | 1.4.0 | 6f410a9984f172b202bad08f4d12aed7629cde43fc02280edd3f4f443558aecc |
| 4399漫画网 | mh4399 | 1.0.5 | LX7kM9/venera-configs | 1.6.0 | 4e25bc428ac5284288bc680eadcb810216b00c2e0df6840550eb198bc04647de |
| MOJOIN | mojoin | 1.0.8 | LX7kM9/venera-configs | 1.0.0 | eac0c6d5ff2f5f5658170e0f0288ea87294a90b698803f802e0dc9ac03ad98ac |
| MYCOMIC | mycomic | 1.1.1 | LX7kM9/venera-configs | 1.4.6 | 0d1ee97148833716ff4b667872e28d14c751a17720c6518edcff1fd91c116448 |
| nhentai | nhentai | 1.1.1 | VComic-org/venera-comic-source | 1.0.0 | 9c637790f59d072003adbdee32b1336082d58e50e6cfa4f5cd5becde18996129 |
| 腾讯动漫（正版） | qq_comic_official | 2.0.0 | LX7kM9/venera-configs | 1.6.0 | 98ce234683ae1141b9f3104e549da0c45391cad41dde0da10fddf4fe404f17fa |
| Rawkuma | rawkuma | 1.1.3 | LX7kM9/venera-configs | 1.0.0 | f15ad92098c3d54c60436f33c3098febbae84bb1cef8a9eae855f5f990fd0f26 |
| 如漫画 | rumanhua | 2.4.1 | Junkrat9527/venera-sources | 1.0.0 | 93e982bd657cea4deedc0f9e785ea1321dff6e46eedb1cb9eb53200961e6f724 |
| SF漫画 | sfacg_manhua | 1.0.2 | LX7kM9/venera-configs | 1.6.0 | 5d9d9c36ea32e270f1aeaea09b69476d3c1cf78f9597d4e67889c660bf2fffa1 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.3.1 | Junkrat9527/venera-sources | 1.2.1 | d7cc9e684b14239e3c921d8ce19da7db9343ccf7692093a7d048f21822130f6b |
| 图库漫画 | tuku_cc | 1.0.2 | LX7kM9/venera-configs | 1.4.0 | 59c79f140dd68c1e848473a17a5916ff52ef009e539cf8a1de94a1b29d4a1b26 |
| W漫画 | wmanhua | 1.0.2 | Junkrat9527/venera-sources | 1.4.0 | 6e60a7ec42164ec8b4bc3e8dad7fa4500fd43c6a1b65b20f021758f54cc476b5 |
| 野蛮漫画 | yemancomic | 1.3.8 | LX7kM9/venera-configs | 1.6.0 | 42b53d66e34198ec4d1cacb31808e9386ac0392e305016d87c98a703f608c25e |
| 优酷漫画 | ykmh | 1.1.0 | Junkrat9527/venera-sources | 1.4.0 | effa08b818616a670bfe5ff5e1abc42e5da925fe767dec86c84d9ea51016e861 |
| 优酷漫画 | ykmh | 1.0.1 | zhimouzhou/venera-manga-sources | 1.4.0 | d0eb522a8fe55d322cca2c27c1a8f7e27dd0bf5b24fe80eab9032dead0f8bde6 |
| 再漫画 | zaimanhua | 1.2.6 | LX7kM9/venera-configs | 1.0.0 | ecef4acbb4548e999cda545931cd71f5951a5b9231a10e8f23d04156064279de |
| 再漫画 | zaimanhua | 1.0.3 | zhimouzhou/venera-manga-sources | 1.0.0 | 2d9e8d071b2cd1cd5b6c5cd5d06716c2f0aa941ebe9da8c9d96c27c1c2a17273 |
| zero搬运网 | zerobyw | 1.2.0 | Junkrat9527/venera-sources | 1.0.0 | 348f7334f1ff01af56b1414ac22bd9a5f34203dd22fd103b64976690abcc057a |
| 包子漫画 | source_02_e3ec7f | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 67f2790696e4269db2248dd60b1bb720a68d2790d208ac453e0e3776c3bd249c |
| 再漫画 | source_06_b7b48e | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 2c2f0a2f012cf7e711f5ef67d42ff7072e144e42af9a267ad993b457c15cfd59 |
| 野蛮漫画 | source_08_fa018e | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 98a15cee618b6b10c40784b70ca8d7af12124d0fc044b75230a4da8d045c5478 |
| 顶漫画 | source_09_fe41f7 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | b75c1ac138cd76b1ff09244404b0ccac858ac84d660138443722d2a7e71f7ed4 |
| Buondua图集 | buondua_15_095853 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | cc42e0fe3ce32a6eb4bced85e7d73682e56ac8d616958dbd211d68b79ead152b |
| 绅士会所 | source_16_d622ad | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 398e1fc8e4707b4eb1b0eeae8ae29f6b5c542c0484bc798ef927959d0ebc51ce |
| 4KHD 美图 | 4khd_24_21d7d1 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 726e2c1fb88f09e6d30f81cef6bb91e060124eaeb18f273e7aa6e27b4241f8a2 |
| CosplayTele | cosplaytele_25_190983 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | c1b9db6ef30749caf774d577e5c2a7ac1c66feb0f52226f2a6d47d144098a48d |
| 腾讯漫画 | source_26_c5541c | 0.2.0 | KadishJoey/venera-json | 1.0.0 | b83b8ba7fea60cea3b38fd8aab61c2841f3ae6fb031453288fd2fd9c9ae4152f |
| SF漫画 | sf_27_eb0a9b | 0.2.0 | KadishJoey/venera-json | 1.0.0 | ef411add79295e8eadfd2829f59168ceb9c51a9b242c8e2e7d5947405b343190 |
| x漫画-M | x_m_29_6ee1ce | 0.2.0 | KadishJoey/venera-json | 1.0.0 | f24c3be55faf795abfae33ad9908dfc5dface64078e376e60b531762f1a6085b |
| x漫画 | x_30_465fc5 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | d4423cf57ccc22cee5c3f3f26a6143e6d34407f533da6e5f940ff1922794ce33 |
| 漫畫櫃 | source_33_05aedf | 0.2.0 | KadishJoey/venera-json | 1.0.0 | fe8ba5a2c6aa5856cbd8c0d925cb72c5bce11ef4bb2acc72860337949349b689 |
| 漫画人 | source_35_667a4f | 0.2.0 | KadishJoey/venera-json | 1.0.0 | bf7ceb95c7581e9d2be88cbccec1f52642310178493a3bd2e04e4dbd2f5f5302 |
| 咚漫 | source_36_d33fb7 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 12015b6a608982e0cac02fcd3b7f883745843fc892eb9c00fbd726e9bb1c6149 |
| 漫漫漫画-M | m_37_824ad0 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 957f3f47c90a4e11e88ef02a27bcc3b8638f4fff5f32d578653a7832aaf46920 |
| 极速漫画 | source_39_7cc572 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 1a6eca09cbb922586a5029cad9606a9caf0a9f2a0a35b66c7c3dedf74c661046 |
| 动漫啦 | source_40_5846eb | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 9b389a91ba553446d40bb819620495218afe8f7556f21f690e87f87146f634d8 |
| 动漫屋 | source_41_b0c446 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 60b0dcc6dc6d17246dc396c093d8bb8c1af84d41dc90b3b8f2cc917f3a75fa44 |
| 漫漫漫画 | source_42_481e60 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 53a600b55b9f11a58fd66fe68ccf3f55eef97b909f8f35e7da4cfc8449753aab |
| 漫本 | source_46_ac3286 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 014da8ab9aba586dc33116469b8a869b6c827756185c92f6012a4411c8e2ac1e |
| 咚漫-M | m_47_c0f177 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 17b3b3ebe9bcedca86b554ab62881f2c5396c78209b94e4c59fe507061083dd1 |
| 漫画皮 | source_48_074d4f | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 25131c16e19fd2649ba44730cd61b40c11cb30bd34d22d3d7d26da3cfdaa8b2e |
| 漫蛙🌐🔞 | source_56_3ebb0b | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 1bf40998a6ec55a8b4845bc4b2d57908939f4aea5ad4a7fa0135c6fc9836e7d6 |
| 包子漫画cw | cw_57_cc4798 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 6fad2dc6dbc90ebfbc9993b2ca1be598852d3aef8f3d41097e7613c91d453719 |
| 拷贝漫画 | source_61_acb91b | 0.2.0 | KadishJoey/venera-json | 1.0.0 | ac108c730710ebc57cac9484a39acf6ee1ffd998b7f824601ffbd1d5ad6b8da6 |
| 漫客栈-A | a_62_528fe9 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | c49cd93c6fb31c9973b28e5a310e76cb20016b02041cdc51fe2e01e9bb647448 |
| 無限動漫 | source_64_2e309a | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 8f662b1b1efb6181e3289c5982a9e928bb4b3c70e70db967eb46a0b7961f8664 |
| Mangabz | mangabz_72_18ed08 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | 510e1cca571f7f48fdf5341fa85bc628965ae6bb9b5e42debb58ae754d3fd90c |
| 漫画柜 | source_74_9820b5 | 0.2.0 | KadishJoey/venera-json | 1.0.0 | cf2bb25be39f6e66c762a325595cf845f6fd5ab0d297c79bcee24f743e971f5c |
| 嬉皮漫画 | hipmh | 1.0.1 | AXmishell/venera-configs | 1.0.0 | 57f23ebd47143defe73117ed24b986bb99ad1904938ec42725c15440b139a0cd |
| 如漫画 | rumanhua | 1.0.3 | caitlin-cheng-ccc/venera-configs | 1.4.0 | 78f7fba17c15bbbf10bb52b4f46d5df2222e3cfef18abfee19c750dad8348800 |
| CCC追漫台 | ccc | 1.0.9 | lldaydayhappy/venera-sources | 1.6.0 | 68821e76778fc7d66451c66f1ca938b004dae72a07c9aba2a4dcd5c2b83c2fa8 |
| comick | comick | 1.3.0 | lldaydayhappy/venera-sources | 1.4.0 | 8e0edfbe706646ee756c35801a6f39aa26368262dd92f8b5b698538fdd906266 |
| ehentai | ehentai | 1.2.4 | lldaydayhappy/venera-sources | 1.5.3 | 1e19caed88cd1c09c3d9baaad22c3928b46dd1efde40b0a521248a81f98e01eb |
| GoDa漫画 | goda | 1.2.4 | lldaydayhappy/venera-sources | 1.4.0 | 25ed744668e4c503383d69345ffe02212123b0829e02758f9d41e22b258c54ad |
| hitomi.la | hitomi | 2.0.0 | lldaydayhappy/venera-sources | 1.4.6 | 1e4fe1b71f1aacfbe6d400a857dac9067a5d8fc952e1b537ba613b470fefaa02 |
| Komiic | Komiic | 1.8.3 | lldaydayhappy/venera-sources | 1.0.0 | c3c7b496f1a2aadb46ea5533f260bb59b3066e0781037c774b747c8ad60659d6 |
| Lanraragi | lanraragi | 1.2.3 | lldaydayhappy/venera-sources | 1.4.0 | a0af5f4cfbcb3bf4a2e8f0f3f562c4ab388b92fafc61d27705b8ee6bf8dc44ac |
| MangaDex | manga_dex | 1.9.4 | lldaydayhappy/venera-sources | 1.4.0 | bbe7c01bd52b93d8d06d5ae200ed0922e62b73fc1f9f23806e12ac9e0d346a92 |
| MYCOMIC | mycomic | 1.1.1 | lldaydayhappy/venera-sources | 1.4.6 | 87f5eee07a9f3b0f557e7068c2974569ed282ccd177898fb5022e098b2b0bf08 |
| nhentai | nhentai | 2.0.0 | lldaydayhappy/venera-sources | 1.0.0 | 6b820fcfd9e630f5570db8f73cb12df7d31f90839b65f7a651dbb78c20942f47 |
| カドコミ | comic_walker | 1.3.2 | lldaydayhappy/venera-sources | 1.6.0 | e8472140e23eedf0c7982720f51db5856d3435f96aecba1e71dcf7f059a1d690 |
| 优酷漫画 | ykmh | 1.1.0 | lldaydayhappy/venera-sources | 1.4.0 | 0ed9c70e032c196278b6cea85b5a84fdfcadbcaa6fa73045e7b67cc887db43b4 |
| 再漫画 | zaimanhua | 1.2.6 | lldaydayhappy/venera-sources | 1.0.0 | 6c56e987c5b07eb6aed724026b17163607ad03440ac5973f051db0238dfcc967 |
| 包子漫画 | baozi | 1.2.1 | lldaydayhappy/venera-sources | 1.0.0 | fd34a872c0b0f3a43d0d8af09037933953e1782febe0b09cca005fb98e627ebf |
| 少年ジャンプ＋ | shonen_jump_plus | 1.3.1 | lldaydayhappy/venera-sources | 1.2.1 | 42659ead9e657a2a7fce6512d2d15ce5f287568935bcd781d206a87124e38541 |
| 拷贝漫画 | copy_manga | 2.3.1 | lldaydayhappy/venera-sources | 1.6.0 | 9f248fb4b64da891b5e7ca79b5bb534cc2f95963997b908ae0689c2cf50a53c8 |
| 漫画1234 | mh1234 | 1.4.3 | lldaydayhappy/venera-sources | 1.4.0 | a3d42dc2ddd3cdbafbc6b4515426b6e9102e4dc7222433b91aa5335bd2d7874f |
| 漫画人 | manhuaren | 2.0.0 | lldaydayhappy/venera-sources | 1.6.0 | cd6b7666ce1f410e87700bc6f5fe9b7c926b8133b8e5ba492aa12e321ed87c80 |
| 漫画柜 | ManHuaGui | 1.2.3 | lldaydayhappy/venera-sources | 1.4.0 | bed4e1425b3582701aa22a39e31496098e5ed8885226991192718291360095ae |
| 漫蛙吧 | manwaba | 1.1.3 | lldaydayhappy/venera-sources | 1.6.0 | b4ac8ca05644f74e4c09a693a09ea001fb094e1a9091b79f76c1bcb5faf22058 |
| 爱看漫 | ikmmh | 3.0.1 | lldaydayhappy/venera-sources | 1.0.0 | 05a9cab20abab530f10520c8b63049e106e54fd4d8ba180793929976d3751bc3 |
| 禁漫天堂 | jm | 1.4.3 | lldaydayhappy/venera-sources | 1.5.0 | 3c56d13955c083fa454f96a0dd5b532994289313ae8a76bedc35cc6b058d0c92 |
| 瓜子漫画 | guazimanhua | 1.0.4 | LX7kM9/venera-configs | 1.0.0 | 07aaf9e53940358eab902e47f7971980b699a09aa4104176fa9bb9d1b656f6ed |
| 动漫啦 | dongman_la | 1.0.6 | LX7kM9/venera-configs | 1.0.0 | 56989eb9acd1cf21a44cde3ddb1726a69dbafaa115b25e1a2a63736f0ebc8d44 |
| 如漫画 | rumanhua | 2.4.2 | LX7kM9/venera-configs | 1.0.0 | 9d9ada706f965a6da4c36588d50827a8ef37d3c47c989f993e991e08994787d7 |
| 飞翔漫画 | ffppt | 1.0.6 | LX7kM9/venera-configs | 1.0.0 | 4eeee3685842c843c12c909ec75680ed6a332120a0f86c27c8bb48b43b68bb96 |
| 来漫画（分流） | laimanhua_split | 1.2.2 | LX7kM9/venera-configs | 1.0.0 | 9874de436f3ee50db72543c53ad47a5375401791daf89f1f6542d485b6ae6c03 |
| W漫画 | wmanhua | 1.0.4 | LX7kM9/venera-configs | 1.4.0 | 9855fb12c571198fae84c9a6b365680b596459654f2cdc8faacee847c8bf255e |
| 爱看漫 | ikmmh | 3.0.1 | LX7kM9/venera-configs | 1.0.0 | e78216115cc4e14484b3cbe299585a99f832944a8e277bd11b365ccae9396c98 |
| 哔哩漫画 | bilimanga | 1.6.3 | LX7kM9/venera-configs | 1.6.0 | 97fd92499c11c4ee0baed1874598862d021051c22abe08674e9152b8458eb2fe |
| 51漫画 | manga51 | 1.3.0 | LX7kM9/venera-configs | 1.6.0 | c02ee18f652724a534d19e5d7206dcf855d43f1768356820caaa6974666a7b10 |
| NoyManga | noymanga | 1.1.6 | LX7kM9/venera-configs | 1.6.0 | 2917b22ca6b78778d7c5761d27b001324475f54ba3548abfc4c8b00c32321381 |
| 优酷漫画 | ykmh | 1.2.0 | LX7kM9/venera-configs | 1.4.0 | fbd0c34abd226cc98980aa3bfb633012f42f8fb90bade985312bb1889358c725 |
| 动漫屋 | dm5 | 2.0.5 | LX7kM9/venera-configs | 1.6.0 | f1082766eade7d5acea8156b19430499fc1f8004408b9dfd4964dcad03f7fcbd |
| Mangabz | mangabz | 1.0.3 | LX7kM9/venera-configs | 1.6.0 | 06aeb01ff5b8ef3be44e36da8f3c4242d80bcdb13581d730191069a735fefc59 |
| MangaDex | manga_dex | 1.9.9 | LX7kM9/venera-configs | 1.4.0 | 3062fc802122a9f346caffce964e6e60eeb0f2a40ba3cae36c53ea805d757fb8 |
| 311漫画 | s311_com | 1.2.0 | LX7kM9/venera-configs | 1.2.2 | 7de2d08ef245b7cb756b5f6500b1c6f1f84733f4211c09f525666e8de4321746 |
| 好看漫画 | haokan_txt | 1.0.4 | LX7kM9/venera-configs | 1.2.2 | 04bfdfb5fd06f5e29c340253cc5c78e5c5f1a47d65766d920b841ea41e5cb53d |
| vomic | vomic | 1.2.2 | LX7kM9/venera-configs | 1.5.0 | 3f76b21647489337c897bb473dedf910ad8ab486ef6b4400071e9585b120e5fb |
| 思思漫画 | sisimanhua | 2.7.0 | LX7kM9/venera-configs | 1.0.0 | 189b8656d816de05b70f07b71da6a593dec6280e054405aeacbfa5c001a6c065 |
| CxC | cxc | 1.0.4 | LX7kM9/venera-configs | 1.6.3 | ea881a3a29c020802f63e20451bd74599b245e063b64decd752f2596caa7bde2 |
| サンデーうぇぶり | sunday_webry | 1.0.1 | LX7kM9/venera-configs | 1.0.0 | b7b5303abd2e69ff690b0f546d3f3a498b46702b81b545f2076a79014730c800 |
| 栗子漫画 | lizimh | 1.2.4 | LX7kM9/venera-configs | 1.2.2 | 2691099d04bf8c4677b32f0c253cfcdfdaddd0afb8e8d435722c7a1290e2f3b4 |
| 90漫画 | mh90 | 0.3.9 | LX7kM9/venera-configs | 1.6.0 | 0a3a000f7bedeee8055017ed4d1170326626582fe7dc544d8872725f7ce89fd1 |
| 大魔兔 | damotu | 0.7.1 | LX7kM9/venera-configs | 1.6.0 | d2a221a509f36fdad9b2a1a0e4109b6deb8055259e9519bc48864cadce6295cc |
| 爱飒漫画 | isamanhua | 1.1.4 | LX7kM9/venera-configs | 1.0.0 | 3205e39afeac75b1a083dbbe0ca122bdb4798985dc1f0b7b0cb91f7c18b9d374 |
| 包子漫画 | baozi | 1.2.3 | LX7kM9/venera-configs | 1.0.0 | 844ee8e10c6a473431c94aba330aa9af4b9804c886b2e0360e9d9b31a715a704 |
| 漫画人 | manhuaren | 2.0.1 | LX7kM9/venera-configs | 1.6.0 | a13a85540e57ee3ae4a8ccdcf0f4c83fd8d396dd678afa04ba5dc0260533e70e |
| CCC追漫台 | ccc | 1.0.9 | LX7kM9/venera-configs | 1.6.0 | 42a220ca017e01b5cd45d53ec9f70e3a20b8453f0c68870f42de7762a4ffe95b |
| 漫画柜 | ManHuaGui | 1.2.3 | LX7kM9/venera-configs | 1.4.0 | e285c5dd21c66dc3fdb3ee20e51b0d9fdee611350565ae40b96a9bc7e3b67934 |
| Cosplay联盟 | pandadiu | 1.2.3 | LX7kM9/venera-configs | 1.0.0 | 629fcf83532f1e816ae1dd8dbde51ee77e70f46a2b1351e8c6ca855019f8c183 |
| 漫画狗 | dogemanga | 1.0.6 | LX7kM9/venera-configs | 1.6.0 | f823b84756dc7048dda5c280fce381fcd4f2ae408f76fe5d983582652b39c557 |
| Project Gutenberg | project_gutenberg | 5.0.0 | LX7kM9/venera-configs | 1.6.3 | 0b6e3d9c10acd166be0e59a649be68fc7f05855998f21e1b7a7d83ad2507dca4 |
| Mengteen | mengteen | 1.0.0 | LX7kM9/venera-configs | 1.6.0 | 1e870bada169704a9d6c548dd8e1b5ed71e5205d747fcdd7d7c4f8e55bc5bd71 |
| 美图公社 | tooopen | 1.0.5 | LX7kM9/venera-configs | 1.0.0 | 6c3111a44ded31694b47e8d955110f4ad39bb5728aabf92a3531be1b0af583c8 |
| 无限动漫 | wuxian | 1.0.8 | LX7kM9/venera-configs | 1.6.0 | 192b561d47b1abf2c823f51459d64d649cdb2a086380e5f91eaa2b26426e3adc |
| zero搬运网 | zerobyw | 1.2.0 | LX7kM9/venera-configs | 1.0.0 | 4cc6a768c02333b851ba9427f2897a69af4ed6a8f17adb1de7baf20a66cffa81 |
| Komiic | Komiic | 1.8.3 | LX7kM9/venera-configs | 1.0.0 | cbb3ac23c4389fb73c341bd14d169c011a81913957fa284e321a86df513ebc8f |
| yande.re | yandere | 4.9.4 | LX7kM9/venera-configs | 1.6.0 | 089c33fde66e90452ee7c1a1662437098a7fc25d98f703bd75d5a4250325ef50 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.4.0 | LX7kM9/venera-configs | 1.6.0 | b7a3564421242b44a7004ece5bdc439624a97b840a31a55d581e1cf8cbdd1b74 |
| カドコミ | comic_walker | 1.3.2 | LX7kM9/venera-configs | 1.6.0 | 342c1d84bebeed6a118878e4ef71f82e21780c32b1ae80c15df48a306932a6ff |
| 百合会 | baihehui | 1.0.1 | Magentadots/venera-configs | 1.4.0 | a8ee1645dbe486e6bcda2309b729873ed2557675226b908604cf07b6dca229c9 |
| 包子漫画 | baozi | 1.2.0 | Magentadots/venera-configs | 1.0.0 | e548cdfaaa2810dbf6c2b007310b15186d6b2fca39927b30ff592fa2cce71cb5 |
| 拷贝漫画 | copy_manga | 1.6.1 | Magentadots/venera-configs | 1.6.0 | b352baa7ce4da19aca93b197f1cebcadf1a739723cce5f8bff1f74b94554ea60 |
| 拷贝漫画M | copy_manga_multi_accounts | 1.4.2 | Magentadots/venera-configs | 1.6.0 | d70f680003d13e1c53155804a7e4014334d52feef47345432829c7aef09e2077 |
| 动漫屋 | dm5 | 7.0.1 | Magentadots/venera-configs | 1.6.0 | 6cac096e047489fdd3d44929f203b860e2b9acb05b4665a0f3c242392703766b |
| ehentai | ehentai | 1.2.1 | Magentadots/venera-configs | 1.5.3 | 1f5e477c32060e2d52a0bd19348bfac53a7f6c8c1962ea086130fcb46f6bf623 |
| 嗨皮漫画 | happy | 1.0.1 | Magentadots/venera-configs | 1.6.0 | 106ac09e4c0582d3a32906976a325598671a41151b744c020f7d49641dce0ebd |
| H-Comic | hcomic | 1.0.1 | Magentadots/venera-configs | 1.6.0 | 208abe75c6c84f45539f90d3bacdd1e066c0f74207acc8a7067f19c67c5c3c31 |
| hitomi.la | hitomi | 1.1.3 | Magentadots/venera-configs | 1.4.6 | fc8463aed012b4ad2eef03f04768c67b8e037ac8047197be15097ba46c07280e |
| 热辣漫画 | hot_manga | 1.0.1 | Magentadots/venera-configs | 1.6.0 | 53c6c18fa86700615237916a7a24738111e31ce76e273bd3ce9a66d707ce6596 |
| 爱看漫 | ikmmh | 1.0.7 | Magentadots/venera-configs | 1.0.0 | 576ec4b1f0a34938d6eac7f026d098b1619237164cd7d7d1dd55b509103f15e7 |
| 禁漫天堂 | jm | 1.4.3 | Magentadots/venera-configs | 1.5.0 | 570b58fb26a794d284c31e054416a090413e59ed396555adc54b1b0f3ee7b376 |
| Kavita | kavita | 1.0.1 | Magentadots/venera-configs | 1.4.0 | 3c48f1f2db7c28ff8a1f837f9172903660b5b0c1f215f1ee0ebd806750ba77f7 |
| Komga | komga | 1.0.1 | Magentadots/venera-configs | 1.4.0 | 5b2307d8ec90f96e255ba34c14ad214e51706a3b46fa66faaee9735434da72e0 |
| Komiic | Komiic | 1.0.7 | Magentadots/venera-configs | 1.0.0 | 7c493973cab70ad0b14a491a2aab864056e553e33e52c31a381799fe11300e17 |
| Lanraragi | lanraragi | 1.2.1 | Magentadots/venera-configs | 1.4.0 | 1f73ebb4f6514ecaa3b5abdeec16975897774bd84ad36d28b3e0d043f7d3e7e6 |
| 漫画柜 | ManHuaGui | 1.2.2 | Magentadots/venera-configs | 1.4.0 | 2f72de4c3de11499f3349af0f746cd966d31a116f8d84e7a29779c0885e1a5fe |
| 香蕉漫画 | manhuauo_banana_v2 | 1.0.4 | Magentadots/venera-configs | 1.0.0 | 1c40729e769ccc048f342498dd0fe5c844432b63d50de4d0db3df076370a17d6 |
| 漫蛙吧 | manwaba | 1.1.4 | Magentadots/venera-configs | 1.6.0 | 2ccbfb1ef6f39bc0c7e99a823a2d1155716e7d674cd35bac231a56921e94a1d1 |
| 漫画1234 | mh1234 | 1.0.1 | Magentadots/venera-configs | 1.4.0 | f42f010f235cf552f2946f2300cdfc5851f7a71c155205a7e7f2e4ce32b25902 |
| 18漫画 | mh18 | 1.0.1 | Magentadots/venera-configs | 1.4.0 | 23dda487981425af402c3a536f920d9e6b70aedcd1f74cde6383338ce6ecfb53 |
| 漫小肆 | mxs | 1.0.1 | Magentadots/venera-configs | 1.5.0 | fdc2d8453aa2915fb027ff1cb38e3210f12d103196d87a28917026947d869ec8 |
| MYCOMIC | mycomic | 1.1.2 | Magentadots/venera-configs | 1.4.6 | 0ff55d097b96f5d567436826943319c8538b65d4b866de1b36cc69f90892e117 |
| nhentai | nhentai | 1.1.1 | Magentadots/venera-configs | 1.0.0 | e0c30482210941fb1783ff2caa95b72f206042c39cb582474afc872258c18c95 |
| Picacg | picacg | 1.0.7 | Magentadots/venera-configs | 1.0.0 | b34ec3ee1cfda521d1995466fb49d370e2e23af045227d24c8b9d27b5b1e8b9e |
| 如漫画 | rumanhua_fixed_v15 | 1.2.6 | n3114576614-cell/N_venera_source | 1.0.0 | bf5b4c9becfbee456bfc02c2cc0851aedb6bde63a568564954208e27d455eec7 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.2 | Magentadots/venera-configs | 1.2.1 | 2851cc1c51e7f0629cd5612f81ec5de6061bf6fccf4e5776435c6975ef387f1f |
| 优酷漫画 (修复版) | ykmh | 1.0.7 | Magentadots/venera-configs | 1.4.0 | 6c61be0f942afc5fa4798479f3d913b7b9bb47da8116e4cea53dfbfec2732e96 |
| 优酷漫画 (修复版) | ykmh | 1.0.7 | Magentadots/venera-configs | 1.4.0 | 08613616a806f0e58a10fe2f0d7b05ac6c9bd7947e6d72f57a6e07ed1b91a041 |
| 再漫画 | zaimanhua | 1.0.3 | Magentadots/venera-configs | 1.0.0 | fba4d1b36b85cb03e0517a0f84ca209f1fd04ff7646f859d33cc76411af7425c |
| 漫画源聚合与全量导入器 | sources_hub | 1.0.0 | Magentadots/venera-configs | 1.6.0 | 7b55eb6a9c010618b3265862d89359152d443de33b13fc2c994e04507fd7a850 |
| 拷贝漫画 | copy_manga | 1.4.4 | maplessovo/venera-configs | 1.6.0 | d6f574c13a37a262d90d964305bf4e86fe9f8454206c1bf0528a0ff868502a0e |
| 包子漫画 | baozi | 1.1.9 | maplessovo/venera-configs | 1.0.0 | 5b184613d62ca2d8406dd3f8a675cddf23c4e0b72a776dc49ee83fc754aadd6c |
| zero搬运网 | zerobyw33 | 1.0.3 | maplessovo/venera-configs | 1.6.0 | bf72c59f97acd82c6d7bf07a41ed6b6b538e2d4f65e44221db917588031fbded |
| 禁漫天堂 | jm | 1.4.1 | maplessovo/venera-configs | 1.5.0 | b11273a9bab54a07a2e2296fac839d25d27cdbd0d15c473c779ce8ef94916be8 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.2.0 | maplessovo/venera-configs | 1.2.1 | f8ae55635af3fb49cfa424053f948169c317a8b131df3eabbacb9edab69d284d |
| 优酷漫画 | ykmh | 1.0.1 | maplessovo/venera-configs | 1.4.0 | 4d561e93dfc9641b07d69af171afaff916f5381bfde9ce1b5fb5406cfedeb300 |
| 漫蛙吧 | manwaba | 1.0.6 | maplessovo/venera-configs | 1.4.0 | 5f0fc881d755d3f1dbef576fe1dd95cf536e211e61ab34e8cfe48303eba267b9 |
| カドコミ | comic_walker | 1.0.2 | maplessovo/venera-configs | 1.6.0 | c1ac850a7273bb8b2f9aebb995192f33eb85c9f043e36ab9821a5bdc01346e78 |
| 漫画1234 | mh1234 | 2.0.2 | maplessovo/venera-configs | 1.6.0 | 0b46486c286186793bae97a926ef3d0446d9e02d6b024f3151dd342346ff16fa |
| GoDa漫画 | goda | 1.2.2 | maplessovo/venera-configs | 1.4.0 | 31646bf9e47c9a218b1e038a509a16adc2fcbacfb2281720bf8b196a05c342db |
| 18漫画 | mh18 | 1.0.1 | maplessovo/venera-configs | 1.4.0 | aa01d8e4a7b85d2e1d3eb91195f5dc0b51e50e7ea656f695ab7c3594a4170d1a |
| MYCOMIC | mycomic | 1.1.1 | maplessovo/venera-configs | 1.4.6 | dd3bd7056c26cf800e3dfa8d1ec1a4913af63e9d9575c3b603d1b8f5d61a0120 |
| CosplayTele | cosplaytele | 1.0.4 | maplessovo/venera-configs | 1.4.6 | d6c091afe1b840a1d68bbd212f228a59c3a07653741fbce2893869505796909f |
| 百合会 | baihehui | 1.0.1 | maplessovo/venera-configs | 1.4.0 | 472d245198404100a8685fe15242ab8ad76ea6bd03bceafeeb7ff624b3c2ac6b |
| 鸟鸟韩漫 | nnhanman | 1.1.1 | meaninglesslyy/venera-config | 1.6.0 | 41b72c230bf6336f67cd99002beca4032be3023cb43ab982288cad29574554a1 |
| 香蕉漫画｜仅外部入口 | banana_external | 1.0.0 | Meloon-dr/venera-sources | 1.16.0 | 164c97511925503496ca1072f21b2d4cb7bd36cf5ad74dc8b52141010ef87529 |
| 包子漫画｜仅外部入口 | baozi_external | 1.0.0 | Meloon-dr/venera-sources | 1.16.0 | 27f1e31e78a06be99888aefe5c608e28ff45aa7478d7ae979df6878f8c716d82 |
| 动漫屋 | dm5_comics | 0.2.2 | Meloon-dr/venera-sources | 1.16.0 | f40677fdcd9f50868dec7604ce926f96054c4c8b5f521b2d6e6473a6b2a33660 |
| 次元狗｜仅外部入口 | acgndog_external | 1.0.0 | Meloon-dr/venera-sources | 1.16.0 | e772c17ef8c5146f26b41fcec432487e3de7041513df54c5367d168e21ff7a8b |
| 漫画迷｜仅外部入口 | manhuade_external | 1.0.0 | Meloon-dr/venera-sources | 1.16.0 | 57ed6aace262e17c7b4d55ef5b17ec2cd6f8c7486cc82f7cce3a5e5a9001ec4d |
| X漫画 | xmanhua_comics | 0.2.2 | Meloon-dr/venera-sources | 1.16.0 | f0c44336e60ff75bed25c5022401cabe7ca58e6546bc244bfed7ea88c28e4b02 |
| H次元｜仅外部入口 | hciyuan_external | 1.0.0 | Meloon-dr/venera-sources | 1.16.0 | 923da4c189970625cce174c7c16ef5732aaa3a57693bb92c500e9a77da38b6f4 |
| 污污漫画｜仅外部入口（18+） | comicbox_external | 1.0.0 | Meloon-dr/venera-sources | 1.16.0 | eddd1c834ec3a4baea59be68589657424eff61f45de8fc778cf2d399d0945ef8 |
| 漫画站 | manhuazhan | 1.0.0 | 940440952/comic-sources | 1.6.0 | 71cd5dca62d7d07b8741a730d7b7c8ac7525101c1a41b5edd59ed84fa5498650 |
| Fantia（个人订阅） | fantia_personal | 0.1.1 | MQ9Reaper/venera-personal-sources | 1.6.0 | 1f29d6abb87816caf5fad3a7c206e02aa9073a14dc2befa751b0d3de8ac7b167 |
| FANBOX（个人订阅） | fanbox_personal | 0.1.1 | MQ9Reaper/venera-personal-sources | 1.6.0 | 1556d3a02fbf77ded1c46d68044d16c2a0bbf7b0d893f76d990a189d29f57ffe |
| 嗶哩漫畫 | bilimanga | 1.1.0 | n3114576614-cell/N_venera_source | 1.6.0 | 0be6c0a5f3bcee229990c90e820f2ec410443d4e0d00dbf01a00155e1eb292f5 |
| 动漫屋 | dm5 | 7.0.0 | n3114576614-cell/N_venera_source | 1.6.0 | 23908d87f455e3d09025ea450a2bf82eafb5a0ae0b9c3eceddb03207abbc7241 |
| zero搬运网 | zerobyw33 | 1.1.0 | n3114576614-cell/N_venera_source | 1.6.0 | 534e23e43bb016cecb0988e11651da049f39e2a4d1ffa7cd4498c8695fde95ca |
| 包子漫画 | baozi | 1.1.8 | nightcat3254/venera-sources | 1.0.0 | 67950535d7d8b085a61ef1d5a605c6010cda66e22de35e31a5e01d13d18db7ca |
| 拷贝漫画 | copy_manga | 1.4.4 | nightcat3254/venera-sources | 1.6.0 | 962506c70015b4e82ca3edf4b9e6bb6d69f979c5da6f26d6f2592039ebc78921 |
| 禁漫天堂 | jm | 1.4.1 | nightcat3254/venera-sources | 1.5.0 | 1cba69d8671c1420d6c404463544cde742ccc2ad75772a22354d75be2ee5811f |
| MangaDex | manga_dex | 1.2.1 | nightcat3254/venera-sources | 1.6.0 | f9184fd626db3406b4614832e21c877194d76e0e035993f129c7fa8e192624f2 |
| 再漫画 | zaimanhua | 1.0.3 | nightcat3254/venera-sources | 1.0.0 | cf5b00660e9eede879563d17a0196a657078ff862da74bfb3b8c87c35dbd228d |
| 漫画柜 | ManHuaGui | 1.2.2 | nightcat3254/venera-sources | 1.4.0 | 725638d97abbabd8a0c5906a13ed473a19d7d0273f4493104896c336b6221b70 |
| 爱看漫 | ikmmh | 1.0.7 | nightcat3254/venera-sources | 1.0.0 | bccc5c4ab0915d09f71e214ec9362e4534aa5ac8ae5a3a677d15f940c4002e6b |
| 优酷漫画 | ykmh | 1.0.1 | nightcat3254/venera-sources | 1.4.0 | cf27c3a5fa154a3efee72f1f7508b17a36e186957f402d225042be9aa4482ad6 |
| GoDa漫画 | goda | 1.2.2 | nightcat3254/venera-sources | 1.4.0 | 0fcf105c1d360a97c0ff0221788761fa75c7c09a2c22d78e09f52ce330a44462 |
| 漫画人 | manhuaren | 1.0.1 | nightcat3254/venera-sources | 1.6.0 | 271bac42cecf82bb672ed5077f204775739b962dde3858f216f5b66f4c8e25ed |
| jcomic.net | jcomic | 1.0.1 | nightcat3254/venera-sources | 1.4.6 | bd644a10c65b11f959ace0ff4d306bfef05c91d3488758d04ac9dbb1a23d847d |
| CCC追漫台 | ccc | 1.0.2 | nightcat3254/venera-sources | 1.6.0 | 341c449b85fcd62ab1f4bdaf64d9b36e9da651ad0df89882a7a8590dc15dbfe7 |
| 热辣漫画 | hot_manga | 1.0.1 | nightcat3254/venera-sources | 1.6.0 | 59b5ae525fca08093a16f5f0496c5c681763ae6fc0e92dbb2bd9bbaf350083d9 |
| hitomi.la | hitomi | 1.1.3 | nightcat3254/venera-sources | 1.4.6 | b323cb07bae1c702a33aff4d2e9082161b5665b4112b39e0cbe312d5a9c369ef |
| 漫蛙漫画 | manwa_routes | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 8b7a65e5a520003d9ce6885848f882ab6b9f50a286bb50109835a5cb5303d5ba |
| 如漫画 | rumanhua_com | 2.1.2 | Ra1nbo-w/mhy-v | 1.16.0 | 3a383515749605a38609e8b5260e1f9aaf6aefd4f2dde22a38c07d9e606b93f2 |
| Komiic漫画 | komiic_cc | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 0d627b63113b1e0ca2c4180df732fd15f9b50f919919e8efaf7159ba99355514 |
| 漫画屋 | mhua5 | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 63b165b1065239b07d94c3a83750824fde8a53bc1c2afc9b0af5f0bfd0195b6c |
| 拷贝漫画 | copy_web_routes | 2.3.2 | Ra1nbo-w/mhy-v | 1.0.0 | 7a472063e163a7a33f888554c83e1043c3a400641ee9e43d04e6de64b4933b22 |
| 瓜子漫画 | guazimanhua | 1.0.1 | Ra1nbo-w/mhy-v | 1.16.0 | 4f94b6801f09db7534de9f98c650e686ff6ff7dfbf5658a81a1b6d38b2ff2d1b |
| MYCOMIC | mycomic | 2.3.3 | Ra1nbo-w/mhy-v | 1.16.0 | 763e7973a8ae82fe2af031bcf24b51796435dd840d45791b87ae2798e38ef826 |
| 包子漫画 | baozi | 2.3.3 | Ra1nbo-w/mhy-v | 1.18.0 | 445daa4d7caace438f7e1a1f9477b8e39fffb8f87b70c969a78aa63930410114 |
| 漫自由 | mheee_catalog | 2.3.4 | Ra1nbo-w/mhy-v | 1.0.0 | ff7d63b45ec92bfd7e78565bfa29becff2c94da2a040d6e18cab9ae235b62dc9 |
| 漫蛙漫画 | manwa_me | 1.0.2 | shixuit/venera-next-manwa-me-source | 1.4.6 | e6435ddc4ab45c3470150078a5240236bccb8f02d9647549d8f0a4cf36e666cb |
| 香香腐宅 | boylove | 1.0.0 | sy0sy0/V | 1.6.0 | 2c9ef1c1271c24c1fb0d0c355cff1824ac9a50fc3fa43a4e7998591798627624 |
| 一耽女孩 | yidan | 1.0.0 | sy0sy0/V | 1.6.0 | 6d2fac84aa85f39c9a05d9846745f9dde22074d98fa2121635720c72248f0d80 |
| 再漫画 | zaimanhua | 1.0.3 | Taototo/venera-comic-sources | 1.0.0 | 91ba937d50da1717136e9bf9e67111b58fb08e0e52222791e3bab49989ee0275 |
| 漫画人 | manhuaren | 1.0.1 | Taototo/venera-comic-sources | 1.6.0 | 2fbb6236652b0ea8776cd46d1b44e4ffc57d7812576550ddfe824ec8688ec42d |
| 禁漫天堂（18+） | jm | 1.4.1 | Taototo/venera-comic-sources | 1.5.0 | 4d0b8897c919c41ef2d44a55c9960ba931c46cc936fc808858e8dccf818cb39b |
| 魅影画廊 | private_myhl | 1.0.2 | Taototo/venera-comic-sources | 1.2.0 | 898fd65f78c53deaa6f7850b58ec499d76c4d55a7c9024208e35263c134b4eea |
| 大人漫画（18+） | private_drmh3 | 1.0.1 | Taototo/venera-comic-sources | 1.0.0 | 8f19da0af3a241cd5bad72970aeefdd792c2c846e6709c285c5044c178b0f9e0 |
| 成色漫画（18+） | private_csmanhua | 1.0.2 | Taototo/venera-comic-sources | 1.0.0 | 2fcb55afdb4ec089109efa40560cbeea1e97b213ad42487a491d0f676616c205 |
| 开心看漫画（18+） | private_kxmanhua | 1.0.4 | Taototo/venera-comic-sources | 1.0.0 | d25285c25f90f3fe4c482c41b4ae23790c11e3af7afc70a12d2a303aa00f2efa |
| 韩漫屋（18+） | private_hmanwu | 1.1.2 | Taototo/venera-comic-sources | 1.0.0 | 9d0be11ce76a7027a8a1e990b2159dc9d534acfb98778e05d447555ed9288d48 |
| SZZS / 4KHD | photo_deck_4khd | 0.1.7 | tide23333-max/venera-photo-sources | 1.17.0 | b08cf69155f15816b8264c49c27daf4a0a28bac485178e61d67eb92c89e3ce7c |
| GirlStop | photo_deck_girlstop | 0.1.4 | tide23333-max/venera-photo-sources | 1.17.0 | f8ebab172959a71ed447c310767c8623f1cc726a9ba0166881a4ef6f870064c5 |
| Geinou Nude | photo_deck_geinou_nude | 0.1.4 | tide23333-max/venera-photo-sources | 1.17.0 | 31a921d2b0f983b894cf0a85d6c657031ed0e876f1bf0d65cf97df811cf2da49 |
| DANRYOKU | photo_deck_danryoku | 0.1.6 | tide23333-max/venera-photo-sources | 1.17.0 | 8224c5f2de04a6381218dfb7a735456b3b453acecffe988c201509a8515a2578 |
| Everia Club | photo_deck_everia_club | 0.2.4 | tide23333-max/venera-photo-sources | 1.17.0 | 1cf4d225ad85622faac0ac3fe97707215d17383ab22b008ed60bbc17ff369de5 |
| V2PH | photo_deck_v2ph | 0.3.48 | tide23333-max/venera-photo-sources | 1.17.0 | 685ae6bde5a5d79d902badcf2e5db42e72adcd2222a56fb112765ab68179b607 |
| Aitoda · Nao Kanzaki | photo_deck_aitoda | 0.1.3 | tide23333-max/venera-photo-sources | 1.17.0 | 85a5bd2ff028d2cc769294123025c1d5d20fd90caa8ef35379788e39943242fe |
| GravureLab | photo_deck_gravurelab | 0.1.3 | tide23333-max/venera-photo-sources | 1.17.0 | 166cd147cbfc817cac6ce6e1f7783f1f8692d26c18580a8a0853b3ae3e4a7d52 |
| IDOL AREA | photo_deck_idol_area | 0.1.3 | tide23333-max/venera-photo-sources | 1.17.0 | 9b1f1b1e8f6e6798674efcfa3b1c79fd40280d1c2ea98b5083eefeb263e1bb6c |
| Gravia | photo_deck_gravia | 0.1.4 | tide23333-max/venera-photo-sources | 1.17.0 | 1bc00e2693e4231f603f46fd94a5dc13e099ec1cb6b4f646cb706014eaf925ad |
| 极速漫画 | jisu_1kkk | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 2a2874b992ab5d632c5e68bbac2b044f022ebe05649c7be5a8d5580af4bc7e79 |
| 看漫画 | kanman | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 34eec9fe833cc3184b0737a37b0fe3865c539d8c231fc76ccb55f29e3eefe9f1 |
| 动漫啦 | dongmanla | 1.0.1 | token1008/venera-cn-64bit | 1.0.0 | 62b7d99ee12997f0e3f4e244f626d95e83d2a3060b8ad4eb1212a37213378800 |
| 漫客栈 | mkzhan | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | c57fecd89d364edab67b412a5c864f0599570775d8eb1e4eb7a3de0889302f26 |
| 腾讯漫画 | acqq | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 6c155c4db1d0ebb1d51c626a7f201048dddd02b81f0315b33b2982305b0c73e2 |
| 诊断与日志上传 | venera_diag | 2.1.2 | token1008/venera-cn-64bit | 1.0.0 | 6435b641481be521f8bb7c8195f53955bba7cc86122cd7ee325059c31ca0eb3d |
| カドコミ | comic_walker | 1.0.2 | token1008/venera-cn-64bit | 1.6.0 | acbf044b6ef6131037fd518874d2de5b7d66891db1e8ec5ac9837901f0d7d561 |
| GoDa漫画 | goda | 1.2.3 | token1008/venera-cn-64bit | 1.4.0 | 5e4bfcb321979017ea4a6b59aaf44e67a45f32417f14c690f2102e65cba1439f |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.2 | token1008/venera-cn-64bit | 1.2.1 | ddd6421d3095f04d22a3cf82256a52bf68792b8241b8513d912c4718fd6b42c4 |
| Komiic | Komiic | 1.0.5 | VComic-org/venera-comic-source | 1.0.0 | 2d2e4aa8068355d265e57d3c4a15ecf1bc9def27ff38cc73b47d0d837658f5ec |
| 爱看漫 | ikmmh | 1.0.8 | VComic-org/venera-comic-source | 1.0.0 | 23ca88878d53f69b783171e968547f6d9fd62521802d1c599721d9dcbae0ce96 |
| 漫蛙吧 | manwaba | 1.0.3 | VComic-org/venera-comic-source | 1.4.0 | 4f44efdf0626623305e02a8fde4af4cedda906795f26ce3cc3c139c756a0c001 |
| Lanraragi | lanraragi | 1.2.0 | VComic-org/venera-comic-source | 1.4.0 | 3db60747709d72eff454d96bef13e907397ebd2a7e4e9cebd3279bddc5d768cd |
| 栗子漫画 | lizimh | 2.33.36 | Walter498/Walter | 1.2.2 | 593287454d650ba00f0605437bf9c3875ac44a1001922acb4075dab719490f08 |
| 百年漫画 | bainianmh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 84501b357e70a8ad932a377a6c6b518a88f93f5535767012effff3d85c5e47eb |
| MangaDex | mangadex | 1.2.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 4f87da9d6d42f8e39d09985bd7aef824f1e7593f329a61c45ceec6dcbd9c98ef |
| 动漫屋 | dm5 | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 78a751955d9ec6c640585220252757ffbc854331657ac0e7bd04d758dbf6d835 |
| 好多漫画 | haoduoman | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 66a40a20e5c77e71dfd3a1e3a2214cacee2f7e0fd549e6e3e0e14e61cfed5c14 |
| 看漫画 | kanman | 1.0.1 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 2bbc3b44b3fca765b8e4e984158a734aa5ad3811456e19cb9981e02a3ca1db74 |
| Komiic | komiic | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | e9ed391dc6aae13299d368ca2edfa148aac161eb525502078ca11a17d0abe742 |
| YY漫画 | yymanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 3a0dded6b83d8e89281ffa73be5d038abb71163a1c25a5511f23f8ed173b07b6 |
| 桂露莉漫画 | guiluoli | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 50698ca2fc0ffdacdc0a52d8b8088176b9c2e86003268b4d23dda8addce1ca2d |
| 读漫屋 | dumanwu | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 146504b647d58270cf9d01138a948b4093ce9c2f368f7c7ec41625ab6d8d8482 |
| Mangabz | mangabz | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 48cd14f63950f02d57d415dc65f038a22249a62944acd807fc45ac7e1789f62f |
| 漫画160 | mh160 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 8bda9f240300d3eaa59c556833d2a709782c34ec36abe428271cfed7ee1ddf22 |
| 36漫画 | mh36 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 7cac94ea3c1148568d00bbb69e8d34498b44733472f56d9e3e5f7ab4585b0d82 |
| X漫画 | xmanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 5d48f377b60a57c0fd076ad7a4b914946df474c44e658529a69a2c209051ec04 |
| Colamanga | colamanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 24f0e6ce8b61d9c048c541f313b0c1ff11fefe850b039ba1b71d2259f175b410 |
| 天天看漫画 | ttkmh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | f89629ba35c9b76c8c85a7b746f6d761c20b86b5fb620cb1bcc8fda36134d7f7 |
| 大树漫画 | dashumanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 151c2241e36e589666c35cf866d86918023bf69cf8e7d54178845b8211e30628 |
| 漫画鱼 | manhuayu | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 42df5b650c70a13e630fb1c773df6aae7824a73653993520c2a07ade1afb647a |
| 入漫画 | rumanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 4a946f6ca208e1aa7ad3156110c96eb9b4cef9c4c5d756b7ed9b142aad957d3c |
| 扑飞漫画 | pufeimh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 2e9cc2c30d2819c99a43b2a43585875c21c84974ba34a03dc3e3035bed0f50b1 |
| 百年漫画 | bainianmh2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 45c98e71b33e9d348861ed20e9e5e0854fb7dc93f334442ce798aabdaf3b0b05 |
| 好多漫画 | haoduoman2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | d630b4dd243e06627d4740038e128c474f7bae1b78ec70eeb681e24f1eda4699 |
| 嗨皮漫画 | happy2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 16b1ebeb1e1f37369367c35a7c24ece64394b5ff4487a7b5d2f52f6829bb0c26 |
| 包子漫画 | baozi2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | ed55379be8cf13d337b9845fa17bc5f94ec83293da2cb0c83808465b93002be1 |
| 漫画柜繁体 | manhuaguitw | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 57d93bcd74a5f09163df63621f88b57a323b50fccaacbad707955af8d385dd59 |
| 咪咕动漫 | migudm | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | b1fe28747575daa75b32248ff3824c6be4e6b5158b506939b2de5851ea8a61d3 |
| 动漫之家 | dmzj | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | df4e428166a6d9f0cff65f06f0f83f042dd7b2aec0dff3f60569e1d99db15319 |
| 古风漫画 | gufengmh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 08ac104b5091cfd0575948b4573f6f9045153ead15998494497f415c759cce1e |
| 有妖气 | u17 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 7570d2e4453554b90ae924efafde6318106ad33af384db3ec34b9fd73cc63bfd |
| MangaDex | mangadex2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 811e12f5038e4b6f3ae8460a3d501330273e8901e97e25dae1167ebf398cc44e |
| Komiic | komiic2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | c515ae96effb945057fc0d982fa39a1a5cc359bd0259eae1c295124c6cde1725 |
| ACG456 | acg456 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 0c20df919a92edfc6962d1d330bc9df2dde116ee3b2277989e83be71065ffa19 |
| ACGN漫画 | acgncc | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 181a418c6769ef0523965ba25fdf4988cfb24c2a843fccb6b0863f9c3617dc1a |
| 哔哩哔哩漫画 | bilimanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 4ee69cd45c7290ceb5b79a747d58830e0c2f180da28dbeb1f9b81ee975b4a9e2 |
| 布卡漫画 | bukamh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 8ab724cea08d98544fba5df04a50f3ab948a02cb6bc3394fbf322e9a7a5f1c43 |
| CartoonMad | cartoonmad | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | e2a3cf6dfd68762d8671b380322e62cf46f2a4bf6c423ea3be4a25140ad1f1df |
| 吹雪漫画 | chuixuemh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 41407917d3b91bba3b4b75237ebddc4fbe7ee07130f3525ff701a4fae8eeb97e |
| 吹妖漫画 | chuiyao | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 97b9e8b17accbc744cd6b41c4b828199339d1c2f0d344cd269de314940f6b6e3 |
| 大树漫画备用 | dashumanhua2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 6c5dae8a5be602d853fd23aa3ede2f16fc4a2ed09205f6551e1debee62dfc575 |
| 丁漫画 | dingmanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | e7d3e3247c676edb741d8dbb25f68e5cf41e194b316e172eb16a61a50230fb5e |
| Dogemanga | dogemanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 6413be028aea9e9730f59915a9751799da0f5f68a67f8b4c6e5273bf06db9863 |
| 读漫屋 | dumanwuorg | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 0d27326532341a1fdf1e4d2ffb6f4353062956405455ec7178b3ee56ede8dead |
| 飞雪漫画 | feixuemh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 54abe9573b6dbe04fcbc614ec678048a3885ec5b3e48ddda8219b9e1f0e8c797 |
| FMH漫画 | fmh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 6f2cc0230466a1f2abe28359f97a38f24330485a65f017c15d7061179a38e0d4 |
| GamerSky | gamersky | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 4603882d813be826486025455d18bfefd6af86e92e622c3a7d0e5f59c296b26d |
| 国漫网 | guomanwang | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | b16cd6785ab8d1c902586244b87292a472e711273b04ad8084e6e6aa6aff30d8 |
| 韩话吧 | hanhuaba | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 6188ccaa384672d6bf09bdc25fa9727e58b5c5c7a5c6eefcf175675eb6ac283f |
| HHXXEE | hhxxee | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 58a18f3e65e6b93d755f7c6ffb661e8d27d61771d5b91253a7e010f4b53b19d4 |
| 热辣漫画备用 | hotmanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | eb25ef1b967173041719bf2903c788d7126b59b93db3aec2c249c675e5e34265 |
| 爱看漫 | ikanman | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | f9cefbcbd1ca8f72665ee2ce94847a667e7096adca838987c6ca93e0a17bcd0f |
| 爱看漫繁体 | ikanmantw | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 2c0002a502ec47362990bf2741e35fd7f033bfeb9e0ebae12a7381b855c2a803 |
| 极速漫画 | jisumh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 27869910b1c6c5032f15f9f00f918f01fcb567151c9c612751f6edef0bb2be30 |
| JPM1234 | jpm1234 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | d75b54adc4c05f35e72b20bfdabf82b1f655107b9fb50b97d8658d761bd01b7b |
| KL漫画 | klmanga | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | e32f22a5c6a1edbd2b4d554f59821c09e31729a279238d49640344ddcb31c6a6 |
| MangaRead | mangaread | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | de204d1115a59d674d9a419831817edf5d53d4b512d322380228c250939b2b54 |
| 漫画DB | manhuadb | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 66e5777e2911bb901dad775297a28720cec432be59b5d03d3a409901951bd8e0 |
| 漫画台 | manhuatai | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 51c51f302841a1c46c637538f507d9dbf52276caca943f04b41eecafc96181d1 |
| 360漫画 | mh360 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 082b7b5f3d94fc81b0d8b2b154febd7558f591f9a23476b4d0635f5d126f9fd1 |
| MH57 | mh57 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | eaa72a09562f0c3767661640d0831e351305d6215cef0139243ef242d7f2098b |
| 522漫画 | mh522 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | b20307fccb8fa8717deb9ee25a09fdebdb4c20c3264d56406b4ed933992d7388 |
| 92漫画 | mh92 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 1efdff54fd28185f03bd11697370e16a2535b20c32fe61c2c707b3e1aaeb2214 |
| 快看漫画 | mkzhan | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | ef3180b57ffb6c32aaceede332b3a5f5e4812e7153aaceb4b174eb85889a6099 |
| MKZHANW | mkzhanw | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | ce0e736de76c38bddba3b03d80aa1fd9f9f674f75509bfb754287c851eb7bd89 |
| 梦游漫画 | mumumh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | c9ee59de31161808432ad3672882c508e75b310bfe4ab8b04da682f15cee4942 |
| MX趣 | mxqf | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 53a3adca770d099642d4da4c80c3c18e9854807e367bb12bc233216a711bea49 |
| 奇漫画 | qimanwu | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 0951a76595bf01f6c99d62ab8b49460ef38c4e393552fa8ac514c6d752be3e22 |
| 奇妙漫画 | qimiaomh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 551bab2142703d5c3201ae6095eb138296c16aa1940d586fc4a6e829725a9cd0 |
| Rou韩漫 | roumh | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 03e823e4286c0e3886c0a0558099d9f8c24d07f0df4df665e6a22b1d198fcfc2 |
| SF轻小说 | sfacg | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | b4ab2f8472a99eb4357c6dd3fb861e44265c8be3be4ae452dfd626fe08bad158 |
| 西西漫画 | sisimanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 86279ebe75df2d56f9990b4b3d9f6c7c0e0ff2ce27c0e493b5bae447337fac49 |
| 搜动漫 | soudongman | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | b224d65ccfa0f3f973b30ef0a7f0fa9e0cba160a4f2dea0851754c9cc881e093 |
| 仙漫网 | xianman123 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 6e54b96e4d5bc3b950a4e2c446b8a32915c8b6015710d211e540dfe5b2d2ff99 |
| X漫画备用 | xmanhua2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | d3f038f90d82b04ab70b5110b3499eb437f300c1863ed781dd2b6706df78fd2b |
| 一本漫画 | yibenmanhua | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | f0cfd7e0bb1a5e78ea854e770ec3548f01c1cfd9de846ff56b45a60578ad7c32 |
| 优动漫 | youdm | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | b152e216e84d22e76fc3a043d0f2b75f70ac6e70d4a2daaf063989dbd7a5dae6 |
| YY漫画备用 | yymanhua2 | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | ef36d29508d9268539bc00e3259581272fd4cc2fdca8cc951fd1e22756e2b5ab |
| 知音漫客 | zymk | 1.0.0 | weihanlong267-spec/Venera-Next-sources | 1.6.0 | 46ab685a91fab10dc9f3e8b6ee5e6b3166067e43ef4585f5f047dd1165e6e2ac |
| 极速漫画 | legacy_1kkk | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | eb0e0aa7c715ce71a3a932b20aa4c8bbcc8a29d7136746a9d766a95b010e91ae |
| 51漫画 | legacy_51sami | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | c4b40776f977d229eee6ed5eaa7fcb000cd361bce2d5f0591037774ecaee6f52 |
| 大魔兔 | legacy_damotu | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | cff311745f5b1ad664e4b19dba062cf3e974cd3ec988d4841cd13b14e06a617f |
| 看漫画 | legacy_kanman | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | 8ab8a3e0ccfe10462264f0130820c579dcd3bdcf3adfdf7100c255522585c19f |
| 神漫画 | legacy_taomanhua | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | 58e772b980531ede08561213022dfcb4163b9ce131d5431e6662ad5af1e9982d |
| 733漫画 | legacy_733so | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | c502bad23746384baf352bee7a4425a92b5d2293d0de6d464989c02040cdd823 |
| 漫画联合国 | legacy_comicun | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | 3e601fef4cf97bc2ef723af643564b019e0c7b146ccd73ed0d853547f474dbe2 |
| 六漫画 | legacy_hbdsfj | 0.1.0 | wuliaoe/venera-extra-sources | 1.6.0 | 3a045fc9d3dea78ad196fb3317b5a7b73fd8c14b6a5982d4134fc52e0999288d |
| 漫蛙 | manwa | 1.0.0 | xiaoxingmian/venera-configs | 1.4.0 | f40d0f77dedeb8a0a4c38dbb59d18686cb7b422bc41aae5bdc79ac88f0d20b81 |
| hitomi.la | hitomi | 2.0.0 | xiaoxingmian/venera-configs | 1.4.6 | 8b5bc5f7dbd3c9e20f944fb328bc2a6256ceee0a234cf2fda11f4631611332c2 |
| 拷贝漫画 | copy_manga | 1.6.1 | xiaoxingmian/venera-configs | 1.6.0 | e0a8d25704b83e3efcf757c0f6b80449bb2404bab5852ec5948a8ded44a99eea |
| 爱看漫 | ikmmh | 1.0.8 | yelongyue197-svg/venera-sources | 1.0.0 | c18c32e12b3ffa9e489c0d9792ee828b9df16ff8948b15eee8b718503871ec91 |
| Komga | komga | 1.0.1 | yelongyue197-svg/venera-sources | 1.4.0 | 7d11fbc62c254a8f2909fc3bdac3762f704b83e03de046fe3d9e209632a73768 |
| Komiic | Komiic | 1.0.6 | yelongyue197-svg/venera-sources | 1.0.0 | 31f0b78a6bf090743763f072e4d5b1a2e20666813ea5b1ef40b079b5f3519f09 |
| nhentai | nhentai | 1.2.1 | yelongyue197-svg/venera-sources | 1.0.0 | 40d2742d0f7bff46abda291d5a564c221bcc8ac0ff019cdc83bf833fdc4f52b0 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.3 | yelongyue197-svg/venera-sources | 1.2.1 | 3b1f2c677db6e6ae8217e32af8d191bc3352bd23e58f9965cee21daa9521344b |
| 漫本 | manben | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 53b79cb16a07e05e1910f77c03a55ef62e4417b4ca94e9b757fcfdce82475dc3 |
| 动漫屋 | dm5 | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | e948c055697747d401ba2177e95d4c341cbd22d894411e85661011a7fd527543 |
| X漫画 | xmanhua | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 89fb57efa92d994006310f45e8aec0a4ea6253bb273a0d58b612d568a2b0e1b2 |
| 漫画看 | mhkan | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | b7cae7695bd43aa034ce3a050e686550d7ae50c4fe359a5ac4ab354430714849 |
| 漫画皮 | manhuapi | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 9ca6d84bf82e3ca03415cd0e05739767d11d32476527833d3048f54b876076c5 |
| 包子漫画 | baozi | 1.1.7 | YHQY-Dev/venera-sources | 1.0.0 | 1d16542756f3bbaa4f699fbf55996239c3842a3c188b05e72b8045c6fd95d650 |
| 如漫画 | rumanhua | 1.1.0 | YHQY-Dev/venera-sources | 1.4.0 | 066120d2cf429efa904c7dc241e793e0ea16108e4bfc6ff482eadf50f7e45c3b |
| 包子漫画 | baozi | 1.1.9 | YongkeDet/venera-configs | 1.5.0 | 9ad7272a59dd26ea7f59e471ef140a63acbbdd16bcdcf694615e2c9201794816 |
| 拷贝漫画 | copy_manga | 1.4.4 | YongkeDet/venera-configs | 1.6.0 | b1a444db46b30b74c5c2852e12e09ce61cf7f68276ec15d5d21e74bd9080a134 |
| 香香腐宅 | boylove | 1.0.0 | YongkeDet/venera-configs | 1.4.0 | ba8f2403ab0f5b42d91950371476b8bd02528dbe38521954475702094fad0b65 |
| ehentai | ehentai | 1.2.0 | YongkeDet/venera-configs | 1.5.3 | ea4bcfde4f7574141806426a3a842a30378e045b14c58d265458489a29f8ea43 |
| Lanraragi | lanraragi | 1.2.0 | YongkeDet/venera-configs | 1.4.0 | 5552689d5e7169ad86d8347a136aa38a6c86744c1afc730aa5ca61ed8e86efb5 |
| 百合会 | baihehui | 1.0.0 | YongkeDet/venera-configs | 1.4.0 | 4b00bf339136b3ed70390b3887c84069eb2e8ac748a564127515d9809f6fd7fc |
| 拷贝漫画M | copy_manga_multi | 1.4.1 | yuxuanmian/venera-configs | 1.6.0 | 71722c9f639f36b85dfe74a09298821ab8c1988e98416326fc5c6bad30dac834 |
| Picacg | picacg | 1.0.8 | yuxuanmian/venera-configs | 1.0.0 | 168318286191f9848702847ac487e3a91061341779597575fc59bd6ce3f44510 |
| 漫蛙 | manwa | 1.0.8 | yuxuanmian/venera-configs | 1.6.0 | 50f92a3a66b5c625cbcc0df93007e5c269efdd55780c57b0e010e0dfcec75c25 |
| X漫画 | xmanhua | 1.0.0 | yuyuyu529/venera | 1.0.0 | ef06cd614412f0d15a594b493c4ebea14091df870d01c1b250aa15affe708187 |
| 卡拉漫画 | kalamanhua | 1.1.0 | yuyuyu529/venera | 1.0.0 | 40974a240f6993a6e2cfc394dccbdbd61c64dfe54c6ca388443ce73003a48041 |
| K-Mansin (韩漫) | kmansin09 | 1.0.2 | yuyuyu529/venera | 1.0.0 | 02a0d90b34f17d08d873f8abbced467c18b9c071954864f6171ff2a3fd94e4e9 |
| MangaKuro | mangakuro | 1.0.3 | yuyuyu529/venera | 1.0.0 | 53b8c89428c509ff202e295e343c2004b36399df11d6599ee1ff56c78a086f58 |
| Nicomanga(生肉) | lovehug | 1.0.1 | yuyuyu529/venera | 1.0.0 | 926672661ff83cce1b704220b4bede3465be95cdcdb3c76aa106a3055c2740a2 |
| jmanga(生肉) | jmanga | 1.0.3 | yuyuyu529/venera | 1.0.0 | 6b1e1245938cae839f6c444ab6301b06f315c1b325eb336c5195ec7321c63cb2 |
| KLManga(生肉) | klmanga | 1.0.0 | yuyuyu529/venera | 1.0.0 | c1f129e654e9031bc8582f7d65feeeb2d91b693a37e0835d77adcb4995baa514 |
| Rawkuma 生肉 | rawkuma | 1.0.0 | yuyuyu529/venera | 1.0.0 | fc9ac7ed1efab09cc477195a302f1316ea2b2e47b9dd036ffc84a2b8fd9c7774 |
| Dokiraw | dokiraw | 1.0.2 | yuyuyu529/venera | 1.0.0 | fb861b4f57f3bf64466c090fb9e12677000945c0f063d352ed6fffb2850329ab |
| Klto9 | klto9 | 1.0.3 | yuyuyu529/venera | 1.0.0 | dacecb6bf46a5a236c1f8617aa4c81369ae646d33c58d5e31c6374f0cdb6f02f |
| Manga1000 | manga1000 | 1.1.0 | yuyuyu529/venera | 1.0.0 | 2b843f03f678177daf3427836b293526cf2c3e7b4077918616928b1a9444b702 |
| Rawdevart | rawdevart | 1.1.2 | yuyuyu529/venera | 1.0.0 | 74abff1089aec0ffdc309075fff4b40d8b5f9918941213c9b3c5c74fed7579e5 |
| 툰코 Toonkor | toonkor | 1.0.0 | yuyuyu529/venera | 1.0.0 | 6e48ef757a254e46506f40e1633d5b22b23c97601094045525847a60881e6f0c |
| マガポケ Magazine Pocket | magazinepocket | 1.0.1 | yuyuyu529/venera | 1.0.5 | dea854e67e2ad373a5cd21727e064a415f5b3a38bf15b9db83559df579532476 |
| Mangabz | mangabz | 1.0.0 | zakkida/venera-sources | 1.6.0 | 8ec53577ba8e5a865589884f3d2be53ec108aff1085610124e66444e943c91b3 |
| 拷贝漫画 | copy_manga | 1.4.4 | zakkida/venera-sources | 1.6.0 | fcb90412e0d16323340337e815267bb02c6ca0491c00cbfabe55241ed67029ac |
| 拷贝漫画M | copy_manga | 1.4.4 | zakkida/venera-sources | 1.6.0 | e2ba75d47461ea726af9fdd933e779ce8ec1bb24cd40ddca033650d6026b99a2 |
| Komiic | Komiic | 1.1.0 | zakkida/venera-sources | 1.0.0 | c01d8348577ca1fa83264d29071af81eca2346aaa026da42ab55c6dce0c32955 |
| hitomi.la | hitomi | 1.1.3 | zakkida/venera-sources | 1.4.6 | 7aeef0e996adbf5a8ee49bd8079f8c9d1fedbde3b9205782647212734f94f7a1 |
| 优酷漫画 | ykmh | 1.0.2 | zakkida/venera-sources | 1.4.0 | f862f6aaac364564740ea77672fa248811d94c9176a6b1c73a42387bc9430ffe |
| 漫画1234 | mh1234 | 1.0.1 | zakkida/venera-sources | 1.4.0 | 913f1b26d976ddf2d67bbd6f56585453120fa9af90e9aa4b3bea50d1fa746538 |
| Komga | komga | 1.0.1 | zakkida/venera-sources | 1.4.0 | 550a18cf941e8f63904b0248ebc39329d124f8b8e259f7cc925873d89930bb79 |
| 漫画1234 | mh1234 | 1.0.1 | zhimouzhou/venera-manga-sources | 1.4.0 | b1f34a65e13d15d6ac3c03836c1b7e0a8f68c40bb6a490d7155d31c134035bab |
| 漫客栈 | mkzhan | 1.0.1 | Zicheng0326/my-venera-sources | 1.0.0 | 1959122cc804977ad90f8b09f23379af3e20fd23cd2ef4dab5da21ad8a854b67 |
| 动漫啦 | dongmanla | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | d447e6094f06b4c15c53ec18b04cfc8d19a02a2f268235287dd77c2a0609ec74 |
| 漫画柜 | manhuagui | 1.2.2 | Zicheng0326/my-venera-sources | 1.4.0 | a70d41ae9b2a8c12430a97c52e154a811bb272e36ff905594929a86c786d56e8 |
| Mangabz | mangabz | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | bac41b0b008db6e18d52bb6975ffcb54a10b63526243075d53bf369a12c7fdc2 |
| 漫本 | manben | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 857078783fc13901bba12ccdbe9e61c6d2e344bfbcd8fc044d207d2e9c7d7f55 |
| 动漫屋 | dm5 | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 23d16ca1bd1848acd3177fd8f1040406a90302e502bf1483c3221e1afb3171d1 |
| X漫画 | xmanhua | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | cd69b8e353ab985a755aacbd818499f7188d0031b4d16665129eb02d78c41bde |
| 思思漫画 | sisimanhua | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 24bc9bc9f6836790010f2610874765bf0d1978302015523570358cf1dfabb719 |
| 漫画看 | mhkan | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | c4e413124508117a54fb268af125e744eeece603a974f045f07c46d174524140 |
| 热门漫画 | remenmanhua | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 6618d81a425fb79ee67bee788f97317cc87e738caa0233ca9c1a9874ac9bf9a3 |
| 漫画皮 | manhuapi | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 6261205a904317e0f966613930a21aaa679384f2246d1b102cddab820e8b001e |
| 爱飒漫画 | isamanhua | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 1819bb5a5a4be11ba95e4429e09aa5d303286097221a5f0bb6ce485beb4e5af1 |
| 看漫画 | kanman | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | fd979921b04b0c0aefc8927f4dfe6af0575348db542f0110aa1a560a9f6c0e91 |
| 包子漫画 | baozi | 1.1.7 | Zicheng0326/my-venera-sources | 1.0.0 | 7d5b1645ae5cab77d662f718b559b816321ded7fcb31062f85c9620b49fba75d |
| 漫蛙 | manwa | 1.1.6 | Zicheng0326/my-venera-sources | 1.4.0 | f1deb62e8300f28934498e426857439a3708f10c1bfa68e881233df869428f2f |
| 如漫画 | rumanhua | 1.1.0 | Zicheng0326/my-venera-sources | 1.4.0 | 0e2041ca3177a48c2bcde2fc54929c26afa5f0b773ec0cdee7e81ab9c270a784 |
| 布卡漫画 | bukamh | 1.0.0 | Zicheng0326/my-venera-sources | 1.4.0 | f5c8c65ab34ddf7fc9bdeab95ad054666f0b1e0e0a1719bab4b6ceb063aad023 |
| 次元漫画 | cycomic | 1.0.0 | Zicheng0326/my-venera-sources | 1.0.0 | 089712e928638293a05efbbed52da9ece5367baf684a303ccce64d274968550d |

## 索引获取问题

- `137syh/venera-syh`：漫画源07：HTTP Error 404: Not Found；漫画源08：暂不执行非 GitHub 原始地址；漫画源09：HTTP Error 404: Not Found；漫画源10：HTTP Error 404: Not Found
- `2869893488/ikmmh-venera-source`：HTTP Error 404: Not Found
- `6678670jsy/venera-sources`：HTTP Error 404: Not Found
- `893954529/venera-configs`：HTTP Error 404: Not Found
- `Bandcomic/RESTful-venera-source`：HTTP Error 404: Not Found
- `BlueStarOne/bluestarone.github.io`：HTTP Error 404: Not Found
- `ChenTeea/veneresource`：HTTP Error 404: Not Found
- `cheyou001/venera-sources`：HTTP Error 404: Not Found
- `F22822/22822`：HTTP Error 404: Not Found
- `kuiti/manga-source-index`：HTTP Error 404: Not Found
- `l233333333/venera-sources`：HTTP Error 404: Not Found
- `LuckyLxi/Sources`：HTTP Error 404: Not Found
- `morpuct/venera-sources-hub`：311漫画：HTTP Error 422: Unprocessable Entity；4399漫画网：HTTP Error 422: Unprocessable Entity；51漫画：HTTP Error 422: Unprocessable Entity；51漫画：HTTP Error 422: Unprocessable Entity；A漫：HTTP Error 422: Unprocessable Entity
- `NinEvandesu/venera-configs`：HTTP Error 404: Not Found
- `nukbodu/mh-configs`：Komiic：HTTP Error 404: Not Found；Picacg：HTTP Error 404: Not Found；nhentai：HTTP Error 404: Not Found；紳士漫畫：HTTP Error 404: Not Found；禁漫天堂：HTTP Error 404: Not Found
- `QWWWQ-MIX/venera-sources`：HTTP Error 409: Conflict
- `snowf14k3/venera-komiic-multi`：Komiic 多账号：暂不执行非 GitHub 原始地址
- `Taototo/venera-comic-sources`：漫小肆（18+）：HTTP Error 404: Not Found；包子漫画：HTTP Error 404: Not Found；鸟鸟韩漫（18+）：HTTP Error 404: Not Found
- `yelongyue197-svg/venera-sources`：动漫啦：暂不执行非 GitHub 原始地址；妙趣漫画：暂不执行非 GitHub 原始地址；六漫画：暂不执行非 GitHub 原始地址；动漫屋：暂不执行非 GitHub 原始地址
- `zetriumyx/noyacg-source-venera`：HTTP Error 404: Not Found

## 新仓库线索

仅列本次 GitHub 更新排序搜索第一页的未登记仓库，尚未认定为漫画源，不代表全网穷尽。

- `veneraproject/native-gui-wallet`：Electron wallet for the native Venera GUI wallet
- `laincat/VeneraCat-Core`：Shared Go core for the Nekularity (iOS) and Nekophage (desktop) clients: Venera-compatible comic sources, video plugins, .venera backups. GPL-3.0
- `venera-app/venera-prime`：A comic app,but prime
- `Taototo/ManComic`：A Flutter comic reader app based on Venera
- `Ciaodar/VenerableKnowledge`：a minecraft mod with a potion effect.
- `jnsingh01/venerabulllife`：Venerabull Life — public website.
- `Maxll51/EZVenera-Lite`：EZVenera 2026 Edition: Lightweight Venera Rewrite with Streamlined Plugin Runtime for Windows & Android
- `venerahome/venerahome.github.io`：Venera Hasanova · Imoti Premier · Property in Greece
- `jnsingh01/venerabullstudios`：Venerabull Studios — a showcase of projects in development.
- `jnsingh01/venerabullinteractive`：Venerabull Interactive — public website.
- `LeylaKhojasteh/venera-jewelry-store`：Venera — Persian RTL jewellery storefront with Next.js, PostgreSQL, Prisma and Three.js
- `staciepomar-spec/venera-glass-build`：CI build of venera v1.6.3 with a Pure-spec liquid glass bottom bar
- `gallhall/venera-v`：venera-v：支持漫画和视频的开源阅读器，基于 venera，支持 Android、iOS、Windows、macOS、Linux。漫画源列表：github.com/gallhall/venerav-configs · 更新频道：t.me/VeneraV_Updates
- `Venera-Works/Venera-Plus`：VeneraPlus 是一个跨平台漫画阅读器，支持本地漫画、网盘 漫画源、第三方网络漫画源
- `Venera-Works/Venera-Native-Prebuilts`：
- `Vulpes-venera/CS50p`：
- `Walter498/Venera-Max`：以 VeneraX 為基礎、按我們自己閱讀習慣深度改裝的漫畫閱讀器（栗子漫畫源優先）。加了什麼、修了什麼，全部寫在 README。
- `ryanp-cloud/venera-ai`：
- `venera-tropnikova/Alexs-Amazing-Garage-play`：Test play build of Alex's Amazing Garage (dist only). Source stays private.
- `w13630039663-bit/venera-miuix`：一款支持漫画阅读器（支持picacg 禁漫 nh ex和其他正常 混合）漫画和图库功能——采用Miuix风格重构的Venera。
- `CyrilPeng/Venera-Next`：VeneraNext 是一个跨平台漫画阅读器，支持本地漫画、WebDAV 漫画源、第三方网络漫画源，支持 Android、iOS、Windows、Linux、macOS 平台。
- `venera-kuz/uchebnaya-praktika`：
- `markiianklymchuk-hash/kingdoms-of-venera`：
- `3176289965f-ai/my-venera-sources`：
- `CangShui/VenHM`：兼容Venera源的鸿蒙开源漫画阅读器
- `lwtor/venera-native`：Android 原生漫画阅读器，使用 Kotlin 与 Jetpack Compose 构建，兼容 Venera 漫画源生态。
- `vonhezhou/mansou`：漫搜：支持多源聚合搜索与下载的自托管漫画工具，兼容 Venera 漫画源插件，适用于 NAS / VPS 部署。
- `Manjit53/venerable-dasik-a5e0ff`：
- `Kyosee/VeneraX`：A personal-use fork of the original Venera, maintained and enhanced to suit my own needs. ／ Fork自原版Venera，仅进行自用需求维护及增强。
- `huangjun7hb/venera-next-sources`：
- `Venera-d1/heart-python`：Draw a heart with Python Turtle
- `wnzmb/venera-configs-wujiajun`：Venera 漫画源：nhentai / e-hentai / hitomi，指向自建 Cloudflare Worker 反代
- `mentalshinobi/venera`：
- `normalice8/VeneraNext-comic-sources`：
- `haukuen/venera`：仅自用 ／ For personal use only
- `Gandum2077/venera-patrol-cli`：
- `noorlightazaz-gif/https-venerable-sunshine-623dd3.netlify.app-`：
- `Ryuzxy/Analisis-Veneralbility-WebGoat-Ilkom-Unej`：
- `Venera0207/venera-portfolio`：
- `amke79/venerastudios-site`：
- `john-cpallc/venerable-grain`：
- `AnziibMeepo/VeneraM`：A comic app，自用版，增加了图片超分功能、拆分跨页功、修改了左右连续阅读功能的滑动BUG、修复了很多地方崩溃闪退的问题、换了一个自己很喜欢的图标。
- `Venera0207/venera-sales`：
- `veneraproject/venera-node`：
- `MatthewLestermun/venera-salon`：
- `Kerollos004/venera`：
- `SYXZyt/Venera`：Official compiler of the Venera hobby language
- `ACGNnsj/venera-unified-configs`：Self-hosted source catalog and configs for venera-unified (B4)
- `rinnki-L/-md3-`：Venera 漫画源移植到阅读MD3的书源（10个漫画源+合集+订阅源）
- `QiongHHHZZZ/VeneraQ`：An Android comic reader. A fork of Venera-Next, Android release only.
- `JUTZUGC/venera-deploy-guide`：Venera 一键安装｜本地和网络漫画都能看，装完导入漫画源即可｜自动校验三平台包｜第三方一键部署方案
- `fave-eng/venera`：
- `matloporokjl-tech/https-venerable-malasada-5a1196.netlify.app-`：Google Keep clone (HTML and CSS)
- `lll152872/venera-lll`：venera 二次开发：无缝跨章阅读、书源隐藏、快捷搜索、追更检测优化、
- `opaiopaio/Venera-Nas`：Venera 漫画阅读器 - SMB/NAS 定制版，支持访问NAS保存的漫画，支持将漫画下载到NAS存储中
- `ikun5200/venera-prime-server`：
- `1148891151a-ui/-veneranext-sources.json`：
- `rytzj2-spec/VeneraX-nagi`：
- `yanyi05/venera-sources`：Personal JavaScript sources for VeneraNext
- `XclusiveM/venera-nailart`：
- `yuxuan965960/VeneraX-ios`：VeneraX - Flutter app
- `KBPZSDP/Venera`：
- `18846743977-alt/my-venera-sources`：my-venera-sources
- `FengHA223/venera-ios12`：
- `a3169249487-sys/Venera-Next-ai-upscale-temp`：Experimental AI upscale build for Venera-Next
- `Gandum2077/venera-runtime`：A venera runtime that works in both Node and JSBox environments. 
- `SnowDreamXUE/venera-next-config`：转换venera-config漫画源配置文件格式为venera-next要求
- `cylendra-info/Venera`：
- `venera-tech-art/Dashboard`：
- `Venera-h/a-b_test`：Анализ A/B-теста нового экрана оплаты: SRM, бутстрап, сегменты
- `vetatina-hub/venera-bot`：
- `pastorig/Voskhod-2-y-Venera-7`：
- `roddup75/venera`：capacity
- `Vartak2/Project-Venera-14`：
- `940440952/comic-sources`：双生态漫画源：Venera / VeneraNext / VeneraPlus JavaScript + Aidoku Rust/WASM；目前维护 manhuazhan.com。
- `buzhidao10068/venera2picacomic`：把 Venera 导出的 .venera 转成 PicaComic 能导入的 .picadata，迁移收藏夹与阅读历史 ／ Convert a Venera (.venera) export into a PicaComic (.picadata) import, migrating favourites and reading history
- `venerasf/Venera`：A modular exploitation framework extensible with Lua
- `venvnft/venv-sc`：Smart contract serving as a marketplace for music in NFT format, facilitating sales and auctions for ERC721 and ERC1155 NFT.
- `decker-archive/venera`：Free and Open Source alternative to Discord and Guilded.
- `nobug-project/venera-configs`：
- `Tzhl-ovo/venera-configs`：Venera comic source configurations
- `zzu8493-debug/venera-configs`：
- `Day-Day-S-t-u-d-y/venera-configs-custom`：
- `clxin43/venera-my-configs`：public
- `StevenSun121/venera-configs`：
- `fuluoydebende/venera-manga-sources`：Venera manga sources (fixed) - 33 sources + index.json, ready to import in Venera
- `yuanshenmingri/venera-comick-sources`：Venera ???:Comick ??(69 ?)+ MangaDex v2.0
- `huang7hb-pixel/venera-next-sources-`：
- `xunchang528/venera-sources`：
- `kkiki11/venera-comic-sources`：Personal Venera comic source JavaScript files
- `amenoshigure/venera-sources`：嗨皮漫画源
- `istayheart/my-venera-sources`：sources_copymanga
- `fuluoydebende/venera-hipmh-source`：Venera 漫画源 - 嬉皮漫畫 hipmh v1.0.2 (API 驱动修复版)
- `dororo42/EZVenera4KO`：EZVenera/Venera JS 漫画源移植层 for KOReader (LuaJIT + quickjs-ng)
- `handahao666-boop/venera`：这是一个自己开发的venera漫画源仓库
- `neffict/venera-mcp`：Venera 漫画源 MCP Server
- `Pinellia451/Venera-local`：将本地漫画做成venera可导入的局域网漫画源
- `Kiastr/Venera-SSR`：A manga viewer.support realtime Coloring  and Anime4kSR and OCR translation.All running locally./ 一个支持不同漫画源,阅读实时,本地黑白漫画上色，anime4k超分辨率，本地ocr翻译的改版漫画阅读器
- `Jieless55/venera-megacomicxadult`：R18漫画源
