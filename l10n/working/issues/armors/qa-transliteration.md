# armors QA：亂音譯／應義譯卻音譯

> 角色：QA｜只讀 `csv/dat-armors-*.csv`（與 `reviews-*.md` 同源）｜**未改譯文**
> 依據：playbook Part A.3／A.4＋STYLE「先整名、普通描述義譯、禁半翻／片假名混中文」
> 腳本：`l10n/working/scratch/qa_armor_transliteration.py`
> 全量命中表：`qa-transliteration-hits.tsv`

## 結論

- 五部位合計 **68730** 列；自動標記 **318** 次（約 **318** 列至少一類）。
- 現況主殘：`truncate` **121**（系列名過短／未定稿未套用）、`need_semantic` **196**。
- 已定稿路徑：`series-dict`（禁洗白）＋`apply_armor_series_dict.py`（只套用非待查）；合作／魔物／義譯例：初音未來、極龍、白蛇、電氣石、守護者。
- **仍 `qa_issues`**：待查詞幹未清零前勿 Gate4 回寫本體；修完重跑本腳本。

## 各部位規模

| 部位 | CSV 列數 | 標記次數 |
|---|---:|---:|
| head | 14594 | 51 |
| body | 13462 | 36 |
| arms | 13452 | 32 |
| waist | 13708 | 59 |
| legs | 13514 | 140 |

## 問題類型計數

| 類型 | severity | 合計 | 說明 |
|---|---|---:|---|
| `truncate` | blocking | 121 | 譯文過短、系列名疑似丟失 |
| `need_semantic` | high | 196 | 普通英詞應義譯卻無義素 |
| `long_phon` | high | 1 | 過長漢字音譯串 |

### 分部位 × 類型

| 部位 | truncate | empty | bad_phon_known | need_semantic | long_phon | kata_mix | half_latin |
|---|---:|---:|---:|---:|---:|---:|---:|
| head | 15 | 0 | 0 | 36 | 0 | 0 | 0 |
| body | 4 | 0 | 0 | 32 | 0 | 0 | 0 |
| arms | 10 | 0 | 0 | 22 | 0 | 0 | 0 |
| waist | 3 | 0 | 0 | 55 | 1 | 0 | 0 |
| legs | 89 | 0 | 0 | 51 | 0 | 0 | 0 |

## 高頻問題詞幹（need_semantic／bad_phon_known／long_phon，Top 50）

| 次數 | 原文詞幹（去部位／級別） |
|---:|---|
| 6 | Red 備ノ Waistband |
| 4 | Rampage |
| 4 | Blaze |
| 3 | Guild Bard |
| 2 | Burning Cliff |
| 2 | Shadow |
| 2 | Scholar |
| 2 | Rolling Sky |
| 2 | Mizuha 丸 Obi Blue |
| 2 | Mizuha 丸 Obi Red |
| 2 | Mizuha 丸 Obi Yellow |
| 2 | Toyotama 丸 Obi Blue |
| 2 | Toyotama 丸 Obi Red |
| 2 | Toyotama 丸 Obi Yellow |
| 2 | Burning Cliff て |
| 2 | Crimson Cliff て |
| 2 | PVタイツ Red |
| 2 | PVタイツ Blue |
| 2 | PVタイツ Purple |
| 1 | Shadow Shinobi |
| 1 | Guild Knight Feather |
| 1 | Golden White |
| 1 | Golden Purple |
| 1 | Golden Green |
| 1 | Hot Blue Star |
| 1 | Cool Blue Star |
| 1 | Sky Blue Star |
| 1 | Sky Wht Stellar |
| 1 | Sky Brown Masque |
| 1 | Sky Pale Masque |
| 1 | Fog Hachigane |
| 1 | King Beetle Vertex |
| 1 | Guild Bard Lobos |
| 1 | Scholar Hood |
| 1 | Sunset Glow Kensei |
| 1 | Demonclad Horn |
| 1 | Crushing Fog Hachigane |
| 1 | Valued Word Headguard |
| 1 | Noon Glow Headguard |
| 1 | Rolling Sky Headguard |
| 1 | of Hidden Infidelity |
| 1 | Mizuha 帽子 Blue |
| 1 | Mizuha 帽子 Red |
| 1 | Mizuha 帽子 Yellow |
| 1 | Toyotama 帽子 Blue |
| 1 | Toyotama 帽子 Red |
| 1 | Toyotama 帽子 Yellow |
| 1 | Comrada White Red |
| 1 | Comrada White Blue |
| 1 | Comrada White Yellow |

## 代表性樣本（每部位 × 類型最多 15）

### head

