# 遊戲翻譯 Agent 強制工作流（父規範）

## 核心目標（一切規則服務這三點）

1. **加快翻譯時程**（子類連續推進，少停少問）  
2. **控制 token**（開場少讀、少重複盤點、少改規則）  
3. **維持品質底線**（不壞檔、不壞標記、不誤導、不高頻專名亂飄、不寫缺字）

若某條規定讓你反覆讀檔、重 scrub、停等確認卻不推進譯文——**那條執行錯了**，回到本節目標。

---

## 規則父子與衝突裁決

```
使用者當下口令
  └── 本 playbook（只讀 Part A + 附錄查表；禁止開場通讀舊通用長文）
        ├── STYLE + charset + terms     → 怎麼寫字
        ├── PHASE3-LOOP + PIPELINE      → 怎麼跑管線
        ├── progress / queue            → 做到哪
        ├── TODO.md                     → 工程閘門（Gate，勿稱翻譯 Phase）
        ├── MCP-TOOLS / .cursor/rules   → 工具；不得每步打斷
        └── PENDING.md                  → 待裁定專名表（不叫停主線）
```

**高→低：** 使用者口令 → 本 Part A → STYLE／charset → PHASE3／PIPELINE → progress／TODO → Cursor 通用規則／MCP  

**日常翻譯：** 以本 Part A＋PHASE3 為準，**不必每步確認、不必叫 feedback**（MCP 沒有就略過）。  
**才准停問：** 缺 `_backup`、工具壞、方針真衝突、使用者明示要審、大改本體方針。  

**禁止**把 STYLE 辯論、PENDING 改欄、開場整庫重讀當成停工理由。

---

# Part A — 本專案規則

## A.0 身分

| 項 | 定案 |
|---|---|
| 遊戲 | MHF 私服 CT4.1 |
| 範圍 | 本機自用；本體不上 git；不追更重翻 |
| AI | 只用 Cursor；禁止外部翻譯 API／平台 MCP |
| 品質底線 | 見「核心目標」第 3 點；文筆小瑕可留 |

## A.1 路徑（摘要）

| 用途 | 路徑 |
|---|---|
| 譯文 | `l10n/working/csv/` |
| 批次 | `l10n/working/batches/{active,awaiting_qa,legacy}/` |
| 隊列／issues | `l10n/working/issues/` |
| 詞庫 | `l10n/glossary/terms.csv`＋`REVIEW.md`＋`PENDING.md` |
| 風格／字型 | `docs/STYLE.md`＋`l10n/charset/` |
| 狀態 | `docs/progress.md`（分類）／`docs/TODO.md`（工程 Gate） |
| 本體 | `client/MHFCT4.1/`（改前 `_backup/`） |

完整對照若需要見 git 歷史；**日常不必重讀長表**。

## A.2 完成單位（釘死）

- 一次任務＝**一種角色**＋**一個語意單位**  
- 語意單位＝`CATEGORY` 或 `CATEGORY/子類`（例：`items-name/tickets`、`items-name/consumables`）  
- **Translator 停止條件／commit 單位＝該語意單位清完**（不是整份 `items-name` 一次做完才准停；也不是 batch N）  
- **禁止** `tickets-a/b/c`、`batch-019`、每 N 筆當結案名  
- 內部可多次 apply／delta；產物累積同一語意 JSON（例：`batch-items-consumables.json`）

## A.3 Translator（主線＝翻譯）

**開場只讀（≤4 步，然後動手）：**

1. 本文件「核心目標」＋本 Part A（角色／完成單位）  
2. `progress.md`＋`issues/queue.md`  
3. 該子類 CSV 未譯列（必要時 `PHASE3-LOOP` 看優先序）  
4. 碰到用字才查 `STYLE.md`／`terms.csv`——**禁止**開場必讀整份 STYLE＋REVIEW＋TODO＋全 CSV  

**執行循環：**

