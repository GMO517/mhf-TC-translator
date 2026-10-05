# 武器分層 series-dict（對齊防具計畫）

> 父計畫：`layered-series-dict-model-routing.md`（P0→P3b 相位不變）。  
> **本輪節奏：** 先 P0 掃詞幹＋類型字根 → 你審 `series-dict`／`type-dict` → 再 P1 判定 → **最後** P2 才動 CSV 大批套用。

## 真源（規劃）

| 檔 | 用途 |
|---|---|
| `l10n/working/issues/weapons/series-dict.tsv` | 系列詞幹（近戰＋遠程共用表，欄 `sections`） |
| `l10n/working/issues/weapons/type-dict.md` | 武器類型字根（Sword／Katana／Bowgun…） |
| `l10n/working/scratch/weapon_stem_tiers.tsv` | P0 分級（S/A/B/C） |

## CSV

- `dat-weapons-melee-name.csv`（section `weapons-melee-name`）
- `dat-weapons-ranged-name.csv`（section `weapons-ranged-name`）

## P0（完成）

1. `scan_weapon_stem_tiers.py` → `weapon_stem_tiers.tsv`  
2. `type-dict.md` **定稿**；`series-dict-all.md` 全 stem

## P1（S+A 完成）

- `build_weapon_series_dict_sa.py` → `series-dict.tsv`（47 列）
- `fill_weapon_stem_tiers_category.py` 標 category

## P2（部分）

- `apply_weapon_series_dict.py`：僅 S+A 定稿 stem 改 CSV；B/C 沿用現譯

## 待辦

- B/C 批次 P1；P3b；人審後回寫本體
