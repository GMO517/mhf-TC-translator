# Phase 3 工作循環（Source of Process）

> Agent 執行翻譯時依本檔循環，**不必每步向使用者要「下一步」或複審確認**。  
> 品質複審找 **subagent**，不是使用者。  
> 僅在真正阻塞（缺備份、工具壞、方針衝突）時才停下來問。  
> 合適段落主動 `commit`（管線／單 section／一批譯文），避免一次還原過多。

## 使用者定下的循環

1. **部分處理**  
   一次只做一個可驗收的小範圍（一個 xpath／一批列），保留前後文與詞庫一致性。
2. **另開 agent 檢視翻譯品質**  
   對照 `docs/STYLE.md`、`l10n/glossary/terms.csv`、字型閘門報告；輸出 PASS／FAIL＋具體問題。
3. **分支**  
   - **PASS** → 擴大範圍（同 section 下一批，或下一 section）  
   - **FAIL** → 修正 → 重跑腳本閘門 → 再 call 檢查，直到 PASS
4. **持續做到完**  
   不因「等使用者說下一步」而中斷；文件與 `docs/TODO.md` 隨時更新。

## 「完」的層次

| 層次 | 內容 | 本輪預設 |
|---|---|---|
| A | 6 個已抽出 xpath 的**詞庫精確命中**列譯完並回寫 | **先做完** |
| B | 同 xpath 內未入庫英文名／說明長文 | A 完成後接續 |
| C | pac／skills／menu、劇情等 | Phase 4／另案 |

## 單批標準步驟

```
選範圍 → 填 l10n/working/csv
      → 腳本閘門（白名單／CP932／placeholder／未譯列保留原文）
      → 產出 reports/
      → subagent 品質複審
      → FAIL：修正並重審；PASS：回寫
      → 指紋比對後寫入 l10n/data，再同步 client/MHFCT4.1（需 _backup 存在）
      → 更新 docs/TODO.md → 下一批
```

## 品質複審檢查清單（給複審 agent）

- 詞庫已核准譯名是否被改壞或漏用 `fallback_glyph` 顯示形  
- 佔位符 `{j}` `{cNN}` `{/c}` 等未破壞  
- 用字：台灣繁中、半形數字、全形標點；MH 共通詞依荒野；Frontier 依既定詞庫  
- 明顯誤配（英文 source 對到錯誤詞條）必須 FAIL  
- 暫用形（罠／鎌／剥／猫 等）可過，但不可默默改回缺字繁體

## 與腳本的對應

詳見 `l10n/working/PIPELINE.md`。  
本檔管**節奏與決策**；PIPELINE 管**指令與路徑**。
