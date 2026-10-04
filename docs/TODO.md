# MHF 繁中翻譯工程 — 代辦清單（Source of Truth）

> Agent／人類都以本檔為準。開始任何階段前先讀本檔與 `docs/STYLE.md`。  
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
- [ ] **未改動 round-trip**：抽出 → 原樣回寫壓縮加密 → smoke（不過關不進翻譯）

## Phase 0.5 — 字型硬閘門（下一個硬前置）

- [ ] 盤點內建字型／可顯示字集
- [ ] 建立 `l10n/charset/` 白名單＋禁字替換表
- [ ] 詞語庫 `display_ok` 必須可判定（目前 170 條皆 `pending`）

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
- [~] **使用者審核詞語庫**（魔物已確認；道具 35 條已核准並寫回 CSV；系統／UI／武器種待審）

## Phase 3 — MVP 翻譯與回寫（小步）

> 閘門：Phase 0 round-trip + Phase 0.5 字型 + Phase 2 審詞，三者未過不開始。

- [ ] 按 section：填 `l10n/working/` → 驗證 placeholder／行寬／編碼
- [ ] `--compress --encrypt` 回寫，覆蓋前對指紋
- [ ] 私服進遊戲驗收該 section 後再做下一 section

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
| 本體父層 | `client/` |
| 本體 | `client/MHFCT4.1/` |
| 抽出 CSV/JSON | `l10n/extracted/` |
| 翻譯工作區 | `l10n/working/` |
| 詞語庫 | `l10n/glossary/` |
| 字集閘門 | `l10n/charset/` |
| 工具 | `tools/` |
| 本機備份 | `_backup/` |

## 建議 Agent 開場動作

1. 讀 `docs/TODO.md`、`docs/STYLE.md`、`docs/MCP-TOOLS.md`
2. 用磁碟實況核對並更新本檔核取方塊（禁止文件與抽出物脫節）
3. 只執行目前未完成且閘門允許的 Phase；改本體前確認 `_backup` 存在
4. 避免重複盤點／重複抽出已存在的 CSV（浪費 token、打斷節奏）


