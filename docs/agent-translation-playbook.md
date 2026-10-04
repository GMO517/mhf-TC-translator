# 遊戲翻譯 Agent 強制工作流（本專案定稿）

本文件是 **Agent 翻譯／審核／修復的最高優先規則**。  
與使用者臨時指示衝突時：若臨時指示更嚴格則服從臨時指示；否則以本文件為準。  
與舊節奏文件衝突時：以 **Part A（本專案特殊規則）** 覆蓋路徑與批次細節；通用角色／停止條件以 **Part B** 為準。

---

# Part A — 適用本專案的特殊規則

## A.0 專案身分

| 項 | 定案 |
|---|---|
| 遊戲 | Monster Hunter Frontier（私服客戶端 CT4.1） |
| 範圍 | 本機自用；不上傳本體；不做公開發佈／追更重翻 |
| AI | 只用 Cursor；**禁止**外部翻譯 API／平台 MCP 做翻譯 |
| 工具鏈 | FrontierTextHandler（FTH）＋ `l10n/working/` Python 管線 |
| 品質 | 允許少量文筆瑕疵；**禁止**壞檔、壞標記、意思誤導、高頻專名漂移、字型缺字寫入 |

## A.1 路徑契約（取代通用稿的目錄名）

通用稿的目錄名**不另建平行樹**；一律對應如下：

| 通用契約 | 本專案實際路徑 |
|---|---|
| `docs/agent-translation-playbook.md` | **本文件** |
| `style-guide.md` | `docs/STYLE.md` |
| `glossary.yaml` | `l10n/glossary/terms.csv`（機器）＋ `REVIEW.md`（審閱）＋ `README.md`（節奏） |
| `progress.md` | `docs/progress.md`（分類狀態機） |
| `source/` | `l10n/extracted/` |
| `translated/` | `l10n/working/csv/`（譯文側） |
| `issues/<CATEGORY>.md` | `l10n/working/issues/<CATEGORY>.md` |
| （工程總進度） | `docs/TODO.md`（Phase 閘門；**不是**分類狀態機） |
| （技術循環） | `docs/PHASE3-LOOP.md`＋ `l10n/working/PIPELINE.md` |
| （字型閘門） | `l10n/charset/`（whitelist／fallback） |
| （二進位工作複本） | `l10n/data/`（gitignore） |
| （遊戲本體） | `client/MHFCT4.1/`（gitignore；改前確認 `_backup/`） |

**雙檔進度分工（禁止雙源打架）：**

- `docs/TODO.md`：Phase 0～4、閘門、明確不做項  
- `docs/progress.md`：單一 `<CATEGORY>` 的 `pending` → `qa_done`  
- 禁止再裝待辦／記憶類 MCP 當第三進度源  

## A.2 分類（CATEGORY）定義

一次任務只做**一個** CATEGORY。本專案 CATEGORY＝抽出 section／語意子類，不是「第 N 批 80 筆」。

| CATEGORY（建議 ID） | 來源 | 譯文 CSV |
|---|---|---|
| `items-name` | `dat/items/name` | `l10n/working/csv/dat-items-name.csv` |
| `items-name/tickets` | 道具子類：票券／勳章／活動票 | 同上（子類進度寫在 progress notes） |
| `items-name/beads` | 道具子類：技能珠／SP・G | 同上 |
| `weapons-melee-name` | `dat/weapons/melee/name` | `dat-weapons-melee-name.csv` |
| `weapons-ranged-name` | `dat/weapons/ranged/name` | `dat-weapons-ranged-name.csv` |
| `armors-head` | `dat/armors/head` | `dat-armors-head.csv` |
| `armors-body` | `dat/armors/body` | `dat-armors-body.csv` |
| `monsters-description` | `dat/monsters/description` | 對應 working CSV |

道具若仍太大，**只允許語意子類**（消耗品／素材／珠／票券…），見 `PHASE3-LOOP.md`。

### A.2.1 絕對禁止的切片方式

