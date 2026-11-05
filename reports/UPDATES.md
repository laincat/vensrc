# 上游变更与待审阅候选

检查时间：2026-11-05T00:29:57.179728+00:00（UTC）。
检查 54 个已登记仓库；发现 284 个未审阅源码构建。

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
| 包子漫画 | baozi | 1.1.7 | ChopDream/venera-source-hub | 1.0.0 | 81214391b7fb95d8e632381d92f284e26939c4b465abed5a0cb324606564e1be |
| 禁漫天堂 | jm | 1.4.2 | ChopDream/venera-source-hub | 1.5.0 | 1b195b4ecd0bcbed61546d11761f6d0c8b027588564da7d28368f2f4645d5b16 |
| nhentai | nhentai | 1.1.2 | ChopDream/venera-source-hub | 1.0.0 | 9379d8441f42d06a7835cee6b21519ea8a951eb01c476402d00dce721ffeaec6 |
| MYCOMIC | mycomic | 1.1.2 | ChopDream/venera-source-hub | 1.4.6 | f35e2e7cb531f7591e81a5edf41ab6303880686f0009c7477f77154e9511f07f |
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
| 动漫屋 | dm5 | 0.2.0 | zhimouzhou/venera-manga-sources | 1.6.0 | 0adf399b0eab25937f07a9b6b23c044b7ebee8b75f1d30dcd55a1a8a4a5a400a |
| 咚漫 | dongman | 1.0.8 | LX7kM9/venera-configs | 1.6.0 | a4e34d9681a48022640c072842dc37ccb4099fd1f9c04d8ab51cc38ebfa57669 |
| 动漫啦 | dongman_la | 1.0.1 | n3114576614-cell/N_venera_source | 1.0.0 | f3599e84cdebd39aa3cf752e0b97b015ea673917314572cf52e567d81a12daba |
| 动漫啦 | dongman_la | 1.0.3 | Junkrat9527/venera-sources | 1.0.0 | 3da97ede8f94cce6127313d582a8dda391d7b74d04bbb125e95c246010ee5ac5 |
| 动漫啦 | dongmanla | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 15a8e8970bd8142accb161272c6491082b193d8ceaad393025877effe63cf009 |
| ehentai | ehentai | 1.2.1 | VComic-org/venera-comic-source | 1.5.3 | 1aa135bfdba24d66eaea1cbd6c66eb4d6b7a97d62ffc8ef8361f2ce5eff6038b |
| 飞翔漫画 | ffppt | 1.0.2 | Junkrat9527/venera-sources | 1.0.0 | 9073ad30b4cbfd080f35154607610450db6a76fc56f1c4f1fb263c5502488318 |
| 古风漫画 | gfmh | 1.3.1 | LX7kM9/venera-configs | 1.6.0 | 2b372bbc3dba44150a359b7475080d6ab6b70ec4f26bf143c1597c60e8619e0d |
| GoDa漫画 | goda | 1.2.4 | LX7kM9/venera-configs | 1.4.0 | d560801cd543d9cec07d1098b46f9992276cde9e904c5a8ff431a678a2f3415e |
| 瓜子漫画 | guazimanhua | 1.0.4 | n3114576614-cell/N_venera_source | 1.0.0 | b93ad63c5e0ac1a41c77ab95e7561f20718ad46228fb9b6b8fbb8196c3f56dc6 |
| 瓜子漫画 | guazimanhua | 1.0.4 | Junkrat9527/venera-sources | 1.0.0 | 3b47fd313cc99c887b6d2fca7d320b6df72f72e52c0b322fe74ff1f683c3c489 |
| 嬉皮漫畫 | hipmh | 1.0.6 | LX7kM9/venera-configs | 1.6.0 | 95a132f5468187e35cd9224cd0ae923ec544187a14a60d8bac376308218f2f1a |
| 爱看漫 | ikmmh | 3.0.1 | Junkrat9527/venera-sources | 1.0.0 | 78cc44bb2c9a69225a3446698005d3d33080dedb67ff9d9e7cc43052e14190f8 |
| 禁漫天堂 | jm | 1.4.3 | VComic-org/venera-comic-source | 1.5.0 | eb059a5ae6ad528bbcbfcfb2296a4b3945405bb5cab1faab326f1b374450d0b7 |
| 来漫画（分流） | laimanhua_split | 1.2.2 | Junkrat9527/venera-sources | 1.0.0 | ed9c0d8a088d31aa8b45d311a7280c35d4b971c728c74b9fe3eead94e08cbb9b |
| Lanraragi | lanraragi | 1.2.3 | LX7kM9/venera-configs | 1.4.0 | 55bc1f431f9e26af5a20a38cc26fc233595df10a00916ca519afc042f33ef8ad |
| 51漫画 | manga51 | 1.3.0 | Junkrat9527/venera-sources | 1.6.0 | edaebdf2b61473888cce47c9d2cf58cb0cfc49c6d2d2ae88bbba2314c851a82c |
| MangaDex | manga_dex | 1.9.4 | Junkrat9527/venera-sources | 1.4.0 | c1fda4f7542327ea9c35a485250b7f97ba51c65b831407a4f1474ee51728ae97 |
| Mangabz | mangabz | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 45ea62f02ef64fa0ad1f176fe125572b78d326060d06bf2964c7f8bc5dd63192 |
| Mangabz | mangabz | 0.2.0 | zhimouzhou/venera-manga-sources | 1.6.0 | ac1d497bfe0ba800b84ae3f5f5d4d0bf07dccd1174e8e24198cf5eadf00623b1 |
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
| 极速漫画 | one_kkk | 0.2.0 | zhimouzhou/venera-manga-sources | 1.6.0 | f71e0d2db4c2771915fd3916eefe1d73440f9cc2611829e300e9b920ff9bb569 |
| 腾讯动漫（正版） | qq_comic_official | 2.0.0 | LX7kM9/venera-configs | 1.6.0 | 98ce234683ae1141b9f3104e549da0c45391cad41dde0da10fddf4fe404f17fa |
| 腾讯动漫（正版） | qq_comic_official_v1 | 1.0.3 | n3114576614-cell/N_venera_source | 1.0.0 | fd53172968ebc576a69d8bda73b8e576589a28b469e84a46890692b93e1256b6 |
| Rawkuma | rawkuma | 1.1.3 | LX7kM9/venera-configs | 1.0.0 | f15ad92098c3d54c60436f33c3098febbae84bb1cef8a9eae855f5f990fd0f26 |
| 如漫画 | rumanhua | 2.4.1 | Junkrat9527/venera-sources | 1.0.0 | 93e982bd657cea4deedc0f9e785ea1321dff6e46eedb1cb9eb53200961e6f724 |
| SF漫画 | sfacg_manhua | 1.0.2 | LX7kM9/venera-configs | 1.6.0 | 5d9d9c36ea32e270f1aeaea09b69476d3c1cf78f9597d4e67889c660bf2fffa1 |
| 少年ジャンプ＋ | shonen_jump_plus | 1.3.1 | Junkrat9527/venera-sources | 1.2.1 | d7cc9e684b14239e3c921d8ce19da7db9343ccf7692093a7d048f21822130f6b |
| 腾讯动漫 | tencent_comics | 1.1.3 | casthan321/Venera-community-URL | 1.6.0 | e696aaf1b4fb36d0bc29591fc407854c89e43ff4280211233192eb66b45963ed |
| 图库漫画 | tuku_cc | 1.0.2 | LX7kM9/venera-configs | 1.4.0 | 59c79f140dd68c1e848473a17a5916ff52ef009e539cf8a1de94a1b29d4a1b26 |
| W漫画 | wmanhua | 1.0.2 | Junkrat9527/venera-sources | 1.4.0 | 6e60a7ec42164ec8b4bc3e8dad7fa4500fd43c6a1b65b20f021758f54cc476b5 |
| 野蛮漫画 | yemancomic | 1.3.8 | LX7kM9/venera-configs | 1.6.0 | 42b53d66e34198ec4d1cacb31808e9386ac0392e305016d87c98a703f608c25e |
| 优酷漫画 | ykmh | 1.1.0 | Junkrat9527/venera-sources | 1.4.0 | effa08b818616a670bfe5ff5e1abc42e5da925fe767dec86c84d9ea51016e861 |
| 优酷漫画 | ykmh | 1.0.1 | zhimouzhou/venera-manga-sources | 1.4.0 | d0eb522a8fe55d322cca2c27c1a8f7e27dd0bf5b24fe80eab9032dead0f8bde6 |
| 优酷漫画 (修复版) | ykmh | 1.0.6 | yelongyue197-svg/venera-sources | 1.4.0 | f0b1979721bf81094772b4575c2cb1a6ebc774a58d4b3f3fa301a36b5a7d641f |
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
| 咚漫漫画 | dongman | 1.0.0 | cattoldme/venera-configs | 1.6.0 | db829f439e27dc33c3ae3303646fa780efe7d2c37ee9c777df1f041d7631485d |
| 嬉皮漫画 | hipmh | 1.0.1 | AXmishell/venera-configs | 1.0.0 | 57f23ebd47143defe73117ed24b986bb99ad1904938ec42725c15440b139a0cd |
| 如漫画 | rumanhua | 1.0.3 | caitlin-cheng-ccc/venera-configs | 1.4.0 | 78f7fba17c15bbbf10bb52b4f46d5df2222e3cfef18abfee19c750dad8348800 |
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
| Fantia（个人订阅） | fantia_personal | 0.1.1 | MQ9Reaper/venera-personal-sources | 1.6.0 | 1f29d6abb87816caf5fad3a7c206e02aa9073a14dc2befa751b0d3de8ac7b167 |
| FANBOX（个人订阅） | fanbox_personal | 0.1.1 | MQ9Reaper/venera-personal-sources | 1.6.0 | 1556d3a02fbf77ded1c46d68044d16c2a0bbf7b0d893f76d990a189d29f57ffe |
| 漫蛙漫画 | manwa_routes | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 8b7a65e5a520003d9ce6885848f882ab6b9f50a286bb50109835a5cb5303d5ba |
| 如漫画 | rumanhua_com | 2.1.2 | Ra1nbo-w/mhy-v | 1.16.0 | 3a383515749605a38609e8b5260e1f9aaf6aefd4f2dde22a38c07d9e606b93f2 |
| Komiic漫画 | komiic_cc | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 0d627b63113b1e0ca2c4180df732fd15f9b50f919919e8efaf7159ba99355514 |
| 漫画屋 | mhua5 | 2.3.3 | Ra1nbo-w/mhy-v | 1.0.0 | 63b165b1065239b07d94c3a83750824fde8a53bc1c2afc9b0af5f0bfd0195b6c |
| 拷贝漫画 | copy_web_routes | 2.3.2 | Ra1nbo-w/mhy-v | 1.0.0 | 7a472063e163a7a33f888554c83e1043c3a400641ee9e43d04e6de64b4933b22 |
| 瓜子漫画 | guazimanhua | 1.0.1 | Ra1nbo-w/mhy-v | 1.16.0 | 4f94b6801f09db7534de9f98c650e686ff6ff7dfbf5658a81a1b6d38b2ff2d1b |
| MYCOMIC | mycomic | 2.3.3 | Ra1nbo-w/mhy-v | 1.16.0 | 763e7973a8ae82fe2af031bcf24b51796435dd840d45791b87ae2798e38ef826 |
| 包子漫画 | baozi | 2.3.3 | Ra1nbo-w/mhy-v | 1.18.0 | 445daa4d7caace438f7e1a1f9477b8e39fffb8f87b70c969a78aa63930410114 |
| 漫自由 | mheee_catalog | 2.3.4 | Ra1nbo-w/mhy-v | 1.0.0 | ff7d63b45ec92bfd7e78565bfa29becff2c94da2a040d6e18cab9ae235b62dc9 |
| 再漫画 | zaimanhua | 1.0.3 | Taototo/venera-comic-sources | 1.0.0 | 91ba937d50da1717136e9bf9e67111b58fb08e0e52222791e3bab49989ee0275 |
| 漫画人 | manhuaren | 1.0.1 | Taototo/venera-comic-sources | 1.6.0 | 2fbb6236652b0ea8776cd46d1b44e4ffc57d7812576550ddfe824ec8688ec42d |
| 禁漫天堂（18+） | jm | 1.4.1 | Taototo/venera-comic-sources | 1.5.0 | 4d0b8897c919c41ef2d44a55c9960ba931c46cc936fc808858e8dccf818cb39b |
| 魅影画廊 | private_myhl | 1.0.2 | Taototo/venera-comic-sources | 1.2.0 | 898fd65f78c53deaa6f7850b58ec499d76c4d55a7c9024208e35263c134b4eea |
| 大人漫画（18+） | private_drmh3 | 1.0.1 | Taototo/venera-comic-sources | 1.0.0 | 8f19da0af3a241cd5bad72970aeefdd792c2c846e6709c285c5044c178b0f9e0 |
| 成色漫画（18+） | private_csmanhua | 1.0.2 | Taototo/venera-comic-sources | 1.0.0 | 2fcb55afdb4ec089109efa40560cbeea1e97b213ad42487a491d0f676616c205 |
| 开心看漫画（18+） | private_kxmanhua | 1.0.4 | Taototo/venera-comic-sources | 1.0.0 | d25285c25f90f3fe4c482c41b4ae23790c11e3af7afc70a12d2a303aa00f2efa |
| 韩漫屋（18+） | private_hmanwu | 1.1.2 | Taototo/venera-comic-sources | 1.0.0 | 9d0be11ce76a7027a8a1e990b2159dc9d534acfb98778e05d447555ed9288d48 |
| Komiic | Komiic | 1.0.5 | VComic-org/venera-comic-source | 1.0.0 | 2d2e4aa8068355d265e57d3c4a15ecf1bc9def27ff38cc73b47d0d837658f5ec |
| 爱看漫 | ikmmh | 1.0.8 | VComic-org/venera-comic-source | 1.0.0 | 23ca88878d53f69b783171e968547f6d9fd62521802d1c599721d9dcbae0ce96 |
| 漫蛙吧 | manwaba | 1.0.3 | VComic-org/venera-comic-source | 1.4.0 | 4f44efdf0626623305e02a8fde4af4cedda906795f26ce3cc3c139c756a0c001 |
| Lanraragi | lanraragi | 1.2.0 | VComic-org/venera-comic-source | 1.4.0 | 3db60747709d72eff454d96bef13e907397ebd2a7e4e9cebd3279bddc5d768cd |
| 栗子漫画 | lizimh | 2.33.36 | Walter498/Walter | 1.2.2 | 593287454d650ba00f0605437bf9c3875ac44a1001922acb4075dab719490f08 |
| 漫客栈 | mkzhan | 1.0.1 | hgnbh/sw | 1.0.0 | 4b8e222d01cd8860a57da0a1e08a894b1f2f1ebb362864ba1db50eb94baae87f |
| 漫本 | manben | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 53b79cb16a07e05e1910f77c03a55ef62e4417b4ca94e9b757fcfdce82475dc3 |
| 动漫屋 | dm5 | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | e948c055697747d401ba2177e95d4c341cbd22d894411e85661011a7fd527543 |
| X漫画 | xmanhua | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 89fb57efa92d994006310f45e8aec0a4ea6253bb273a0d58b612d568a2b0e1b2 |
| 漫画看 | mhkan | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | b7cae7695bd43aa034ce3a050e686550d7ae50c4fe359a5ac4ab354430714849 |
| 漫画皮 | manhuapi | 1.0.0 | YHQY-Dev/venera-sources | 1.0.0 | 9ca6d84bf82e3ca03415cd0e05739767d11d32476527833d3048f54b876076c5 |
| 看漫画 | kanman | 1.0.0 | hgnbh/sw | 1.0.0 | 42ff5a70afda843fa9cc2cd12d8223dc6da3594b811fa7c4a0459794887c907f |
| 包子漫画 | baozi | 1.1.7 | YHQY-Dev/venera-sources | 1.0.0 | 1d16542756f3bbaa4f699fbf55996239c3842a3c188b05e72b8045c6fd95d650 |
| 如漫画 | rumanhua | 1.1.0 | YHQY-Dev/venera-sources | 1.4.0 | 066120d2cf429efa904c7dc241e793e0ea16108e4bfc6ff482eadf50f7e45c3b |
| 布卡漫画 | bukamh | 1.0.0 | hgnbh/sw | 1.4.0 | 32402780e73a061ea0c60431fd8ca3ad0b9a24ea61c1d7d81891d7133fdb0b78 |
| 次元漫画 | cycomic | 1.0.0 | hgnbh/sw | 1.0.0 | 942f29bd9a6834d7a7d9f7a5a115b3ff1164f0990828f4eb9c2358ed354303d7 |
| 包子漫画 | baozi | 1.1.9 | YongkeDet/venera-configs | 1.5.0 | 9ad7272a59dd26ea7f59e471ef140a63acbbdd16bcdcf694615e2c9201794816 |
| 拷贝漫画 | copy_manga | 1.4.4 | YongkeDet/venera-configs | 1.6.0 | b1a444db46b30b74c5c2852e12e09ce61cf7f68276ec15d5d21e74bd9080a134 |
| 香香腐宅 | boylove | 1.0.0 | YongkeDet/venera-configs | 1.4.0 | ba8f2403ab0f5b42d91950371476b8bd02528dbe38521954475702094fad0b65 |
| ehentai | ehentai | 1.2.0 | YongkeDet/venera-configs | 1.5.3 | ea4bcfde4f7574141806426a3a842a30378e045b14c58d265458489a29f8ea43 |
| Lanraragi | lanraragi | 1.2.0 | YongkeDet/venera-configs | 1.4.0 | 5552689d5e7169ad86d8347a136aa38a6c86744c1afc730aa5ca61ed8e86efb5 |
| 百合会 | baihehui | 1.0.0 | YongkeDet/venera-configs | 1.4.0 | 4b00bf339136b3ed70390b3887c84069eb2e8ac748a564127515d9809f6fd7fc |
| NoyManga | noymanga | 1.1.3 | hgnbh/sw | 1.6.0 | feffe371db3a294e17202041e2da0b0b021f1a0f810c3eaf55e79ab847cf0fde |
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
| Pixiv | pixiv_token | 0.3.35 | gallhall/venerav-configs | 2.0.0 | 81b538dcdbbdf438d0b06e0855d3cf9fcf792ff7447873e52e7073f7d8f7dcb8 |
| Hanime1.me | hanime1 | 2.4.0 | gallhall/venerav-configs | 2.0.0 | 75628a9e8392a0630b713cf443cccfd1c16347ff303420ec7f32702f5e8beafb |
| Hanime1 H漫画 | hanime1_comics | 1.2.1 | gallhall/venerav-configs | 1.0.0 | 729836e4e65b01161f5ba1f9998fdc1630d08dd6407e480f063d578cfa7ea7c7 |
| 包子漫画 | baozi | 1.1.8 | handahao666-boop/venera_comic_source | 1.0.0 | db40b64506f7002420eb5d6e23b3f7829a0fe3c6c36afff77991ec1097d78f25 |
| W漫画 | wmanhua | 1.0.3 | handahao666-boop/venera_comic_source | 1.4.0 | 113b94d281f16f53877f75c18df909c2e0b3e3233746cb99ac7b3976e6cc0398 |
| LINE WEBTOON | webtoons_zh_hant | 1.0.0 | hgnbh/sw | 1.6.0 | d4bc4b0641af7533e2a7ca1bd358c099ce2844a57721f256b9e8c42a3664bfb6 |
| 栗子漫画 | lizimh | 1.2.4 | handahao666-boop/venera_comic_source | 1.2.2 | 51450326c6bff18d8fde7744aff9d822e2341908c4863fd7c48af28ce42f9ac7 |
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
| 51漫画 | manga51 | 1.1.0 | meaninglesslyy/venera-config | 1.6.0 | 5a505f80319071bddf6f0de2b1bc2f32d9153bcb7c5d11679e7c1fe88ab3221e |
| 嗶哩漫畫 | bilimanga | 1.2.0 | meaninglesslyy/venera-config | 1.6.0 | e21b7984e309e0a1b730d737da914834ce15908b59c45c0d4d2be2627cecbbe2 |
| 如漫画 | rumanhua | 1.0.0 | meaninglesslyy/venera-config | 1.6.0 | 017847c6901f8e491c28e6cb7b3da2a3475e6512b88374ecd41b7922dcca38a7 |
| zero搬运网 | zerobyw33 | 1.2.0 | meaninglesslyy/venera-config | 1.6.0 | 17b9a4ae12100e367b54c116d5ee9810a9520eacbf7ab46cf930fe6485dd2fe7 |
| 鸟鸟韩漫 | nnhanman | 1.1.1 | meaninglesslyy/venera-config | 1.6.0 | 41b72c230bf6336f67cd99002beca4032be3023cb43ab982288cad29574554a1 |
| 嗶哩漫畫 | bilimanga | 1.1.0 | n3114576614-cell/N_venera_source | 1.6.0 | 0be6c0a5f3bcee229990c90e820f2ec410443d4e0d00dbf01a00155e1eb292f5 |
| 动漫屋 | dm5 | 7.0.0 | n3114576614-cell/N_venera_source | 1.6.0 | 23908d87f455e3d09025ea450a2bf82eafb5a0ae0b9c3eceddb03207abbc7241 |
| zero搬运网 | zerobyw33 | 1.1.0 | n3114576614-cell/N_venera_source | 1.6.0 | 534e23e43bb016cecb0988e11651da049f39e2a4d1ffa7cd4498c8695fde95ca |
| 极速漫画 | jisu_1kkk | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 2a2874b992ab5d632c5e68bbac2b044f022ebe05649c7be5a8d5580af4bc7e79 |
| 看漫画 | kanman | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 34eec9fe833cc3184b0737a37b0fe3865c539d8c231fc76ccb55f29e3eefe9f1 |
| 动漫啦 | dongmanla | 1.0.1 | token1008/venera-cn-64bit | 1.0.0 | 62b7d99ee12997f0e3f4e244f626d95e83d2a3060b8ad4eb1212a37213378800 |
| 漫客栈 | mkzhan | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | c57fecd89d364edab67b412a5c864f0599570775d8eb1e4eb7a3de0889302f26 |
| 腾讯漫画 | acqq | 1.0.0 | token1008/venera-cn-64bit | 1.0.0 | 6c155c4db1d0ebb1d51c626a7f201048dddd02b81f0315b33b2982305b0c73e2 |
| 诊断与日志上传 | venera_diag | 2.1.2 | token1008/venera-cn-64bit | 1.0.0 | 6435b641481be521f8bb7c8195f53955bba7cc86122cd7ee325059c31ca0eb3d |
| カドコミ | comic_walker | 1.0.2 | token1008/venera-cn-64bit | 1.6.0 | acbf044b6ef6131037fd518874d2de5b7d66891db1e8ec5ac9837901f0d7d561 |
| GoDa漫画 | goda | 1.2.3 | token1008/venera-cn-64bit | 1.4.0 | 5e4bfcb321979017ea4a6b59aaf44e67a45f32417f14c690f2102e65cba1439f |
| 少年ジャンプ＋ | shonen_jump_plus | 1.1.2 | token1008/venera-cn-64bit | 1.2.1 | ddd6421d3095f04d22a3cf82256a52bf68792b8241b8513d912c4718fd6b42c4 |
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
| Mangabz | mangabz | 1.0.0 | zakkida/venera-sources | 1.6.0 | 8ec53577ba8e5a865589884f3d2be53ec108aff1085610124e66444e943c91b3 |
| 拷贝漫画 | copy_manga | 1.4.4 | zakkida/venera-sources | 1.6.0 | fcb90412e0d16323340337e815267bb02c6ca0491c00cbfabe55241ed67029ac |
| 拷贝漫画M | copy_manga | 1.4.4 | zakkida/venera-sources | 1.6.0 | e2ba75d47461ea726af9fdd933e779ce8ec1bb24cd40ddca033650d6026b99a2 |
| Komiic | Komiic | 1.1.0 | zakkida/venera-sources | 1.0.0 | c01d8348577ca1fa83264d29071af81eca2346aaa026da42ab55c6dce0c32955 |
| hitomi.la | hitomi | 1.1.3 | zakkida/venera-sources | 1.4.6 | 7aeef0e996adbf5a8ee49bd8079f8c9d1fedbde3b9205782647212734f94f7a1 |
| 优酷漫画 | ykmh | 1.0.2 | zakkida/venera-sources | 1.4.0 | f862f6aaac364564740ea77672fa248811d94c9176a6b1c73a42387bc9430ffe |
| 漫画1234 | mh1234 | 1.0.1 | zakkida/venera-sources | 1.4.0 | 913f1b26d976ddf2d67bbd6f56585453120fa9af90e9aa4b3bea50d1fa746538 |
| Komga | komga | 1.0.1 | zakkida/venera-sources | 1.4.0 | 550a18cf941e8f63904b0248ebc39329d124f8b8e259f7cc925873d89930bb79 |
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
- `Taototo/venera-comic-sources`：漫小肆（18+）：HTTP Error 404: Not Found；包子漫画：HTTP Error 404: Not Found；鸟鸟韩漫（18+）：HTTP Error 404: Not Found
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
- `Taototo/ManComic`：A Flutter comic reader app based on Venera
- `Ciaodar/VenerableKnowledge`：a minecraft mod with a potion effect.
- `laincat/VeneraCat-Core`：Shared Go core for the Nekularity (iOS) and Nekophage (desktop) clients: Venera-compatible comic sources, video plugins, .venera backups. GPL-3.0
- `jnsingh01/venerabulllife`：Venerabull Life — public website.
- `Maxll51/EZVenera-Lite`：EZVenera 2026 Edition: Lightweight Venera Rewrite with Streamlined Plugin Runtime for Windows & Android
- `venerahome/venerahome.github.io`：Venera Hasanova · Imoti Premier · Property in Greece
- `jnsingh01/venerabullstudios`：Venerabull Studios — a showcase of projects in development.
- `jnsingh01/venerabullinteractive`：Venerabull Interactive — public website.
- `LeylaKhojasteh/venera-jewelry-store`：Venera — Persian RTL jewellery storefront with Next.js, PostgreSQL, Prisma and Three.js
- `venera-app/venera-prime`：A comic app,but prime
- `staciepomar-spec/venera-glass-build`：CI build of venera v1.6.3 with a Pure-spec liquid glass bottom bar
- `gallhall/venera-v`：venera-v：支持漫画和视频的开源阅读器，基于 venera，支持 Android、iOS、Windows、macOS、Linux。漫画源列表：github.com/gallhall/venerav-configs · 更新频道：t.me/VeneraV_Updates
- `Venera-Works/Venera-Native-Prebuilts`：
- `Vulpes-venera/CS50p`：
- `Venera-Works/Venera-Plus`：VeneraPlus 是一个跨平台漫画阅读器，支持本地漫画、网盘 漫画源、第三方网络漫画源
- `yuyuyu529/venera`：Venera日语生肉源
- `Walter498/Venera-Max`：以 VeneraX 為基礎、按我們自己閱讀習慣深度改裝的漫畫閱讀器（栗子漫畫源優先）。加了什麼、修了什麼，全部寫在 README。
- `ryanp-cloud/venera-ai`：
- `venera-tropnikova/Alexs-Amazing-Garage-play`：Test play build of Alex's Amazing Garage (dist only). Source stays private.
- `w13630039663-bit/venera-miuix`：一款支持漫画阅读器（支持picacg 禁漫 nh ex和其他正常 混合）漫画和图库功能——采用Miuix风格重构的Venera。
- `hp5588/venera-sources`：借助 Codex 开发与维护的 VeneraNext 个人漫画源分发清单：包子、拷贝、漫蛙。使用前请阅读说明与隐私注意事项。
- `maplessovo/venera-configs`：
- `CyrilPeng/Venera-Next`：VeneraNext 是一个跨平台漫画阅读器，支持本地漫画、WebDAV 漫画源、第三方网络漫画源，支持 Android、iOS、Windows、Linux、macOS 平台。
- `venera-kuz/uchebnaya-praktika`：
- `markiianklymchuk-hash/kingdoms-of-venera`：
- `3176289965f-ai/my-venera-sources`：
- `CangShui/VenHM`：兼容Venera源的鸿蒙开源漫画阅读器
- `lwtor/venera-native`：Android 原生漫画阅读器，使用 Kotlin 与 Jetpack Compose 构建，兼容 Venera 漫画源生态。
- `vonhezhou/mansou`：漫搜：支持多源聚合搜索与下载的自托管漫画工具，兼容 Venera 漫画源插件，适用于 NAS / VPS 部署。
- `quluogucheng-source/VeneraNext-8-Sources`：
- `Manjit53/venerable-dasik-a5e0ff`：
- `Kyosee/VeneraX`：A personal-use fork of the original Venera, maintained and enhanced to suit my own needs. ／ Fork自原版Venera，仅进行自用需求维护及增强。
- `huangjun7hb/venera-next-sources`：
- `Venera-d1/heart-python`：Draw a heart with Python Turtle
- `wnzmb/venera-configs-wujiajun`：Venera 漫画源：nhentai / e-hentai / hitomi，指向自建 Cloudflare Worker 反代
- `tide23333-max/venera-photo-sources`：Personal VeneraNext photo source scripts and update catalog
- `mentalshinobi/venera`：
- `normalice8/VeneraNext-comic-sources`：
- `haukuen/venera`：仅自用 ／ For personal use only
- `Gandum2077/venera-patrol-cli`：
- `noorlightazaz-gif/https-venerable-sunshine-623dd3.netlify.app-`：
- `Ryuzxy/Analisis-Veneralbility-WebGoat-Ilkom-Unej`：
- `Venera0207/venera-portfolio`：
- `morpuct/venera-sources-hub`：Venera 漫画源合订索引：汇总官方与社区仓库共 105 个源，每条指向原作者仓库原文，用于逐个比对效果
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
- `ZhiLin-Sam/venera-sources`：Venera 源目录 ／ 一条订阅装齐 60 个源（镜像+去重），自带夹具驱动的解析回归测试台
- `fave-eng/venera`：
- `matloporokjl-tech/https-venerable-malasada-5a1196.netlify.app-`：Google Keep clone (HTML and CSS)
- `lll152872/venera-lll`：venera 二次开发：无缝跨章阅读、书源隐藏、快捷搜索、追更检测优化、
- `opaiopaio/Venera-Nas`：Venera 漫画阅读器 - SMB/NAS 定制版，支持访问NAS保存的漫画，支持将漫画下载到NAS存储中
- `Meloon-dr/venera-sources`：
- `ikun5200/venera-prime-server`：
- `1148891151a-ui/-veneranext-sources.json`：
- `rytzj2-spec/VeneraX-nagi`：
- `yanyi05/venera-sources`：Personal JavaScript sources for VeneraNext
- `XclusiveM/venera-nailart`：
- `nightcat3254/venera-sources`：Venera personal source fixes: Baozi domain migration and shared updates.
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
- `Zicheng0326/my-venera-sources`：漫画源仓库
- `940440952/comic-sources`：双生态漫画源：Venera / VeneraNext / VeneraPlus JavaScript + Aidoku Rust/WASM；目前维护 manhuazhan.com。
- `Venera0207/venera-bot`：
