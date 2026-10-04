# Progress（分類狀態機・子規範）

> **父規範**：`docs/agent-translation-playbook.md`。  
> 本檔**只管**各 CATEGORY／子類狀態：`pending` | `in_progress` | `translated` | `qa_issues` | `qa_done`。  
> 工程 Gate 看 `docs/TODO.md`；用字看 `STYLE.md`；二者都不得在本檔發明新流程。

---

## items-name

- status: in_progress
- notes: "validate PASS。新加系列標記用【天廊】／【簡易】；既有()沿用；Nullberry→打消果實。"

### files

- path: l10n/extracted/（dat-items-name）
  status: translated
  notes: "抽出完成；勿無故重抽"

- path: l10n/working/csv/dat-items-name.csv
  status: in_progress
  notes: "all-rest C 區語意重分類後 CSV 已第一輪對齊（changed=142）；殘譯第二輪未做；未整批回寫本體"

### subclasses（語意，非流水號）

- beads / info: translated → issues/items-name__beads-info.md（awaiting_qa）
- seals / jebia: translated → issues/items-name__seals-jebia.md（awaiting_qa）
- tickets: qa_done → issues/items-name__tickets.md；review→`archive/items-name/`；batch n=1927
- consumables: qa_done → issues/items-name__consumables.md；review→`archive/items-name/`；batch n=282
- monster-materials: qa_done → issues/items-name__monster-materials.md；review→`archive/items-name/`；batch n=1095
- gathering: qa_done → issues/items-name__gathering.md；review→`archive/items-name/`；batch n=488
- jewels: qa_done → issues/items-name__jewels.md；review→`archive/items-name/`；batch n=480
- skill-cuffs: qa_done → issues/items-name__skill-cuffs.md；review→`archive/items-name/`；batch n=2877
- dummy: qa_done → issues/items-name__dummy.md；review→`archive/items-name/`；batch n=676
- remainder（舊 stub）: qa_done → issues/items-name__remainder.md；細審改看 all-rest
- kits: qa_done → issues/items-name__kits.md；review→`archive/items-name/`；batch n=45
- monster-rest: qa_done → issues/items-name__monster-rest.md；review→`archive/items-name/`；batch n=438
- misc: qa_done → issues/items-name__misc.md；review→`archive/items-name/`；batch n=199
- all-rest 拆分: in_progress → `issues/items-name/all-rest/`（**29** 檔／**5450** 筆）
  - A＋B 已標 qa_done：**18** 檔／**2492** 筆（B 5 檔已補標）
  - C 已語意重分類＋殘譯清零：**11** 檔／**2958** 筆；CSV 已對齊
  - **下一動**：整批回寫本體（待明示；勿自行 finish_batch）
  - 詳見 `issues/items-name/README.md`；舊切片→`all-rest/_deprecated_index_split/`

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