- `batch-items-019`、`tickets-a/b/c/d/e`、每 150 筆一刀當「完成單位」  
- 用流水號當 commit 主體（`feat: … 續段C`）  
- JSON／commit **不要**用 A/B/C／續段編號當主名稱  

內部因 token／FTH 需分段執行時：仍算**同一 CATEGORY 未完成**；可多次 apply／delta，產物累積進語意檔名（例：`batch-items-tickets.json`），**整類清完**再 commit：`feat: items-name 票券`。

## A.3 角色與本專案動作對照

### Translator

1. Phase 0：確認角色＋CATEGORY；資訊夠就直接做  
2. 必讀：本文件 → `STYLE.md` → `terms.csv`／`REVIEW.md` → `progress.md` → `TODO.md`（閘門）→ 該類 CSV／抽出  
3. 詞彙：高頻專名先入 `terms.csv`（未審走 REVIEW 節奏）；Frontier 音譯走 STYLE 五步  
4. 翻譯寫入 working CSV；`apply_batch_json.py` → `validate_working.py` →（日常）`finish_batch.py` delta 回寫  
5. 每推進一批立刻更新 `progress.md`；分類未完**禁止**只交摘要就停  
6. 機械自檢另加本專案項：charset／CP932／`display_ok`／fallback；佔位符 `{j}` `{cNN}` `{/c}` `{K…}` `{i…}` `{u…}`  

**禁止：** 自稱 QA 通過；一次多 CATEGORY；為文筆改標記。

### QA

- 新對話／新 agent；讀原文＋working CSV＋glossary＋STYLE  
- 只寫 `l10n/working/issues/<CATEGORY>.md`；預設**不改譯文**  
- 全量覆蓋該 CATEGORY（可分批檢查，最終必須蓋完）  
- 額外必查：字型白名單違規、Shift-JIS 不可編碼、明顯缺字繁體未走 fallback  

### Fixer

- 只修 issues 內 `blocking`／`high`  
- 修完跑 validate（必要時 finish_batch）；更新 issue 狀態與 `progress.md`  
- 不得借機大範圍重翻  

## A.4 本專案硬閘門（Translator 大批回寫前）

下列未滿足時，**不得**對本體做大批翻譯回寫（層次 A 已完成者除外；新譯文仍須通過 validate）：

1. Phase 0 離線 round-trip PASS（見 `l10n/roundtrip/RESULT.md`）  
2. Phase 0.5 字型白名單／fallback 可用  
3. 詞語庫已審核節奏（高頻定譯不得漂移）  
4. 改本體前 `_backup/` 存在  

## A.5 編碼與寫入約束

- working CSV：**UTF-8 無 BOM**  
- 數字半形、標點全形、台灣漢字（見 `STYLE.md`）  
- MH 系列詞以《荒野》為準；Frontier 專有以 MHFO 台灣 wiki 為主，衝突則對照日服／可信來源  
- 無法顯示之字：用 `fallback_glyph`／詞庫註記形，禁止硬寫缺字  
- FTH 產物：`*-modified.bin`；狀態：`l10n/working/reports/writeback-state.json`  
- **禁止**把本體二進位加入 git commit  

## A.6 Commit 與 Git（翻譯任務內）

- 僅在使用者要求，或 playbook／PHASE3-LOOP 允許的「子類完成／管線節點」時 commit  
- 訊息格式依使用者 git 規則（兩層：`type: 短標題`＋`調整項目:`）  
- 禁止 Cursor `Co-authored-by`；用空 hooksPath 若使用者規則要求  
- **禁止擅自 push**  

## A.7 與舊文件的關係

| 文件 | 角色 |
|---|---|
| **本 playbook** | 角色、停止條件、QA／Fixer、分類狀態機 |
| `PHASE3-LOOP.md` | 子類優先序、finish_batch／commit 節奏細節 |
| `PIPELINE.md` | 具體指令與腳本表 |
| `TODO.md` | Phase 總覽 |
| `MCP-TOOLS.md` | 不裝待辦 MCP；feedback 僅用於閘門確認 |

開場必讀順序（精簡）：

