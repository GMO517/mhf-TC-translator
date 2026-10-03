# -*- coding: utf-8 -*-
"""同步 REVIEW.md 手動修改，並擴充 MHF 特有魔物詞條。"""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXTRACTED = ROOT.parent / "extracted"
TERMS = ROOT / "terms.csv"
REVIEW = ROOT / "REVIEW.md"

# REVIEW 手動修正（相對初稿）
MANUAL_FIXES = {
    ("monster", "Kelbi"): ("精靈鹿", "使用者修正；系列慣用"),
    ("monster", "Khezu"): ("奇怪龍", "使用者修正；系列慣用"),
    ("weapon_type", "Magnet Spike"): ("磁斬槌", "使用者修正；Frontier 專有武器"),
}

# MHF／Frontier 特有或高出現魔物（英／日／繁）
# 繁中以台灣社群／舊 COG／系列慣用為準，待審
MHF_MONSTERS = [
    # 已有系列但補亞種詞綴
    ("棘竜", "Espinas", "棘龍", True, "Frontier 主力"),
    ("エスピナス亜種", "Orange Espinas", "橘棘龍", True, "Frontier 亞種"),
    ("エスピナス希少種", "White Espinas", "白棘龍", True, "Frontier 稀有種"),
    ("ヒプノック", "Hypnocatrice", "眠鳥", True, "Frontier／舊作"),
    ("ヒプノック繁殖期", "Breeding Season Hypnoc", "繁殖期眠鳥", True, "Frontier"),
    ("パリアプリア", "Pariapuria", "吞食元祖", True, "Frontier"),
    ("ラヴィエンテ", "Raviente", "拉維克", True, "Frontier 大討伐"),
    ("ラヴィエンテ猛狂", "Violent Raviente", "猛狂拉維克", True, "Frontier"),
    ("アクラ・ヴァシム", "Akura Vashimu", "晶蠍", True, "Frontier"),
    ("アクラ・ジェビア", "Akura Jebia", "紫晶蠍", True, "Frontier"),
    ("アノルパティス", "Anorupatisu", "冰鯊", True, "Frontier"),
    ("ポカラ", "Pokara", "波卡拉", True, "Frontier 小怪"),
    ("ポカラドン", "Pokaradon", "波卡拉頓", True, "Frontier"),
    ("ミドガロン", "Midogaron", "炎狐龍", True, "Frontier"),
    ("ギアオルグ", "Giaorugu", "凍狐龍", True, "Frontier"),
    ("アビオルグ", "Abiorugu", "熾狐龍", True, "Frontier"),
    ("ガスラバズラ", "Gasurabazura", "岩穿龍", True, "Frontier"),
    ("ベルキュロス", "Berukyurosu", "舞雷龍", True, "Frontier"),
    ("ドラギュロス", "Doragyurosu", "煌雷龍", True, "Frontier"),
    ("ヒュジキキ", "Hyujikiki", "針纏龍", True, "Frontier"),
    ("クアルセプス", "Kuarusepusu", "泡狐？待核／水獸系", True, "Frontier；譯名待審"),
    ("オディバトラス", "Odibatorasu", "崩砦蟹", True, "Frontier"),
    ("トリドクレス", "Toridcless", "照閃鳥", True, "Frontier"),
    ("バルラガル", "Baruragaru", "喰血龍", True, "Frontier"),
    ("ミ・ル", "Mi Ru", "密盧", True, "Frontier；譯名待審"),
    ("ディスフィロア", "Disufiroa", "煌黑龍迪斯菲羅亞", True, "Frontier 天廊／極位系；簡稱待審"),
    ("シャンティエン", "Shantien", "天廻龍", True, "Frontier"),
    ("エルゼリオン", "Elzelion", "雙極龍", True, "Frontier"),
    ("ゼルレウス", "Zerureusu", "輝火龍", True, "Frontier"),
    ("メラギナス", "Meraginasu", "黑蝕？待核／黑龍系", True, "Frontier；譯名待審"),
    ("ディオレックス", "Diorekkusu", "電甲龍", True, "Frontier"),
    ("グレアドモス", "Gureadomosu", "水砦龍", True, "Frontier"),
    ("ポボルバルム", "Poborubarumu", "霧海龍／待核", True, "Frontier；譯名待審"),
    ("ヴァルサブロス", "Varusaburosu", "炎角龍", True, "Frontier"),
    ("ヴォルジャン", "Voljang", "爆狼？待核", True, "Frontier；譯名待審"),
    ("ゼナセリス", "Zenaserisu", "天彗龍？待核", True, "Frontier；譯名待審"),
    ("ケオアルボル", "Keoaruboru", "焦炎王？待核", True, "Frontier；譯名待審"),
    ("ゴア・マガラ", "Gore Magala", "黑蝕龍", False, "系列／荒野有關聯譜系"),
    ("シャガルマガラ", "Shagaru Magala", "天迴龍／天彗龍", False, "系列；與 Shantien 勿混淆"),
    ("アマツマガツチ", "Amatsu", "嵐龍", False, "系列"),
    ("アルセルタス", "Seltas", "徹甲蟲", False, "系列"),
    ("セルタス女王", "Seltas Queen", "重甲蟲", False, "系列"),
    ("ネルスキュラ", "Nerscylla", "影蜘蛛", False, "系列"),
    ("ガララアジャラ", "Kecha Wacha", "奇猿狐", False, "系列"),
    ("テツカブラ", "Tetsucabra", "鬼蛙", False, "系列"),
    ("ザボアザギル", "Zamtrios", "鬼鮫", False, "系列"),
    ("ホロロホルル", "Malfestio", "夜鳥", False, "系列"),
    ("ディノバルド", "Glavenus", "斬龍", False, "系列"),
    ("ライゼクス", "Astalos", "電龍", False, "系列；勿與奇怪龍混淆"),
    ("タマミツネ", "Mizutsune", "泡狐龍", False, "荒野／系列"),
    ("ガムート", "Gammoth", "巨獸", False, "系列"),
    ("ナルガクルガ", "Nargacuga", "迅龍", False, "系列"),
    ("ジンオウガ", "Zinogre", "雷狼龍", False, "荒野／系列"),
    ("イビルジョー", "Deviljho", "恐暴龍", False, "系列"),
    ("ラージャン", "Rajang", "金獅子", False, "系列"),
    ("ティガレックス", "Tigrex", "轟龍", False, "系列"),
    ("バルファルク", "Valstrax", "天彗龍", False, "系列"),
    ("イャンクック", "Yian Kut-Ku", "怪鳥", False, "系列"),
    ("イャンガルルガ", "Yian Garuga", "黑狼鳥", False, "系列"),
    ("ドスランポス", "Velocidrome", "藍速龍王", False, "系列"),
    ("ドスゲネポス", "Gendrome", "黃速龍王", False, "系列"),
    ("ドスイーオス", "Iodrome", "紅速龍王", False, "系列"),
    ("ドスギアノス", "Giadrome", "白速龍王", False, "系列"),
    ("フルフル", "Khezu", "奇怪龍", False, "使用者用語"),
    ("ケルトビスク", "Cephalos", "砂龍", False, "系列"),
    ("ガノトトス", "Plesioth", "水龍", False, "系列"),
    ("リオレウス", "Rathalos", "雄火龍", False, "荒野"),
    ("リオレイア", "Rathian", "雌火龍", False, "荒野"),
    ("リオレウス希少種", "Silver Rathalos", "銀火龍", False, "系列"),
    ("リオレイア希少種", "Gold Rathian", "金火龍", False, "系列"),
    ("リオレウス亜種", "Azure Rathalos", "蒼火龍", False, "系列"),
    ("リオレイア亜種", "Pink Rathian", "櫻火龍", False, "系列"),
    ("クシャルダオラ", "Kushala Daora", "鋼龍", False, "系列"),
    ("テオ・テスカトル", "Teostra", "炎王龍", False, "荒野"),
    ("ナナ・テスカトリ", "Lunastra", "炎妃龍", False, "系列"),
    ("オオナズチ", "Chameleos", "霞龍", False, "系列"),
    ("ミラボレアス", "Fatalis", "黑龍", False, "系列"),
    ("老山龍", "Lao-Shan Lung", "老山龍", False, "系列"),
    ("ヤマツカミ", "Yama Tsukami", "山神龍", False, "系列"),
    ("シェンガオレン", "Shen Gaoren", "砦蟹", False, "系列"),
    ("シャンティエン", "Shantien", "天廻龍", True, "Frontier"),
    ("タイクンザムザ", "Taikun Zamuza", "大君蟹", True, "Frontier"),
    ("ハプルボッカ", "Hapulubokka", "河童蛙？待核", True, "Frontier；譯名待審"),
    ("ウルクムルク", "Uruki", "小兔？待核", True, "Frontier 小怪；譯名待審"),
    ("ファーガナ", "Farunakk", "待核", True, "Frontier；譯名待審"),
    ("ゴウガルフ", "Gougarf", "剛猿？待核", True, "Frontier；譯名待審"),
    ("ケオアルボル", "Keoaruboru", "焦炎王待核", True, "Frontier"),
    ("グァンゾルム", "Guanzorumu", "戰帝王龍", True, "Frontier"),
    ("ディスフィロア", "Disufiroa", "煌黑龍", True, "Frontier；簡稱待審"),
    ("エルゼリオン", "Eruzerion", "雙極龍", True, "Frontier"),
    ("アルガノス", "Aruganosu", "銀火？待核", True, "Frontier 對；譯名待審"),
    ("ゴルガノス", "Goruganosu", "金火？待核", True, "Frontier 對；譯名待審"),
    ("フォルタイオス", "Forokururu", "彩鳥系？待核", True, "Frontier；譯名待審"),
    ("レビディオラ", "Rebidiora", "雷龍？待核", True, "Frontier；譯名待審"),
    ("トリドクレス", "Toridcless", "照閃鳥", True, "Frontier"),
    ("ボルボロス", "Barroth", "土砂龍", False, "系列"),
    ("ウラガンキン", "Uragaan", "爆錘龍", False, "系列"),
    ("アグナコトル", "Agnaktor", "炎戈龍", False, "系列"),
    ("イビルジョー", "Deviljho", "恐暴龍", False, "系列"),
    ("ブラキディオス", "Brachydios", "碎龍", False, "系列"),
    ("ベリオロス", "Barioth", "冰牙龍", False, "系列"),
    ("ジンオウガ亜種", "Stygian Zinogre", "獄狼龍", False, "系列"),
    ("ティガレックス亜種", "Brute Tigrex", "黑轟龍", False, "系列"),
    ("ナルガクルガ亜種", "Green Nargacuga", "綠迅龍", False, "系列"),
    ("アカムトルム", "Akantor", "霸龍", False, "系列"),
    ("ウカムルバス", "Ukanlos", "崩龍", False, "系列"),
    ("アルビノ", "Albino", "白變種詞綴", True, "Frontier 詞綴待核"),
    ("ヒプノック希少種", "Silver Hypnocatrice", "銀眠鳥", True, "Frontier"),
    ("デュラガウア", "Duramboros", "尾錘龍", False, "系列"),
    ("ハプルボッカ", "Hapulubokka", "河童蛙", True, "Frontier"),
    ("ゴア・マガラ", "Gore Magala", "黑蝕龍", False, "系列"),
    ("シャガルマガラ", "Shagaru Magala", "天迴龍", False, "系列"),
    ("オディバトラ", "Odibatorasu", "崩砦蟹", True, "Frontier"),
    ("バルファルク", "Valstrax", "天彗龍", False, "系列"),
    ("ラージャン", "Rajang", "金獅子", False, "系列"),
    ("キリン", "Kirin", "麒麟", False, "荒野"),
    ("クシャルダオラ", "Kushala Daora", "鋼龍", False, "系列"),
    ("ヤマクライ", "Inagami", "雲羊鹿？待核／Frontier", True, "Frontier；譯名待審"),
    ("イナガミ", "Inagami", "雲羊鹿", True, "Frontier"),
    ("トリドクレス", "Toridcless", "照閃鳥", True, "Frontier"),
    ("ボガバドール", "Bogabadorumu", "爆鎚？待核", True, "Frontier；譯名待審"),
    ("ドゥレムディア", "Duremudira", "天廊守護龍", True, "Frontier 天廊"),
    ("UNKNOWN", "Unknown", "未知怪物", True, "占位／遷悠相關待核"),
]


