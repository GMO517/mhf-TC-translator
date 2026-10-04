# Phase 3 管線（指令與路徑）

節奏見 `docs/PHASE3-LOOP.md`。

## 日常一批（省時）

```bash
python next_batch.py items-name 200
# → subagent 產 reports/batch-items-00N.json 並 apply+validate
python finish_batch.py reports/batch-items-00N.json
# → validate + 只回寫本批 delta + 同步本體
# → 再 git commit 本批
```

## 腳本

| 檔 | 用途 |
|---|---|
| `apply_glossary_section.py` | 層次 A 詞庫命中 |
| `next_batch.py` | 列出未譯候選 |
| `apply_batch_json.py` | 合併批次譯文＋charset |
| `validate_working.py` | 白名單／CP932／placeholder |
| `writeback_sections.py --batch …` | **只回寫該批** |
| `writeback_sections.py --all-changed …` | 全量（慢，少用） |
| `finish_batch.py` | validate＋delta 回寫一鍵 |

## 注意

- working CSV：**UTF-8 無 BOM**  
- FTH 產物：`output/mhfdat-modified.bin`（腳本會拷回）  
- 狀態：`reports/writeback-state.json`（已回寫過的 index 累計）  
- 暫存目錄：`_writeback_work_*`／`_verify*`（gitignore）
