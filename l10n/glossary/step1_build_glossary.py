# -*- coding: utf-8 -*-
"""【step1】從抽出 CSV 與定稿種子產生詞語庫初稿（會覆寫 terms.csv）。見 README.md。"""
import csv
import pathlib
from collections import Counter

OUT = pathlib.Path(__file__).with_name("terms.csv")
REVIEW = pathlib.Path(__file__).with_name("REVIEW.md")
EXTRACTED = pathlib.Path(__file__).resolve().parents[1] / "extracted"

seed = []


def add(cat, src_jp, src_en, zh, wilds, frontier, register, notes, approved="N"):
    seed.append(
        {
            "category": cat,
            "source_jp": src_jp,
            "source_en": src_en,
            "target_zh_tw": zh,
            "wilds_ref": wilds,
            "frontier_only": "Y" if frontier else "N",
            "register": register,
            "display_ok": "pending",
            "fallback_glyph": "",
            "notes": notes,
            "approved": approved,
        }
    )


# 武器種（荒野）
for jp, en, zh in [
    ("大剣", "Great Sword", "大劍"),
    ("太刀", "Long Sword", "太刀"),
    ("片手剣", "Sword & Shield", "單手劍"),
    ("双剣", "Dual Blades", "雙劍"),
    ("ハンマー", "Hammer", "大錘"),
    ("狩猟笛", "Hunting Horn", "狩獵笛"),
    ("ランス", "Lance", "長槍"),
    ("ガンランス", "Gunlance", "銃槍"),
    ("スラッシュアックス", "Switch Axe", "斬擊斧"),
    ("チャージアックス", "Charge Blade", "充能斧"),
    ("操虫棍", "Insect Glaive", "操蟲棍"),
    ("弓", "Bow", "弓"),
    ("ライトボウガン", "Light Bowgun", "輕弩"),
    ("ヘヴィボウガン", "Heavy Bowgun", "重弩"),
]:
    add("weapon_type", jp, en, zh, zh, False, "ui", "荒野武器種")

for jp, en, zh in [
    ("穿龍棍", "Tonfa", "穿龍棍"),
    ("磁斬撃", "Magnet Spike", "磁斬擊"),
]:
    add("weapon_type", jp, en, zh, "", True, "ui", "荒野無對應，Frontier 專有")

