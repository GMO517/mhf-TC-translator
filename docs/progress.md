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

- status: in_progress
- notes: "2026-10-05 分層 series-dict 主線 P0：`weapon_stem_tiers.tsv`＋`issues/weapons/type-dict.md`；**未**改 CSV。舊 translated 為層次 B 殘零。"

### files

- path: l10n/working/csv/dat-weapons-melee-name.csv
  status: translated
  notes: "`_session_jp_weapon_names` WEAPON_KATA＋charset 安全；殘英 lex／manual remain"

---

## weapons-ranged-name

- status: in_progress
- notes: "2026-10-05 與近戰共用武器 series-dict；P0 掃描完成，待人審 type／stem。"

### files

- path: l10n/working/csv/dat-weapons-ranged-name.csv
  status: translated
  notes: "片假名 batch jp-kata；殘英 manual remain"

---

## armors-head

- status: qa_done
- notes: "2026-10-05 防具收尾 QA 0；已全量回寫 mhfdat（見 logs/writeback.md）。"

### files

- path: l10n/working/csv/dat-armors-head.csv
  status: qa_done
  notes: "14594 列；qa-transliteration 0 命中"

---

## armors-body

- status: qa_done
- notes: "2026-10-05 同五部位收尾；見 qa-armors.md。"

### files

- path: l10n/working/csv/dat-armors-body.csv
  status: qa_done
  notes: "13462 列；QA 0"

---

## armors-arms / armors-waist / armors-legs

- status: qa_done
- notes: "2026-10-05 五部位機械 QA 清零。"

### files

- path: l10n/working/csv/dat-armors-arms.csv
  status: qa_done
  notes: "13452 列；QA 0"

- path: l10n/working/csv/dat-armors-waist.csv
  status: qa_done
  notes: "13708 列；QA 0"

- path: l10n/working/csv/dat-armors-legs.csv
  status: qa_done
  notes: "13514 列；QA 0"

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
