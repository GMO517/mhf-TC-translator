# 待審／進行中隊列（防譯文作廢）

> 已寫入 csv/ 的譯文**不要重翻**。拿不定見 glossary/PENDING.md。  
> 禁止半翻／片假名混中文（見 STYLE.md）。  
> 履歷／耗時：`issues/queueHistory.md`。  
> 已結案 review：`issues/archive/`（勿當待審重做）。

## 進行中

### weapons（整類：近戰＋遠程＋字典＋reviews）

> 完成定義：**[`docs/plans/weapons.md`](../../../docs/plans/weapons.md) §完成定義**（非僅 series-dict）。  
> Translator **收工**＝下列 Blocking **全清**；做完一項 **立刻**做下一項。

| 優先 | Blocking | 現況／產物 | 完成條 |
|:---:|---|---|---|
| 1 | **reviews** | 近戰 **36**＋遠程 **9** | 完成 |
| 2 | **P1 pending** | **0** | 完成 |
| 3 | **P3 機械** | validate PASS；mismatch **0**；殘英 **0** | 完成 |
| 4 | **P3b** | wash after_strip **0**；Grok 抽核修 **10**；high **0** | 完成（另開 QA 複核） |
| 5 | **P4** | needs_rework **0**；音譯清單 **119** 已記 | 完成（另開 QA 複核） |
| 6 | **C tier** | 僅增量 | 禁止全表 |

- 機械：`validate` PASS；`qa_weapon_series_dict` mismatch **0**（見 `qa-weapons.md`）  
- **未** mhfdat（除非你另案要求）

### 其他

| CATEGORY | 進度 | 下一筆 |
|---|---|---|
| Gate4 延伸（任務／UI／劇情） | pending | 見 `docs/TODO.md` Gate4；疑問→`armors/open-questions.md` Q-02 |

## 待獨立 QA

| CATEGORY | issue |
|---|---|
| beads-info / seals-jebia | 見既有 stub；勿重翻 |
| monsters-description | `issues/monsters/review-monsters-description.md` |

## 處理完（qa_done）

| CATEGORY | issue／review 歸檔 |
|---|---|
| **armors 五部位** | `issues/armors/qa-armors.md`；QA 0／wash 0；CSV 已更新；**未** finish_batch 本體 |
| tickets | `items-name__tickets.md`；`archive/items-name/review-items-name__tickets.md` |
| consumables | `items-name__consumables.md`；`archive/items-name/review-items-name__consumables.md` |
| monster-materials | `items-name__monster-materials.md`；`archive/items-name/review-items-name__monster-materials.md` |
| gathering | `items-name__gathering.md`；`archive/items-name/review-items-name__gathering.md` |
| jewels | `items-name__jewels.md`；`archive/items-name/review-items-name__jewels.md` |
| skill-cuffs | `items-name__skill-cuffs.md`；`archive/items-name/review-items-name__skill-cuffs.md` |
| kits | `items-name__kits.md`；`archive/items-name/review-items-name__kits.md` |
| monster-rest | `items-name__monster-rest.md`；`archive/items-name/review-items-name__monster-rest.md` |
| misc | `items-name__misc.md`；`archive/items-name/review-items-name__misc.md` |
| dummy | `items-name__dummy.md`；`archive/items-name/review-items-name__dummy.md` |
| remainder（舊 stub） | `items-name__remainder.md`；`archive/items-name/review-items-name__remainder.md` |
| all-rest 拆分（29／5450） | `archive/items-name/all-rest/`；batch `batches/active/batch-items-allrest-writeback.json`；**已回寫** 2026-10-04 |

相關 delta 批次歸檔：`batches/legacy/items-name-qa-done-20261004/`。