1. 本文件 Part A（知對應與禁切片）  
2. Part B 與自己角色相關章節  
3. `docs/progress.md`、`docs/STYLE.md`、`docs/TODO.md`  
4. 該 CATEGORY 的 CSV／issues  

## A.8 啟動指令模板（本專案）

### Translator

```text
角色：Translator
分類：items-name/tickets
嚴格依 docs/agent-translation-playbook.md 執行。
完成該分類並通過翻譯方自檢前不得停止。
技術步驟見 docs/PHASE3-LOOP.md 與 l10n/working/PIPELINE.md。
```

### QA

```text
角色：QA
分類：items-name/tickets
嚴格依 docs/agent-translation-playbook.md 執行。
只寫 l10n/working/issues/<CATEGORY>.md；預設不直接改譯文。
全量檢查完成前不得停止。
```

### Fixer

```text
角色：Fixer
分類：items-name/tickets
嚴格依 docs/agent-translation-playbook.md 執行。
只修 issues 內 blocking／high，修完更新 issue 與 docs/progress.md。
```

---

# Part B — 通用強制工作流（原文收錄）

> 下列為通用規則全文。路徑名若與 Part A 衝突，**以 Part A 對照表為準**。  
> 詞彙庫檔名以 `terms.csv` 為準（勿新建平行 `glossary.yaml`，除非使用者明確要求遷移）。

## 0. 適用前提

- 場景：單機遊戲、自用或少數朋友使用
- AI：只用 Cursor；不得改呼叫外部翻譯 API／MCP 做翻譯
- 不做：ParaTranz、Crowdin、Locize、Lara、DeepL 等平台流程
- 不做：遊戲版本更新後的增量重翻流程（本專案不處理追更）
- 品質取向：允許少量文筆瑕疵；**禁止**造成壞檔、壞標記、意思誤導、高頻專名漂移

---

## 1. 角色與任務邊界

每次啟動只擔任**一種角色**。使用者未指定時，先問清楚再開始；若使用者已指定分類與角色，直接執行。

### 1.1 角色 A：翻譯 Agent（Translator）

**可以做：**

- 讀取原文、詞彙庫、風格規則、進度
- 翻譯指定分類
- 更新譯文檔、詞彙庫、`progress.md`
- 做翻譯後的自我機械檢查

**禁止做：**

- 同時充當最終 QA 並宣告「已審核通過」
- 一次處理多個分類
- 為了文筆去改 placeholder／控制碼／檔案結構
- 未達停止條件就結束並只給摘要

### 1.2 角色 B：審核 Agent（QA）

**可以做：**

- 讀取原文、譯文、詞彙庫、風格規則、進度
- 產出 `issues/<CATEGORY>.md`
- 只修正「阻塞級」問題（見第 8 節／嚴重度），或只記錄不修改（依使用者指示；預設**只記錄**）

**禁止做：**

- 全面重寫譯文、潤飾文筆、統一「更好聽」的同義詞
- 把 low 級文筆問題當阻塞
- 擴大審核到未指定分類

### 1.3 角色 C：修復 Agent（Fixer）

- 只根據 `issues/<CATEGORY>.md` 中的 blocking／high 項目修改
- 修完後更新 issue 狀態與 `progress.md`
- 不得借機大範圍重翻

---

## 2. 必要檔案與目錄契約

若專案尚無下列結構，翻譯開始前先建立最小骨架，再開始翻譯。

```text
.
├── source/                      # → 本專案：l10n/extracted/
├── translated/                  # → 本專案：l10n/working/csv/
├── glossary.yaml                # → 本專案：l10n/glossary/terms.csv
├── style-guide.md               # → 本專案：docs/STYLE.md
├── progress.md                  # → 本專案：docs/progress.md
├── issues/                      # → 本專案：l10n/working/issues/
└── docs/agent-translation-playbook.md
```

### 2.1 `progress.md` 狀態（必須使用）

每個分類、每個檔案只能是以下狀態之一：

| 狀態 | 含義 |
|---|---|
| `pending` | 尚未開始 |
| `in_progress` | 翻譯中 |
| `translated` | 該檔／該分類已譯完，待 QA |
| `qa_issues` | QA 發現阻塞問題，待修復 |
| `qa_done` | QA 通過（無 blocking／high 未解項） |

