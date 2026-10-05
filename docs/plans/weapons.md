# 武器 — 近戰＋遠程（含分層 series-dict）

> 主流程：[`l10n-orchestration.md`](l10n-orchestration.md)。防具同源規則見 [`armors.md`](armors.md)（Integrity／M2）。  
> **語意單位（Translator 收工單位）：** `weapons-melee-name` **＋** `weapons-ranged-name` **＋** 共用 `series-dict` **＋** `type-dict` **＋** 兩類 **`reviews-*.md` 全量**。  
> 分層字典（P0–P3b）是**達成整類譯完的手段**，不是可單獨結案的子任務。

## 範圍

- CSV：`dat-weapons-melee-name.csv`、`dat-weapons-ranged-name.csv`（**baseline**；勿為對齊文件清空 zh 或無故整表重翻）  
- Type：**先** [`type-dict.md`](../../l10n/working/issues/weapons/type-dict.md)（**WEA001–016** 定稿）  
- 系列：`issues/weapons/series-dict.tsv`（**機器真源**）  
- P0：`scratch/weapon_stem_tiers.tsv`（全 stem；**不**取代 S+A+B 人審表）  
- 譯文終審產物：`issues/weapons/melee/reviews-*.md`、`issues/weapons/ranged/reviews-*.md`（與兩 CSV **全量同步**；**尚無檔＝未完成**）

## 使用者審閱面

| 順序 | 路徑 |
|------|------|
| 1 | **`type-dict.md`**（十六武器／token） |
| 2 | **`series-dict-all.md`**（S+A+B；`| stem | zh | reason | source |`；**非** P0 裸 stem 當交件） |
| **譯文終審** | 近戰／遠程 **`reviews-*.md` 全量**（與 CSV 同步） |

**禁止**叫使用者審 `qa-p3b-wash-hits.tsv` 或 tsv 當主清單。

## 相位

| 相位 | 說明 |
|------|------|
| P0 | `scan_weapon_stem_tiers.py`；不覆寫已定稿 type-dict |
| P1 | **S+A+B** 入 tsv；**Grok L1–L5**（同 armors） |
| P2 | `apply_weapon_series_dict.py`＋charset；兩 CSV |
| P3 | validate＋`qa_weapon_series_dict` mismatch **原始數** |
| P3b | **Grok** 或 queue 明列；wash 表僅 agent 用 |
| **P4** | 兩 CSV **殘英／語意**全表 QA（對標防具；缺腳本則自檢＋記命中數） |
| **P5** | **重產**近戰／遠程 **reviews 全量**（P2 後亦須做；字典或 CSV 任一變更後必重做） |

### P1（釘死，堵 infer loophole）

- **S+A+B 的 zh：** 僅 **Grok Task**、**terms L1**、**與防具同 stem 且已有合格定稿**、**使用者已定稿保留**。  
- **禁止：** Composer `patch_*` PATCH dict；**禁止** `build_weapon_series_dict_tiers.py`（或同類）**新增字義 zh** 充 P1。  
- **C tier：** 僅允許 **terms 命中**或 **複製同 stem 已定稿**；否則 pending；**禁止** C 全表強翻。  
- 失敗 → **pending**，不套用。

### P2 後（每次套用必做）

- 刷新 **`series-dict-all.md`**（S+A+B 有 zh）。  
- **重產**近戰／遠程 **reviews 全量**（見 P5）。

## 完成定義（才可標 `progress` **qa_done**）

下列 **全部**成立；缺一即 **in_progress**／`qa_issues`，**不得**以 M3 交件或「誠實寫剩餘」代替收工。

1. **`type-dict.md`** 十六武器定稿。  
2. **P1：** S+A+B 列皆已定稿或 queue **Blocking** 已寫明 Grok 不可用原因；**S+A+B pending＝0**（待查不得當套用預設）。  
3. **P2、P3：** 兩 CSV 已套用；`validate_working` PASS；`qa_weapon_series_dict` mismatch 已記且 **0**（或已修）。  
4. **P3b：** 已用 Grok 處理 wash／need_semantic；**blocking／high 依 playbook 清零**（原始計數寫 `qa-weapons.md`）；僅「已跑一輪」不算完成。  
5. **P4：** 殘英、應義譯卻音譯等 **語意 QA 原始命中**已記（禁空 PASS）。  
6. **`series-dict-all.md` 已刷新**（非過期 P0 裸 stem）。  
7. **近戰＋遠程 `reviews-*.md` 已存在且與兩 CSV 全量同步。**

**使用者 reviews 終審**屬 orchestration **M3 之後**；**不**列入 agent `qa_done` 條件。agent **不得**代為宣告「你已審完」。

**不算完成（常見誤停）：**

- 只做 series-dict／只清部分 pending；P3 validate PASS 或 mismatch 0 即停。  
- 只刷新 `series-dict-all.md` 但 **reviews 未產出**。  
- `progress` 將 CSV 标 `translated` 但 notes 仍有殘英／manual remain。  
- 把 **M3 交件**、**queue 更新**、**session 摘要**當整類譯完。  
- 交 P0 索引或過期 all.md 當字首終審。

## 續跑（不得誤停）

- **queue「下一筆」**＝[`queue.md`](../../l10n/working/issues/queue.md) 武器區 **由上而下**；做完一項立刻做下一項，**非**停點。  
- 只做 S+A、或 B／P3b／P4／reviews 未依 queue 處理 → **不得**宣稱收工。  
- validate／commit／push／下一相位 **≠** 收工（見 orchestration §續跑）。  
- **「或誠實寫清剩餘」**僅用於 **Grok 判定失敗→pending** 的**單 stem**紀錄，**禁止**用整段 session 摘要替代清 queue。  
- playbook A.3：**子類（本類＝整包武器）未完禁止只交摘要就停。**

## Exit → 回主線（進 M2 前）

**進 M2／M3 的前提：** 本 session 已推進 queue 武器區，且 **未**在 §完成定義 仍缺項時假裝結案。

| 檢查 | 說明 |
|------|------|
| `qa-weapons.md` | validate、P3／P3b／P4 **原始命中**（非空 PASS） |
| `series-dict-all.md` | 本 session 有改字典或 P2 則已刷新 |
| reviews | 本 session 有改 CSV／字典則已 **全量重產** |
| `queue.md` | 下一筆與實際缺口一致；**Blocking 清單**誠實 |
| 使用者 | **未**要求開 tsv／wash hits |

**`qa_done`：** 僅當 §完成定義 **1–7 全 true** 後，才更新 `progress.md` 武器類與兩 CSV 檔狀態。

## 備忘

- `type-dict.md` ↔ `weapon_name_parse.py` 同步（操蟲棍／穿龍棍／磁斬槌等）。  
- 語意 QA 對標防具全表掃描級（缺則補腳本＋原始計數）。

## 狀態

以 [`progress.md`](../progress.md)｜[`queue.md`](../../l10n/working/issues/queue.md) 為準；本 plan 不維護逐 commit 數字。
