# batches

| 子目錄 | 用途 |
|--------|------|
| `active/` | Translator **進行中**語意批次（例：票券） |
| `awaiting_qa/` | 已寫入 CSV、**待獨立 QA**；禁止當未譯重做 |
| `legacy/` | 歷史流水號／誤切 A–D；僅溯源，以 CSV 為準 |

用法：

```bash
python apply_batch_json.py batches/active/<name>.json
python finish_batch.py batches/active/<name>.json
```

待審隊列：`../issues/queue.md`。
