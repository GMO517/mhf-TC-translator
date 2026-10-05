# 遊戲翻譯 Agent 強制工作流（父規範）

## 核心目標（三點並立；有衝突按下表裁決）

1. **加快翻譯時程**（子類連續推進，少停少問）  
2. **控制 token**（開場少讀、少重複盤點、少為改規則停工）  
3. **維持品質底線**（不壞檔、不壞標記、不誤導、不寫缺字；**且**不高頻專名亂飄、不應義譯卻音譯、不未搜尋就灌音譯）

### 目標衝突時（釘死）

| 衝突 | 裁決 |
|---|---|
| 「快／省 token」vs 全量檢查、專名 web search、字典註記出處 | **品質程序優先**；不得用快／省 token 跳過 |
| 「少讀」vs 查 STYLE／terms／wiki | 開場仍少讀；**碰到該條用字再查**；結案前用腳本／字典做全量，不靠通讀全文充數 |
| 「少停少問」vs 使用者要審、回寫本體、方針真衝突 | **後者優先，才准停問** |
| 「推進譯文」vs 停等逐條批 PENDING／字典 | **不為批字典／PENDING 停主線**；字典可逕行（見 A.3）；**「待查」不得當套用預設譯** |
| 本機 Cursor「逐步確認／feedback」類規則 vs 翻譯主線 | **翻譯推進以本 Part A 為準**（含建字典、全量檢查）；僅 **commit／回寫本體／方針真衝突／使用者明示要審** 才停問 |

若某條規定讓你**只為儀式性重讀／空轉 scrub**而停工——那條執行錯了。  
若某條讓你**跳過全量檢查或未搜尋灌音譯**來「推進」——同樣執行錯了。

### 對話輸出（省 token）

- **非必要禁止**展示後台過程（log／逐步旁白／長對照）。  
- 結案時交：**結果路徑＋全量檢查數字**（CSV 列數、validate 結果、QA 腳本**原始命中計數**或「無腳本＋最低語意自檢勾選」）；禁止只寫「PASS」／SAMPLE。  
- 例外＝使用者要看 log／diff，或工具失敗需一句原因。

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
        └── PENDING.md／系列字典        → 待裁定／詞幹表（不叫停主線）
