# 武器 series-dict 分層 QA（進行中）

> 2026-10-05：type-dict 定稿；P0 重掃；**P1 S+A=47** 入 `series-dict.tsv`；P2 套用（僅已定稿 stem）。

## P0

- `weapon_stem_tiers.tsv`：stems **14583**（S=3 A=44）
- 人審全表：`series-dict-all.md`

## P1（S+A）

- 字典列：**47**｜待查：**0**
- category：見 `series-dict.md`

## P2 套用

- `apply_weapon_series_dict.py`（scratch）
- 近戰＋遠程合計改寫列：約 **2528**（僅 stem 命中 S+A 字典者；其餘保留原 target）
- `validate_working.py` weapons-melee-name／weapons-ranged-name：**PASS**

## 待辦

- B/C 詞幹：不洗表；逐批 P1 或沿用現譯
- P3b 語意抽核（高頻 wash）— 未跑
- **未**回寫 mhfdat
