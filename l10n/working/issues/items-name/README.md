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
> **本體尚未整批回寫**（CSV 已對齊本輪結構／第一輪修譯）

### 狀態總覽

| 狀態 | 檔數 | 筆數 | 說明 |
|---|---:|---:|---|
| 先前已標 `qa_done`（A＋B） | 18 | 2492 | A 13＋B 5（B 已補標） |
| 語意重分類後新檔（C→新） | 11 | 2958 | 結構完成；**殘留垃圾譯待第二輪** |
| **合計** | **29** | **5450** | |

### 本輪已完成

1. **背景行程清除**（無殘留 finish_batch／reclass）
2. **B 區 5 檔補標 `qa_done`**：dummy／equip-related／gather-craft／gem-like／jp-src-mid
3. **C 區 16 檔 → 語意 11 檔**：廢止 misc／BM／weapon-soul 的 index 高中低切片
4. **CSV 第一輪對齊**：`changed=142`（`scratch/reclass_fix_remaining_allrest.py`）
5. 產物：`batches/awaiting_qa/items-name/all-rest/{新id}.json`＋`batches/active/batch-items-allrest-reclass-fix.json`

### 本輪未完成（下一動）

- **仍不回寫本體**，除非明示（殘留垃圾譯已清；C→新 11 檔可當結案）

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

> 註：`misc-high`／`misc-low` 維持既有認可切片，不再併入本輪語意重分。

---

### C→新. 語意重分類（11 檔／2958 筆）

> 舊 16 檔（misc-mid／BM×3／weapon-soul×3／monster-mat／raw-mat／seal／proof／song／skill×2／permit／otoshidama）已歸檔 `_deprecated_index_split/`。  
> 檔頭目前標 `qa_done`＝**結構＋第一輪修譯完成**；**譯質殘留未清零**，勿當最終結案。

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

**抽查殘留（待第二輪）示例：**

- `misc-rest`：Confessional→波奇可、Magma Mango→岩漿征服拉 等
- `monster-mat`／`raw-mat`：里法磁／納桃／努波 碎片
- `skill-related`：Skill Slots Up PZ* 尾綴垃圾
- `weapon-soul`：`【low】`／Sweet Ribbon／SAF* 半翻
- `proof`：少數「的之証」

---

### 分類雜亂原因（紀錄）

當初 all-rest 為加快切批，對過大袋（misc／BM／weapon-soul）用 **index 高中低** 均分，不是語意分類。本輪已廢止該切片。

---

## 建議下一步

1. 執行第二輪清垃圾譯（`scratch/_fix_garbage_pass2.py` 或等價）→ 再核 CSV／review  
2. 確認殘留為 0 後，才把 C→新 11 檔當真正結案  
3. **仍不回寫本體**，除非明示  
