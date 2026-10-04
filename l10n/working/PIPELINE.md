# Phase 3 管線（指令與路徑）

工作流：`docs/agent-translation-playbook.md`。  
節奏：`docs/PHASE3-LOOP.md`。分類狀態：`docs/progress.md`。  
**待審隊列：`issues/queue.md`（已譯勿重做）**。  
目錄契約：`README.md`＋`paths.py`。

## 目錄

| 路徑 | 用途 |
|---|---|
| `csv/` | 譯文 CSV（主真相） |
| `batches/active/` | 進行中語意批次 |
| `batches/awaiting_qa/` | 已譯待 QA |
| `batches/legacy/` | 歷史流水號歸檔 |
| `state/` | `writeback-state.json` |
| `logs/` | validate／writeback／apply |
| `catalogs/` | 一覽 |
| `scratch/` | `next-*.json`（gitignore） |
| `issues/` | QA 隊列與問題 |

## 日常

```bash
python apply_batch_json.py batches/active/<batch-label>.json
python validate_working.py <section>
python finish_batch.py batches/active/<batch-label>.json
# 子類完成才 commit；工作進度保全可另 commit（見 issues/queue.md）
```

`next_batch.py` → `scratch/`。  
**禁止** `batch-items-019`／`tickets-e`；票券累積進 `batches/active/batch-items-tickets.json`。

## 腳本

| 檔 | 用途 |
|---|---|
| `paths.py` | 路徑契約 |
| `apply_glossary_section.py` | 層次 A → `logs/*-apply.md` |
| `next_batch.py` | 候選 → `scratch/` |
| `apply_batch_json.py` | 合併譯文＋charset |
| `validate_working.py` | → `logs/validate.md` |
| `writeback_sections.py` | → `state/`＋`logs/writeback.md` |
| `finish_batch.py` | validate＋delta |

## 注意

- CSV：UTF-8 無 BOM  
- 暫存：`_writeback_work_*`／`_verify*`／`scratch/`（gitignore）