#### `truncate`（blocking）・本部位 15 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 296 | Butterfly Kabuto | 蝶兜 | 疑似截斷／系列名丟失 |
| 841 | Demon Lord Horn | 魔王角 | 疑似截斷／系列名丟失 |
| 912 | Weiss Brain | 白腦 | 疑似截斷／系列名丟失 |
| 913 | Weiss Soul | 白魂 | 疑似截斷／系列名丟失 |
| 2241 | Flame Crown | 炎冠 | 疑似截斷／系列名丟失 |
| 2821 | Wind Glare | 風睨 | 疑似截斷／系列名丟失 |
| 2822 | Wind Snarl | 風咆 | 疑似截斷／系列名丟失 |
| 2897 | Demon Lord Horn・Extreme | 魔王角 | 疑似截斷／系列名丟失 |
| 9942 | Kurai Kabuto | 暗兜 | 疑似截斷／系列名丟失 |
| 9948 | Kurai Kabuto | 暗兜 | 疑似截斷／系列名丟失 |
| 11600 | Thunder D Kabuto | 雷兜 | 疑似截斷／系列名丟失 |
| 11710 | Demon Lord Horn D | 魔王角 | 疑似截斷／系列名丟失 |
| 13822 | Box Blue D Festa | 青箱祭 | 疑似截斷／系列名丟失 |
| 13823 | Box Red D Festa | 赤箱祭 | 疑似截斷／系列名丟失 |
| 14582 | Kut-Ku D Festa | 怪鳥祭 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 36 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 58 | Shadow Shinobi Mask | 夏阿德歐帽子 | 英詞「shadow」應義譯（期望：影\|闇） |
| 230 | Guild Knight Feather | 獵團頭兜 | 英詞「knight」應義譯（期望：騎士） |
| 431 | Golden Tie SP White | 格歐爾艾頭兜【ＳＰ】・白 | 英詞「golden」應義譯（期望：金） |
| 432 | Golden Tie SP Purple | 格歐爾艾頭兜【ＳＰ】・紫 | 英詞「golden」應義譯（期望：金） |
| 433 | Golden Tie SP Green | 格歐爾艾頭兜【ＳＰ】・緑 | 英詞「golden」應義譯（期望：金） |
| 467 | Hot Blue Star Mask | 熱帽子 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 475 | Cool Blue Star Mask | 涼帽子 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 483 | Sky Blue Star Mask | 天空帽子 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 489 | Sky Wht Stellar Mask | 斯艾爾阿帽子 | 英詞「sky」應義譯（期望：天\|空） |
| 537 | Sky Brown Masque | 斯歐沃面罩 | 英詞「sky」應義譯（期望：天\|空） |
| 539 | Sky Pale Masque | 斯阿爾艾面罩 | 英詞「sky」應義譯（期望：天\|空） |
| 8916 | Fog FY Hachigane | 芙歐格鉢金 | 英詞「fog」應義譯（期望：霧） |
| 11706 | King Beetle D Vertex | 克伊恩艾頭頂 | 英詞「king」應義譯（期望：王） |
| 12480 | Rampage D Helm | 爾阿姆阿頭兜 | 英詞「rampage」應義譯（期望：狂暴\|暴） |
| 12481 | Blaze D Helm | 布阿茲艾頭兜 | 英詞「blaze」應義譯（期望：烈焔\|焰\|焔\|炎） |

### body

