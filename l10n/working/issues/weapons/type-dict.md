# 武器類型字根（定稿）

> **兩層概念：**  
> 1. **武器種（MHF 十六種）**— 以 `l10n/glossary/terms.csv` **WEA001–WEA016** 為準（含 **操蟲棍**、**充能斧**、穿龍棍、磁斬槌）。  
> 2. **英文名尾綴 token**— 剝詞用；尾綴譯文對齊 `dat-weapons-*-name.csv`（例：幸運**猫棒**、**劍盾**）。  
> 剝詞：`weapon_name_parse.py`（長詞優先；**Mace≠Hammer**；**Fishing Rod≠Rod**）。

## MHF 十六武器（WEA001–WEA016）↔ 資料尾綴

| WEA | 武器種 | 常見英文尾綴 | 名稱尾綴譯文 | 備註 |
|---|---|---|---|---|
| 001 | 大劍 | `Great Sword`／`Greatsword`；`Sword`；`Blade` | 大劍；劍；刃 | |
| 002 | 太刀 | `Long Sword`／`L.Sword`；`Katana`；`Edge` | 太刀；刀；刃 | |
| 003 | 單手劍 | `Knife`；`Rapier`；`Dagger`；`Pick`；整詞 `Sword and Shield` | 刀；細劍；短劍；証明球；劍盾 | 魂稱單手劍 |
| 004 | 雙劍 | `Dual Sword(s)`；`Claws` | 雙劍；爪 | |
| 005 | 大錘 | `Hammer` | **大錘** | |
| 006 | 狩獵笛 | `Hunting Horn`；`Horn` | 狩獵笛；角 | |
| 007 | 長槍 | `Lance`；`Spear` | 長槍；槍 | |
| 008 | 銃槍 | `Gunlance` | 銃槍 | |
| 009 | 斬擊斧 | `Switch Axe`／`Switch-Axe`／`Switchaxe`；部分 `Axe` | 斬擊斧；斧 | 魂作斬撃斧 |
| 010 | **充能斧** | **`Shield`**（配 `Sword`／`Blade`／`Edge` 名） | **盾** | 例：劍盾、刃盾；**非**單手劍之 `Knife` 線 |
| 011 | **操蟲棍** | **`Stick`；`Rod`；`Staff`；`Pole`；`Glaive`／`Insect Glaive`** | **棒**；杖／棒；杖；柱；（整詞）操蟲棍 | 資料**幾無** Glaive 字串；主線 **Stick→猫棒** |
| 012 | 弓 | `Bow`；部分 `Arrow` | 弓；矢 | |
| 013 | 輕弩槍 | `Light Bowgun`；`Lbg` | 輕弩槍 | terms 作輕弩 |
| 014 | 重弩槍 | `Heavy Bowgun`；`Hbg`；`Gun`；`Bowgun` | 重弩槍；弩槍；銃 | |
| 015 | 穿龍棍 | `Tonfa`／`Tonfas` | 穿龍棍 | |
| 016 | 磁斬槌 | `Mace`／`Mallet`／`Scythe` | 鎚；鎌 | 無 `Magnet Spike` 字面 |

> **遠程修飾**（非獨立武器種）：`Launcher`／`Cannon`／`Carbine`／`Shooter`／`Assault` — 見下方 token 表。  
> **素魂**（Raw Soul）為通用素材，**不**佔十六種之一。

---

## 剝詞 token 表（定稿用）

| 原文 token | 建議譯文 | 槽 | WEA | 備註 |
|---|---|---|---|---|
| Insect Glaive | 操蟲棍 | melee | 011 | 整詞 |
| Glaive | 操蟲棍 | melee | 011 | 預留；現 CSV 多為 0 |
| Hunting Horn | 狩獵笛 | melee | 006 | |
| Light Bowgun | 輕弩槍 | ranged | 013 | |
| Heavy Bowgun | 重弩槍 | ranged | 014 | |
| Switch Axe | 斬擊斧 | melee | 009 | |
| Switch-Axe | 斬擊斧 | melee | 009 | |
| Switchaxe | 斬擊斧 | melee | 009 | |
| Sword and Shield | 劍盾 | melee | 003 | 整詞；SnS 條目名 |
| Great Sword | 大劍 | melee | 001 | |
| Long Sword | 太刀 | melee | 002 | |
| Fishing Rod | 釣魚杖 | melee | 011 | 整詞；勿與 `Rod` 混淆 |
| Dual Swords | 雙劍 | melee | 004 | |
| Dual Sword | 雙劍 | melee | 004 | |
| Gunlance | 銃槍 | melee | 008 | |
| Greatsword | 大劍 | melee | 001 | |
| Bowgun | 弩槍 | ranged | 014 | |
| Launcher | 發射器 | ranged | — | 修飾 |
| L.Sword | 太刀 | melee | 002 | |
| Mace | 鎚 | melee | 016 | |
| Mallet | 鎚 | melee | 016 | |
| Scythe | 鎌 | melee | 016 | |
| Carbine | 卡賓槍 | ranged | — | |
| Shooter | 射手 | ranged | — | |
| Assault | 強襲 | ranged | — | |
| Hammer | 大錘 | melee | 005 | |
| Rapier | 細劍 | melee | 003 | |
| Lance | 長槍 | melee | 007 | |
| Dagger | 短劍 | melee | 003 | |
| Katana | 刀 | melee | 002 | |
| Sword | 劍 | melee | 001 | |
| Blade | 刃 | melee | 001 | 大劍系；CB 名見 Shield |
| Spear | 槍 | melee | 007 | |
| Claws | 爪 | melee | 004 | |
| Knife | 刀 | melee | 003 | |
| Edge | 刃 | melee | 002 | 太刀系；CB 名見 Shield |
| Shield | 盾 | melee | 010 | 充能斧：Sword/Blade/Edge Shield |
| Stick | 棒 | melee | 011 | 操蟲棍：幸運猫棒 等 |
| Staff | 杖 | melee | 011 | |
| Pole | 柱 | melee | 011 | |
| Rod | 杖 | melee | 011 | 惡魔杖、橡棒；長詞 Fishing Rod 先剝 |
| Tonfas | 穿龍棍 | melee | 015 | |
| Tonfa | 穿龍棍 | melee | 015 | |
| Cannon | 加農砲 | both | — | |
| Horn | 角 | melee | 006 | |
| Bow | 弓 | ranged | 012 | |
| Axe | 斧 | melee | 009 | 非 Switch 時 |
| Gun | 銃 | ranged | 014 | |
| Arrow | 矢 | ranged | 012 | |
| Pick | 証明球 | melee | 003 | |
| Hbg | 重弩槍 | ranged | 014 | |
| Lbg | 輕弩槍 | ranged | 013 | |

## 本次修正（操蟲棍）

- 十六種總表改對 **terms WEA001–016**；**010 充能斧**、**011 操蟲棍** 不再被素魂／遠程列擠掉。  
- 操蟲棍：**Stick→棒** 為主；**Rod／Staff／Pole** 同系；**Glaive** 依 UI 定稿預留。  
- 充能斧：**Shield→盾**（劍盾／刃盾），與 SnS 之 Knife／Rapier 分線。
