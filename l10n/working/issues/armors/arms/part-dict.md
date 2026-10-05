# arms 部位字典（固定詞）

> 防具名＝**系列詞幹**＋**部位**（直連、中間不加・）。本檔只定「部位」英／日→繁中。  
> 系列詞幹（全身共用）：`../series-dict.md`／`series-dict.tsv`。  
> 權威：`docs/STYLE.md` §防具五部位＋`l10n/glossary/terms.csv`（UI*）＞台服 wiki＞字義。  
> 字型缺字時顯示形走 `charset/fallback_map.csv`（語意仍用本表定稿）。

| 原文（部位） | 譯文 | 理由 | 出處 |
|---|---|---|---|
| Arms | 護腕 | 鎗／Arms 側定稿（對 Guard 臂甲） | 使用者定稿；台服 wiki 腕頁鎗側慣用「手甲」，本專案統一作「護腕」 |
| Guard / Guards | 臂甲 | 劍側腕部；wiki 腕頁高頻 | [台服 wiki・腕](https://w.atwiki.jp/mhfotw/pages/189.html)；terms UI006 |
| Vambraces | 臂甲 | 護臂＝劍側臂甲 | 與 Guard 對齊 |
| Brachia | 臂甲 | 上臂＝臂甲 | 與 Guard 對齊 |
| Gauntlets | 手甲 | wiki 鎗側亦見手甲；鐵手套 | 台服 wiki／字義 |
| Hands | 手甲 | 手部防具 | 與 Gauntlets 對齊 |
| Cuffs | 護腕 | 袖口護腕；與 Arms 同譯 | 字義／與 Arms 對齊 |
| Sleeve / Sleeves | 袖 | 袖型防具 | 字義 |
| Gloves / グローブ | 手套 | 手套 | 字義 |
| ミトン | 手套 | 連指手套 | 字義 |
| Claws / クロウ | 爪 | 爪型 | 字義 |
| Grip | 握套 | 握持具 | 字義 |
| Grasp | 抓握 | 抓握具 | 字義 |
| Punch | 拳套 | 拳套 | 字義 |
| フィスト | 拳 | 拳 | 字義 |
| Kote | 籠手 | 日文「籠手」 | 日文原語；MH 和風套 |
| 御手 | 御手 | 日文原語保留 | 原文 |
| 大袖 | 大袖 | 日文原語保留 | 原文 |
| Creeper | 蔓腕 | 蔓生腕部 | 字義 |
| ブラッソ | 臂甲 | 歐式臂甲片假名→臂甲 | 與 Guard 對齊 |
| ハトゥー／マカーン／サクンペ／ノキリペ | 臂甲 | Frontier 專用部位片假名→臂甲 | 與 Guard 對齊 |

## 組成規則（本槽）

- 模板：`{系列}{部位}`＋可選**一個**`【級別】`＋可選**一個**`・{色}`  
- 例：`Rathalos Guard`→`雄火龍臂甲`；`Bone S Arms`→`骨製護腕【Ｓ】`；`Carmine Arms Blue`→`深紅護腕・青`；`Hunter's Arms`→`獵人護腕`  
- 例：`S・Sol Arms SP Black`→`S索倫護腕【ＳＰ】・黑`；`Star Festival Gauntlets・Heaven [Red 】`→`星祭天手甲・赤`  
- **硬性：**整名最多一個`【】`、最多一個`・`（見 `docs/STYLE.md` §防具）。  
- 成對：同一系列 `Guard`＝臂甲、`Arms`＝護腕（勿互混）。  
- **禁止**系列與部位之間加・；**禁止**級別夾在系列與部位中間。
