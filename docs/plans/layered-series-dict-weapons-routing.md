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

## P1（S+A+B 完成）

- `build_weapon_series_dict_tiers.py` → `series-dict.tsv`（923 列；定稿 648；pending 275）
- `fill_weapon_stem_tiers_category.py` 標 S/A/B category

## P2（定稿 stem）

- `apply_weapon_series_dict.py` + `charset_apply`；C tier 不進字典、不洗表

## P3

- `validate_working.py` PASS；`qa_weapon_series_dict.py`

## 待辦

- C tier（13660）維持現譯；P3b wash；回寫 mhfdat
