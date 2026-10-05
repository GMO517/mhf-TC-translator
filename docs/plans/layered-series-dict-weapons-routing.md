# 武器分層 series-dict（對齊防具計畫）

> 父計畫：`layered-series-dict-model-routing.md`（P0→P3b；**§9 禁誤停**必守）。  
> **節奏：** P0 掃詞幹＋**type-dict 定稿** → P1 系列詞幹（S→A→B）→ P2 只套用定稿 → P3／P3b →（另案）回寫 mhfdat。

## 真源

| 檔 | 用途 |
|---|---|
| `l10n/working/issues/weapons/series-dict.tsv` | 系列詞幹（近戰＋遠程；`sections`） |
| `l10n/working/issues/weapons/type-dict.md` | 武器類型字根（WEA001–016） |
| `l10n/working/scratch/weapon_stem_tiers.tsv` | P0 分級 |
| `l10n/working/issues/weapons/series-dict-all.md` | 全 stem 索引（**無 zh**；非主編輯面） |

## CSV

- `dat-weapons-melee-name.csv`（`weapons-melee-name`）
- `dat-weapons-ranged-name.csv`（`weapons-ranged-name`）

---

## 相位（做到哪算哪 — 見下方「完成定義」）

| 相位 | 腳本（scratch） | 產物 |
|---|---|---|
| P0 | `scan_weapon_stem_tiers.py` | `weapon_stem_tiers.tsv`；不覆寫已定稿 `type-dict.md` |
| P1 | `build_weapon_series_dict_tiers.py`（S+A+B） | `series-dict.tsv`；`fill_weapon_stem_tiers_category.py` |
| P2 | `apply_weapon_series_dict.py` + `charset_apply` | 兩 CSV（**僅** reason≠待查 且有 zh） |
| P3 | `validate_working.py`、`qa_weapon_series_dict.py` | `qa-weapons.md`、命中數 **0** 為 P2 一致 |

**P1 範圍（釘死）：**

- **必做 tier：S、A、B**（寫入 `series-dict.tsv`；能 L1–L5／infer 則填 zh，否則 **待查** 且不套用）。
- **C tier（約 1.3 萬 stem）：** **禁止** P1 全表強翻、禁止 short_phonetic 洗表；**允許**只對「armor 同 stem／infer 可定」逐批擴列——這是**增量**，不是「C 不做就可以停整條線」。

**P3b：** 語意 wash／新 `need_semantic`（對齊防具）；未清則 **queue 標 in_progress**，不得改標 `qa_done`。

---

## 完成定義（武器分層主線）

下列**全部**滿足前，不得在 `progress` 標武器子類 `qa_done`：

1. `type-dict.md` 定稿（使用者已審或 plan 標定稿）。  
2. P1：**S+A+B 已入 tsv**；B 的 **pending** 已盡力 L1–infer（剩餘數寫入 `series-dict.md`／`qa-weapons.md`）。  
3. P2 已跑；P3 validate **PASS**；`qa_weapon_series_dict` **mismatches 原始數**已記。  
4. P3b 已跑或 **queue** 明列「P3b 待跑＋原因」。  
5. **未**回寫 mhfdat（除非使用者另案要求）——缺此項**不是**停問理由，只是狀態維持 `in_progress`。

**不算完成（常見誤停）：**

- 只做 S+A、或只 commit、或只 validate PASS 就停。  
- 用「C 不洗表」結束對話，但 B pending／P3b／queue 未更新。  
- 問 push、問「要不要做 B」——見父 plan **§9**。

---

## 當前快照（2026-10-05，agent 維護）

- P0／type-dict：完成  
- P1：923 列（648 定稿，**275 pending**）  
- P2／P3：PASS；qa mismatches 0  
- 下一筆（寫 queue）：**清 B pending** → **P3b** → 視需要 C 增量 infer  

---

## Agent 備忘（武器專用）

- `series-dict-all.md` 給人看字首；**譯文只寫 `series-dict.tsv`**。  
- 磁斬槌／操蟲棍／十六武器 type 見 `type-dict.md`；P2 與 `weapon_name_parse.py` 同步。  
- 套用後必走 `charset_apply`（Parone／Lethe／斬撃斧 等 CP932 坑已踩過）。
