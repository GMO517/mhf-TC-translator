# Phase 3 管線（指令與路徑）

節奏見 `docs/PHASE3-LOOP.md`。  
**分批依分類**（道具／武器／防具／說明文本／詞庫），不用固定筆數流水號。

## 日常（一類或一子類）

```bash
# 依分類挑列、產 JSON（label 寫子類，如 items-consumables）
# → apply_batch_json.py → validate_working.py <section>
python finish_batch.py reports/<batch-label>.json
# → git commit（訊息標分類＋缺字）
```

`next_batch.py` 仍可用來列未譯候選，但 **limit 僅輔助**，規劃以子類為準，勿再開 `batch-019` 這類流水。

## 腳本

| 檔 | 用途 |
|---|---|
| `apply_glossary_section.py` | 層次 A 詞庫命中 |
| `next_batch.py` | 列出未譯候選（輔助） |
| `apply_batch_json.py` | 合併譯文＋charset |
| `validate_working.py` | 白名單／CP932／placeholder |
| `writeback_sections.py --batch …` | 只回寫該批 |
| `finish_batch.py` | validate＋delta 回寫 |

## 注意

- working CSV：**UTF-8 無 BOM**  
- FTH 產物：`output/mhfdat-modified.bin`  
- 狀態：`reports/writeback-state.json`  
- 暫存：`_writeback_work_*`／`_verify*`（gitignore）