def load_terms() -> list[dict]:
    with TERMS.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def apply_manual_fixes(rows: list[dict]) -> int:
    changed = 0
    for r in rows:
        key = (r["category"], r["source_en"])
        if key in MANUAL_FIXES:
            zh, note = MANUAL_FIXES[key]
            if r["target_zh_tw"] != zh or note not in (r.get("notes") or ""):
                r["target_zh_tw"] = zh
                if r["category"] != "frontier" and r.get("wilds_ref"):
                    # 非 Frontier 專有且有 wilds_ref 時可同步
                    if key[1] in {"Kelbi", "Khezu"}:
                        r["wilds_ref"] = zh
                r["notes"] = note
                r["approved"] = "Y"  # 使用者已在 REVIEW 手改 → 視同核准該列
                changed += 1
        # Magnet Spike 在 weapon_type
        if r["source_en"] == "Magnet Spike":
            r["target_zh_tw"] = "磁斬槌"
            r["notes"] = "使用者修正；Frontier 專有武器"
            r["approved"] = "Y"
            r["frontier_only"] = "Y"
            changed += 1
    return changed


def mine_tokens() -> Counter:
    pat = re.compile(r"\b([A-Z][A-Za-z][A-Za-z'-]{2,})\b")
    c: Counter = Counter()
    for fn in [
        "dat-weapons-melee-name.csv",
        "dat-weapons-ranged-name.csv",
        "dat-armors-head.csv",
        "dat-armors-body.csv",
        "dat-items-name.csv",
    ]:
        path = EXTRACTED / fn
        if not path.exists():
            continue
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                for m in pat.findall(row.get("source") or ""):
                    c[m] += 1
    return c


