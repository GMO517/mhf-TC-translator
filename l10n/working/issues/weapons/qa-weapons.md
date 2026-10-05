# 武器 QA

> **你審：** [`series-dict.md`](series-dict.md) ＋ [`series-dict-all.md`](series-dict-all.md) ＋ `melee/`／`ranged/` reviews ＋ **硬垃圾分堆** [`triage/`](triage/)（`bad/`＋`ok/` 分檔）＋ **系列專名叢** [`series-nick-rule.md`](series-nick-rule.md)

## P1 Integrity

| 項目 | 計數 |
|---|---:|
| `qa_weapon_p1_integrity.py` blocking | **0** |
| S+A+B 定稿／待查 | **923**／**0** |

## P2／P3（機械）

| 項目 | 計數／結果 |
|---|---|
| `validate_working` melee／ranged | **PASS**／**PASS**（壞字清零後複驗） |
| `qa_weapon_series_dict` mismatches | **0** |
| `needs_rework`（殘英半翻） | **0**／**0** |
| reviews | 近戰 **36**＋遠程 **9** |

## P3b

| 項目 | 原始計數 |
|---|---:|
| wash `raw_ascii_in_target` | **2458** |
| wash `after_strip_ok` | **0** |
| Grok 音譯抽核 [Grok P3b phonetic spot](801b4a97-710c-4d77-90cb-55738fed7a25) | 建議改 **10**（high）；已 merge＋重套 |

修正摘要：Zidoria×6→希托利亞…；Parone→巴羅内；Azoth→阿佐特；Sfida Crest→挑戰紋章。

**blocking／high（本輪 P3b）：0**（修完後）

## P4

| 項目 | 原始計數 |
|---|---:|
| CSV `needs_rework` | **0** |
| 字典仍標「音譯」stem | **119**（`qa-p4-phonetic-stems.tsv`；Grok 已抽核，餘為有出處短音譯） |

## Triage（A＋Y 硬垃圾分堆｜未改譯）

> 你審：[`triage/README.md`](triage/README.md) ＋ [`triage/bad/`](triage/bad/) ＋ [`triage/ok/`](triage/ok/)（每檔約 **400** 列）  
> 腳本：`scratch/_triage_weapon_zh.py`（可複跑）。**本節不標 qa_done。**

| 項目 | 原始計數 |
|---|---:|
| 全列（近＋遠） | **21791** |
| bad 合計 | **4832**（`reviews-bad-*.md` × **13**） |
| └ `raden_end`（螺鈿終） | **98** |
| └ `type_phonetic`（Rifle／Turret 等） | **160** |
| └ `phonetic_salad` | **4574** |
| ok 合計 | **16959**（近戰 × **35**＋遠程 × **9**） |

抽核：Lightning Turret／Reino Rifle／Essence Rifle → `type_phonetic`；Positron Rifle（歩槍）→ ok；melee 15500／15504／15507／15513 → bad。

**停等你回：** `排除 ok 全部`／`撥回 ok index …`／誤抓類別＋index。確認前不改 CSV。

### triage 譯稿進度（未回寫 CSV）

> 只改 [`triage/bad/`](triage/bad/)／[`triage/ok/`](triage/ok/) 分檔；表僅原文＋譯文（不記舊譯／來源）。CSV 未回寫。

| 堆 | 檔數 | 未定稿 | 狀態 |
|---|---:|---:|---|
| bad | **13** | **0** | 譯稿完成 |
| ok | **44** | **0** | 譯稿完成 |

**專名叢／垃圾音譯補強（本輪）：**

| 項目 | 原始計數 |
|---|---:|
| `series-nick-clusters.tsv` | **234** |
| 引號名仍無【】（殘） | 少數截斷引號／特殊 SP（見 [`triage/README.md`](triage/README.md)） |
| `魯貝魯`／長串`加諾`／`普里特伊`／`瓦恩達特` 垃圾標記 | **0**（bad 定稿） |

確認後才一次回寫兩 CSV。腳本：`scratch/_expand_series_nick_clusters.py`＋`scratch/_draft_triage_file.py`。

## `'s` 誤當等級 S（本輪）

| 項目 | 計數 |
|---|---:|
| 誤插裸 `S`／`Ｓ`（source 含 `'s`） | **219** 命中 → 已修 **286**（含 wiki 精確覆寫） |
| 修復後同規則殘留 | **0** |
| 例：`Luna's Flare` | `月神S輝` → **炎妃爆炎槍**（wiki／ナナ＝フレア） |

成因：所有格 `'s` 被 compose／剝詞當成等級 **S**。修法：wiki 精確優先，否則刪裸 S 並視情況補「之」。

| 項目 | 計數 |
|---|---:|
| 修復前（melee） | **647**（backup 對照約 659） |
| 修復後（melee／ranged） | **0**／**0** |
| 殘「老」字（合法名如斬老刀等） | melee **4**／ranged **6** |

來源：wiki-en-zh／EN-JP-CN 對齊＋機械尾綴＋手補（Grok 四批因用量耗盡未成）。reviews 已重產 36+9。

## 狀態註記

- 完成定義 1–7 機械＋本輪 Grok 抽核已齊；**本 Translator 對話不自標 `qa_done`**（另開 QA 對話複核後再標）。
- 你可先審 `series-dict-all.md`／reviews。

## 可複跑

```text
cd l10n/working
python scratch/_triage_weapon_zh.py
python scratch/qa_weapon_p3b_wash.py
python scratch/_p4_weapon_counts.py
python validate_working.py weapons-melee-name
python validate_working.py weapons-ranged-name
```