1. 選定一個未完成子類 → 譯 → `apply_batch_json.py` → `validate_working.py`  
2. 日常可 `finish_batch.py` delta；更新 `progress.md`／`queue.md`  
3. 子類告一段落（finish／awaiting_qa）時：產 `issues/review-<單位>.md`（**完整**原文→譯文表，供**最終**確認）→ **不中斷、不等使用者當場批完**  
4. 子類未完：**禁止**只交摘要就停；繼續下一批內部切片  
5. 專名：STYLE **先整名、再詞庫／義譯／音譯**；魔物素材魔物名必對齊 `terms.csv`／Info；**禁止**把普通英文詞拆開音譯  
6. PENDING：漢字暫譯＋列待裁定；**不中途逐條問**；子類完再請使用者填決定 → 另開 Fixer  

**機械自檢（子類宣告 translated 前）：** charset／CP932／半翻／片假名混中文警告／`{j}` 段數。  

**禁止：** 自稱 QA 通過；一次多子類；為文筆改標記；半翻／片假名混中文充數；為改規則格式停主線。

## A.4 QA／Fixer

| 角色 | 做 | 不做 |
|---|---|---|
| QA | 新對話；全量子類檢查；只寫 `issues/<單位>.md`；預設不改譯文 | 全面重翻、文筆潤飾當阻塞 |
| Fixer | 只修 issues 的 blocking／high；validate；更新 issue／progress | 借機大範圍重翻 |

QA **預設不改檔**；僅使用者明示或 blocking 且無法只靠 Fixer 時例外（寫進 issue）。

## A.5 工程閘門（大批回寫本體前）

`TODO.md` 用 **Gate** 稱呼，避免與舊「翻譯 Phase」混淆：

1. Gate0 離線 round-trip PASS  
2. Gate0.5 字型 whitelist／fallback 可用  
3. 高頻詞已有審核節奏（不是每條都要進 PENDING）  
4. `_backup/` 存在  

## A.6 寫入約束（一行版）

CSV UTF-8 無 BOM；用字見 STYLE；禁半翻／片假名混中文；缺字走 fallback；本體 bin 不進 git。

## A.7 Commit

- 預設：**子類完成**才 commit（或使用者要求的保全點）  
- 格式依使用者 git 規則；禁 Cursor 署名；禁擅自 push  

## A.8 啟動模板

```text
角色：Translator
分類：items-name/consumables
嚴格依 docs/agent-translation-playbook.md（核心目標＋Part A）執行。
開場精簡讀；子類完成前不得只交摘要就停。
```

```text
角色：QA
分類：items-name/tickets
只寫 issues；預設不改譯文；全量檢查完才停。
```

```text
角色：Fixer
分類：items-name/tickets
只修 blocking／high。
```

---

# 附錄 — 查表用（禁止開場通讀）

> 舊「通用 Part B」長文已刪除重複敘事。以下僅在 QA／裁決時查。

## 附錄 A｜嚴重度

- **blocking**：壞檔／壞標記／空譯／會讓玩家做錯／不可顯示字寫入／高頻專名嚴重衝突  
- **high**：違反 glossary 定譯、關鍵 UI 難懂、重要意思偏差  
- **low**：翻譯腔、極低頻不統一、非關鍵略長——**可留，不為此停**

## 附錄 B｜品質優先級

1. 不壞檔與標記  
2. 不誤導操作／任務  
3. glossary／高頻一致  
4. 子類完成  
5. 用語自然  
6. 文筆（最低）

## 附錄 C｜issues 骨架

```markdown
# QA: <CATEGORY或子類>
- progress_suggestion: qa_done | qa_issues
- blocking_open: <N>
- high_open: <N>
- low_open: <N>
## blocking
### ISSUE-001
- status: open
- file: l10n/working/csv/...
- locator: index_or_line
- source: "..."
- current: "..."
- problem: "..."
- suggestion: "..."
```
