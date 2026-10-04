# Phase 3 工作循環（技術節奏）

> **最高優先**：`docs/agent-translation-playbook.md`（角色、停止條件、QA／Fixer）。  
> 本檔只補 **子類優先序、finish_batch／commit、禁流水切片** 等技術細節。  
> Translator 執行時依本檔循環，**不必每步向使用者要「下一步」**；最終 QA 必須換獨立 agent／對話。  
> 僅在真正阻塞（缺備份、工具壞、方針衝突）時才停下來問。  
> Commit 以**子類完成**為主（見 playbook Part A）；禁止續段字母／batch N 當結案單位。  
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

### 道具子類（粗分，禁止再切 A/B/C 或 batch N）

子類是**語意分類**，一類做到完再換下一類。  
**禁止**：`tickets-a/b/c`、`batch 19`、每 150 筆一刀——那只是換皮的流水號。

內部若因 token／FTH 需分段執行，仍算**同一子類未完成**；可多次 apply／delta 回寫，但：
- JSON／commit **不要**用 A/B/C／續段編號當主名稱  
- **commit 以「子類完成」為主**（或使用者同意的自然斷點，如「武器票」vs「防具票」語意斷點，而非筆數）

優先序（為品質）：

1. 詞庫已有  
2. 技能珠／SP・G 珠  
3. Frontier 情報／專有道具（STYLE 五步）  
4. 消耗品／調合／陷阱彈刀  
5. 魔物素材  
6. 採集素材  
7. **票券／勳章／活動**（整類做完）  
8. 其餘  

### 單類標準步驟

```
1. 選定一個子類（例：票券）— 做到該子類清完
2. 批次 JSON：進行中→`batches/active/`；譯完待審→`batches/awaiting_qa/`；歷史誤切→`batches/legacy/`；隊列見 `issues/queue.md`
3. 可多輪 agent／apply／delta 回寫，但不另立「續段字母」
4. 子類完成 → 一次（或少數）commit：feat: items-name 票券
5. 下一子類
```

### Commit 訊息

- 標**子類完成**：`feat: items-name 票券`  
- 缺字寫進 body  
- 歷史上的 `batch 01–18`／`tickets-a…d` 僅作遺留，**不再新增**

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
