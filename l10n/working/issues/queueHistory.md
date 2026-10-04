# 隊列履歷（queueHistory）

> 現況看 `queue.md`。本檔只記：**翻了哪類／要你決定幾筆／總花費時間**。

---

## 2026-10-04

| 翻譯類別 | 需要你決定 | 總花費時間 | 備註 |
|---|---|---|---|
| items-name／tickets（PENDING 定稿＋Fixer 回修＋delta） | **23** 筆（`／` 併多物拆開後；其餘已直接核可移出） | **~6 min** | 定稿後 CSV 441 列；delta 1927 |
| items-name／tickets（人審 QA） | **0** | **~1 min** | review 無問題 → **qa_done** |
| items-name／consumables（剩餘消耗品／彈刀罠／笛等） | **0** | **~3 min** | 既有 216＋新譯 66＝batch n=282；已 awaiting_qa |
| items-name／consumables（人審 QA） | **0** | **~1 min** | review 無問題 → **qa_done**；系列【天廊】／【簡易】＋投擲刀．屬性＋認真飲料．屬性 |

| items-name／monster-materials（魔物素材主體） | **0** | **~8 min** | batch n≈1088 已 delta；殘餘複合修飾名未清完（子類仍 in_progress） |
| items-name／monster-materials（手改 review 同步） | **0**（C 剩 3 筆維持） | **~5 min** | 6 筆回寫；charset：黄金／汚；validate PASS；delta 1095；子類→awaiting_qa |
| items-name／monster-materials（人審 QA） | **0** | **~1 min** | review 無問題 → **qa_done** |
| items-name／gathering（採集礦蟲草魚） | **0** | **~12 min** | batch n=488；charset fallback（可片／麻痺／温暖等）；delta 完成；awaiting_qa |
| items-name／gathering（人審 QA） | **0** | **~3 min** | ・色／紙牌礦石／蠕蟲／黑鎧龍／瑪傑基特礦石 → **qa_done** |
| items-name／jewels（裝飾珠 Jewel） | **0** | **~8 min** | batch n=480；charset：多拉／鷄翅／獅毛／乳脂；delta 完成 |
| items-name／jewels（人審 QA） | **0** | **~2 min** | 分區＋義譯＋手改梅拉魯珠 → **qa_done** |
| items-name／skill-cuffs（PA/PB/PC…） | **0** | **~10 min** | batch n=2877；格式如匠ＰＡ１；delta 完成 |
| items-name／skill-cuffs（人審 QA） | **0** | **~2 min** | 採取→採集（84）；其餘無問題 → **qa_done** |
| items-name／dummy（Dummy→(dummy)） | **0** | **~5 min** | n=676；charset 無「虛設」改沿用 (dummy)；delta |
| items-name／dummy（人審 QA） | **0** | **~1 min** | review 無問題 → **qa_done** |
| items-name／remainder（人審 QA） | **0** | **~1 min** | 舊 stub 結案；細審改看 all-rest → **qa_done** |
| items-name／all-rest 首批 9 檔（人審） | **0** | **~30 min** | info／bond／chunks／coin／collectible／companion／consumable-like／cuff-base／dot-series → **qa_done**（暫不回寫） |
| items-name／kits（防具套件 Kit） | **0** | **~5 min** | n=45；delta |
| items-name／kits（人審 QA） | **0** | **~1 min** | wiki 無定名維持現譯 → **qa_done** |
| items-name／monster-rest（中斷後全表重譯） | **0** | **~45 min** | n=438；片假名0；仍偏原文0；delta+bin |
| items-name／monster-rest（人審 QA） | **0** | **~3 min** | STYLE＋Z級＋劍寶玉．屬性＋手改同步 → **qa_done** |
| items-name／monster-rest（殘餘魔物素材） | **0** | **~8 min** | n=438；鬣毛取代缺字鬃；delta 259 新 |
| items-name／misc（公會／獵人／旅團雜項） | **0** | **~5 min** | n=199；delta |
| items-name／misc（人審 QA） | **0** | **~3 min** | STYLE＋公會的護腕ＲＮ → **qa_done** |
| items-name／remainder（義譯掃尾） | **0** | **~15 min** | n=5450；delta 4436 新；殘未譯約 1147 |

| items-name／殘留清零（英文＋片假名） | **0** | **~120 min** | validate PASS、半翻警告 0；needs_rework=0；delta 多次 |

**當日合計（續跑段）**：約 **210 min**｜待決合計 **0** 筆
