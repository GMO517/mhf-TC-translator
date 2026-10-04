# 字型／編碼閘門（Gate0.5）

## 結論

現行 CT4.1／日系客戶端：

- **編碼**：CP932（Windows Shift-JIS）
- **繪字**：內嵌點陣 ≈ **JIS X 0208** + 可列印 ASCII  
  （FrontierTextHandler `docs/translation-format.md`）

台服當年 Big5／系統 TTF **不能**直接當本體白名單。

## 檔案

| 檔 | 用途 |
|---|---|
| `whitelist.txt` | 全部允許字元連成一字串（**7421** 字） |
| `fallback_map.csv` | 禁字 → 建議替換 |
| `check_glossary.py` | 更新詞語庫 `display_ok`／`fallback_glyph` |
| `build_whitelist.py` | 重建白名單 |

## 使用

```bash
python build_whitelist.py
python check_glossary.py
```

- `display_ok=Y`：繁中每字皆在白名單，且可 CP932 編碼  
- `display_ok=N`：有缺字；若 fallback 有對應則填 `fallback_glyph`
