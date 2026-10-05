# Progress（分類狀態機・子規範）

> **父規範**：`docs/agent-translation-playbook.md`。  
> 本檔**只管**各 CATEGORY／子類狀態：`pending` | `in_progress` | `translated` | `qa_issues` | `qa_done`。  
> 工程 Gate 看 `docs/TODO.md`；用字看 `STYLE.md`；二者都不得在本檔發明新流程。

---

## items-name

- status: translated
- notes: "2026-10-04 all-rest 整批回寫完成；validate PASS；delta 5277／batch 5450；SHA→816694b4…。"

### files

- path: l10n/extracted/（dat-items-name）
  status: translated
  notes: "抽出完成；勿無故重抽"

- path: l10n/working/csv/dat-items-name.csv
  status: translated
  notes: "all-rest 29／5450 qa_done 後已 finish_batch 回寫 mhfdat＋client"

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
- all-rest 拆分: qa_done → review 已歸檔 `archive/items-name/all-rest/`（**29**／**5450**）
  - 2026-10-04 已回寫：`batch-items-allrest-writeback.json`；delta **5277**；同步 `l10n/data`＋`client/MHFCT4.1/dat/mhfdat.bin`
  - 殘：beads／seals stub 待獨立 QA（勿重翻）
  - 舊切片→`issues/items-name/all-rest/_deprecated_index_split/`

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

- status: qa_issues
- notes: "2026-10-05 獨立 QA＋修譯：標記 1397→318（need 196／trunc 121／long 1）；validate PASS；issue→armors/qa-armors.md。Gate4 舊回寫仍在；本輪 CSV 未再 finish_batch。"

### files

- path: l10n/working/csv/dat-armors-head.csv
  status: qa_issues
  notes: "QA 修訂已寫入 CSV；待使用者指示再回寫本體"

---

## armors-body

- status: qa_issues
- notes: "2026-10-05 同五部位 QA／修譯；見 qa-armors.md。"

### files

- path: l10n/working/csv/dat-armors-body.csv
  status: qa_issues
  notes: "QA 修訂已寫入 CSV"

---

## armors-arms / armors-waist / armors-legs

- status: qa_issues
- notes: "2026-10-05 同五部位 QA／修譯；原始計數見 qa-armors.md／qa-transliteration。"

### files

- path: l10n/working/csv/dat-armors-arms.csv
  status: qa_issues
  notes: "QA 修訂已寫入 CSV"

- path: l10n/working/csv/dat-armors-waist.csv
  status: qa_issues
  notes: "QA 修訂已寫入 CSV；long_phon 殘 #681"

- path: l10n/working/csv/dat-armors-legs.csv
  status: qa_issues
  notes: "QA 修訂已寫入 CSV；truncate 誤報多在本槽"

---

## monsters-description

- status: translated
- notes: "2026-10-04 圖鑑說明 142 全譯；validate PASS；delta 139 回寫；review→issues/monsters/。"

### files

- path: l10n/extracted/（dat-monsters-description）
  status: translated
  notes: "抽出完成"

- path: l10n/working/csv/dat-monsters-description.csv
  status: translated
  notes: "still_need=0"