systems = [
    ("クエスト", "Quest", "任務", "荒野常用「任務」", False, "system"),
    ("ギルド", "Guild", "公會", "系列慣用", False, "system"),
    ("ハンター", "Hunter", "獵人", "荒野", False, "ui"),
    ("武器", "Weapon", "武器", "荒野", False, "ui"),
    ("防具", "Armor", "防具", "荒野", False, "ui"),
    ("スキル", "Skill", "技能", "荒野", False, "ui"),
    ("アイテム", "Item", "道具", "荒野", False, "ui"),
    ("アイテムボックス", "Item Box", "道具箱", "荒野", False, "ui"),
    ("鍛冶屋", "Smithy", "鍛造屋", "荒野用語待微調", False, "ui"),
    ("食堂", "Canteen", "食堂", "荒野", False, "ui"),
    ("集会所", "Gathering Hub", "集會所", "荒野", False, "ui"),
    ("キャンプ", "Camp", "營地", "荒野", False, "ui"),
    ("マップ", "Map", "地圖", "荒野", False, "ui"),
    ("チャット", "Chat", "聊天", "系統", False, "system"),
    ("パーティー", "Party", "隊伍", "系統", False, "system"),
    ("ロビー", "Lobby", "大廳", "系統", False, "system"),
    ("HR", "HR", "HR", "等級縮寫維持半形", False, "ui"),
    ("GR", "GR", "GR", "Frontier／G 級", True, "ui"),
    ("G級", "G-Rank", "G級", "Frontier", True, "system"),
    ("剛種", "Hardcore / HC", "剛種", "Frontier", True, "system"),
    ("烈種", "Violent Species", "烈種", "Frontier", True, "system"),
    ("始種", "Origin Species", "始種", "Frontier", True, "system"),
    ("遷悠種", "Unknown Species", "遷悠種", "Frontier", True, "system"),
    ("極位", "Zenith", "極位", "Frontier", True, "system"),
    ("天廊", "Tower", "天廊", "Frontier 專有，細節待核", True, "system"),
    ("狩煉道", "Hunter's Road", "狩煉道", "Frontier", True, "system"),
    ("歌姫", "Diva", "歌姬", "Frontier", True, "npc"),
    ("メゼポルタ", "Mezeporta", "梅傑波爾塔", "Frontier 城鎮", True, "place"),
    ("アイルー", "Felyne", "艾路", "荒野／系列", False, "npc"),
    ("メラルー", "Melynx", "梅拉路", "系列", False, "npc"),
    ("オトモ", "Buddy / Palico", "隨從", "荒野偏「隨從」", False, "ui"),
    ("肉質", "Hitzone", "肉質", "獵人用語", False, "system"),
    ("属性", "Element", "屬性", "荒野", False, "system"),
    ("火", "Fire", "火", "荒野", False, "ui"),
    ("水", "Water", "水", "荒野", False, "ui"),
    ("雷", "Thunder", "雷", "荒野", False, "ui"),
    ("氷", "Ice", "冰", "荒野", False, "ui"),
    ("龍", "Dragon", "龍", "荒野", False, "ui"),
    ("毒", "Poison", "毒", "荒野", False, "ui"),
    ("麻痺", "Paralysis", "麻痺", "荒野", False, "ui"),
    ("睡眠", "Sleep", "睡眠", "荒野", False, "ui"),
    ("爆破", "Blast", "爆破", "荒野", False, "ui"),
    ("気絶", "Stun", "昏厥", "台灣慣用待核：昏厥／暈眩", False, "system"),
    ("切れ味", "Sharpness", "鋒利度", "荒野", False, "ui"),
    ("会心率", "Affinity", "會心率", "荒野", False, "ui"),
    ("防御力", "Defense", "防禦力", "荒野", False, "ui"),
    ("攻撃力", "Attack", "攻擊力", "荒野", False, "ui"),
    ("成功", "Success", "成功", "系統清楚", False, "system"),
    ("失敗", "Failure", "失敗", "系統清楚", False, "system"),
    ("制限時間", "Time Limit", "限制時間", "系統", False, "system"),
    ("報酬", "Reward", "報酬", "系統", False, "system"),
    ("納品", "Deliver", "交貨", "任務條件", False, "system"),
    ("討伐", "Hunt / Slay", "討伐", "荒野任務用語", False, "system"),
    ("捕獲", "Capture", "捕獲", "荒野", False, "system"),
]
for jp, en, zh, note, fr, reg in systems:
    add("frontier" if fr else "system", jp, en, zh, "" if fr else zh, fr, reg, note)

for jp, en, zh in [
    ("回復薬", "Potion", "回復藥"),
    ("回復薬グレート", "Mega Potion", "回復藥．大"),
    ("解毒薬", "Antidote", "解毒藥"),
    ("冷却飲料", "Cool Drink", "冷卻飲料"),
    ("保温飲料", "Hot Drink", "保溫飲料"),
    ("鬼人薬", "Demondrug", "鬼人藥"),
    ("硬化薬", "Armorskin", "硬化藥"),
    ("力の護符", "Powercharm", "力量護符"),
    ("守りの護符", "Armorcharm", "守護護符"),
    ("力の爪", "Powertalon", "力量之爪"),
    ("守りの爪", "Armortalon", "守護之爪"),
    ("砥石", "Whetstone", "砥石"),
    ("捕獲用麻酔玉", "Tranq Bomb", "捕獲用麻醉球"),
    ("落とし穴", "Pitfall Trap", "陷阱"),
    ("シビレ罠", "Shock Trap", "麻痺陷阱"),
    ("生肉", "Raw Meat", "生肉"),
]:
    add("item", jp, en, zh, zh, False, "ui", "荒野道具名")

