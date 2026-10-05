# QA: armors（五部位）

- progress_suggestion: qa_issues
- blocking_open: 121（腳本 `truncate` 原始計數；多數為合法短名誤報，見 Q-03／下方 triage）
- high_open: 197（`need_semantic` 196 + `long_phon` 1）
- low_open: 0
- validate: PASS（五部位 charset／半翻／片假名混中文／`{j}` 無錯）
- 腳本: `l10n/working/scratch/qa_armor_transliteration.py`
- 命中表: `l10n/working/issues/armors/qa-transliteration-hits.tsv`
- 摘要: `l10n/working/issues/armors/qa-transliteration.md`

## 本輪（2026-10-05）

角色：QA（使用者明示可改有問題譯文 → 同步修 CSV／series-dict／套用邏輯）

| 指標 | 開場 | 本輪後 |
|---|---:|---:|
| 自動標記次數 | 1397 | **318** |
| need_semantic | 1242 | **196** |
| truncate | 154 | **121** |
| long_phon | 1 | **1** |
| 至少一類列數 | 1377 | **318** |

### 已修（結構性／高頻）

- 合作長詞幹覆蓋：騎士王 Hair／英雄王 Earring／BM D 等劣音譯 → 定譯
- 應義譯：屠龍、貫光、魔王、忍、流星、星祭、真空、操偶、砲／軸意志…
- 洗白清除：單字母 `D→德`、標誌字-only（覇／鬼／の）長詞幹
- 套用：尾／首色剝除、`Water` 色、`胴当て` 部位、魁標記位置
- 色詞補掛：Gold・Red、Gloria・Water、Demon ドレス Green、Shinryu Black…

### triage

| 類型 | 原始 | 研判 |
|---|---:|---|
| truncate | 121 | **多為合法短名**（蝶兜／龍皮／金帶／翼足等，Q-03）；真截斷本輪已清大半 |
| need_semantic | 196 | 殘：中綴色／Star／True 變體／少數頭部位 Rampage 音譯殘／色尾未掛 |
| long_phon | 1 | waist#681 `Hypno ルータウエスト`→`魯塔烏艾斯托腰甲` |

## blocking

### ISSUE-001
- status: open
- file: l10n/working/csv/dat-armors-*.csv
- locator: qa-transliteration-hits.tsv kind=truncate（121）
- source: （全表見 TSV）
- current: （短譯如「蝶兜」「龍皮」）
- problem: 腳本 `looks_truncated` 對合法短系列名誤報；與真截斷混計
- suggestion: Fixer 勿整批重翻短名；改腳本閾值或白名單（對齊 Q-03）

## high

### ISSUE-002
- status: open
- file: l10n/working/csv/dat-armors-*.csv
- locator: kind=need_semantic（196）
- source: 例 `Sky Red Star Mask`／`Star Festival D Mask`／殘 True 變體
- current: 例「天空帽子」（缺赤）／殘音譯
- problem: 英詞應義譯色／True／Star 等仍有缺漏或長詞幹未入典
- suggestion: 續補 series-dict 定稿＋重跑 apply；優先色尾與 Star／True 家族

### ISSUE-003
- status: open
- file: l10n/working/csv/dat-armors-waist.csv
- locator: index 681
- source: "Hypno ルータウエスト"
- current: "魯塔烏艾ス托腰甲"
- problem: 長音譯串（long_phon）
- suggestion: 眠鳥＋ルータ義譯／短音譯定稿後重套

## 分部位原始計數（本輪後）

| 部位 | need_semantic | truncate | long_phon |
|---|---:|---:|---:|
| head | 86 | 15 | 0 |
| body | 80 | 4 | 0 |
| arms | 70 | 10 | 0 |
| waist | 103 | 3 | 1 |
| legs | 99 | 97 | 0 |

## 產物／工具變更（供 Fixer）

- `issues/armors/series-dict.tsv`（定稿補丁＋洗白清除）
- `scratch/patch_series_dict_qa_fix.py`
- `scratch/apply_armor_series_dict.py`（色剝除／標誌）
- `scratch/armor_overnight_pipeline.py`（COLORS＋water）
- 五部位 `csv/dat-armors-*.csv`＋`reviews-*`（apply 重產）

## 結論

- **不可**標 `qa_done`／裸 `translated`：high 仍 197。
- validate **PASS**；較開場標記約降 **77%**。
- 下一動：Fixer 清 ISSUE-002／003；truncate 以腳本收斂為主勿亂翻。
- **尚未**另次回寫本體（Gate4 已回寫過舊譯；本輪 CSV 變更待使用者要再 finish_batch）。
