# armors QA：亂音譯／應義譯卻音譯

> 角色：QA｜只讀 `csv/dat-armors-*.csv`（與 `reviews-*.md` 同源）｜**未改譯文**
> 依據：playbook Part A.3／A.4＋STYLE「先整名、普通描述義譯、禁半翻／片假名混中文」
> 腳本：`l10n/working/scratch/qa_armor_transliteration.py`
> 全量命中表：`qa-transliteration-hits.tsv`

## 結論

- 五部位合計 **68730** 列；自動標記 **0** 次（約 **0** 列至少一類）。
- 現況主殘：`truncate` **0**（系列名過短／未定稿未套用）、`need_semantic` **0**。
- 已定稿路徑：`series-dict`（禁洗白）＋`apply_armor_series_dict.py`（只套用非待查）；合作／魔物／義譯例：初音未來、極龍、白蛇、電氣石、守護者。
- **仍 `qa_issues`**：待查詞幹未清零前勿 Gate4 回寫本體；修完重跑本腳本。

## 各部位規模

| 部位 | CSV 列數 | 標記次數 |
|---|---:|---:|
| head | 14594 | 0 |
| body | 13462 | 0 |
| arms | 13452 | 0 |
| waist | 13708 | 0 |
| legs | 13514 | 0 |

## 問題類型計數

| 類型 | severity | 合計 | 說明 |
|---|---|---:|---|

### 分部位 × 類型

| 部位 | truncate | empty | bad_phon_known | need_semantic | long_phon | kata_mix | half_latin |
|---|---:|---:|---:|---:|---:|---:|---:|
| head | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| body | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| arms | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| waist | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| legs | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 高頻問題詞幹（need_semantic／bad_phon_known／long_phon，Top 50）

| 次數 | 原文詞幹（去部位／級別） |
|---:|---|

## 代表性樣本（每部位 × 類型最多 15）

### head

（無自動標記）

### body

（無自動標記）

### arms

（無自動標記）

### waist

（無自動標記）

### legs

（無自動標記）

## 人工抽樣複核（與 reviews 目視一致）

| 原文 | 現譯（抽樣） | 狀態 |
|---|---|---|
| White Snake Sleeve D | 白蛇袖 | 已定稿義譯 |
| Tourmaline Guard | 電氣石臂甲 | 已定稿義譯 |
| Miku Arms / Snow Miku Arms | 初音未來護腕／雪初音護腕 | 合作定稿 |
| Guardian Helm／Mask | 守護者頭兜／帽子 | 定稿（Helm 缺字→頭兜） |
| Io Arms | 伊歐護腕 | 已補（原 truncate） |
| 殘 pending 專名（Zakka 等） | 見 series-dict 空 zh | 續 batch 查證後套用 |

## Fixer 建議順序

1. **blocking**：`truncate` — 對 `series-dict` 空 zh／待查詞幹查證後寫入再套用。
2. **high**：`need_semantic` — 普通英詞／寶石／色詞整名義譯；禁音節灌表。
3. 只套用已定稿（`apply_armor_series_dict.load_finalized_series`）；禁字典洗白。
4. 修完重跑本腳本；人審前不回寫本體。