for en, zh in [
    ("Helm", "頭盔"),
    ("Cap", "兜帽"),
    ("Mail", "鎧甲"),
    ("Vest", "背心"),
    ("Greaves", "護腿"),
    ("Guards", "腕甲"),
    ("Tassets", "腰甲"),
    ("Coil", "腰甲"),
    ("Nothing Equipped", "未裝備"),
    ("Leather", "皮革"),
    ("Bone", "骨製"),
    ("Iron", "鐵"),
    ("Chainmail", "鎖鍊"),
    ("Alloy", "合金"),
]:
    add("ui", "", en, zh, zh, False, "ui", "裝備／部位常見詞")

monster_map = {
    "Rathalos": ("雄火龍", "荒野／系列"),
    "Rathian": ("雌火龍", "荒野／系列"),
    "Khezu": ("電龍", "系列"),
    "Basarios": ("岩龍", "系列"),
    "Gravios": ("鎧龍", "系列"),
    "Diablos": ("角龍", "荒野／系列"),
    "Monoblos": ("一角龍", "系列"),
    "Tigrex": ("轟龍", "系列"),
    "Nargacuga": ("迅龍", "系列"),
    "Barioth": ("冰牙龍", "系列"),
    "Zinogre": ("雷狼龍", "荒野／系列"),
    "Brachydios": ("碎龍", "系列"),
    "Deviljho": ("恐暴龍", "系列"),
    "Rajang": ("金獅子", "系列"),
    "Kirin": ("麒麟", "荒野／系列"),
    "Kushala": ("鋼龍", "系列"),
    "Teostra": ("炎王龍", "荒野／系列"),
    "Chameleos": ("霞龍", "系列"),
    "Lunastra": ("炎妃龍", "系列"),
    "Akantor": ("霸龍", "系列"),
    "Ukanlos": ("崩龍", "系列"),
    "Alatreon": ("煌黑龍", "系列"),
    "Fatalis": ("黑龍", "系列"),
    "Veloci": ("藍速龍", "詞綴／藍速龍王系列"),
    "Geno": ("黃速龍", "詞綴"),
    "Ioprey": ("紅速龍", "系列"),
    "Giaprey": ("白速龍", "系列"),
    "Conga": ("桃毛獸", "系列"),
    "Blango": ("雪獅子", "系列"),
    "Ceanataur": ("鐮蟹", "系列"),
    "Daimyo": ("大名盾蟹", "系列"),
    "Shogun": ("將軍鐮蟹", "系列"),
    "Plesioth": ("水龍", "系列"),
    "Lavasioth": ("熔岩龍", "系列"),
    "Garuga": ("黑狼鳥", "系列"),
    "Gypceros": ("毒怪鳥", "系列"),
    "Hypnocatrice": ("眠鳥", "Frontier／系列"),
    "Espinas": ("棘龍", "Frontier"),
    "Pariapuria": ("吞食元祖", "Frontier"),
    "Raviente": ("拉維克", "Frontier 大討伐"),
    "Felyne": ("艾路", "系列"),
    "Melynx": ("梅拉路", "系列"),
    "Shakalaka": ("奇面族", "系列"),
    "Vespoid": ("巨蜂", "系列"),
    "Hornetaur": ("巨甲蟲", "系列"),
    "Kelbi": ("溫暖草食龍", "系列"),
    "Mosswine": ("蘑菇豬", "系列"),
    "Aptonoth": ("艾普諾斯", "系列"),
    "Popo": ("波波", "系列"),
    "Bullfango": ("野豬", "系列"),
    "Hermitaur": ("盾蟹", "系列"),
    "Remobra": ("翼蛇龍", "系列"),
    "Lagiacrus": ("海龍", "系列"),
    "Gobul": ("燈魚龍", "系列"),
    "Qurupeco": ("彩鳥", "系列"),
    "Agnaktor": ("炎戈龍", "系列"),
    "Uragaan": ("爆錘龍", "系列"),
    "Duramboros": ("尾錘龍", "系列"),
    "Nibelsnarf": ("潛口龍", "系列"),
    "Barroth": ("土砂龍", "系列"),
    "Gigginox": ("毒怪龍", "系列"),
    "Zenith": ("極位", "Frontier 詞綴"),
    "Kut-Ku": ("怪鳥", "系列"),
}

