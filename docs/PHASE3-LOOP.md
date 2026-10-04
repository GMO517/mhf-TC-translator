# Phase 3 工作循環（Source of Process）

> Agent 執行翻譯時依本檔循環，**不必每步向使用者要「下一步」或複審確認**。  
> 品質複審找 **subagent**，不是使用者。  
> 僅在真正阻塞（缺備份、工具壞、方針衝突）時才停下來問。  
> 合適段落主動 `commit`（管線／一批譯文），避免一次還原過多。  
> **禁止**把過期的背景行程通知當現況複述。

## 分批原則（依分類，不再依固定筆數切片）

以 **內容分類／xpath section** 為單位推進，不要再用 `batch 01…N` 每 80／200 筆切道具表。

| 分類 | 對應 | 完成定義 |
|---|---|---|
| **名詞／詞庫** | `l10n/glossary/` | 審核＋display_ok（層次 A 已大致完成） |
| **道具** | `dat/items/name` | 該 section 未譯列處理完（或分段時以**子類**切：消耗品／素材／裝飾珠／票券…） |
| **武器名** | `dat/weapons/melee/name`、`ranged/name` | 近戰／遠程可分兩段 commit |
| **防具名** | `dat/armors/head`、`body` | 頭／身可分兩段 |
| **文本／說明** | `dat/monsters/description` 等長文 | 以圖鑑／說明段為批，用語感樣本校準後整類推進 |
| **系統／UI**（後續） | pac／menu 等 | Phase 4 |

道具表若仍太大，**依遊戲內子類**切（例：消耗品→素材→彈瓶→裝飾品→票券），不要依 index 流水號硬切固定筆數。

### 單類標準步驟

```
1. 選定分類／子類（寫進 batch JSON 的 label）
2. subagent 譯該範圍 → apply + validate
3. finish_batch.py（delta 回寫）
4. commit（訊息標分類，不用「第 N 批」中文數字流水）
5. 下一分類；勿開多個同質背景 agent 搶跑
```

### Commit 訊息

- 標**分類**：`feat: items-name 消耗品`／`feat: monsters-description 樣本`  
- 若暫用缺字，subject／body 寫清對照  
- 舊的 `batch 01–18` 流水僅作歷史；**新工作不再開 batch-019+**

## 回寫

- 日常：`finish_batch.py`／`writeback_sections.py --batch`（delta）  
- 全量（少用）：`--all-changed <section-id>`

## 「完」的層次

| 層次 | 內容 |
|---|---|
| A | 6 xpath 詞庫命中（已完成並回寫） |
| B | 依分類清完已抽出 section（道具→武器→防具→說明文本） |
| C | pac／skills／menu、劇情 → Phase 4 |

## 品質複審檢查清單

- 詞庫顯示形／fallback 未寫回缺字繁體  
- 佔位符未破壞  
- 台灣繁中、半形數字、全形標點  
- 誤配必須 FAIL  

詳指令見 `l10n/working/PIPELINE.md`。
