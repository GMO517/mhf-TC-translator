# Progress（分類狀態機・子規範）

> **父規範**：`docs/agent-translation-playbook.md`。  
> 本檔**只管**各 CATEGORY／子類狀態：`pending` | `in_progress` | `translated` | `qa_issues` | `qa_done`。  
> 工程 Gate 看 `docs/TODO.md`；用字看 `STYLE.md`；二者都不得在本檔發明新流程。

---

## items-name

- status: in_progress
- notes: "主真相＝csv。validate PASS。review 審計後 tickets 半角拉丁 46 已全形化；各子類 kata/still_en=0。可進武器／防具。"

### files

- path: l10n/extracted/（dat-items-name）
  status: translated
  notes: "抽出完成；勿無故重抽"

- path: l10n/working/csv/dat-items-name.csv
  status: in_progress
  notes: "skill-cuffs 等已 delta；misc/kits/monster-rest/remainder 2026-10-04 審計後 delta"

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

- status: translated
- notes: "2026-10-04 層次 B 殘列清零：needs_rework=0（非空 ok=16825／17568）；validate PASS；bin delta（jp-kata 49＋lex 68＋manual 67）。"

### files

- path: l10n/working/csv/dat-weapons-melee-name.csv
  status: translated
  notes: "`_session_jp_weapon_names` WEAPON_KATA＋charset 安全；殘英 lex／manual remain"

---

## weapons-ranged-name

- status: translated
- notes: "2026-10-04 needs_rework=0（ok=4223）；validate PASS；bin delta（jp-kata 29＋manual 21）。"

### files

- path: l10n/working/csv/dat-weapons-ranged-name.csv
  status: translated
  notes: "片假名 batch jp-kata；殘英 manual remain"

---

## armors-head

- status: translated
- notes: "2026-10-04 needs_rework=0／14594；validate PASS；all-changed 回寫 14590 列。"

### files

- path: l10n/working/csv/dat-armors-head.csv
  status: translated
  notes: "fix_armors_translate_v2＋remain 清殘"

---

## armors-body

- status: translated
- notes: "2026-10-04 needs_rework=0／13462；validate PASS；all-changed 回寫 13442 列。"

### files

- path: l10n/working/csv/dat-armors-body.csv
  status: translated
  notes: "同 head 管線"

---

## armors-arm / armors-waist / armors-leg

- status: pending
- notes: "sections.json 尚未列入；extracted/working CSV 未建。待抽表後接 head 管線。"

### files

- path: l10n/working/csv/（dat-armors-arm 等）
  status: pending
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
