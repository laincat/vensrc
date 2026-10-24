# 上游变更与待审阅候选

检查时间：2026-10-24T06:47:27.566145+00:00（UTC）。
检查 49 个已登记仓库；发现 159 个未审阅源码构建。

新代码只下载计算哈希及读取声明字段，不通过 list、init 或巡检执行。维护者在 GitHub 审阅固定提交的 JS 后，把候选加入 monitor/catalog.json；后续 Actions 才会执行巡检并按主／扩展标准自动收录。

候选排除官方原版、转引，以及未严格高于官方版本的社区同 key 源；版本更高也必须审阅、巡检后才可收录。

## 源码变动

| 名称 | key | 版本 | 仓库 | 最低应用版本 | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| 爱看漫 | ikmmh | 2.1.2 | Junkrat9527/venera-sources | 1.0.0 | fdab1f9f87c055e33fdf069a744ef1ed60c1f421c4c85806b5e69412be9a6ee3 |
| vomic | vomic | 1.2.0 | 137syh/venera-syh | 1.5.0 | 525cf99fc99d62991069c3c01ecaff16b4044804ec451743ec7188af3f853846 |
| 漫蛙漫画 | mwuu | 1.2.0 | Angus-fw/venera-configs | 1.0.0 | 1cd62034164549749d971b15a7ac1e085c6d9b9bd721029038660d1635f1d49b |
| 快看漫画 | kuaikan | 1.0.3 | Angus-fw/venera-configs | 1.0.0 | a2a515bde9bb5c7b7c1b22417559e7d4db03e872523cef4053b9808c11cf93de |
| 包子漫画 | baozi | 1.1.7 | ChopDream/venera-source-hub | 1.0.0 | 81214391b7fb95d8e632381d92f284e26939c4b465abed5a0cb324606564e1be |
| 禁漫天堂 | jm | 1.4.2 | ChopDream/venera-source-hub | 1.5.0 | 1b195b4ecd0bcbed61546d11761f6d0c8b027588564da7d28368f2f4645d5b16 |
| nhentai | nhentai | 1.1.2 | ChopDream/venera-source-hub | 1.0.0 | 9379d8441f42d06a7835cee6b21519ea8a951eb01c476402d00dce721ffeaec6 |
| MYCOMIC | mycomic | 1.1.2 | ChopDream/venera-source-hub | 1.4.6 | f35e2e7cb531f7591e81a5edf41ab6303880686f0009c7477f77154e9511f07f |
| 紳士漫畫 | wnacg | 1.0.9 | ChopDream/venera-source-hub | 1.0.0 | b2886d9c54ae662f2b0da391fe6769779043a6cf01af4174eaec64d7e9f2f734 |
| Komiic | Komiic | 1.8.3 | Junkrat9527/venera-sources | 1.0.0 | d957a4de13948a967368975b43e947a3dc56cb094f02e4fa9b62f8339a5e678a |
| 包子漫画 | baozi | 1.2.1 | Junkrat9527/venera-sources | 1.0.0 | 0fe528ef087e092a2d57ec32f2d9414642987e07ceaced9973c6ecf8acb1cb40 |
| 包子漫画 | baozi | 1.1.7 | zhimouzhou/venera-manga-sources | 1.0.0 | ed698fbc58b216b0a22bc178947f56f637400629cd4a852bcda70b68b34349f3 |
| CCC追漫台 | ccc | 1.0.9 | Junkrat9527/venera-sources | 1.6.0 | 062c6d3948d728e97d529330b0db07b102b259302571a0aeb2ec0e213b38b5b5 |
| カドコミ | comic_walker | 1.3.2 | LX7kM9/venera-configs | 1.6.0 | 266cab4c1172866c25fb5b61f57f56502817b2c7dc14a707d67e5e8b1f3fdf0a |
| comick | comick | 1.3.0 | LX7kM9/venera-configs | 1.4.0 | 510fbc210f12ab0260d26b4b708c8d23582e11c68fad4d5f7a0aac820bc7d236 |
| 拷贝漫画 | copy_manga | 2.3.1 | LX7kM9/venera-configs | 1.6.0 | ea1f834157acd3787eade0a4c436f172b46e983f576e46142aa650574f373ca5 |
| 动漫啦 | dongman_la | 1.0.1 | n3114576614-cell/N_venera_source | 1.0.0 | f3599e84cdebd39aa3cf752e0b97b015ea673917314572cf52e567d81a12daba |
| 动漫啦 | dongmanla | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 15a8e8970bd8142accb161272c6491082b193d8ceaad393025877effe63cf009 |
| ehentai | ehentai | 1.2.1 | VComic-org/venera-comic-source | 1.5.3 | 1aa135bfdba24d66eaea1cbd6c66eb4d6b7a97d62ffc8ef8361f2ce5eff6038b |
| GoDa漫画 | goda | 1.2.4 | LX7kM9/venera-configs | 1.4.0 | d560801cd543d9cec07d1098b46f9992276cde9e904c5a8ff431a678a2f3415e |
| 爱看漫 | ikmmh | 3.0.1 | Junkrat9527/venera-sources | 1.0.0 | 78cc44bb2c9a69225a3446698005d3d33080dedb67ff9d9e7cc43052e14190f8 |
| 禁漫天堂 | jm | 1.4.3 | VComic-org/venera-comic-source | 1.5.0 | eb059a5ae6ad528bbcbfcfb2296a4b3945405bb5cab1faab326f1b374450d0b7 |
| Lanraragi | lanraragi | 1.2.3 | LX7kM9/venera-configs | 1.4.0 | 55bc1f431f9e26af5a20a38cc26fc233595df10a00916ca519afc042f33ef8ad |
| MangaDex | manga_dex | 1.9.4 | LX7kM9/venera-configs | 1.4.0 | c1fda4f7542327ea9c35a485250b7f97ba51c65b831407a4f1474ee51728ae97 |
| 漫画柜 | manhuagui | 1.2.2 | YHQY-Dev/venera-sources | 1.4.0 | b7f7995704b42b31010edf007c6a069bef77d3a96d03b5dca2d3456c6e2b29a4 |
| 漫画人 | manhuaren | 2.0.0 | Junkrat9527/venera-sources | 1.6.0 | 5adc51fbd180f7f4b987d9f36c1f06951d3507a61def96385af2b72eb078508d |
| 漫蛙吧 | manwaba | 1.0.3 | zhimouzhou/venera-manga-sources | 1.4.0 | 2727adee5abf680436db5a962b460bd416bfdb3042c3e5b0256a595efe22323c |
| 漫画1234 | mh1234 | 1.4.3 | LX7kM9/venera-configs | 1.4.0 | a1d71934255b57ea7f7895a9bdedbfedceeda4fcdaec9aa765cd974792c985d5 |
| 漫画1234 | mh1234 | 1.0.1 | Junkrat9527/venera-sources | 1.4.0 | 6f410a9984f172b202bad08f4d12aed7629cde43fc02280edd3f4f443558aecc |
| MYCOMIC | mycomic | 1.1.1 | LX7kM9/venera-configs | 1.4.6 | 0d1ee97148833716ff4b667872e28d14c751a17720c6518edcff1fd91c116448 |
| nhentai | nhentai | 1.1.1 | VComic-org/venera-comic-source | 1.0.0 | 9c637790f59d072003adbdee32b1336082d58e50e6cfa4f5cd5becde18996129 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.3.1 | Junkrat9527/venera-sources | 1.2.1 | d7cc9e684b14239e3c921d8ce19da7db9343ccf7692093a7d048f21822130f6b |
| 优酷漫画 | ykmh | 1.1.0 | Junkrat9527/venera-sources | 1.4.0 | effa08b818616a670bfe5ff5e1abc42e5da925fe767dec86c84d9ea51016e861 |
| 优酷漫画 | ykmh | 1.0.1 | zhimouzhou/venera-manga-sources | 1.4.0 | d0eb522a8fe55d322cca2c27c1a8f7e27dd0bf5b24fe80eab9032dead0f8bde6 |
| 优酷漫画 (修复版) | ykmh | 1.0.6 | yelongyue197-svg/venera-sources | 1.4.0 | f0b1979721bf81094772b4575c2cb1a6ebc774a58d4b3f3fa301a36b5a7d641f |
| 再漫画 | zaimanhua | 1.2.6 | LX7kM9/venera-configs | 1.0.0 | ecef4acbb4548e999cda545931cd71f5951a5b9231a10e8f23d04156064279de |
| 再漫画 | zaimanhua | 1.0.3 | zhimouzhou/venera-manga-sources | 1.0.0 | 2d9e8d071b2cd1cd5b6c5cd5d06716c2f0aa941ebe9da8c9d96c27c1c2a17273 |
| 咚漫漫画 | dongman | 1.0.0 | cattoldme/venera-configs | 1.6.0 | db829f439e27dc33c3ae3303646fa780efe7d2c37ee9c777df1f041d7631485d |
| 嬉皮漫画 | hipmh | 1.0.1 | AXmishell/venera-configs | 1.0.0 | 57f23ebd47143defe73117ed24b986bb99ad1904938ec42725c15440b139a0cd |
| 如漫画 | rumanhua | 1.0.3 | caitlin-cheng-ccc/venera-configs | 1.4.0 | 78f7fba17c15bbbf10bb52b4f46d5df2222e3cfef18abfee19c750dad8348800 |
| 瓜子漫画 | guazimanhua | 1.0.4 | LX7kM9/venera-configs | 1.0.0 | 07aaf9e53940358eab902e47f7971980b699a09aa4104176fa9bb9d1b656f6ed |
| 动漫啦 | dongman_la | 1.0.6 | LX7kM9/venera-configs | 1.0.0 | 56989eb9acd1cf21a44cde3ddb1726a69dbafaa115b25e1a2a63736f0ebc8d44 |
| 如漫画 | rumanhua | 2.4.2 | LX7kM9/venera-configs | 1.0.0 | 9d9ada706f965a6da4c36588d50827a8ef37d3c47c989f993e991e08994787d7 |
| 飞翔漫画 | ffppt | 1.0.6 | LX7kM9/venera-configs | 1.0.0 | 4eeee3685842c843c12c909ec75680ed6a332120a0f86c27c8bb48b43b68bb96 |
| 来漫画 | laimanhua_split | 1.2.2 | LX7kM9/venera-configs | 1.0.0 | 9874de436f3ee50db72543c53ad47a5375401791daf89f1f6542d485b6ae6c03 |
| 爱看漫 | ikmmh | 3.0.1 | LX7kM9/venera-configs | 1.0.0 | e78216115cc4e14484b3cbe299585a99f832944a8e277bd11b365ccae9396c98 |
| 哔哩漫画 | bilimanga | 1.6.3 | LX7kM9/venera-configs | 1.6.0 | 97fd92499c11c4ee0baed1874598862d021051c22abe08674e9152b8458eb2fe |
| 51漫画 | manga51 | 1.3.0 | LX7kM9/venera-configs | 1.6.0 | c02ee18f652724a534d19e5d7206dcf855d43f1768356820caaa6974666a7b10 |
| NoyManga | noymanga | 1.1.6 | LX7kM9/venera-configs | 1.6.0 | 2917b22ca6b78778d7c5761d27b001324475f54ba3548abfc4c8b00c32321381 |
| 优酷漫画 | ykmh | 1.2.0 | LX7kM9/venera-configs | 1.4.0 | fbd0c34abd226cc98980aa3bfb633012f42f8fb90bade985312bb1889358c725 |
| 动漫屋 | dm5 | 2.0.5 | LX7kM9/venera-configs | 1.6.0 | f1082766eade7d5acea8156b19430499fc1f8004408b9dfd4964dcad03f7fcbd |
| Mangabz | mangabz | 1.0.3 | LX7kM9/venera-configs | 1.6.0 | 06aeb01ff5b8ef3be44e36da8f3c4242d80bcdb13581d730191069a735fefc59 |
| 311漫画 | s311_com | 1.2.0 | LX7kM9/venera-configs | 1.2.2 | 7de2d08ef245b7cb756b5f6500b1c6f1f84733f4211c09f525666e8de4321746 |
| 好看漫画 | haokan_txt | 1.0.4 | LX7kM9/venera-configs | 1.2.2 | 04bfdfb5fd06f5e29c340253cc5c78e5c5f1a47d65766d920b841ea41e5cb53d |
| 思思漫画 | sisimanhua | 2.7.0 | LX7kM9/venera-configs | 1.0.0 | 189b8656d816de05b70f07b71da6a593dec6280e054405aeacbfa5c001a6c065 |
| CxC | cxc | 1.0.4 | LX7kM9/venera-configs | 1.6.3 | ea881a3a29c020802f63e20451bd74599b245e063b64decd752f2596caa7bde2 |
| サンデーうぇぶり | sunday_webry | 1.0.1 | LX7kM9/venera-configs | 1.0.0 | b7b5303abd2e69ff690b0f546d3f3a498b46702b81b545f2076a79014730c800 |
| 包子漫画 | baozi | 1.2.2 | LX7kM9/venera-configs | 1.0.0 | 5a6472e9eb85f98ac97f6456c2b7217c5d9117126e1863690df41f3c085108f1 |
| 漫画人 | manhuaren | 2.0.1 | LX7kM9/venera-configs | 1.6.0 | a13a85540e57ee3ae4a8ccdcf0f4c83fd8d396dd678afa04ba5dc0260533e70e |
| CCC追漫台 | ccc | 1.0.9 | LX7kM9/venera-configs | 1.6.0 | 42a220ca017e01b5cd45d53ec9f70e3a20b8453f0c68870f42de7762a4ffe95b |
| zero搬运网 | zerobyw | 1.2.0 | LX7kM9/venera-configs | 1.0.0 | 4cc6a768c02333b851ba9427f2897a69af4ed6a8f17adb1de7baf20a66cffa81 |
| Komiic | Komiic | 1.8.3 | LX7kM9/venera-configs | 1.0.0 | cbb3ac23c4389fb73c341bd14d169c011a81913957fa284e321a86df513ebc8f |
| yande.re | yandere | 4.9.4 | LX7kM9/venera-configs | 1.6.0 | 089c33fde66e90452ee7c1a1662437098a7fc25d98f703bd75d5a4250325ef50 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.4.0 | LX7kM9/venera-configs | 1.6.0 | b7a3564421242b44a7004ece5bdc439624a97b840a31a55d581e1cf8cbdd1b74 |
| 百合会 | baihehui | 1.0.1 | Magentadots/venera-configs | 1.4.0 | a8ee1645dbe486e6bcda2309b729873ed2557675226b908604cf07b6dca229c9 |
| 包子漫画 | baozi | 1.2.0 | Magentadots/venera-configs | 1.0.0 | e548cdfaaa2810dbf6c2b007310b15186d6b2fca39927b30ff592fa2cce71cb5 |
| 拷贝漫画 | copy_manga | 1.6.1 | Magentadots/venera-configs | 1.6.0 | b352baa7ce4da19aca93b197f1cebcadf1a739723cce5f8bff1f74b94554ea60 |
| 拷贝漫画(多账号) | copy_manga_multi_accounts | 1.4.2 | Magentadots/venera-configs | 1.6.0 | d70f680003d13e1c53155804a7e4014334d52feef47345432829c7aef09e2077 |
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
| 漫蛙漫画 | manwa_routes | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 8b7a65e5a520003d9ce6885848f882ab6b9f50a286bb50109835a5cb5303d5ba |
| 如漫画 | rumanhua_com | 2.1.2 | Ra1nbo-w/mhy-v | 1.16.0 | 3a383515749605a38609e8b5260e1f9aaf6aefd4f2dde22a38c07d9e606b93f2 |
| Komiic漫画 | komiic_cc | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 0d627b63113b1e0ca2c4180df732fd15f9b50f919919e8efaf7159ba99355514 |
| 漫画屋 | mhua5 | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 63b165b1065239b07d94c3a83750824fde8a53bc1c2afc9b0af5f0bfd0195b6c |
| 拷贝漫画 | copy_web_routes | 2.3.2 | Ra1nbo-w/mhy-v | 1.0.0 | 7a472063e163a7a33f888554c83e1043c3a400641ee9e43d04e6de64b4933b22 |
| 瓜子漫画 | guazimanhua | 1.0.1 | Ra1nbo-w/mhy-v | 1.16.0 | 4f94b6801f09db7534de9f98c650e686ff6ff7dfbf5658a81a1b6d38b2ff2d1b |
| MYCOMIC | mycomic | 2.3.3 | Ra1nbo-w/mhy-v | 1.16.0 | 763e7973a8ae82fe2af031bcf24b51796435dd840d45791b87ae2798e38ef826 |
| 包子漫画 | baozi | 2.3.3 | Ra1nbo-w/mhy-v | 1.18.0 | 445daa4d7caace438f7e1a1f9477b8e39fffb8f87b70c969a78aa63930410114 |
| 漫自由 | mheee_catalog | 2.3.4 | Ra1nbo-w/mhy-v | 1.0.0 | ff7d63b45ec92bfd7e78565bfa29becff2c94da2a040d6e18cab9ae235b62dc9 |
| HLZY资源（私人） | private_hlzy_video | 1.2.0 | Taototo/venera-comic-sources | 1.0.0 | 7fe92bd8b3a421ffc246403d2e20640c20680ec3ab16f8eb26244cd99bd8b4ed |
| 91短视频（私人） | private_91short_video | 1.0.1 | Taototo/venera-comic-sources | 1.0.0 | f63d4e8e04fe08ab960331baa72378ac606814a1eefcc0a86b8dc85ae1be9024 |
| 黄果漫剧（私人） | private_huangguo_video | 1.2.1 | Taototo/venera-comic-sources | 1.0.0 | d9b5ffb2b84aa9934b017342543059a3b75e9e2d091b715d8a7f46668e404241 |
| 51吃瓜（私人） | private_51_video | 1.2.0 | Taototo/venera-comic-sources | 1.0.0 | 9654318585a04e1a082a0402f4c91e2deaca26727e6cc63294a67b86d256dae0 |
| 91porna（私人） | private_91porna_video | 1.2.0 | Taototo/venera-comic-sources | 1.0.0 | a15b6dd07059ac75bc05c9be967b9a61686454240d2ecbe65dd5fe58ff802b82 |
| 源力资源（私人） | private_yuanlib_video | 1.3.0 | Taototo/venera-comic-sources | 1.0.0 | 3be0ebd33018e66548a0915c62d6f98921ae7d90c334d7b419ec71aa3ab3a976 |
| Komiic | Komiic | 1.0.5 | VComic-org/venera-comic-source | 1.0.0 | 2d2e4aa8068355d265e57d3c4a15ecf1bc9def27ff38cc73b47d0d837658f5ec |
| 爱看漫 | ikmmh | 1.0.8 | VComic-org/venera-comic-source | 1.0.0 | 23ca88878d53f69b783171e968547f6d9fd62521802d1c599721d9dcbae0ce96 |
| 漫蛙吧 | manwaba | 1.0.3 | VComic-org/venera-comic-source | 1.4.0 | 4f44efdf0626623305e02a8fde4af4cedda906795f26ce3cc3c139c756a0c001 |
| Lanraragi | lanraragi | 1.2.0 | VComic-org/venera-comic-source | 1.4.0 | 3db60747709d72eff454d96bef13e907397ebd2a7e4e9cebd3279bddc5d768cd |
| 漫客栈 | mkzhan | 1.0.1 | YHQY-Dev/venera-sources | 1.0.0 | 4b8e222d01cd8860a57da0a1e08a894b1f2f1ebb362864ba1db50eb94baae87f |
| 漫本 | manben | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 53b79cb16a07e05e1910f77c03a55ef62e4417b4ca94e9b757fcfdce82475dc3 |
| 动漫屋 | dm5 | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | e948c055697747d401ba2177e95d4c341cbd22d894411e85661011a7fd527543 |
| X漫画 | xmanhua | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 89fb57efa92d994006310f45e8aec0a4ea6253bb273a0d58b612d568a2b0e1b2 |
| 漫画看 | mhkan | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | b7cae7695bd43aa034ce3a050e686550d7ae50c4fe359a5ac4ab354430714849 |
| 漫画皮 | manhuapi | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 9ca6d84bf82e3ca03415cd0e05739767d11d32476527833d3048f54b876076c5 |
| 看漫画 | kanman | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 42ff5a70afda843fa9cc2cd12d8223dc6da3594b811fa7c4a0459794887c907f |
| 包子漫画 | baozi | 1.1.7 | YHQY-Dev/venera-sources | 1.0.0 | 1d16542756f3bbaa4f699fbf55996239c3842a3c188b05e72b8045c6fd95d650 |
| 如漫画 | rumanhua | 1.1.0 | YHQY-Dev/venera-sources | 1.4.0 | 066120d2cf429efa904c7dc241e793e0ea16108e4bfc6ff482eadf50f7e45c3b |
| 布卡漫画 | bukamh | 1.0.0 | YHQY-Dev/venera-sources | 1.4.0 | 32402780e73a061ea0c60431fd8ca3ad0b9a24ea61c1d7d81891d7133fdb0b78 |
| 次元漫画 | cycomic | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 942f29bd9a6834d7a7d9f7a5a115b3ff1164f0990828f4eb9c2358ed354303d7 |
| 包子漫画 | baozi | 1.1.9 | YongkeDet/venera-configs | 1.5.0 | 9ad7272a59dd26ea7f59e471ef140a63acbbdd16bcdcf694615e2c9201794816 |
| NoyManga | noymanga | 1.1.3 | casthan321/Venera-community-URL | 1.6.0 | feffe371db3a294e17202041e2da0b0b021f1a0f810c3eaf55e79ab847cf0fde |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.2 | cattoldme/venera-configs | 1.2.1 | a3f346b5569d945c4953ef32dd017735ddf81ecc0b0e5929cb79de69ea59e848 |
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
| 嗶哩漫畫 | bilimanga | 1.2.0 | meaninglesslyy/venera-config | 1.6.0 | e21b7984e309e0a1b730d737da914834ce15908b59c45c0d4d2be2627cecbbe2 |
| 如漫画 | rumanhua | 1.0.0 | meaninglesslyy/venera-config | 1.6.0 | 017847c6901f8e491c28e6cb7b3da2a3475e6512b88374ecd41b7922dcca38a7 |
| 嗶哩漫畫 | bilimanga | 1.1.0 | n3114576614-cell/N_venera_source | 1.6.0 | 0be6c0a5f3bcee229990c90e820f2ec410443d4e0d00dbf01a00155e1eb292f5 |
| 动漫屋 | dm5 | 7.0.0 | n3114576614-cell/N_venera_source | 1.6.0 | 23908d87f455e3d09025ea450a2bf82eafb5a0ae0b9c3eceddb03207abbc7241 |
| 飞翔漫画 | ffppt | 1.0.1 | n3114576614-cell/N_venera_source | 1.0.0 | b86d41220d3fcfafd0799ac569332adfc0978c5ac0509a08cf077b6f51853d3e |
| zero搬运网 | zerobyw33 | 1.1.0 | n3114576614-cell/N_venera_source | 1.6.0 | 534e23e43bb016cecb0988e11651da049f39e2a4d1ffa7cd4498c8695fde95ca |
| 看漫画 | kanman | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 34eec9fe833cc3184b0737a37b0fe3865c539d8c231fc76ccb55f29e3eefe9f1 |
| 漫客栈 | mkzhan | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | c57fecd89d364edab67b412a5c864f0599570775d8eb1e4eb7a3de0889302f26 |
| 诊断与日志上传 | venera_diag | 2.1.2 | token1008/venera-cn-64bit | 1.0.0 | 6435b641481be521f8bb7c8195f53955bba7cc86122cd7ee325059c31ca0eb3d |
| カドコミ（官方） | comic_walker | 1.0.2 | token1008/venera-cn-64bit | 1.6.0 | acbf044b6ef6131037fd518874d2de5b7d66891db1e8ec5ac9837901f0d7d561 |
| GoDa漫画（官方） | goda | 1.2.3 | token1008/venera-cn-64bit | 1.4.0 | 5e4bfcb321979017ea4a6b59aaf44e67a45f32417f14c690f2102e65cba1439f |
| 少年ジャンプ＋（官方） | shonen_jump_plus | 1.1.2 | token1008/venera-cn-64bit | 1.2.1 | ddd6421d3095f04d22a3cf82256a52bf68792b8241b8513d912c4718fd6b42c4 |
| 漫蛙 | manwa | 1.0.0 | xiaoxingmian/venera-configs | 1.4.0 | f40d0f77dedeb8a0a4c38dbb59d18686cb7b422bc41aae5bdc79ac88f0d20b81 |
| hitomi.la | hitomi | 2.0.0 | xiaoxingmian/venera-configs | 1.4.6 | 8b5bc5f7dbd3c9e20f944fb328bc2a6256ceee0a234cf2fda11f4631611332c2 |
| 拷贝漫画 | copy_manga | 1.6.1 | xiaoxingmian/venera-configs | 1.6.0 | e0a8d25704b83e3efcf757c0f6b80449bb2404bab5852ec5948a8ded44a99eea |
| Komga | komga | 1.0.1 | yelongyue197-svg/venera-sources | 1.4.0 | 7d11fbc62c254a8f2909fc3bdac3762f704b83e03de046fe3d9e209632a73768 |
| Komiic | Komiic | 1.0.6 | yelongyue197-svg/venera-sources | 1.0.0 | 31f0b78a6bf090743763f072e4d5b1a2e20666813ea5b1ef40b079b5f3519f09 |
| Mangabz | mangabz | 1.0.0 | zakkida/venera-sources | 1.6.0 | 8ec53577ba8e5a865589884f3d2be53ec108aff1085610124e66444e943c91b3 |
| 拷贝漫画(多账号) | copy_manga | 1.4.4 | zakkida/venera-sources | 1.6.0 | e2ba75d47461ea726af9fdd933e779ce8ec1bb24cd40ddca033650d6026b99a2 |
| Komiic | Komiic | 1.1.0 | zakkida/venera-sources | 1.0.0 | c01d8348577ca1fa83264d29071af81eca2346aaa026da42ab55c6dce0c32955 |
| 漫画1234 | mh1234 | 1.0.1 | zhimouzhou/venera-manga-sources | 1.4.0 | b1f34a65e13d15d6ac3c03836c1b7e0a8f68c40bb6a490d7155d31c134035bab |

