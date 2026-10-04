# Progress（分類狀態機）

> Source of Truth：**分類／檔案狀態**以本檔為準。  
> Phase 總覽與閘門仍看 `docs/TODO.md`。  
> 狀態僅允許：`pending` | `in_progress` | `translated` | `qa_issues` | `qa_done`。  
> 規則見 `docs/agent-translation-playbook.md`。

---

## items-name

- status: in_progress
- notes: "層次 A 詞庫命中已回寫。層次 B 子類：珠／情報／印記已譯；票券進行中。下一未譯票券 #6018 Parin WhtTea Tkt。整類票券清完再 commit feat: items-name 票券。禁止 tickets-a/b/c 流水切片。"

### files

- path: l10n/extracted/（dat-items-name）
  status: translated
  notes: "抽出完成；勿無故重抽"

- path: l10n/working/csv/dat-items-name.csv
  status: in_progress
  notes: "票券子類未完；working 產物 batch-items-tickets.json 已 delta 回寫未另 commit"

### subclasses（語意，非流水號）

- beads / info / seals: translated（待獨立 QA）
- tickets: in_progress

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
- notes: "已抽出；Phase 3 層次 B 較後；長文語感樣本後整類推進"

### files

- path: l10n/extracted/（dat-monsters-description）
  status: translated
  notes: "抽出完成"

- path: l10n/working/csv/（對應 monsters description）
  status: pending
  notes: ""
