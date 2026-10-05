# armors QA：亂音譯／應義譯卻音譯

> 角色：QA｜只讀 `csv/dat-armors-*.csv`（與 `reviews-*.md` 同源）｜**未改譯文**
> 依據：playbook Part A.3／A.4＋STYLE「先整名、普通描述義譯、禁半翻／片假名混中文」
> 腳本：`l10n/working/scratch/qa_armor_transliteration.py`
> 全量命中表：`qa-transliteration-hits.tsv`

## 結論

- 五部位合計 **68730** 列；自動標記 **1397** 次（約 **1377** 列至少一類）。
- 現況主殘：`truncate` **154**（系列名過短／未定稿未套用）、`need_semantic` **1242**。
- 已定稿路徑：`series-dict`（禁洗白）＋`apply_armor_series_dict.py`（只套用非待查）；合作／魔物／義譯例：初音未來、極龍、白蛇、電氣石、守護者。
- **仍 `qa_issues`**：待查詞幹未清零前勿 Gate4 回寫本體；修完重跑本腳本。

## 各部位規模

| 部位 | CSV 列數 | 標記次數 |
|---|---:|---:|
| head | 14594 | 328 |
| body | 13462 | 232 |
| arms | 13452 | 149 |
| waist | 13708 | 328 |
| legs | 13514 | 360 |

## 問題類型計數

| 類型 | severity | 合計 | 說明 |
|---|---|---:|---|
| `truncate` | blocking | 154 | 譯文過短、系列名疑似丟失 |
| `need_semantic` | high | 1242 | 普通英詞應義譯卻無義素 |
| `long_phon` | high | 1 | 過長漢字音譯串 |

### 分部位 × 類型

| 部位 | truncate | empty | bad_phon_known | need_semantic | long_phon | kata_mix | half_latin |
|---|---:|---:|---:|---:|---:|---:|---:|
| head | 22 | 0 | 0 | 306 | 0 | 0 | 0 |
| body | 8 | 0 | 0 | 224 | 0 | 0 | 0 |
| arms | 16 | 0 | 0 | 133 | 0 | 0 | 0 |
| waist | 11 | 0 | 0 | 316 | 1 | 0 | 0 |
| legs | 97 | 0 | 0 | 263 | 0 | 0 | 0 |

## 高頻問題詞幹（need_semantic／bad_phon_known／long_phon，Top 50）

| 次數 | 原文詞幹（去部位／級別） |
|---:|---|
| 18 | Dragon Slayer Armor |
| 12 | Knight King BM Blue |
| 12 | Knight King BM Red |
| 12 | Knight King BM Black |
| 12 | Knight King BM White |
| 12 | Light |
| 8 | Issen 胴当て Red |
| 8 | Steno Elytra ー Blue |
| 8 | Steno Elytra ー Red |
| 7 | Knight King GN Blue |
| 7 | Knight King GN Red |
| 7 | Knight King GN Black |
| 7 | Knight King GN White |
| 7 | Hero King Earring BM Gold |
| 7 | Hero King Earring BM Black |
| 7 | Hero King Earring BM White |
| 7 | Hero King Earring BM Red |
| 7 | Issen 胴当て Blue |
| 7 | Issen 胴当て Yellow |
| 7 | Issen 胴当て Black |
| 7 | Cannon Will Water |
| 7 | Axel Will Water |
| 6 | Hero King Earring GN Gold |
| 6 | Hero King Earring GN Black |
| 6 | Hero King Earring GN White |
| 6 | Hero King Earring GN Red |
| 6 | of Hidden Infidelity Blade |
| 6 | of Hidden Infidelity Bow |
| 6 | Light Suit |
| 6 | Demon Lord |
| 6 | Dragon Slayer Armor Gauntlets |
| 6 | Red 備ノ Waistband |
| 6 | Dragon Slayer Armor Waistband |
| 6 | Light Feet |
| 6 | Dragon Slayer Armor Toenail |
| 5 | Demon Lord Horn |
| 5 | Royal |
| 5 | Garnet |
| 5 | Amethyst |
| 5 | Coral |
| 5 | Quartz |
| 5 | Emerald |
| 5 | Pearl |
| 5 | Ruby |
| 5 | Sapphire |
| 5 | Hisui |
| 5 | Onyx |
| 4 | マー Gear Blue |
| 4 | Blue Ice Emperor |
| 4 | White Ice Emperor |

