# MCP 方針（本專案）

## 結論

**不要再裝待辦／記憶類 MCP**（Todokit、Taskmaster、Anchor、Task Guardian、MegaMemory、Context Manager 等）。  
它們解決的是「記得做什麼」；本專案主痛點是「做對沒有」（字型、round-trip、詞語審核、品質）。  
再加一套狀態源會造成：**進度雙寫、中途打斷、token 浪費、成品變差**。

唯一 Source of Truth：

1. `docs/agent-translation-playbook.md` — 角色／停止條件／最高優先工作流  
2. `docs/progress.md` — 分類狀態機  
3. `docs/TODO.md` — Phase 總覽與閘門  
4. `docs/STYLE.md` + `l10n/glossary/terms.csv` — 用語與風格  
5. `.cursor/rules/mhf-l10n.mdc` — 強制開場必讀上列檔案  

## 為何那些推薦是雞肋

| 類型 | 評價 | 原因 |
|------|------|------|
| 待辦 MCP（Todokit 等） | 雞肋 | 與 `TODO.md` 重疊；易雙源不同步 |
| 記憶／知識圖 MCP | 雞肋到有害 | 知識已集中在 STYLE／詞語庫／TODO；向量記憶易撈過期決策 |
| 把 FTH 再包成 MCP | 不值得 | CLI／Shell 已夠；多一層協議無增益 |
| GitHub Projects MCP | 不做 | 私服本地工程，Issue 板非必要 |

## 已有 MCP：保留什麼

| MCP | 本專案用途 |
|-----|------------|
| `interactive_feedback` | **保留**：審詞、Phase 閘門、避免 agent 自作主張連做 |
| `context7` | **弱相關**：FTH／MHF 幾乎查不到；勿為查文件硬繞 |
| Cursor `TodoWrite` | 僅單 session 輔助；**跨 session 以 `TODO.md` 為準** |

## 真正該補的（腳本／文件，不是 MCP）

1. 字型／Shift-JIS 可顯示閘門 → `l10n/charset/`  
2. 未改動 round-trip 驗證  
3. section 進遊戲驗收清單  
4. FTH 常用指令速查（`l10n/README.md`）  
5. 有抽出／詞庫變更時**立刻**改 `TODO.md`，禁止文件與磁碟脫節  
6. Phase 3 循環節奏 → `docs/PHASE3-LOOP.md`＋`l10n/working/PIPELINE.md`  

## 禁止

- 為「不忘代辦」再裝第二套 todo／memory MCP  
- 同一進度寫兩處（MCP JSON + Markdown）卻不同步  
- 用記憶 MCP 取代讀 `STYLE.md`／`terms.csv`
