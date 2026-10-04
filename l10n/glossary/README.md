# 詞語庫（glossary）

**審閱主檔：`REVIEW.md`（人手改這裡）**  
機器可讀主檔：`terms.csv`  
**翻譯中待決專名：`PENDING.md`**（拿不定／曾半翻者；子類完成後一次定稿再回修）

命名原則見 `docs/STYLE.md`：系列→荒野；Frontier 專有→台服 wiki 為主，但 wiki 可能缺漏／與日服不一致，缺條或衝突時對照日服補齊。  
**禁止半翻**（`Ｃクレスト` 類）；見 STYLE。

## 最終三步（腳本）

| 步 | 腳本 | 用途 |
|---|---|---|
| 1 | `step1_build_glossary.py` | 從 `l10n/extracted/`＋種子**重建** `terms.csv` 初稿（會覆寫 CSV；平常不要跑） |
| 2 | `step2_write_review.py` | 從 `terms.csv` **整檔重寫** `REVIEW.md`（**只輸出未審**；有手改先 step3） |
| 3 | `step3_sync_review_to_csv.py` | 以 `REVIEW.md` 為準回寫 `terms.csv` 繁中／✓ |

## 建議作業節奏（定稿）

1. **補詞**：新條目寫入 `terms.csv`（`approved=N`）→ 跑 step2 → 只在 `REVIEW.md` 審未審列  
2. **審完**：✓ 改 `Y`（或代核准）→ step3（若手改過繁中）→ step2 清空未審區  
3. **定稿**：相關變更 **commit**（不擅自 push）  
4. **原則**：`REVIEW` 不堆已核准；已核准只在 `terms.csv`；命名見 `docs/STYLE.md`

中間一次性腳本已刪除，過程見 `HISTORY.md`。
