# Phase 3 管線（指令與路徑）

節奏與決策見 `docs/PHASE3-LOOP.md`。本檔只列怎麼跑。

## 循環對應

| 循環步驟 | 指令／動作 |
|---|---|
| 1 部分處理 | `python apply_glossary_section.py [section-id…]` |
| 腳本閘門 | `python validate_working.py` |
| 一鍵 1+閘門 | `python run_glossary_pass.py` |
| 2～3 複審 | 另開 agent 讀 `reports/`；FAIL 則改 CSV／詞庫後重跑 |
| 4 回寫 | `python writeback_sections.py`（需 `_backup`；先 data 再 client） |

## section 定義

見 `sections.json`（xpath、抽出 CSV、允許的 glossary category）。

## 目錄

| 路徑 | 用途 |
|---|---|
| `csv/` | working 譯文 |
| `reports/` | 套用／驗證／複審報告 |
| `../data/*.bin` | 回寫目標（gitignore） |
| `../../client/MHFCT4.1/dat/mhfdat.bin` | 本體同步目標 |

## 未命中列策略

`target = source`（暫留英文／原文），避免回寫空白；待層次 B 再譯。

## 注意

- working CSV **必須 UTF-8 無 BOM**（FTH 靠首欄名 `index` 辨識格式；BOM 會變成 offset 模式並寫入 0 條）。
- FTH `--csv-to-bin` 產物是 `output/mhfdat-modified.bin`，**不是**原地改 `data/mhfdat.bin`；`writeback_sections.py` 會再拷回。


