# 待審／進行中隊列（防譯文作廢）

> 已寫入 `csv/` 的譯文**不要重翻**。本隊列只供獨立 QA／Fixer 接手。  
> 狀態對齊 `docs/progress.md`。格式見 `docs/agent-translation-playbook.md`。

## 進行中（Translator 未停）

| CATEGORY | 進度 | 批次產物 | 下一筆 |
|---|---|---|---|
| `items-name/tickets` | in_progress | `batches/active/batch-items-tickets.json`（#4856–5772 已在 CSV） | **#6018** `Parin WhtTea Tkt` |

詳見 `items-name__tickets.md`。

## 待獨立 QA（已譯完子段，禁止重做）

| CATEGORY | 批次產物 | CSV 核對 | issue |
|---|---|---|---|
| `items-name/beads-info` | `batches/awaiting_qa/batch-items-jewels-sp-info.json`（53） | 53/53 已在 CSV | `items-name__beads-info.md` |
| `items-name/seals-jebia` | `batches/awaiting_qa/batch-items-jebia-marks.json`（38） | 38/38 已在 CSV | `items-name__seals-jebia.md` |

層次 A 詞庫命中歷史複審：`archive/qa-layer-a.md`（PASS；非本隊列重做對象）。

## 歷史歸檔（已 commit 的流水切片，勿重產）

`batches/legacy/`：`batch-items-001…018`、`tickets-a…d` 等。  
內容已併入 `csv/dat-items-name.csv`；QA 時以 **CSV 為準**，legacy JSON 僅溯源。

## 規則

1. Translator 不得因「看起來沒整理」而重翻 CSV 已有譯文  
2. QA 只寫 issues；預設不改譯文  
3. 子類整段清完才 `feat: items-name <子類>` 結案 commit（票券進行中除外：工作進度可先保全 commit）