def existing_en(rows: list[dict]) -> set[str]:
    return {(r.get("source_en") or "").strip().lower() for r in rows if r.get("source_en")}


def add_monsters(rows: list[dict]) -> int:
    have = existing_en(rows)
    # 也比對 target 避免日文重複
    have_jp = {(r.get("source_jp") or "").strip() for r in rows}
    added = 0
    n = sum(1 for r in rows if r["category"] == "monster")
    f = sum(1 for r in rows if r["category"] == "frontier")

    for jp, en, zh, frontier, note in MHF_MONSTERS:
        if en.strip().lower() in have:
            # 更新已存在列的繁中（若手動表有更好譯名且尚未 approved）
            continue
        if jp and jp in have_jp:
            continue
        if frontier:
            f += 1
            cid = f"FRO{f:03d}"
            cat = "frontier"
        else:
            n += 1
            cid = f"MON{n:03d}"
            cat = "monster"
        rows.append(
            {
                "id": cid,
                "category": cat,
                "source_jp": jp,
                "source_en": en,
                "target_zh_tw": zh,
                "wilds_ref": "" if frontier else zh,
                "frontier_only": "Y" if frontier else "N",
                "register": "ui",
                "display_ok": "pending",
                "fallback_glyph": "",
                "notes": f"MHF 擴充；{note}",
                "approved": "N",
            }
        )
        have.add(en.strip().lower())
        if jp:
            have_jp.add(jp)
        added += 1
    return added


