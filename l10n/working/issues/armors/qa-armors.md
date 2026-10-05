# QA: armors（五部位）

- progress_suggestion: **qa_done**（機械 QA 原始命中 **0**；validate PASS）
- blocking_open: **0**
- high_open: **0**
- low_open: **0**
- validate: PASS（五部位 charset／半翻／片假名混中文／`{j}` 無錯）
- 腳本: `l10n/working/scratch/qa_armor_transliteration.py`
- 命中表: `l10n/working/issues/armors/qa-transliteration-hits.tsv`（**0 列**）
- wash: `scratch/_semantic_wash_hits.tsv`（**0 列**）

## 收尾（2026-10-05 一次跑完）

| 項目 | 開場（同日早） | 收尾 |
|---|---:|---:|
| QA 標記 | 318 | **0** |
| need_semantic | 196 | **0** |
| truncate | 121 | **0**（Q-03 部位尾白名單＋真截斷修譯） |
| long_phon | 1 | **0** |
| `_semantic_wash_hits` | 82 | **0** |

### 結構修復（非重翻）

- 分層 P0→P3b：`patch_series_dict_en_semantic_p1.py`／`patch_series_dict_p3b.py`／`patch_armors_finalize.py`
- 套用：`apply_armor_series_dict.py`（多色・、Red 備ノ、四神前綴、Hypno ルータ、禁 greaves 搶命中）
- QA：`looks_truncated` 對齊 Q-03（合法短名＋部位尾不標）

### 殘留（非 QA blocking）

- `series-dict.tsv` **15** 列「魁／亜D」標誌待查（刻意不套用洗白）
- 五 CSV 各 **1** 列空 source（index 見 validate；非譯文問題）
- **68730** 列中 `kept_pendingish` 約 **1522** 列仍靠舊譯（無定稿詞幹）；非空譯、validate PASS

## 整體 review（完整清單，非前 40／50）

| 用途 | 路徑 | 列數 |
|---|---|---:|
| 五槽譯文全表 | `issues/armors/armor-reviews-all.tsv` | **68730** |
| 140 份 reviews 索引 | `issues/armors/REVIEW-MANIFEST.md` | 140 檔 |
| 詞幹字典全表 | `issues/armors/series-dict.tsv` | **3796** |
| 詞幹 human 全表 | `issues/armors/series-dict-all.md` | 3781+15 |
| 詞幹摘要＋待查全列 | `issues/armors/series-dict.md` | 待查全列 |

產生腳本：`scratch/build_armor_review_manifest.py`、`scratch/refresh_series_dict_md.py`

## 工具路徑

- P0: `scratch/armor_stem_tiers.tsv`、`scan_armor_stem_tiers.py`
- 字典: `issues/armors/series-dict.tsv`（3781 定稿／15 待查）
- 套用: `scratch/apply_armor_series_dict.py`

## 結論

- 機械 QA **清零**；可標五部位 **qa_done**（Translator 本輪不代 commit）。
- **已回寫本體**（2026-10-05 `writeback_sections.py --all-changed` 五槽；見 `logs/writeback.md`）。
