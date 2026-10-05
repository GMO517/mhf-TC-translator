# 防具系列詞幹字典（全身共用）

> 五部位同一系列詞幹必須同譯。部位詞見各槽 `part-dict.md`。
> **機器全表：** `series-dict.tsv`（與下方 human 全表同步）。
> **human 全表：** `series-dict-all.md`（**# 分節**，不截前 N）。
> **組裝硬性（STYLE）：**整名最多一個`【】`、最多一個`・`。

## 查序（與 playbook A.3 同一套）

1. 整名語意 → terms → 神話 → 遊戲專名 → Web → 字義 → 短音譯／待查

**禁洗白：** 待查／純音譯不得全表套用。

**短音譯人審：** 勿只看英文 stem；以 `source`／`example_source` 追 **日版片假名・和名**。
宜 2～4 字自然專名，禁音節機械拼字（如冗長「爾艾德」式）。

## 分級統計（P0 `armor_stem_tiers.tsv`）

| tier | stems |
|---|---:|
| S | 591 |
| A | 985 |
| B | 1514 |
| C | 2310 |

- 字典已對：**3781**｜待查／空：**15**

## S+A 歸類分布（P1 category）

| category | count |
|---|---:|
| pending | 598 |
| phonetic_last | 597 |
| en_semantic | 149 |
| game_proper | 118 |
| monster | 95 |
| color_suffix | 10 |
| collab | 7 |
| myth | 2 |

## 待查（全 **15** 列）

| count | stem | example | slots |
|---:|---|---|---|
| 20 | D | arms:Gold D Arms・Red | arms,body,head,legs,waist |
| 8 | Mizuha 魁 | arms:Mizuha 魁【大袖】 | arms,body,legs,waist |
| 8 | Toyotama 魁 | arms:Toyotama 魁【大袖】 | arms,body,legs,waist |
| 5 | Welkin 魁 | arms:Welkin Sleeve・魁 | arms,body,head,legs,waist |
| 5 | True Shadow 魁 | arms:True Shadow Sleeve・魁 | arms,body,head,legs,waist |
| 5 | Snake 魁 | arms:White Snake Sleeve・魁 | arms,body,head,legs,waist |
| 5 | Valued Word 魁 | arms:Valued Word Sleeve・魁 | arms,body,head,legs,waist |
| 4 | Sky 魁 | arms:Blue Sky Sleeve・魁 | arms,body,head,waist |
| 4 | Rolling Sky 魁 | arms:Rolling Sky Kote・魁 | arms,body,head,legs |
| 4 | Rolling Earth 魁 | arms:Rolling Earth Kote・魁 | arms,body,head,legs |
| 4 | Golden 魁 | legs:Golden Hakama・魁 | body,legs |
| 3 | Rolling Flow 魁 | legs:Rolling Flow Greaves・魁 | body,head,legs |
| 2 | Shikari 魁 | arms:Shikari Kote・魁 | arms,legs |
| 2 | Demon Lord 魁 | arms:Demon Lord Kote・魁 | arms,head |
| 1 | Khezu 亜D | head:Khezu 亜D Festa | head |

## 已定稿

共 **3781** 列 — 見 `series-dict-all.md`（**依 # 分節**）或 `series-dict.tsv`。

### 全表分節一覽

| 分節 | 列數 |
|---|---:|
| 專名短音譯 — 原文日文・片假名（優先複核） | 483 |
| 專名短音譯 — 英文 stem（須對日版讀音，禁生硬灌字） | 884 |
| 魔物／詞庫 | 103 |
| 詞庫（terms／UI） | 255 |
| 遊戲專名／合作 | 309 |
| 神話／典故 | 23 |
| 日文原語（和文 stem） | 1299 |
| 字義／拼裝 | 425 |