## 索引获取问题

- `137syh/venera-syh`：漫画源07：HTTP Error 404: Not Found；漫画源08：暂不执行非 GitHub 原始地址；漫画源09：HTTP Error 404: Not Found；漫画源10：HTTP Error 404: Not Found
- `2869893488/ikmmh-venera-source`：HTTP Error 404: Not Found
- `6678670jsy/venera-sources`：HTTP Error 404: Not Found
- `893954529/venera-configs`：HTTP Error 404: Not Found
- `Bandcomic/RESTful-venera-source`：HTTP Error 404: Not Found
- `BlueStarOne/bluestarone.github.io`：HTTP Error 404: Not Found
- `ChenTeea/veneresource`：HTTP Error 404: Not Found
- `F22822/22822`：HTTP Error 404: Not Found
- `LuckyLxi/Sources`：HTTP Error 404: Not Found
- `NinEvandesu/venera-configs`：HTTP Error 404: Not Found
- `QWWWQ-MIX/venera-sources`：HTTP Error 409: Conflict
- `cheyou001/venera-sources`：HTTP Error 404: Not Found
- `kuiti/manga-source-index`：HTTP Error 404: Not Found
- `l233333333/venera-sources`：HTTP Error 404: Not Found
- `nukbodu/mh-configs`：Komiic：HTTP Error 404: Not Found；Picacg：HTTP Error 404: Not Found；nhentai：HTTP Error 404: Not Found；紳士漫畫：HTTP Error 404: Not Found；禁漫天堂：HTTP Error 404: Not Found
- `snowf14k3/venera-komiic-multi`：Komiic 多账号：暂不执行非 GitHub 原始地址
- `yelongyue197-svg/venera-sources`：动漫啦：暂不执行非 GitHub 原始地址；妙趣漫画：暂不执行非 GitHub 原始地址；六漫画：暂不执行非 GitHub 原始地址；动漫屋：暂不执行非 GitHub 原始地址
- `zetriumyx/noyacg-source-venera`：HTTP Error 404: Not Found

