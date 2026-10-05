# 武器 series-dict 分層 QA

> 2026-10-05：分層主線進行中（見 `docs/plans/layered-series-dict-weapons-routing.md` 完成定義）。

## P0

- stems **14583**（S=3 A=44 B=876 C=13660）

## P1（S+A+B）

| 項目 | 計數 |
|---|---:|
| `series-dict.tsv` 列 | 923 |
| 定稿（有 zh） | **731** |
| 待查 | **192** |
| 本輪 `resolve_weapon_pending_b` 消化 | +83 |

## P2

- 套用列（累計命中字典）：近戰 **408**／遠程 **440**（本輪 +848 次改寫後總命中行為見 scratch log）
- `qa_weapon_series_dict` mismatches：**0**（expect 含 charset_apply）

## P3

- `validate_working.py` weapons-melee-name／weapons-ranged-name：**PASS**

## P3b

- `qa-p3b-wash-hits.tsv`：**831**（字典命中列 target 仍含英文字母；多為 SP／級別／舊音，待語意抽核）
- **非**結案阻擋；queue 下一筆：降 wash／擴 nick map

## 狀態

- progress／queue：**in_progress**（192 B pending；P3b 未清；C 未增量；未回寫 mhfdat）
