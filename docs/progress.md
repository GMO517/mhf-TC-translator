# Progress（分類狀態機・子規範）

> **父規範**：`docs/agent-translation-playbook.md`。  
> 本檔**只管**各 CATEGORY／子類狀態：`pending` | `in_progress` | `translated` | `qa_issues` | `qa_done`。  
> 工程 Gate 看 `docs/TODO.md`；用字看 `STYLE.md`；二者都不得在本檔發明新流程。

---

## items-name

- status: in_progress
- notes: "主真相＝csv。票券已 finish_batch（delta 1927）。PENDING 建議已去片假名（漢字音譯／義譯）；現況欄仍可能是舊片假名暫譯。待使用者定稿→Fixer 回修 CSV／半翻與片假名混中文警告。"

### files

- path: l10n/extracted/（dat-items-name）
  status: translated
  notes: "抽出完成；勿無故重抽"

- path: l10n/working/csv/dat-items-name.csv
  status: in_progress
  notes: "票券 CSV 完並已 delta 回寫本體；batch → awaiting_qa/batch-items-tickets.json（n=1927）"

### subclasses（語意，非流水號）

- beads / info: translated → issues/items-name__beads-info.md（awaiting_qa）
- seals / jebia: translated → issues/items-name__seals-jebia.md（awaiting_qa）
- tickets: translated → issues/items-name__tickets.md（awaiting_qa；PENDING 定稿後 Fixer）；batches/awaiting_qa/batch-items-tickets.json
- consumables: in_progress → batches/active/batch-items-consumables.json（n=216 已 apply；未 finish_batch）

---

## weapons-melee-name

- status: in_progress
- notes: "層次 A 詞庫命中已回寫；層次 B 未入庫列待推進"

### files

- path: l10n/working/csv/dat-weapons-melee-name.csv
  status: in_progress
  notes: ""

---

## weapons-ranged-name

- status: in_progress
- notes: "層次 A 詞庫命中已回寫；層次 B 未入庫列待推進"

### files

- path: l10n/working/csv/dat-weapons-ranged-name.csv
  status: in_progress
  notes: ""

---

## armors-head

- status: in_progress
- notes: "層次 A 詞庫命中已回寫；層次 B 未入庫列待推進"

### files

- path: l10n/working/csv/dat-armors-head.csv
  status: in_progress
  notes: ""

---

## armors-body

- status: in_progress
- notes: "層次 A 詞庫命中已回寫；層次 B 未入庫列待推進"

### files

- path: l10n/working/csv/dat-armors-body.csv
  status: in_progress
  notes: ""

---

## monsters-description

- status: pending
- notes: "已抽出；Gate3 層次 B 較後；長文語感樣本後整類推進"

### files

- path: l10n/extracted/（dat-monsters-description）
  status: translated
  notes: "抽出完成"

- path: l10n/working/csv/（對應 monsters description）
  status: pending
  notes: ""
