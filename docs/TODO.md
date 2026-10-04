# MHF 繁中翻譯工程 — 代辦清單（Source of Truth）

> Agent／人類都以本檔為 **Phase 總覽**。開始任何階段前先讀：  
> `docs/agent-translation-playbook.md`（角色／停止條件／最高優先）→ `docs/progress.md`（分類狀態）→ 本檔 → `docs/STYLE.md`。  
> 範圍：**私服自用**客戶端文字；不做公開伺服器／持續線上翻譯管線。  
> MCP 方針見 `docs/MCP-TOOLS.md`（**不裝**待辦／記憶類 MCP）。

## 狀態圖例

- `[ ]` 未開始
- `[~]` 進行中
- `[x]` 完成
- `[-]` 取消／不做

---

## Phase 0 — 環境與基線

- [x] 調整倉庫目錄：`l10n/`（取出物）+ `client/`（本體父層）+ `client/MHFCT4.1/`（本體）
- [x] 撰寫 `.gitignore`（本體不上 GitHub）
- [x] 倉庫預設分支 `main`（遠端舊 `master` 已刪）
- [x] 本機備份 `_backup/20261004-070421/`（exe/dll + 文字主 bin + dat 頂層）
- [x] 安裝 Python 3.12 + FrontierTextHandler 於 `tools/`（已驗證 `mhfsqd.bin`）
- [ ] （可選）安裝 ReFrontier
- [ ] 確認 game-version／fingerprint 與 CT4.1 相符
- [x] **未改動 round-trip（離線）**：MVP 6 個 xpath 抽出→原樣回寫→字串／雜湊一致（見 `l10n/roundtrip/RESULT.md`）
- [ ] **round-trip 進遊戲 smoke**（可選補強；離線已 PASS）

## Phase 0.5 — 字型硬閘門（下一個硬前置）

- [x] 盤點可顯示字集依據：JIS X 0208 + ASCII（FTH 文件／內嵌點陣）
- [x] 建立 `l10n/charset/`：`whitelist.txt`（7421）＋`fallback_map.csv`＋檢查腳本
- [x] 詞語庫 `display_ok` 可判定（報告見 `charset/glossary_display_report.md`）
- [x] 處理缺字：整詞定稿＋fallback；目前 **Y=358／N=0**（罠／鎌／剥 等暫用形已註記）

## Phase 1 — 抽出（MVP）

- [x] 所需 `.bin` 已複製到 `l10n/data/`（gitignore）
- [x] 已抽出（在 `l10n/extracted/`）：  
  `dat-weapons-melee-name`、`dat-weapons-ranged-name`、`dat-items-name`、  
  `dat-armors-head`、`dat-armors-body`、`dat-monsters-description`  
  （名稱欄以**英文**為主）
- [ ] `pac/skills/name` 抽出失敗（pointer 越界）— 待查 game-version／headers
- [ ] `pac/menu/*` 目前不可用（options 結果異常）— 暫緩
- [ ] （可選）量測行寬 `--measure-line-lengths`

## Phase 2 — 風格與詞語庫

- [x] 風格規範 `docs/STYLE.md`
- [x] 詞語庫初稿：`l10n/glossary/terms.csv` + `REVIEW.md`（**170** 條）
- [x] 詞語庫管線收斂為 step1～3（見 `l10n/glossary/README.md`；中間腳本見 `HISTORY.md`）
- [x] MHF 特有魔物擴充（frontier／monster 加厚；總詞條見 REVIEW）
- [x] 補漏：辿異種／辿異技能／武器／防具／任務／發達部位
- [x] **使用者審核詞語庫**（358 條全核准；補詞→REVIEW 只審未審→回寫 terms→commit 為定稿節奏）

## Phase 3 — MVP 翻譯與回寫（小步）

> 閘門：Phase 0 round-trip + Phase 0.5 字型 + Phase 2 審詞，三者未過不開始。  
> **工作流**：`docs/agent-translation-playbook.md`（Translator → 獨立 QA → Fixer）。  
> **技術循環**：`docs/PHASE3-LOOP.md`＋`l10n/working/PIPELINE.md`。  
> **分類狀態**：`docs/progress.md`；QA 產出：`l10n/working/issues/`。

- [x] 定稿 Agent 工作流文件（playbook＋progress＋issues 骨架）
- [~] 按循環執行（層次 A 詞庫命中已回寫本體 → 層次 B：未入庫列）
- [x] working 管線腳本（apply／validate／writeback／batch；CSV 無 BOM）
- [x] 層次 A 回寫：items／melee／ranged／head／body（FTH 產物為 `*-modified.bin`）
- [~] 層次 B：**依子類整段推進**（禁止再切 A/B/C／batch N；見 playbook Part A／`PHASE3-LOOP.md`）  
  - 道具 `items-name`：珠／情報／印記已做；票券 A–D 為遺留誤切；產物 `batch-items-tickets.json`（#4856～5772）已 delta 回寫、**不**另 commit 續段；下一未譯 **#6018 Parin WhtTea Tkt**；票券未完（約 1764+）；整類清完再 `feat: items-name 票券`  
  - 一覽／缺字：`working/reports/ITEMS-TRANSLATED.md`
- [ ] 私服進遊戲驗收



## Phase 4 — 延伸

- [ ] 任務說明、高頻 UI
- [ ] NPC／劇情（語域：人話）
- [ ] 標註延後：`*.txb` 圖片字、`mhfo.dll` 內嵌字串、伺服端下發文案

## 明確不做

- [-] Weblate／雲端翻譯 API／持續 CI 翻譯
- [-] 公開伺服器相容與發佈審核流程
- [-] 上傳遊戲本體到 GitHub
- [-] 再裝待辦／記憶類 MCP（見 `docs/MCP-TOOLS.md`）

---

## 路徑速查

| 用途 | 路徑 |
|------|------|
| Agent 工作流 | `docs/agent-translation-playbook.md` |
| 分類進度 | `docs/progress.md` |
| QA issues | `l10n/working/issues/` |
| 本體父層 | `client/` |
| 本體 | `client/MHFCT4.1/` |
| 抽出 CSV/JSON | `l10n/extracted/` |
| 翻譯工作區 | `l10n/working/` |
| 詞語庫 | `l10n/glossary/` |
| 字集閘門 | `l10n/charset/` |
| 工具 | `tools/` |
| 本機備份 | `_backup/` |

## 建議 Agent 開場動作

1. 確認角色（Translator／QA／Fixer）與單一 CATEGORY；讀 `docs/agent-translation-playbook.md`
2. 讀 `docs/progress.md`、本檔、`docs/STYLE.md`、`docs/MCP-TOOLS.md`
3. 用磁碟實況核對並更新 progress／本檔（禁止文件與抽出物脫節）
4. 只執行目前未完成且閘門允許的 Phase；改本體前確認 `_backup` 存在
5. 避免重複盤點／重複抽出已存在的 CSV（浪費 token、打斷節奏）