**規則：**

- 開始翻譯某分類時，立即把該分類標為 `in_progress`
- 不得憑聊天記憶宣稱進度；一律以 `progress.md` 為準
- 已是 `translated` 或 `qa_done` 的檔案，不得無故重翻（除非使用者明確要求，或 Fixer 針對 issue 修改）

### 2.2 詞彙庫最小語義（本專案用 CSV）

通用 YAML 語義對應到 `terms.csv` 欄位（以檔內表頭為準），至少能表達：

- 原文／定譯／備註  
- 禁譯或「勿用 X、應用 Y」（可寫在 note／REVIEW）  
- 可顯示性／fallback（本專案 charset 相關欄）  

### 2.3 `style-guide.md` 最小要求

至少包含（本專案已由 `docs/STYLE.md` 覆蓋）：

- 目標：台灣繁體中文
- 稱謂／語氣：UI 簡潔／對話可自然；系統清楚、NPC 像人話
- 明確：「禁止只做簡轉繁；禁止保留簡中常用詞」

---

## 3. 總流程（嚴格順序）

對**單一分類** `<CATEGORY>` 必須按此順序：

```text
Phase 0  確認角色、分類、輸入輸出路徑
Phase 1  讀取規則與現況（playbook / glossary / style / progress）
Phase 2  詞彙預處理（該分類高頻專名先入庫）
Phase 3  分批翻譯並持續更新 progress（未完成不得停）
Phase 4  翻譯方機械自檢
Phase 5  換獨立 QA Agent 審核（新對話／新 agent）
Phase 6  若有 blocking／high → Fixer 修復 → 再 QA
Phase 7  標記 qa_done，輸出簡短完成報告
```

**硬性限制：**

1. 一次任務只做一個 `<CATEGORY>`
2. 翻譯與最終 QA 必須分開（不同 agent 或至少不同對話）
3. 未達該 Phase 停止條件，禁止進入「任務完成」話術並停下

---

## 4. Phase 細則

### Phase 0：啟動確認

開始前在心中（或簡短回覆）確認：

- 角色：Translator / QA / Fixer
- 分類：`<CATEGORY>`
- 原文路徑、譯文路徑
- 使用者是否允許 QA／Fixer 直接改檔（預設 QA 只寫 issues）

缺關鍵資訊且無法從 repo 推得時，先問再做。  
若資訊已足夠，不要反覆確認，直接執行。

### Phase 1：必讀

依序讀取：

1. `docs/agent-translation-playbook.md`（本文件）
2. 詞彙庫（`l10n/glossary/terms.csv` 等）
3. `docs/STYLE.md`
4. `docs/progress.md`
5. 該分類相關原文／working 檔

### Phase 2：詞彙預處理（Translator）

在大量翻譯前：

1. 掃該分類原文，抽出角色名、地名、技能名、物品名、組織名、UI 專用語
2. 已在 glossary 的：直接沿用
3. 未在 glossary 的高頻／會重複出現者：先寫入 glossary，再翻譯
4. 極低頻且無把握者：可先合理翻譯，並在 progress 或 issues 註記「待確認專名」；不得因此停止整個分類

### Phase 3：分批翻譯（Translator）

**批次規則（通用預設＋本專案覆蓋）：**

- 通用預設每批 30～80 條；**本專案完成單位是語意子類**，內部批次只是執行切片，不是結案單位  
- 每批完成後立刻寫入譯文側，並更新 `progress.md`  
- 寫完一批，若分類未完成：**立即繼續下一批**，禁止只輸出進度然後結束  

**翻譯規則（必須遵守）：**

1. 只改需要翻譯的文本值；不改 key、ID、路徑、欄位名、檔名結構  
2. 保留全部 placeholder／控制碼／富文本／腳本標記  
3. 看不懂的標記：**原樣保留**，不得刪除、翻譯、重排  
4. 已入庫詞彙：必須用定譯  
5. 禁譯詞：不得出現  
6. 目標語言：繁體中文；不得輸出簡體  
7. 意思優先於文筆；UI／任務／系統訊息尤須正確  
8. 主選單、按鈕、短標籤：優先短譯，避免可能截斷  
9. 不得憑空添加原文沒有的劇情／設定  
10. 編碼與格式：保持與原文檔一致的可用結構（JSON／YAML／CSV／PO 等不可破壞）

