# 待決專名（翻譯中標記）

> Translator 拿不定、或曾出現**半翻**時列在這裡。  
> **禁止**用「全形拉丁字母＋片假名」充數（見 `docs/STYLE.md`）。  
> 該 CATEGORY／子類**整段譯完後**，使用者在「決定」欄給定譯 → Fixer 回寫 CSV／batches。  
> 已定稿可移入 `terms.csv`（approved=Y）並從本表刪除或標 `decided`。

格式：

| source 關鍵 | 例 index | 例原文 | 現況（半翻／暫譯） | 決定（使用者填） | status |
|---|---|---|---|---|---|

---

## 已決定

| source 關鍵 | 例 index | 例原文 | 現況 | 決定 | status |
|---|---|---|---|---|---|
| Crest | 9345 | C Crest Tkt | （已改） | **紋章** → `Ｃ・紋章票` | decided |

---

## items-name / tickets（待決）

> 下列由現有「字母＋片假名」半翻掃出；票券子類完成後一次審。

| source 關鍵 | 例 index | 例原文 | 現況（半翻） | 決定（使用者填） | status |
|---|---|---|---|---|---|
| Creek | 1708 | M Creek Tkt | Ｍクリーク票 | | pending |
| Marsh | 1709 | B Marsh Tkt | Ｂマルシュ票 | | pending |
| Bolt | 2974 | W Bolt Tkt | Ｗボルト票 | | pending |
| Fang | 2975 | C Fang Tkt | Ｃファング票 | | pending |
| Lever | 4017 | V Lever Tkt | Ｖレバー票 | | pending |
| Rose | 4021 | A Rose Tkt | Ａローズ票 | | pending |
| Derose | 4022 | A Derose Tkt | Ａデローズ票 | | pending |
| Tweeter | 5655 | S Tweeter Tkt | Ｓツィータ票 | | pending |
| Fanare | 5657 | S Fanare Tkt | Ｓファナレ票 | | pending |
| Blade | 6476 | D Blade Tkt | Ｄブレイド票 | | pending |
| Lance | 6478 | C Lance Tkt | Ｃランス票 | | pending |
| Mortar | 6480 | S Mortar Tkt | Ｓモルタル票 | | pending |
| Cavalry | 6484 | S Cavalry Tkt | Ｓカルバリ票 | | pending |
| Gear | 7164 | D Gear Tkt | Ｄギア票 | | pending |
| Carbine | 7166 | IM Carbine Tkt | ＩＭカービン票 | | pending |
| Tomen | 7272 | IM Tomen Tkt | ＩＭトメン票 | | pending |
| Regil | 7999 | GE Regil Tkt | ＧＥレギル票 | | pending |
| Dore | 8000 | GE Dore Tkt | ＧＥドーレ票 | | pending |
| Greed | 8190 | E Greed Tkt | Ｅグリード票 | | pending |
| Vang | 8339 | E Vang Tkt | Ｅヴァング票 | | pending |
| Aria | 8820 | I Aria Tkt | Ｉアリア票 | | pending |
| Bank | 8821 | I Bank Tkt | Ｉバンク票 | | pending |
| Tavros | 9346 | N Tavros Tkt | Ｎタウロス票 | | pending |
| Pact | 9696 | C Pact Tkt | Ｃパクト票 | | pending |

（`S ParisTeatea`／`S ParisBerybery` 屬色味玩梗＋字母前綴，另案；勿再擴半翻。）

---

## 使用方式（Agent）

1. 翻譯中遇到無把握專名 → **新增一列** `pending`（可先保守暫譯，勿半翻）  
2. 子類宣告 `translated` 前：確認本表該子類列已齊  
3. 使用者填「決定」→ status=`decided` → Fixer 批次回修 → 入 `terms.csv`  
