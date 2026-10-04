# 詞語庫（glossary）

**審閱主檔：`REVIEW.md`（人手改這裡）**  
機器可讀主檔：`terms.csv`

## 最終三步

| 步 | 腳本 | 用途 |
|---|---|---|
| 1 | `step1_build_glossary.py` | 從 `l10n/extracted/`＋種子**重建** `terms.csv` 初稿（會覆寫 CSV；平常不要跑） |
| 2 | `step2_write_review.py` | 從 `terms.csv` **整檔重寫** `REVIEW.md` 版面（有手改時禁止直接跑） |
| 3 | `step3_sync_review_to_csv.py` | 以 `REVIEW.md` 為準，把繁中回寫 `terms.csv`（**日常審完後跑這個**） |

日常流程：改 `REVIEW.md` → 跑 step3。

若必須跑 step2：先 step3 把 REVIEW 手改併進 CSV，再 step2。

中間一次性腳本已刪除，過程見 `HISTORY.md`。
