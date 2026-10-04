# Phase 3 工作循環（Source of Process）

> Agent 執行翻譯時依本檔循環，**不必每步向使用者要「下一步」或複審確認**。  
> 品質複審找 **subagent**，不是使用者。  
> 僅在真正阻塞（缺備份、工具壞、方針衝突）時才停下來問。  
> 合適段落主動 `commit`（管線／一批譯文），避免一次還原過多。  
> **禁止**把過期的背景行程通知當現況複述。

## 標準循環（層次 B：道具名等）

```
1. next_batch.py <section> 80          → 候選
2. subagent 只譯「這一 batch」         → batch-XXX.json
3. apply_batch_json.py + validate      → 寫入 working CSV
4. finish_batch.py batch-XXX.json      → 只回寫本批 delta → 本體
5. commit 本批（csv／batch json／writeback*）
6. 立刻開下一批；不要重講舊進度
```

### 為何一定要用 delta 回寫

FTH 每次會重建整個 section 並 compress+encrypt。  
若每次把「累積全部已譯列」送進去，第 N 批會越寫越慢、白耗時間。  
**只送本批 index** 即可疊加進目前的 `mhfdat.bin`。

全量回寫僅在修復／對齊異常時用：

```bash
python writeback_sections.py --all-changed items-name
```

## 使用者定下的原則

1. **部分處理** — 一小批可驗收範圍  
2. **subagent 檢品質** — PASS 才擴大；FAIL 修正再審  
3. **做到完** — 不等人喊下一步  
4. **分段 commit** — 一批一 commit（或一種類一 commit）

## 「完」的層次

| 層次 | 內容 |
|---|---|
| A | 6 xpath 詞庫命中（已完成並回寫） |
| B | 未入庫英文名／說明長文（進行中：items-name） |
| C | pac／skills／menu、劇情 → Phase 4 |

## 品質複審檢查清單

- 詞庫顯示形／fallback 未寫回缺字繁體  
- 佔位符未破壞  
- 台灣繁中、半形數字、全形標點  
- 誤配必須 FAIL  

詳指令見 `l10n/working/PIPELINE.md`。
