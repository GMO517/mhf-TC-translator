# MHF 繁中翻譯工程 — 代辦清單（Source of Truth）

> Agent／人類都以本檔為準。開始任何階段前先讀本檔與 `docs/STYLE.md`。  
> 範圍：**私服自用**客戶端文字；不做公開伺服器／持續線上翻譯管線。

## 狀態圖例

- `[ ]` 未開始
- `[~]` 進行中
- `[x]` 完成
- `[-]` 取消／不做

---

## Phase 0 — 環境與基線

- [x] 調整倉庫目錄：`l10n/`（取出物）+ `client/`（本體父層）+ `client/MHFCT4.1/`（本體）
- [x] 撰寫 `.gitignore`（本體不上 GitHub）
- [x] 倉庫預設分支改為 `main`（內容承接原 `1225f4e`；舊 `master` 廢棄）
- [x] 本機備份 `_backup/20261004-070421/`（exe/dll + 文字主 bin + dat 頂層）
- [x] 安裝 Python 3.12 + FrontierTextHandler 於 `tools/`（已驗證 `mhfsqd.bin`）
- [ ] （可選）安裝 ReFrontier
- [ ] 確認 game-version／fingerprint 與 CT4.1 相符
- [ ] **未改動 round-trip**：抽出 → 原樣回寫壓縮加密 → smoke（不過關不進翻譯）

## Phase 0.5 — 字型硬閘門

- [ ] 盤點內建字型／可顯示字集
- [ ] 建立 `l10n/charset/` 白名單＋禁字替換表
- [ ] 規定：詞語庫譯文必須通過可顯示檢查

## Phase 1 — 抽出（MVP）

- [ ] 從本體複製所需 `.bin` 到 `l10n/data/`（該目錄已 gitignore）
- [ ] 抽出 MVP section → `l10n/extracted/`  
  優先：系統 UI、怪物名、武器名、防具名、道具名、技能名
- [ ] （可選）量測行寬 `--measure-line-lengths`

## Phase 2 — 風格與詞語庫

- [x] 風格規範初稿 `docs/STYLE.md`
- [x] 建立 `l10n/glossary/terms.csv` 骨架與 P0 類別
- [ ] 填入 P0 專有名詞（含荒野對照／Frontier 專有／可顯示狀態）
- [ ] **使用者審核詞語庫**（未核准不進大批翻譯）

## Phase 3 — MVP 翻譯與回寫（小步）

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

1. 讀 `docs/TODO.md`、`docs/STYLE.md`
2. 更新本檔核取方塊
3. 只執行目前 Phase；改本體前確認 `_backup` 存在