## 代表性樣本（每部位 × 類型最多 15）

### head

#### `truncate`（blocking）・本部位 22 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 70 | Glyph Crown | 格冠 | 疑似截斷／系列名丟失 |
| 296 | Butterfly Kabuto | 蝶兜 | 疑似截斷／系列名丟失 |
| 912 | Weiss Brain | 白腦 | 疑似截斷／系列名丟失 |
| 913 | Weiss Soul | 白魂 | 疑似截斷／系列名丟失 |
| 1291 | Inari 覇 Kabuto | 覇兜 | 疑似截斷／系列名丟失 |
| 2215 | Demon Lord Horn・魁 | 魁角 | 疑似截斷／系列名丟失 |
| 2241 | Flame Crown | 炎冠 | 疑似截斷／系列名丟失 |
| 2380 | True Shadow Headguard・魁 | 魁護額 | 疑似截斷／系列名丟失 |
| 2611 | Rolling Flow Headguard・魁 | 魁護額 | 疑似截斷／系列名丟失 |
| 2714 | Ahaba ー Piercing | 耳飾 | 疑似截斷／系列名丟失 |
| 2821 | Wind Glare | 風睨 | 疑似截斷／系列名丟失 |
| 2822 | Wind Snarl | 風咆 | 疑似截斷／系列名丟失 |
| 2866 | Valued Word Headguard・魁 | 魁護額 | 疑似截斷／系列名丟失 |
| 2953 | Rolling Sky Headguard・魁 | 魁護額 | 疑似截斷／系列名丟失 |
| 9942 | Kurai Kabuto | 暗兜 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 306 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 58 | Shadow Shinobi Mask | 夏阿德歐帽子 | 英詞「shadow」應義譯（期望：影\|闇） |
| 113 | Shinobi Mask・Sky | 夏伊恩歐帽子 | 英詞「sky」應義譯（期望：天\|空） |
| 230 | Guild Knight Feather | 獵團頭兜 | 英詞「knight」應義譯（期望：騎士） |
| 431 | Golden Tie SP White | 格歐爾艾頭兜【ＳＰ】・白 | 英詞「golden」應義譯（期望：金） |
| 432 | Golden Tie SP Purple | 格歐爾艾頭兜【ＳＰ】・紫 | 英詞「golden」應義譯（期望：金） |
| 433 | Golden Tie SP Green | 格歐爾艾頭兜【ＳＰ】・緑 | 英詞「golden」應義譯（期望：金） |
| 466 | Hot Red Star Mask | 赫歐特帽子 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 467 | Hot Blue Star Mask | 赫歐特帽子 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 468 | Hot Black Star Mask | 赫歐特帽子 | 英詞「black」應義譯（期望：黑\|墨） |
| 469 | Hot White Star Mask | 赫歐特帽子 | 英詞「white」應義譯（期望：白） |
| 470 | Hot Red Stellar Mask | 赫歐特帽子 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 474 | Cool Red Star Mask | 克歐爾帽子 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 475 | Cool Blue Star Mask | 克歐爾帽子 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 476 | Cool Black Star Mask | 克歐爾帽子 | 英詞「black」應義譯（期望：黑\|墨） |
| 477 | Cool White Star Mask | 克歐爾帽子 | 英詞「white」應義譯（期望：白） |

### body