**遇到不確定：**

- 會影響操作或劇情理解：選較保守、可還原原文意思的譯法，並在該批摘要註記
- 純文筆偏好：自行決定，不詢問、不停止

### Phase 4：翻譯方機械自檢（Translator）

該分類全部條目進入譯完狀態前，必須完成：

- [ ] 無空譯（應翻譯的條目不得空白）
- [ ] placeholder／控制碼與原文對得起來
- [ ] 未改壞 key／結構
- [ ] glossary 定譯無明顯違反
- [ ] `progress.md` 該分類為 `translated`（或檔案級完成）
- [ ] （本專案）validate／charset／CP932 通過

自檢失敗：先修到通過，才可結束 Translator 任務。

### Phase 5：QA（QA Agent）

輸出檔：`l10n/working/issues/<CATEGORY>.md`（路徑見 Part A）

每個問題必須包含：

- 嚴重度：`blocking` / `high` / `low`
- 位置：檔案路徑 + key／行號／條目 ID
- 原文
- 現譯
- 問題原因
- 建議修法（簡短）

**只准檢查這些：**

1. 標記／控制碼／結構是否損壞（blocking）
2. 空譯、明顯漏譯（blocking／high）
3. glossary 定譯／禁譯違反（high；高頻為 blocking）
4. 會誤導玩家操作或任務理解的誤譯（high／blocking）
5. 關鍵 UI 過長到可能無法辨識（high；非關鍵 UI 放 low）
6. 明顯簡中用詞（high 或 low，視可讀性）
7. （本專案）字型／編碼不可顯示（blocking／high）

**不要做：**

- 全文潤色
- 同義詞品味之爭
- 為「更文學」而改正確譯文

QA 結束條件：

- 已完整覆蓋該分類（不是抽樣幾句就結束）
- issues 檔已寫好
- 若無 blocking／high：建議將 progress 標為 `qa_done`（若使用者要求 QA 不改 progress，則在報告說明）
- 若有 blocking／high：progress 標 `qa_issues`

### Phase 6：修復（Fixer）

1. 只處理 `blocking`、`high`
2. `low` 預設忽略（除非使用者要求）
3. 每修一項，更新 issue 狀態（例如 `open` → `fixed`）
4. 全部 blocking／high 關閉後，progress → `translated` 或直接交給再 QA
5. 再 QA 仍有 blocking／high：繼續修，不得宣告完成

### Phase 7：完成報告（極短）

僅在停止條件滿足後輸出：

- 分類名
- 處理檔案列表
- 新增／變更的 glossary 條目數
- 殘留 low 問題數量（如有）
- progress 最終狀態

---

## 5. 停止條件（未全部满足 = 禁止停止）

### 5.1 Translator 停止條件

必須全部为真：

1. 只處理了使用者指定的那一個分類  
2. 該分類所有應翻譯條目已寫入譯文側  
3. `progress.md` 中該分類（或其下所有檔）為 `translated`  
4. Phase 4 機械自檢通過  
5. 已給極短完成報告  

若尚未满足：繼續下一翻译批次。  
**禁止**使用「先到這裡」「其餘下次再做」「已示範流程」作為結束理由。

### 5.2 QA 停止條件

必須全部为真：

1. 該分類全量檢查完成（可分批，但最終必須覆蓋完）  
2. `issues/<CATEGORY>.md` 已更新且嚴重度已標好  
3. 已給極短 QA 結論：通過／需修復  

### 5.3 全流程（分類結案）停止條件

必須全部为真：

1. Translator 完成  
2. QA 完成  
3. 無未關閉的 `blocking`／`high`  
4. `progress.md` 為 `qa_done`  

---

## 6. 嚴重度定義（決策用）

