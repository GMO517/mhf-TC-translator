# 武器 series-dict 分層 QA

> 2026-10-05：type-dict 定稿；P0 重掃（14583 stems）；P1 **S+A+B=923** 列（定稿 **648**｜待查 **275**）；P2 套用＋charset；P3 機械 QA。

## P0

- `weapon_stem_tiers.tsv`：S=3 A=44 B=876 C=13660
- `series-dict-all.md`：全 stem 索引（無 zh）

## P1

- `series-dict.tsv`：923 列（S+A+B）
- 定稿可套用：**648**（armor／infer／manual）
- **275** pending（B tier 無反推；不套用）
- category：見 `series-dict.md`

## P2

- `apply_weapon_series_dict.py` + `charset_apply.to_display`
- 字典命中列已與 compose 對齊（`qa-series-apply-hits.tsv` mismatches **0**）

## P3

- `validate_working.py` weapons-melee-name／weapons-ranged-name：**PASS**
- `qa_weapon_series_dict.py`：字典命中列一致性掃描

## 範圍外（plan 明訂）

- **C tier**（13660 stems）：不 P1 全表；保留現譯
- P3b 語意 wash、mhfdat 回寫：未做

## 狀態

- progress：**in_progress**（分層主線 S+A+B 完成；C 未收斂）