#### `truncate`（blocking）・本部位 8 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 67 | Dragon Skin | 龍皮 | 疑似截斷／系列名丟失 |
| 1955 | True Shadow Haori・魁 | 魁羽織 | 疑似截斷／系列名丟失 |
| 2381 | Valued Word Haori・魁 | 魁羽織 | 疑似截斷／系列名丟失 |
| 9365 | Mark.06F Suit | 套裝 | 疑似截斷／系列名丟失 |
| 9371 | Mark.06F Vest | 背心 | 疑似截斷／系列名丟失 |
| 10802 | Dragon D Skin | 龍皮 | 疑似截斷／系列名丟失 |
| 11560 | Dragon SC Skin | 龍皮 | 疑似截斷／系列名丟失 |
| 11562 | Dragon GD Skin | 龍皮 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 224 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 313 | Golden Haori・魁 | 魁羽織 | 英詞「golden」應義譯（期望：金） |
| 329 | Golden Haori・魁 | 魁羽織 | 英詞「golden」應義譯（期望：金） |
| 430 | Star Festival Shozoku・Summer [Red 】 | 斯阿爾艾裝束・赤 | 英詞「star」應義譯（期望：星） |
| 431 | Star Festival Shozoku・Summer [Blue 】 | 斯阿爾艾裝束・青 | 英詞「star」應義譯（期望：星） |
| 432 | Star Festival Shozoku・Summer [Black 】 | 斯阿爾艾裝束・黑 | 英詞「star」應義譯（期望：星） |
| 433 | Star Festival Shozoku・Summer [White 】 | 斯阿爾艾裝束・白 | 英詞「star」應義譯（期望：星） |
| 438 | Star Festival Shozoku・織 [Red 】 | 織裝束・赤 | 英詞「star」應義譯（期望：星） |
| 439 | Star Festival Shozoku・織 [Blue 】 | 織裝束・青 | 英詞「star」應義譯（期望：星） |
| 440 | Star Festival Shozoku・織 [Black 】 | 織裝束・黑 | 英詞「star」應義譯（期望：星） |
| 441 | Star Festival Shozoku・織 [White 】 | 織裝束・白 | 英詞「star」應義譯（期望：星） |
| 515 | Kushala バダル SP Red | 鋼龍鎧甲【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 516 | Kushala バダル SP Yellow | 鋼龍鎧甲【ＳＰ】 | 英詞「yellow」應義譯（期望：黄\|黃） |
| 517 | Kushala バダル SP Green | 鋼龍鎧甲【ＳＰ】 | 英詞「green」應義譯（期望：緑\|綠\|翠） |
| 521 | Kirin ケープ SP Red | 麒麟鎧甲【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 522 | Kirin ケープ SP Purple | 麒麟鎧甲【ＳＰ】 | 英詞「purple」應義譯（期望：紫） |

### arms

#### `truncate`（blocking）・本部位 16 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 64 | Dragon クロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 65 | Dragon フィスト | 龍拳 | 疑似截斷／系列名丟失 |
| 221 | Puppeteer ノ Kote | 籠手 | 疑似截斷／系列名丟失 |
| 1658 | Welkin Sleeve・魁 | 魁袖 | 疑似截斷／系列名丟失 |
| 1938 | Okami [Sleeves 】 | 狼袖 | 疑似截斷／系列名丟失 |
| 1942 | True Shadow Sleeve・魁 | 魁袖 | 疑似截斷／系列名丟失 |
| 2368 | Valued Word Sleeve・魁 | 魁袖 | 疑似截斷／系列名丟失 |
| 8170 | Fog [Sleeve 】 | 霧袖 | 疑似截斷／系列名丟失 |
| 9356 | Mark.06F Arms | 護腕 | 疑似截斷／系列名丟失 |
| 9362 | Mark.06F Guard | 臂甲 | 疑似截斷／系列名丟失 |
| 10791 | Dragon Dクロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 10792 | Dragon Dフィスト | 龍拳 | 疑似截斷／系列名丟失 |
| 11549 | Dragon SCクロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 11550 | Dragon SCフィスト | 龍拳 | 疑似截斷／系列名丟失 |
| 11551 | Dragon GDクロウ | 龍爪 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 133 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 425 | Star Festival Gauntlets・Summer [Red 】 | 斯阿爾艾手甲・赤 | 英詞「star」應義譯（期望：星） |
| 426 | Star Festival Gauntlets・Summer [Blue 】 | 斯阿爾艾手甲・青 | 英詞「star」應義譯（期望：星） |
| 427 | Star Festival Gauntlets・Summer [Black 】 | 斯阿爾艾手甲・黑 | 英詞「star」應義譯（期望：星） |
| 428 | Star Festival Gauntlets・Summer [White 】 | 斯阿爾艾手甲・白 | 英詞「star」應義譯（期望：星） |
| 433 | Star Festival Gauntlets・織 [Red 】 | 織手甲・赤 | 英詞「star」應義譯（期望：星） |
| 434 | Star Festival Gauntlets・織 [Blue 】 | 織手甲・青 | 英詞「star」應義譯（期望：星） |
| 435 | Star Festival Gauntlets・織 [Black 】 | 織手甲・黑 | 英詞「star」應義譯（期望：星） |
| 436 | Star Festival Gauntlets・織 [White 】 | 織手甲・白 | 英詞「star」應義譯（期望：星） |
| 666 | Demon Lord Kote | 德艾姆歐籠手 | 英詞「demon」應義譯（期望：鬼\|魔） |
| 1034 | Death Stench アルム SP White | 阿魯穆護腕【ＳＰ】 | 英詞「white」應義譯（期望：白） |
| 1035 | Death Stench アルム SP Red | 阿魯穆護腕【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 1036 | Death Stench アルム SP Blue | 阿魯穆護腕【ＳＰ】 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 1656 | Blue Sky Sleeve・魁 | 魁袖・青 | 英詞「sky」應義譯（期望：天\|空） |
| 1729 | True 空 Kote・Black | 空籠手・黑 | 英詞「true」應義譯（期望：真） |
| 1730 | True 空F Kote・Black | 空籠手【Ｆ】・黑 | 英詞「true」應義譯（期望：真） |

### waist

#### `truncate`（blocking）・本部位 11 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 216 | Golden Obi | 金帶 | 疑似截斷／系列名丟失 |
| 217 | Puppeteer ノ Obi | 帶 | 疑似截斷／系列名丟失 |
| 309 | Puppeteer ノ Obi・魁 | 魁帶 | 疑似截斷／系列名丟失 |
| 325 | Puppeteer ノ Obi・魁 | 魁帶 | 疑似截斷／系列名丟失 |
| 1817 | Welkin Obi・魁 | 魁帶 | 疑似截斷／系列名丟失 |
| 2101 | True Shadow Obi・魁 | 魁帶 | 疑似截斷／系列名丟失 |
| 2526 | Valued Word Obi・魁 | 魁帶 | 疑似截斷／系列名丟失 |
| 8317 | Mist 【 Obi 】 | 霧帶 | 疑似截斷／系列名丟失 |
| 8324 | Fog 【 Obi 】 | 霧帶 | 疑似截斷／系列名丟失 |
| 9510 | Mark.06F Coil | 腰甲 | 疑似截斷／系列名丟失 |
| 9516 | Mark.06F Coat | 腰衣 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 316 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 2 | Skin Light Belt | 斯伊恩伊腰帶 | 英詞「light」應義譯（期望：光\|明） |
| 219 | White Fatalis テイル | 黑龍腰甲 | 英詞「white」應義譯（期望：白） |
| 247 | White Cat テイル | 猫腰甲 | 英詞「white」應義譯（期望：白） |
| 248 | Black Cat テイル | 猫腰甲 | 英詞「black」應義譯（期望：黑\|墨） |
| 249 | Gold Cat テイル | 猫腰甲 | 英詞「gold」應義譯（期望：金） |
| 257 | Red Cat Fテイル | 猫腰甲 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 432 | Star Festival Obi・Summer 【 Red 】 | 斯阿爾艾帶・赤 | 英詞「star」應義譯（期望：星） |
| 433 | Star Festival Obi・Summer 【 Blue 】 | 斯阿爾艾帶・青 | 英詞「star」應義譯（期望：星） |
| 434 | Star Festival Obi・Summer 【 Black 】 | 斯阿爾艾帶・黑 | 英詞「star」應義譯（期望：星） |
| 435 | Star Festival Obi・Summer 【 White 】 | 斯阿爾艾帶・白 | 英詞「star」應義譯（期望：星） |
| 440 | Star Festival Obi・織【 Red 】 | 織帶・赤 | 英詞「star」應義譯（期望：星） |
| 441 | Star Festival Obi・織【 Blue 】 | 織帶・青 | 英詞「star」應義譯（期望：星） |
| 442 | Star Festival Obi・織【 Black 】 | 織帶・黑 | 英詞「star」應義譯（期望：星） |
| 443 | Star Festival Obi・織【 White 】 | 織帶・白 | 英詞「star」應義譯（期望：星） |
| 538 | Kushala アンダ SP Red | 鋼龍腰甲【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |

#### `long_phon`（high）・本部位 1 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 681 | Hypno ルータウエスト | 魯塔烏艾斯托腰甲 | 長音譯串 run=6 dens=0.75 |

### legs

#### `truncate`（blocking）・本部位 97 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 48 | Gen ーツ Feet | 源足 | 疑似截斷／系列名丟失 |
| 60 | 凛【 Hakama 】 | 凛袴 | 疑似截斷／系列名丟失 |
| 61 | 艶【 Hakama 】 | 艶袴 | 疑似截斷／系列名丟失 |
| 64 | Dragon Feet | 龍足 | 疑似截斷／系列名丟失 |
| 216 | Golden Hakama | 金袴 | 疑似截斷／系列名丟失 |
| 217 | Puppeteer ノ Tabi | 足袋 | 疑似截斷／系列名丟失 |
| 260 | Strength Leg | 力腿 | 疑似截斷／系列名丟失 |
| 293 | Death Stench Heel | 死臭踵 | 疑似截斷／系列名丟失 |
| 311 | Golden Hakama・魁 | 魁袴 | 疑似截斷／系列名丟失 |
| 327 | Golden Hakama・魁 | 魁袴 | 疑似截斷／系列名丟失 |
| 721 | Weiss Heel | 白踵 | 疑似截斷／系列名丟失 |
| 830 | Kagura・覇【 Hakama 】 | 覇袴 | 疑似截斷／系列名丟失 |
| 832 | Kamiza・覇【 Hakama 】 | 覇袴 | 疑似截斷／系列名丟失 |
| 1490 | Rising Leg B | 昇腿 | 疑似截斷／系列名丟失 |
| 1492 | Rising Boots B | 昇靴 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 263 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 167 | Guild Guard タイツ Crimson | 獵團護腿 | 英詞「crimson」應義譯（期望：深紅\|紅\|緋\|緋紅\|霞） |
| 169 | Guild Guard タイツ Crimson | 獵團護腿 | 英詞「crimson」應義譯（期望：深紅\|紅\|緋\|緋紅\|霞） |
| 224 | Guild Knight タイツ | 獵團護腿 | 英詞「knight」應義譯（期望：騎士） |
| 228 | Guild Guard タイツ Green | 獵團護腿 | 英詞「green」應義譯（期望：緑\|綠\|翠） |
| 230 | Guild Guard タイツ Green | 獵團護腿 | 英詞「green」應義譯（期望：緑\|綠\|翠） |
| 311 | Golden Hakama・魁 | 魁袴 | 英詞「golden」應義譯（期望：金） |
| 327 | Golden Hakama・魁 | 魁袴 | 英詞「golden」應義譯（期望：金） |
| 428 | Star Festival の Tabi・Summer 【 Red 】 | の足袋・赤 | 英詞「star」應義譯（期望：星） |
| 429 | Star Festival の Tabi・Summer 【 Blue 】 | の足袋・青 | 英詞「star」應義譯（期望：星） |
| 430 | Star Festival の Tabi・Summer 【 Black 】 | の足袋・黑 | 英詞「star」應義譯（期望：星） |
| 431 | Star Festival の Tabi・Summer 【 White 】 | の足袋・白 | 英詞「star」應義譯（期望：星） |
| 436 | Star Festival の Tabi・織【 Red 】 | の織足袋・赤 | 英詞「star」應義譯（期望：星） |
| 437 | Star Festival の Tabi・織【 Blue 】 | の織足袋・青 | 英詞「star」應義譯（期望：星） |
| 438 | Star Festival の Tabi・織【 Black 】 | の織足袋・黑 | 英詞「star」應義譯（期望：星） |
| 439 | Star Festival の Tabi・織【 White 】 | の織足袋・白 | 英詞「star」應義譯（期望：星） |

## 人工抽樣複核（與 reviews 目視一致）

| 原文 | 現譯（抽樣） | 狀態 |
|---|---|---|
| White Snake Sleeve D | 白蛇袖 | 已定稿義譯 |
| Tourmaline Guard | 電氣石臂甲 | 已定稿義譯 |
| Miku Arms / Snow Miku Arms | 初音未來護腕／雪初音護腕 | 合作定稿 |
| Guardian Helm／Mask | 守護者頭兜／帽子 | 定稿（Helm 缺字→頭兜） |
| Io Arms | 伊歐護腕 | 已補（原 truncate） |
| 殘 pending 專名（Zakka 等） | 見 series-dict 空 zh | 續 batch 查證後套用 |

## Fixer 建議順序

1. **blocking**：`truncate` — 對 `series-dict` 空 zh／待查詞幹查證後寫入再套用。
2. **high**：`need_semantic` — 普通英詞／寶石／色詞整名義譯；禁音節灌表。
3. 只套用已定稿（`apply_armor_series_dict.load_finalized_series`）；禁字典洗白。
4. 修完重跑本腳本；人審前不回寫本體。