## 新仓库线索

仅列本次 GitHub 更新排序搜索第一页的未登记仓库，尚未认定为漫画源，不代表全网穷尽。

- `laincat/vensrc`：Vensrc：VeneraX / Venera-Next 漫画源巡检、订阅与单一滚动 Release
- `Maxll51/EZVenera-Lite`：EZVenera 2026 Edition: Lightweight Venera Rewrite with Streamlined Plugin Runtime for Windows & Android
- `ikun5200/venera-prime-server`：
- `MQ9Reaper/venera-personal-sources`：
- `Kyosee/VeneraX`：A personal-use fork of the original Venera, maintained and enhanced to suit my own needs. ／ Fork自原版Venera，仅进行自用需求维护及增强。
- `w13630039663-bit/venera-miuix`：一款支持漫画阅读器（支持picacg 禁漫 nh ex和其他正常 混合）漫画和图库功能——采用Miuix风格重构的Venera。
- `amke79/venerastudios-site`：
- `yuyuyu529/venera`：Venera日语生肉源
- `CyrilPeng/Venera-Next`：VeneraNext 是一个跨平台漫画阅读器，支持本地漫画、WebDAV 漫画源、第三方网络漫画源，支持 Android、iOS、Windows、Linux、macOS 平台。
- `gallhall/venera-v`：venera-v：支持漫画和视频的开源阅读器，基于 venera，支持 Android、iOS、Windows、macOS、Linux。漫画源列表：github.com/gallhall/venerav-configs · 更新频道：t.me/VeneraV_Updates
- `CangShui/VenHM`：兼容Venera源的鸿蒙开源漫画阅读器
- `venerahome/venerahome.github.io`：Venera Hasanova · Imoti Premier · Property in Greece
- `Vulpes-venera/CS50p`：
- `1148891151a-ui/-veneranext-sources.json`：
- `Magic-Miku/venera-store`：
- `jnsingh01/venerabullstudios`：Venerabull Studios — a showcase of projects in development.
- `hgnbh/sw`：Venera 漫画源索引（59 个源）
- `rytzj2-spec/VeneraX-nagi`：
- `veneraproject/venera-node`：
- `yanyi05/venera-sources`：Personal JavaScript sources for VeneraNext
- `Gandum2077/venera-patrol-cli`：
- `XclusiveM/venera-nailart`：
- `Kerollos004/venera`：
- `nightcat3254/venera-sources`：Venera personal source fixes: Baozi domain migration and shared updates.
- `yuxuan965960/VeneraX-ios`：VeneraX - Flutter app
- `lwtor/venera-native`：Android 原生漫画阅读器，使用 Kotlin 与 Jetpack Compose 构建，兼容 Venera 漫画源生态。
- `KBPZSDP/Venera`：
- `Walter498/Venera-Max`：以 VeneraX 為基礎、按我們自己閱讀習慣深度改裝的漫畫閱讀器（栗子漫畫源優先）。加了什麼、修了什麼，全部寫在 README。
- `john-cpallc/venerable-grain`：
- `fave-eng/venera`：
- `FengHA223/venera-ios12`：
- `opaiopaio/Venera-Nas`：Venera 漫画阅读器 - SMB/NAS 定制版，支持访问NAS保存的漫画，支持将漫画下载到NAS存储中
- `a3169249487-sys/Venera-Next-ai-upscale-temp`：Experimental AI upscale build for Venera-Next
- `Venera-Works/Venera-Plus`：VeneraPlus 是一个跨平台漫画阅读器，支持本地漫画、网盘 漫画源、第三方网络漫画源
- `Gandum2077/venera-runtime`：A venera runtime that works in both Node and JSBox environments. 
- `SnowDreamXUE/venera-next-config`：转换venera-config漫画源配置文件格式为venera-next要求
- `cylendra-info/Venera`：
- `venera-tech-art/Dashboard`：
- `Venera-h/a-b_test`：Анализ A/B-теста нового экрана оплаты: SRM, бутстрап, сегменты
- `vetatina-hub/venera-bot`：
- `pastorig/Voskhod-2-y-Venera-7`：
- `roddup75/venera`：capacity
- `Vartak2/Project-Venera-14`：
- `Zicheng0326/my-venera-sources`：漫画源仓库
- `940440952/comic-sources`：双生态漫画源：Venera / VeneraNext / VeneraPlus JavaScript + Aidoku Rust/WASM；目前维护 manhuazhan.com。
- `venera-app/venera-prime`：A comic app,but prime
- `Venera0207/venera-bot`：
- `Venera0207/venera-portfolio`：
- `PrincessGods/venera`：
- `Venera-Works/Venera-Native-Prebuilts`：
- `venerahm/venerahm.github.io`：Website
- `rehansajeev5-gif/venerable-parfait-13a105`：
- `yashbhosale2403/web-venerability-scanner-`：
- `FDEAABH6/Venera`：VeneraNext 是一个跨平台漫画阅读器，支持本地漫画、WebDAV 漫画源、第三方网络漫画源，支持 Android、iOS、Windows、Linux、macOS 平台。
- `xiati007/venera-project`：
- `LiliaKhazieva/VeneraStore`：Интернет магазин украшений Venera
- `maplessovo/venera-configs`：
- `Teresian/VeneraL`：
- `NagasakiAno/VENERA_NEXT`：强大！可爱！自动化！一往无前！
- `tide23333-max/venera-photo-sources`：Personal VeneraNext photo source scripts and update catalog
- `MoYangking/venera_comic_js`：
- `kuhnliza35-ux/venera-mangadistrict`：
- `hamdahff44-arch/venerable-capybara-530077mentalhealth`：
- `aidar41k/venera-uzatuu`：
- `venerandahospital/ihms_online_ui_for_local_veneranda`：
- `shehabeldeen/venera-theme-guide`：Venera Salla theme guide — setup, home blocks, product data and support
- `ismoses62-svg/venerable-kitten-41cd16`：
- `novestudios-hq/Venera-Beauty-Center-SPA`：
- `fuluoydebende/venera-manga-sources`：Venera manga sources (fixed) - 33 sources + index.json, ready to import in Venera
- `fuluoydebende/venera-configs-fixed`：修复后的 Venera 漫画源：9 个源已修复域名/端点/图片拼接，版本号已在 index.json 同步。
- `VenerableHouse/VenerableWebsite`：Source code for the Venerable House website.
- `WEP-56/EZVenera`：Venera重写+简化版本，只提供windows、安卓包体，简化大量功能尤其是插件模块运行时，方便持续维护。／ 请勿提出超出EZVenera边界的需求，如果你真的需要，欢迎pr或自行fork
- `fuluoydebende/venera-hipmh-source`：Venera 漫画源 - 嬉皮漫畫 hipmh v1.0.2 (API 驱动修复版)
- `yuanshenmingri/venera_comic_source`：Legado ????(???? id72 ??,75 ?)
- `yuanshenmingri/venera-comick-sources`：Venera ???:Comick ??(69 ?)+ MangaDex v2.0
- `hlf2016/venera-config`：
- `haukuen/venera`：仅自用 ／ For personal use only
- `lizhenghe616/venera-baozi-source`：
- `ZhiLin-Sam/venera-sources`：Venera 源目录 ／ 一条订阅装齐 56 个源（镜像+去重），自带夹具驱动的解析回归测试台
- `Tobeinlovewith/veneranext-source`：
- `noelle-silva/Venera`：
- `hasanrakib42679-ctrl/venerable-valkyrie-3e891c`：
- `VenusUK/Ms.-Venera-s-English-Studio`：IE Support
- `bandcomic/RESTful-venera-source`：
- `lll152872/venera-lll`：venera 二次开发：无缝跨章阅读、书源隐藏、快捷搜索、追更检测优化、