#### `truncate`（blocking）・本部位 4 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 67 | Dragon Skin | 龍皮 | 疑似截斷／系列名丟失 |
| 10802 | Dragon D Skin | 龍皮 | 疑似截斷／系列名丟失 |
| 11560 | Dragon SC Skin | 龍皮 | 疑似截斷／系列名丟失 |
| 11562 | Dragon GD Skin | 龍皮 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 32 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 430 | Star Festival Shozoku・Summer [Red 】 | 斯阿爾艾裝束・赤 | 英詞「star」應義譯（期望：星） |
| 431 | Star Festival Shozoku・Summer [Blue 】 | 斯阿爾艾裝束・青 | 英詞「star」應義譯（期望：星） |
| 432 | Star Festival Shozoku・Summer [Black 】 | 斯阿爾艾裝束・黑 | 英詞「star」應義譯（期望：星） |
| 433 | Star Festival Shozoku・Summer [White 】 | 斯阿爾艾裝束・白 | 英詞「star」應義譯（期望：星） |
| 438 | Star Festival Shozoku・織 [Red 】 | 織裝束・赤 | 英詞「star」應義譯（期望：星） |
| 439 | Star Festival Shozoku・織 [Blue 】 | 織裝束・青 | 英詞「star」應義譯（期望：星） |
| 440 | Star Festival Shozoku・織 [Black 】 | 織裝束・黑 | 英詞「star」應義譯（期望：星） |
| 441 | Star Festival Shozoku・織 [White 】 | 織裝束・白 | 英詞「star」應義譯（期望：星） |
| 4648 | True 空HS胴着・Black | 空胴着鎧甲・黑 | 英詞「true」應義譯（期望：真） |
| 4649 | True 空GS胴着・Black | 空胴着鎧甲・黑 | 英詞「true」應義譯（期望：真） |
| 4650 | True 空GP胴着・Black | 空胴着鎧甲・黑 | 英詞「true」應義譯（期望：真） |
| 4664 | True 空HS胴着・Tea | 空胴着鎧甲・茶 | 英詞「true」應義譯（期望：真） |
| 4665 | True 空GS胴着・Tea | 空胴着鎧甲・茶 | 英詞「true」應義譯（期望：真） |
| 4666 | True 空GP胴着・Tea | 空胴着鎧甲・茶 | 英詞「true」應義譯（期望：真） |
| 4680 | True 空HS胴着・White | 空胴着鎧甲・白 | 英詞「true」應義譯（期望：真） |

### arms

#### `truncate`（blocking）・本部位 10 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 64 | Dragon クロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 65 | Dragon フィスト | 龍拳 | 疑似截斷／系列名丟失 |
| 1938 | Okami [Sleeves 】 | 狼袖 | 疑似截斷／系列名丟失 |
| 8170 | Fog [Sleeve 】 | 霧袖 | 疑似截斷／系列名丟失 |
| 10791 | Dragon Dクロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 10792 | Dragon Dフィスト | 龍拳 | 疑似截斷／系列名丟失 |
| 11549 | Dragon SCクロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 11550 | Dragon SCフィスト | 龍拳 | 疑似截斷／系列名丟失 |
| 11551 | Dragon GDクロウ | 龍爪 | 疑似截斷／系列名丟失 |
| 11552 | Dragon GDフィスト | 龍拳 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 22 次

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
| 8172 | Fog FY [Sleeve 】 | 芙歐格袖 | 英詞「fog」應義譯（期望：霧） |
| 10782 | King Beetle D Brachia | 克伊恩艾臂甲 | 英詞「king」應義譯（期望：王） |
| 10785 | Demon Tale Kote D | 德艾姆歐籠手 | 英詞「demon」應義譯（期望：鬼\|魔） |
| 11526 | Rampage D Arms | 爾阿姆阿護腕 | 英詞「rampage」應義譯（期望：狂暴\|暴） |
| 11527 | Blaze D Arms | 布阿茲艾護腕 | 英詞「blaze」應義譯（期望：烈焔\|焰\|焔\|炎） |
| 11536 | Guild Bard C Arms | 獵團護腕 | 英詞「bard」應義譯（期望：吟遊\|詩人\|詩） |
| 11537 | Scholar C Claws | 施歐爾阿爪 | 英詞「scholar」應義譯（期望：學者\|学士\|學） |

### waist

#### `truncate`（blocking）・本部位 3 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 216 | Golden Obi | 金帶 | 疑似截斷／系列名丟失 |
| 8317 | Mist 【 Obi 】 | 霧帶 | 疑似截斷／系列名丟失 |
| 8324 | Fog 【 Obi 】 | 霧帶 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 55 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 2 | Skin Light Belt | 斯伊恩伊腰帶 | 英詞「light」應義譯（期望：光\|明） |
| 432 | Star Festival Obi・Summer 【 Red 】 | 斯阿爾艾帶・赤 | 英詞「star」應義譯（期望：星） |
| 433 | Star Festival Obi・Summer 【 Blue 】 | 斯阿爾艾帶・青 | 英詞「star」應義譯（期望：星） |
| 434 | Star Festival Obi・Summer 【 Black 】 | 斯阿爾艾帶・黑 | 英詞「star」應義譯（期望：星） |
| 435 | Star Festival Obi・Summer 【 White 】 | 斯阿爾艾帶・白 | 英詞「star」應義譯（期望：星） |
| 440 | Star Festival Obi・織【 Red 】 | 織帶・赤 | 英詞「star」應義譯（期望：星） |
| 441 | Star Festival Obi・織【 Blue 】 | 織帶・青 | 英詞「star」應義譯（期望：星） |
| 442 | Star Festival Obi・織【 Black 】 | 織帶・黑 | 英詞「star」應義譯（期望：星） |
| 443 | Star Festival Obi・織【 White 】 | 織帶・白 | 英詞「star」應義譯（期望：星） |
| 731 | True・Hypnoc S Mask | 特烏斯歐腰甲【Ｓ】 | 英詞「true」應義譯（期望：真） |
| 780 | Mizuha 【丸 Obi 】 SP Blue | 水羽腰甲【ＳＰ】 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 781 | Mizuha 【丸 Obi 】 SP Red | 水羽腰甲【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 782 | Mizuha 【丸 Obi 】 SP Yellow | 水羽腰甲【ＳＰ】 | 英詞「yellow」應義譯（期望：黄\|黃） |
| 783 | Toyotama 【丸 Obi 】 SP Blue | 豐玉腰甲【ＳＰ】 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 784 | Toyotama 【丸 Obi 】 SP Red | 豐玉腰甲【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |

#### `long_phon`（high）・本部位 1 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 681 | Hypno ルータウエスト | 魯塔烏艾斯托腰甲 | 長音譯串 run=6 dens=0.75 |

### legs

#### `truncate`（blocking）・本部位 89 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 48 | Gen ーツ Feet | 源足 | 疑似截斷／系列名丟失 |
| 60 | 凛【 Hakama 】 | 凛袴 | 疑似截斷／系列名丟失 |
| 61 | 艶【 Hakama 】 | 艶袴 | 疑似截斷／系列名丟失 |
| 64 | Dragon Feet | 龍足 | 疑似截斷／系列名丟失 |
| 172 | 凛・覇【 Hakama 】 | 凛袴 | 疑似截斷／系列名丟失 |
| 173 | 艶・覇【 Hakama 】 | 艶袴 | 疑似截斷／系列名丟失 |
| 216 | Golden Hakama | 金袴 | 疑似截斷／系列名丟失 |
| 260 | Strength Leg | 力腿 | 疑似截斷／系列名丟失 |
| 293 | Death Stench Heel | 死臭踵 | 疑似截斷／系列名丟失 |
| 721 | Weiss Heel | 白踵 | 疑似截斷／系列名丟失 |
| 1490 | Rising Leg B | 昇腿 | 疑似截斷／系列名丟失 |
| 1492 | Rising Boots B | 昇靴 | 疑似截斷／系列名丟失 |
| 1498 | Rising Leg Y | 昇腿 | 疑似截斷／系列名丟失 |
| 1500 | Rising Boots Y | 昇靴 | 疑似截斷／系列名丟失 |
| 1832 | Noon Glow Hakama | 午暉袴 | 疑似截斷／系列名丟失 |

#### `need_semantic`（high）・本部位 51 次

| index | 原文 | 譯文 | 註 |
|---|---|---|---|
| 428 | Star Festival の Tabi・Summer 【 Red 】 | 斯阿爾艾足袋・赤 | 英詞「star」應義譯（期望：星） |
| 429 | Star Festival の Tabi・Summer 【 Blue 】 | 斯阿爾艾足袋・青 | 英詞「star」應義譯（期望：星） |
| 430 | Star Festival の Tabi・Summer 【 Black 】 | 斯阿爾艾足袋・黑 | 英詞「star」應義譯（期望：星） |
| 431 | Star Festival の Tabi・Summer 【 White 】 | 斯阿爾艾足袋・白 | 英詞「star」應義譯（期望：星） |
| 436 | Star Festival の Tabi・織【 Red 】 | 織足袋・赤 | 英詞「star」應義譯（期望：星） |
| 437 | Star Festival の Tabi・織【 Blue 】 | 織足袋・青 | 英詞「star」應義譯（期望：星） |
| 438 | Star Festival の Tabi・織【 Black 】 | 織足袋・黑 | 英詞「star」應義譯（期望：星） |
| 439 | Star Festival の Tabi・織【 White 】 | 織足袋・白 | 英詞「star」應義譯（期望：星） |
| 809 | PVタイツ SP Red | 塔伊茨護腿【ＳＰ】 | 英詞「red」應義譯（期望：赤\|紅\|緋） |
| 810 | PVタイツ SP Blue | 塔伊茨護腿【ＳＰ】 | 英詞「blue」應義譯（期望：青\|藍\|蒼） |
| 811 | PVタイツ SP Purple | 塔伊茨護腿【ＳＰ】 | 英詞「purple」應義譯（期望：紫） |
| 1734 | True 空脚着・Black | 空脚着護腿・黑 | 英詞「true」應義譯（期望：真） |
| 1735 | True 空F脚着・Black | 空脚着護腿・黑 | 英詞「true」應義譯（期望：真） |
| 1742 | True 空脚着・Tea | 空脚着護腿・茶 | 英詞「true」應義譯（期望：真） |
| 1743 | True 空F脚着・Tea | 空脚着護腿・茶 | 英詞「true」應義譯（期望：真） |

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

