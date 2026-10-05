# 武器系列詞幹字典（近戰＋遠程共用）

> **你審這包即可**（口頭常簡稱 `series-dict.md`）：本檔摘要 ＋ [`series-dict-all.md`](series-dict-all.md) 字首全表 ＋ [`melee/reviews-*.md`](melee/)／[`ranged/reviews-*.md`](ranged/) 譯名全量（與 CSV 同步）。
> **機器真源：** `series-dict.tsv`（S+A+B 本輪 **923** 列）。**類型字根：** [`type-dict.md`](type-dict.md)。
> **修改字首：** 告知 agent 改 tsv／本 md → 重跑 `scratch/refresh_weapon_series_dict_md.py` → 必要時 P2。

## 查序（與 playbook A.3 同一套）

1. 整名語意 → terms → 神話 → 遊戲專名 → Web → 字義 → 短音譯／待查

**禁洗白：** 待查／純音譯不得全表套用。

## 分級統計（P0 `weapon_stem_tiers.tsv`）

| tier | stems |
|---|---:|
| S | 3 |
| A | 44 |
| B | 876 |
| C | 13660 |

- 字典已對：**923**｜待查／空：**0**

## S+A+B 歸類分布（P1 category，tier 檔）

| category | count |
|---|---:|
| game_proper | 594 |
| pending | 192 |
| en_semantic | 59 |
| phonetic_last | 36 |
| monster | 33 |
| myth | 8 |
| collab | 1 |

## 待查（全 **0** 列）

| count | stem | example | sections |
|---:|---|---|---|

## 已定稿

共 **923** 列 — 見 [`series-dict-all.md`](series-dict-all.md)（**# 分節**）或 `series-dict.tsv`。

### 全表分節一覽

| 分節 | 列數 |
|---|---:|
| 專名短音譯 — 原文日文・片假名（優先複核） | 110 |
| 專名短音譯 — 英文 stem（須對日版讀音，禁生硬灌字） | 9 |
| 魔物／詞庫 | 34 |
| 詞庫（terms／UI） | 12 |
| 遊戲專名／合作 | 163 |
| 神話／典故 | 33 |
| 日文原語（和文 stem） | 1 |
| 字義／拼裝 | 515 |
| 其他 | 46 |