def rewrite_ids(rows: list[dict]) -> list[dict]:
    """依 category 重編 id，保持穩定閱讀。"""
    counters: Counter = Counter()
    out = []
    # 固定類別順序
    order = [
        "weapon_type",
        "system",
        "frontier",
        "item",
        "monster",
        "ui",
        "place",
        "npc",
    ]
    by = {k: [] for k in order}
    other = []
    for r in rows:
        if r["category"] in by:
            by[r["category"]].append(r)
        else:
            other.append(r)
    for cat in order:
        for r in by[cat]:
            counters[cat] += 1
            prefix = cat[:3].upper()
            r = dict(r)
            r["id"] = f"{prefix}{counters[cat]:03d}"
            out.append(r)
    for r in other:
        counters[r["category"]] += 1
        r = dict(r)
        r["id"] = f"{r['category'][:3].upper()}{counters[r['category']]:03d}"
        out.append(r)
    return out


def write_terms(rows: list[dict]) -> None:
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
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def write_review(rows: list[dict], mined_extra: list[tuple[str, int]]) -> None:
    by: dict[str, list] = {}
    for r in rows:
        by.setdefault(r["category"], []).append(r)

    lines = [
        "# 詞語庫初稿審閱",
        "",
        "> 本體抽出名稱以**英文**為主；譯文採台灣繁中，MH 詞彙以《荒野》為準。",
        "> `frontier_only=Y` 為 Frontier 專有。同意的列請在 CSV 把 `approved` 改成 `Y`（或繼續改本檔後再同步）。",
        "",
        f"總詞條：{len(rows)}",
        "",
        "## 本次使用者已核准（來自 REVIEW 手改）",
        "",
        "| 原文 | 建議繁中 |",
        "|---|---|",
        "| Kelbi | 精靈鹿 |",
        "| Khezu | 奇怪龍 |",
        "| Magnet Spike | 磁斬槌 |",
        "",
    ]
    for cat in sorted(by):
        lines.append(f"## {cat}（{len(by[cat])}）")
        lines.append("")
        lines.append("| 原文(EN/JP) | 建議繁中 | Frontier | approved | 備註 |")
        lines.append("|---|---|---|---|---|")
        for r in by[cat]:
            src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
            lines.append(
                f"| {src} | {r['target_zh_tw']} | {r['frontier_only']} | {r['approved']} | {r['notes']} |"
            )
        lines.append("")

    if mined_extra:
        lines.append("## 裝備／道具詞綴候選（尚未入庫，供下輪）")
        lines.append("")
        lines.append("| 英文詞綴 | 出現次數 |")
        lines.append("|---|---|")
        for w, c in mined_extra[:80]:
            lines.append(f"| {w} | {c} |")
        lines.append("")

    REVIEW.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = load_terms()
    fix_n = apply_manual_fixes(rows)
    add_n = add_monsters(rows)

    # 去重：同 source_en 保留第一筆（已修正者優先）
    seen = set()
    uniq = []
    for r in rows:
        k = (r["category"], (r.get("source_en") or "").lower(), r.get("source_jp") or "")
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)

    uniq = rewrite_ids(uniq)

    tokens = mine_tokens()
    have = existing_en(uniq)
    stop = {
        "nothing",
        "equipped",
        "hunter",
        "leather",
        "chainmail",
        "bone",
        "iron",
        "alloy",
        "sword",
        "blade",
        "helm",
        "mail",
        "cap",
        "vest",
        "greaves",
        "guards",
        "tassets",
        "coil",
        "great",
        "long",
        "heavy",
        "light",
        "true",
        "fake",
        "plus",
        "series",
        "armor",
        "weapon",
        "item",
        "book",
        "guide",
        "potion",
        "bomb",
        "trap",
        "seed",
        "drink",
        "steak",
        "meat",
        "charm",
        "talon",
        "shell",
        "scale",
        "claw",
        "fang",
        "wing",
        "tail",
        "head",
        "hide",
        "horn",
        "ore",
        "gem",
        "jewel",
        "ticket",
        "coin",
        "medal",
        "stone",
        "crystal",
        "normal",
        "pierce",
        "pellet",
        "crag",
        "cluster",
        "status",
        "element",
        "attack",
        "defense",
        "health",
        "stamina",
        "expert",
        "reload",
        "recoil",
        "affinity",
        "sharpness",
        "mega",
        "max",
        "ancient",
        "raw",
        "cool",
        "hot",
        "flash",
        "sonic",
        "smoke",
        "barrel",
        "shock",
        "pitfall",
        "tranq",
        "capture",
        "herbal",
        "medicine",
        "alchemy",
        "combos",
        "well",
        "rare",
        "might",
        "adamant",
        "honey",
        "herb",
        "nulberry",
        "powercharm",
        "armorcharm",
        "powertalon",
        "armortalon",
        "demondrug",
        "armorskin",
        "whetstone",
        "antidote",
        "cross",
        "shotgun",
        "valkyrie",
        "spartacus",
        "hornet",
        "buster",
        "hellish",
        "slasher",
        "soul",
        "blue",
        "red",
        "black",
        "white",
        "gold",
        "silver",
        "green",
        "pink",
        "azure",
        "crimson",
        "dark",
        "super",
        "hyper",
        "ultra",
        "guard",
        "marathon",
        "recover",
        "demon",
    }
    mined_extra = []
    for w, c in tokens.most_common(500):
        if c < 12:
            continue
        if w.lower() in stop or w.lower() in have:
            continue
        if not w[0].isupper():
            continue
        mined_extra.append((w, c))

    write_terms(uniq)
    write_review(uniq, mined_extra)
    mon = sum(1 for r in uniq if r["category"] == "monster")
    fro = sum(1 for r in uniq if r["category"] == "frontier" and "龍" in r["target_zh_tw"] or r["category"] == "frontier")
    print(f"manual_fixes~={fix_n}")
    print(f"added_monsters={add_n}")
    print(f"total={len(uniq)} monster_rows={mon}")
    print(f"review={REVIEW}")
    print(f"mined_candidates={len(mined_extra)}")


if __name__ == "__main__":
    main()
