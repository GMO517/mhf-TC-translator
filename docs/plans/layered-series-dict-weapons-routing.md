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

## P0（現在做）

1. `scan_weapon_stem_tiers.py` → `weapon_stem_tiers.tsv`  
2. 產 `type-dict.md` 初稿＋`series-dict.md` 摘要（**不套用 CSV**）

## P1 起

同防具：S+A 判定、禁 short_phonetic 洗表；近戰／遠程**同一詞幹同譯**。
