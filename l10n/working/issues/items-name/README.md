# items-name 審閱目錄

## 正式子類（既有・多已歸檔）

路徑：`issues/review-items-name__*.md` 或 `issues/archive/items-name/`

- tickets／consumables／monster-materials／gathering／jewels
- skill-cuffs／dummy／kits／monster-rest／misc 等（主線多已 `qa_done`）

---

## 原 all-rest 拆分（現況快照・2026-10-04 晚）

> 目錄：`issues/items-name/all-rest/review-*.md`（現 **29** 檔／**5450** 筆）  
> 舊 index 高中低切片：已移至 `all-rest/_deprecated_index_split/`（32 件）  
> 全集備份：`batches/awaiting_qa/batch-items-all-rest.json`  
> **本體尚未整批回寫**（CSV／review／batch 已對齊；待明示）

### 狀態總覽

| 狀態 | 檔數 | 筆數 | 說明 |
|---|---:|---:|---|
| 全部分拆 review **qa_done** | **29** | **5450** | A＋B 18＋C 11；品質＋主規則巡檢完成 |
| **合計** | **29** | **5450** | |

### 已完成

1. 語意重分類（C 16→11）＋品質重譯（misc／raw／seal／魂／ＳＺ／許可證／proof…）
2. 主規則巡檢：防具【Ｇ／ＧＦ／ＧＸ】、ＰＺ【】、MS＝磁斬槌、魔物縮寫對 terms
3. CSV／`awaiting_qa` batch／review 表已對齊

### 下一動

1. **整批回寫本體**（待明示；`finish_batch`／csv-to-bin；改前 `_backup/`）
2. 回寫後 `validate_working`／必要時抽查客戶端顯示

---

### A＋B. 已標 qa_done（18 檔／2492 筆）

| 子類 | 筆數 | review |
|---|---:|---|
| ・分隔系列（其餘） | 218 | [`review-dot-series.md`](all-rest/review-dot-series.md) |
| 幣／勳章／支票 | 107 | [`review-coin-medal.md`](all-rest/review-coin-medal.md) |
| 紙牌／骰子／書／袋 | 85 | [`review-collectible.md`](all-rest/review-collectible.md) |
| 護腕基底 | 82 | [`review-cuff-base.md`](all-rest/review-cuff-base.md) |
| Dummy／占位 | 58 | [`review-allrest-dummy.md`](all-rest/review-allrest-dummy.md) |
| 裝備相關 | 56 | [`review-equip-related.md`](all-rest/review-equip-related.md) |
| 採集／製作雜項 | 51 | [`review-gather-craft.md`](all-rest/review-gather-craft.md) |
| 絆／地圖／紀録 | 35 | [`review-bond-map.md`](all-rest/review-bond-map.md) |
| 艾路／貓／古古 | 26 | [`review-companion.md`](all-rest/review-companion.md) |
| 塊／碎片／感謝色票 | 17 | [`review-chunks-shards.md`](all-rest/review-chunks-shards.md) |
| 寶玉／珠樣 | 13 | [`review-gem-like.md`](all-rest/review-gem-like.md) |
| 消耗品樣 | 9 | [`review-consumable-like.md`](all-rest/review-consumable-like.md) |
| 情報 | 6 | [`review-allrest-info.md`](all-rest/review-allrest-info.md) |
| 日文源名・高 | 135 | [`review-jp-src-high.md`](all-rest/review-jp-src-high.md) |
| 日文源名・中 | 134 | [`review-jp-src-mid.md`](all-rest/review-jp-src-mid.md) |
| 日文源名・低 | 134 | [`review-jp-src-low.md`](all-rest/review-jp-src-low.md) |
| 未歸細類・高 index | 663 | [`review-misc-high.md`](all-rest/review-misc-high.md) |
| 未歸細類・低 index | 663 | [`review-misc-low.md`](all-rest/review-misc-low.md) |

---

### C→新. 語意重分類（11 檔／2958 筆）・qa_done

| 新 id | 名稱 | 筆數 | review |
|---|---|---:|---|
| `armor-bm-gn` | 防具系列・劍士／射手（ＢＭ／ＧＮ） | 1277 | [`review-armor-bm-gn.md`](all-rest/review-armor-bm-gn.md) |
| `misc-rest` | 雜項（重分類後剩餘） | 835 | [`review-misc-rest.md`](all-rest/review-misc-rest.md) |
| `weapon-soul` | 武器魂／飾帶／功績塊 | 179 | [`review-weapon-soul.md`](all-rest/review-weapon-soul.md) |
| `monster-mat` | 魔物素材 | 173 | [`review-monster-mat.md`](all-rest/review-monster-mat.md) |
| `seal-mark` | 封印／紋章／印 | 125 | [`review-seal-mark.md`](all-rest/review-seal-mark.md) |
| `skill-related` | 技能強化／技能果／護腕殘段 | 103 | [`review-skill-related.md`](all-rest/review-skill-related.md) |
| `raw-mat` | 礦石／布／一般素材 | 101 | [`review-raw-mat.md`](all-rest/review-raw-mat.md) |
| `proof` | 之証／證明 | 67 | [`review-proof.md`](all-rest/review-proof.md) |
| `song` | 歌曲／音符 | 67 | [`review-song.md`](all-rest/review-song.md) |
| `permit` | 許可／通行／推薦 | 26 | [`review-permit.md`](all-rest/review-permit.md) |
| `otoshidama` | 紅包／年玉 | 5 | [`review-otoshidama.md`](all-rest/review-otoshidama.md) |

---

### 分類雜亂原因（紀錄）

當初 all-rest 為加快切批，對過大袋用 **index 高中低** 均分。本輪已廢止該切片並改語意分類。