frontier_keys = {
    "Zenith",
    "Espinas",
    "Pariapuria",
    "Raviente",
    "Hypnocatrice",
}

name_files = [
    "dat-weapons-melee-name.csv",
    "dat-weapons-ranged-name.csv",
    "dat-armors-head.csv",
    "dat-armors-body.csv",
    "dat-items-name.csv",
]

seen_mon = set()
for fn in name_files:
    path = EXTRACTED / fn
    if not path.exists():
        continue
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            text = row.get("source") or ""
            low = text.lower()
            for key in monster_map:
                if key.lower() in low:
                    seen_mon.add(key)

for key in sorted(seen_mon):
    zh, note = monster_map[key]
    fr = key in frontier_keys
    add(
        "frontier" if fr else "monster",
        "",
        key,
        zh,
        "" if fr else zh,
        fr,
        "ui",
        f"自抽出名稱偵測；{note}",
    )

common_item_en = {
    "Herbal Medicine": "漢方藥",
    "Max Potion": "萬能藥",
    "Ancient Potion": "秘藥",
    "Well-done Steak": "熟牛排",
    "Rare Steak": "半熟牛排",
    "Flash Bomb": "閃光彈",
    "Sonic Bomb": "音爆彈",
    "Barrel Bomb L": "大桶爆彈",
    "Barrel Bomb S": "小桶爆彈",
    "Smoke Bomb": "煙霧彈",
    "Might Seed": "力量種子",
    "Adamant Seed": "忍耐種子",
    "Nulberry": "消散果",
    "Honey": "蜂蜜",
    "Herb": "藥草",
    "Book of Combos 1": "調合書①",
    "Alchemy Guide": "煉金術指南",
    "Mega Demondrug": "鬼人藥．大",
    "Mega Armorskin": "硬化藥．大",
}

existing_en = {(r["source_en"] or "").lower() for r in seed}
for en, zh in common_item_en.items():
    if en.lower() in existing_en:
        continue
    add("item", "", en, zh, zh, False, "ui", "自抽出常見道具／荒野對照")
    existing_en.add(en.lower())

fields = [
    "id",
    "category",
    "source_jp",
    "source_en",
    "target_zh_tw",
    "wilds_ref",
    "frontier_only",
    "register",
    "display_ok",
    "fallback_glyph",
    "notes",
    "approved",
]

cat_count = Counter()
rows = []
for r in seed:
    cat_count[r["category"]] += 1
    cid = f"{r['category'][:3].upper()}{cat_count[r['category']]:03d}"
    rows.append({"id": cid, **r})

seen = set()
uniq = []
for r in rows:
    key = (r["source_jp"], r["source_en"], r["target_zh_tw"])
    if key in seen:
        continue
    seen.add(key)
    uniq.append(r)

with OUT.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(uniq)

by = {}
for r in uniq:
    by.setdefault(r["category"], []).append(r)

lines = [
    "# 詞語庫初稿審閱",
    "",
    "> 本體抽出名稱以**英文**為主；譯文採台灣繁中，MH 詞彙以《荒野》為準。",
    "> `frontier_only=Y` 為 Frontier 專有。請把同意的列在 CSV 把 `approved` 改成 `Y`。",
    "",
    f"總詞條：{len(uniq)}",
    "",
]
for cat in sorted(by):
    lines.append(f"## {cat}（{len(by[cat])}）")
    lines.append("")
    lines.append("| 原文(EN/JP) | 建議繁中 | Frontier | 備註 |")
    lines.append("|---|---|---|---|")
    for r in by[cat]:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(
            f"| {src} | {r['target_zh_tw']} | {r['frontier_only']} | {r['notes']} |"
        )
    lines.append("")

REVIEW.write_text("\n".join(lines), encoding="utf-8")
print(f"terms {len(uniq)} -> {OUT}")
print(f"review -> {REVIEW}")
for cat, n in cat_count.most_common():
    print(f"  {cat}: {n}")
