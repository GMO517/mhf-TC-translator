# Progress（分類狀態機・子規範）

> **父規範**：`docs/agent-translation-playbook.md`。  
> 本檔**只管**各 CATEGORY／子類狀態：`pending` | `in_progress` | `translated` | `qa_issues` | `qa_done`。  
> 工程 Gate 看 `docs/TODO.md`；用字看 `STYLE.md`；二者都不得在本檔發明新流程。

---

## items-name

- status: in_progress
- notes: "主真相＝csv。validate PASS、半翻警告 0；needs_rework=0。子類皆 awaiting_qa；可進武器／防具。"

### files

- path: l10n/extracted/（dat-items-name）
  status: translated
  notes: "抽出完成；勿無故重抽"

- path: l10n/working/csv/dat-items-name.csv
  status: in_progress
  notes: "skill-cuffs 等已 delta；dummy/kits/monster-rest/misc/remainder 本輪已 delta"

### subclasses（語意，非流水號）

- beads / info: translated → issues/items-name__beads-info.md（awaiting_qa）
- seals / jebia: translated → issues/items-name__seals-jebia.md（awaiting_qa）
- tickets: translated → issues/items-name__tickets.md（awaiting_qa）；batches/awaiting_qa/batch-items-tickets.json
- consumables: translated → issues/items-name__consumables.md（awaiting_qa）；batches/awaiting_qa/batch-items-consumables.json（n=282）
- monster-materials: translated → issues/review-items-name__monster-materials.md（awaiting_qa）；batches/awaiting_qa/batch-items-monster-materials.json（n=1095）
- gathering: translated → issues/review-items-name__gathering.md（awaiting_qa）；batches/awaiting_qa/batch-items-gathering.json（n=488）
- jewels: translated → issues/review-items-name__jewels.md（awaiting_qa）；batches/awaiting_qa/batch-items-jewels.json（n=480）
- skill-cuffs: translated → issues/review-items-name__skill-cuffs.md（awaiting_qa）；batches/awaiting_qa/batch-items-skill-cuffs.json（n=2877）
- dummy: translated → issues/review-items-name__dummy.md（awaiting_qa）；batches/awaiting_qa/batch-items-dummy.json（n=676）
- kits: translated → issues/review-items-name__kits.md（awaiting_qa）；batches/awaiting_qa/batch-items-kits.json（n=45）
- monster-rest: translated → issues/review-items-name__monster-rest.md（awaiting_qa；2026-10-04 重譯全表＋片假名清零）；batches/awaiting_qa/batch-items-monster-rest.json（n=438）
- misc: translated → issues/review-items-name__misc.md（awaiting_qa）；batches/awaiting_qa/batch-items-misc.json（n=199）
- remainder: translated → issues/review-items-name__remainder.md（awaiting_qa）；batches/awaiting_qa/batch-items-all-rest.json（n=5450）

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
