# 防具 — 分層 series-dict 次流程

> 主流程：[`l10n-orchestration.md`](l10n-orchestration.md)（M2／M3／Integrity）。  
> 憲法：[`agent-translation-playbook.md`](../agent-translation-playbook.md) Part A。

## 範圍

- CSV：`dat-armors-{head,body,arms,waist,legs}.csv`  
- 系列詞幹：`l10n/working/issues/armors/series-dict.tsv`（**機器真源**）  
- 部位：`issues/armors/<slot>/part-dict.md`  
- P0 分級：`l10n/working/scratch/armor_stem_tiers.tsv`

## 使用者審閱面

| 用途 | 路徑 |
|------|------|
| **譯文終審** | 五槽 **`reviews-*.md` 全量**（與 CSV 同步）；索引可選 `REVIEW-MANIFEST.md` |
| **字首終審** | `issues/armors/series-dict-all.md`（`#` 分節；待查全列） |
| 統計 | `series-dict.md`（非前 N 充數） |

## 相位與 model

```mermaid
flowchart LR
  P0[P0 掃 tier] --> P1[P1 Grok L1-L5]
  P1 --> P2[P2 套用定稿]
  P2 --> P3[P3 機械 QA]
  P3 --> P3b[P3b Grok 抽核]
  P3b -->|未清| P1
```

| 相位 | slug | 輸出 |
|------|------|------|
| P0 | `composer-2.5-fast`／腳本 | `armor_stem_tiers.tsv` |
| P1 | `grok-4.7-high-fast`（P1b：`cursor-grok-4.6-high-fast`） | 更新 tsv；category 由 **Grok** 填 |
| P2 | 腳本／Composer | 五 CSV（僅 §已定稿） |
| P3 | 腳本／Composer | `qa-armors.md` **原始命中** |
| P3b | Grok | wash＋need_semantic 修訂 |

**分級：** S≥50；A 10–49；B 3–9；C&lt;3。P1 主戰 **S+A+B**（queue 明示縮 scope 除外）。

### P0

1. 五 CSV → count／stem／tier → `armor_stem_tiers.tsv`；`category` 先空。  
2. 詞幹切法與 `apply_armor_series_dict.py` 同規（色、部位、・、【】、已知坑 White Snake 等）。

### P1（Grok）

- S 一次；A **每批 40–50 stem**；須 WebSearch。  
- L1 terms → L2 合作／神話 → L3 `搜：…→…` → L4 字義（含 wash）→ L5 短音譯≤4 或 **pending**。  
- **禁止** patch 腳本硬灌 zh；**禁止** heuristic 腳本貼 category。

### 已定稿（可 P2 套用）

`zh` 非空；`reason` 非僅待查／音譯；`source` 屬 terms／神話／專名／`搜：…→…`／合格字義。

### P2

只吃已定稿；刷新 **`series-dict-all.md`**；**重產五槽 reviews 全量**。

### P3／P3b

- `validate_working.py`＋`qa_armor_transliteration.py`。  
- P3b：**Grok** 抽 wash＋新 need_semantic；未清 → queue → 回 P1。

## 續跑（不得誤停）

- 只做 S+A 而 B／P3b 未依 queue 處理 → **不得 Exit**。  
- validate／commit **≠** 收工；須 QA 原始計數＋reviews 同步。  
- push／commit／下一相位 **非停點**（見 orchestration）。

## Exit → 回主線（M2 前必 true）

1. 當次相位跑完或剩餘寫 `queue.md`（含 pending 數）。  
2. `qa-armors.md` 含 validate＋**原始命中**（非空 PASS）。  
3. **`series-dict-all.md` 已刷新**；五槽 **reviews 與 CSV 全量同步**。  
4. 未要求使用者審 tsv／wash hits。

## 不做

- 全表 `compact_phonetic` 灌譯；C 全表 P1 強翻；未明示回寫 mhfdat／commit。