### blocking（必須立刻修，否則不能 qa_done）

- 譯文導致檔案無效／明顯無法載入
- placeholder／控制碼缺失、被翻譯、被破壞
- 空譯（應有文本處）
- 任務／選項／系統提示誤譯到會讓玩家做錯
- 高頻專有名詞明顯多種譯法且衝突
- （本專案）寫入不可顯示字元導致壞字／驗證失敗

### high（結案前必須修）

- glossary 定譯被違反
- 禁譯詞出現
- 明顯簡中用詞導致難受讀
- 關鍵 UI（主選單／確認／取消／主要操作）過長到可能看不懂
- 重要對白意思偏差（未到完全反義也可能算 high）

### low（自用可留）

- 翻譯腔、不夠傳神
- 極低頻名稱不統一
- 非關鍵 UI 稍長
- 少數可接受的用詞偏好差異
- 語氣略平

---

## 7. 絕對禁止清單

1. 破壞或改寫 placeholder／控制碼／腳本標記  
2. 改 key、ID、檔案結構、無關係數值  
3. 輸出簡體中文當譯文  
4. 只用字形「簡轉繁」而不顧用語  
5. 未更新 `progress.md` 就宣稱完成  
6. 一次任務做多個分類  
7. 翻譯 Agent 自我宣布 QA 通過  
8. 為文筆犧牲正確性或標記安全  
9. 呼叫外部翻譯 API／平台 MCP 做翻譯  
10. 未达停止條件提前結束  

---

## 8. 可接受瑕疵（不要為此停下或大改）

- 句子略硬、略翻譯腔
- 非關鍵描述不夠漂亮
- 極低頻雜兵／道具名輕微不統一（應記錄，不必阻塞）
- 非關鍵 UI 輕微偏長但仍可理解
- 少數語氣可更口語但意思正確

---

## 9. 給使用者啟動時的標準指令模板

見 **Part A.8**（路徑已換成本專案）。通用原文模板：

### 9.1 翻譯

```text
角色：Translator
分類：<CATEGORY>
嚴格依 docs/agent-translation-playbook.md 執行。
完成該分類並通過翻譯方自檢前不得停止。
```

### 9.2 審核

```text
角色：QA
分類：<CATEGORY>
嚴格依 docs/agent-translation-playbook.md 執行。
只寫 issues/<CATEGORY>.md；預設不直接改譯文。
全量檢查完成前不得停止。
```

### 9.3 修復

```text
角色：Fixer
分類：<CATEGORY>
嚴格依 docs/agent-translation-playbook.md 執行。
只修 issues 內 blocking／high，修完更新 issue 狀態與 progress。
```

---

## 10. `issues/<CATEGORY>.md` 格式（必須）

```markdown
# QA: <CATEGORY>

- progress_suggestion: qa_done | qa_issues
- blocking_open: <N>
- high_open: <N>
- low_open: <N>

## blocking
### ISSUE-001
- status: open
- file: translated/...
- locator: key_or_line
- source: "..."
- current: "..."
- problem: "..."
- suggestion: "..."

## high
### ISSUE-002
- status: open
- ...

## low
### ISSUE-003
- status: open
- ...
```

本專案 `file` 欄請寫實際路徑（例：`l10n/working/csv/dat-items-name.csv`）。

---

## 11. `progress.md` 格式（必須）

```markdown
# Progress

## <CATEGORY>
- status: pending | in_progress | translated | qa_issues | qa_done
- notes: ""

### files
- path: source/<CATEGORY>/file.json
  status: pending | in_progress | translated | qa_issues | qa_done
  notes: ""
```

本專案實例見 `docs/progress.md`。

---

## 12. 衝突時的優先級

1. 不破壞檔案與標記（最高）  
2. 不誤導玩家操作／任務理解  
3. 遵守 glossary  
4. 完成指定分類的停止條件（自循環）  
5. 繁中用語自然度  
6. 文筆潤色（最低）  

---

## 13. 一句话执行纲领

先保檔案與標記，再保意思與專名，再完成整個分類；文筆小瑕可留，未达停止條件不准停。