```

**高→低：** 使用者口令 → 本 Part A → STYLE／charset → PHASE3／PIPELINE → progress／TODO → Cursor 通用規則／MCP  

**日常推進（不必每步確認／feedback）：** 譯文、apply、validate、**建／補字典**、產 reviews、跑全量 QA 腳本、更新 progress／queue。  

**才准停問：** 缺 `_backup`、工具壞、方針真衝突、使用者明示要審、**大批回寫本體**、**建立 git commit**。  

**禁止**把 STYLE 辯論、PENDING／字典改欄、開場整庫重讀當成停工理由。  
**禁止**同一次 Translator 結案訊息自稱 `qa_done`（QA 須另開對話或獨立腳本結果寫入 issue）。

---

# Part A — 本專案規則

## A.0 身分

| 項 | 定案 |
|---|---|
| 遊戲 | MHF 私服 CT4.1 |
| 範圍 | 本機自用；本體不上 git；不追更重翻 |
| AI | 只用 Cursor；禁止外部翻譯 API／平台 MCP |
| 品質底線 | 見「核心目標」第 3 點＋衝突表；文筆小瑕可留 |

## A.1 路徑（摘要）

| 用途 | 路徑 |
|---|---|
| 譯文 | `l10n/working/csv/` |
| 批次 | `l10n/working/batches/{active,awaiting_qa,legacy}/` |
| 隊列／issues | `l10n/working/issues/` |
| 詞庫 | `l10n/glossary/terms.csv`＋`REVIEW.md`＋`PENDING.md` |
| 防具字典 | `issues/armors/series-dict.*`（全身詞幹）＋各槽 `part-dict.md` |
| 風格／字型 | `docs/STYLE.md`＋`l10n/charset/` |
| 狀態 | `docs/progress.md`（分類）／`docs/TODO.md`（工程 Gate） |
| 本體 | `client/MHFCT4.1/`（改前 `_backup/`） |

日常不必重讀長表；防具以字典為準，不必每輪重發明部位／詞幹。

## A.2 完成單位（釘死）

- 一次任務＝**一種角色**＋**一個語意單位**  
- 語意單位＝`CATEGORY` 或 `CATEGORY/子類`  
- **Translator 停止條件／commit 單位＝該語意單位清完**（不是 batch N）  
- **禁止** `tickets-a/b/c`、`batch-019`、每 N 筆當結案名  
- 內部可多次 apply／delta

## A.3 Translator（主線＝翻譯）

**開場只讀（≤4 步，然後動手）：**

1. 本文件「核心目標」＋本 Part A  
2. `progress.md`＋`issues/queue.md`  
3. 該子類 CSV（未譯／或防具則看字典待查）  
4. 碰到用字再查 `STYLE.md`／`terms.csv`——**禁止**開場通讀整份 STYLE＋REVIEW＋TODO＋全庫  

**專名查序（全專案同一套；與 STYLE「先整名」一致）：**

1. 整名語意  
2. `terms.csv`（魔物／縮寫／UI）  
3. 神話／既定專名  
4. 遊戲專名（含 **合作／聯名**；Frontier 常見）  
5. **Web search**（台服 wiki／MH 大典／官方合作稿／可信中文慣譯）  
6. 字義／描述義譯  
7. 最後才短音譯，或列 PENDING／字典「待查」  

**禁止：** 跳過第 5 步做音節灌表／`compact_phonetic`／同等碎音譯；禁止把普通英文描述／寶石名等應義譯詞拆開音譯（**不論長短**，至少算 high）。  
**短音譯上限（第 7 步）：** 僅專名；宜 ≤4 漢字；出處須寫「搜：〈查詢詞〉→無／連〈URL 或站名〉」；禁止無搜尋紀錄的長串音譯用字。

**字典（逕行；不停問；禁止洗白）：**

- 可直接建立／更新詞幹與部位字典；每條註 **譯文／理由／出處**（terms／wiki／web＋查詢詞或 URL／字義）。  
- **「待查」或僅「音譯」不得當作已定稿去全表套用**；套用預設只許：terms／神話／遊戲專名／已搜尋有出處／字義。待查列留在字典等人審或補搜。  
- 描述英詞、寶石名未走完查序（含 search 或字義）→ **禁止入庫當套用譯**。  
- 使用者事後從字典抽查即可；不為「字典要不要建」停工。  
- 防具：詞幹＝`issues/armors/series-dict.tsv`（全身共用）；部位＝各槽 `part-dict.md`。

**執行循環：**

1. 選定未完成子類 →（防具：補字典→只套用已定稿詞幹）→ 譯／套用 → `validate_working.py`  
2. 可 `finish_batch.py` delta；更新 `progress.md`／`queue.md`  
3. 告一段落：產**完整** `reviews-*.md`（不抽樣）→ 不中斷等使用者當場批完  
4. 子類未完：禁止只交摘要就停  
5. PENDING：暫譯＋列待裁定；不中途逐條問；子類完再請填決定 → Fixer  

**全量語意自檢（有無專用 QA 腳本都要做）：**

- 必做機械：charset／CP932／半翻／片假名混中文／`{j}`  
- 必做語意（可用腳本）：應義譯英詞卻音譯、已知劣質音譯片段、截斷／系列丟失、錯部位（他槽詞）。防具預設腳本：`l10n/working/scratch/qa_armor_transliteration.py`（結案須附原始計數）。  
- 無現成腳本的分類：仍須對上列語意項做全表掃描（自寫亦可，但規則不得刻意調到永遠 0 hit），結案寫明「無腳本＋自檢項與命中數」。

**結案狀態（分開，禁止混用）：**

| progress | 何時 |
|---|---|
| `qa_issues` | 全量已跑、issue 已登錄，但仍有開放 blocking／high（或結構性錯未清） |
| `translated`／可交人審完譯 | 全量檢查後 **blocking／high＝0**（low 可留） |
| 禁止 | 裸 `translated` 掩蓋未關 issue；用 SAMPLE／「PASS」無數字結案 |

- 有開放 **結構性錯** 或 **high＞50**（或該單位＞5% 列涉 high）→ **不得開下一個語意子類**，先 Fixer。  
- `qa_issues` 不是「做完走人」；只表示譯文已交卷、帳還在。  
- **禁止**自稱 QA 通過。

**禁止：** 一次多子類（上條閘門開啟時）；為文筆改標記；半翻／片假名混中文充數；為改規則格式停主線。

## A.4 QA／Fixer

| 角色 | 做 | 不做 |
|---|---|---|
| QA | **另開對話**；全量檢查；只寫 issues；預設不改譯文 | 抽檢結案；順便大翻 |
| Fixer | 修 issues 的 blocking／high；可依字典／查序改正；修完全量重跑 QA／validate；更新 issue／progress | 抽檢宣告修完；無關大範圍亂翻 |

- 結構性錯（如整槽部位詞、詞幹查序錯）＝高優先，Fixer 應修，不算「借機亂翻」。  
- QA 預設不改檔；使用者明示或 blocking 無法只靠 Fixer 時例外（寫進 issue）。

## A.5 工程閘門（大批回寫本體前）

1. Gate0 離線 round-trip PASS  
2. Gate0.5 字型 whitelist／fallback 可用  
3. 該批相關：字典「待查」已處理或不影響套用；PENDING 未決若會進本體 UI 則已標 issue（可檢查，非空話「有節奏」）  
4. `_backup/` 存在  
5. 該批 progress **非**裸 `translated` 掩蓋未關的 blocking／high  

## A.6 寫入約束（一行版）

CSV UTF-8 無 BOM；用字見 STYLE；禁半翻／片假名混中文；缺字走 fallback；本體 bin 不進 git。

## A.7 Commit

- 預設：子類完成才 commit（或使用者要求的保全點）  
- 格式依使用者 git 規則；禁 Cursor 署名；禁擅自 push  

## A.8 啟動模板

```text
角色：Translator
分類：items-name/consumables
嚴格依 docs/agent-translation-playbook.md（核心目標＋Part A）執行。
開場精簡讀；結案須全量檢查摘要；字典可逕行更新。
```

```text
角色：QA
分類：armors
只寫 issues；預設不改譯文；全量檢查完才停（禁止抽檢結案）。
```

```text
角色：Fixer
分類：armors
只修 blocking／high（含結構性錯）；修完全量重跑 QA；禁止抽檢宣告完成。
```

---

# 附錄 — 查表用（禁止開場通讀）

## 附錄 A｜嚴重度

- **blocking**：壞檔／壞標記／空譯／會讓玩家做錯／不可顯示字／未搜尋灌音譯（**含短爛音譯**若屬應義譯詞）／部位錯槽／字典洗白後全表套用待查音譯  
- **high**：違反 glossary／字典定譯、**凡應義譯的英文描述／寶石名卻音譯（不論長短）**、合作／專名錯譯、關鍵 UI 難懂  
- **low**：翻譯腔、極低頻專名譯法可討論、非關鍵略長——可留，不為此停  
- **禁止**把「應義譯卻音譯」降級成 low／文筆小瑕  

## 附錄 B｜品質優先級

1. 不壞檔與標記  
2. 不誤導操作／任務／專名  
3. glossary／字典／高頻一致  
4. 全量檢查通過或 issue 已登錄  
5. 子類完成  
6. 用語自然  
7. 文筆（最低）  

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
