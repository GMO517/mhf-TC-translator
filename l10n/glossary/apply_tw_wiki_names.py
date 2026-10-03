# -*- coding: utf-8 -*-
"""
更新邊境魔物譯名。

命名優先序（本專案）：
1. 邊境專屬魔物 → 以 MHFO 台灣 wiki 為主
   https://w.atwiki.jp/mhfotw/ （魔物一覽 pages/22）
2. 真的找不到慣用名時 → 再查台服 wiki；仍無則標「找不到」
3. 系列共通魔物／系統詞 → 玩家常講 ≥ 日文漢字 ≥ 荒野（不強制蓋台服）

備註維持短標籤；修改／找不到供審核。
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

# 來源：https://w.atwiki.jp/mhfotw/pages/22.html 魔物一覽
# (zh, note) note 短標籤；None zh → 找不到
TW_WIKI: dict[str, tuple[str | None, str]] = {
    "Espinas": ("棘龍", "台服"),
    "Orange Espinas": ("棘茶龍", "台服"),
    "White Espinas": ("棘白龍", "台服"),
    "Hypnocatrice": ("眠鳥", "台服"),
    "Breeding Season Hypnoc": ("蒼眠鳥", "台服"),
    "Silver Hypnocatrice": ("白眠鳥", "台服"),
    "Pariapuria": ("吞龍", "台服"),
    "Raviente": ("大巖龍", "台服"),
    "Violent Raviente": ("猛狂大巖龍", "台服"),
    "Akura Vashimu": ("尾晶蠍", "台服"),
    "Akura Jebia": ("灰晶蠍", "台服"),
    "Anorupatisu": ("暴鋸龍", "台服"),
    "Pokara": ("凍海獸", "台服"),
    "Pokaradon": ("凍海獸", "台服"),
    "Midogaron": ("爆狼", "台服"),
    "Giaorugu": ("冰獰龍", "台服"),
    "Abiorugu": ("獰龍", "台服"),
    "Gasurabazura": ("怒貌龍", "台服"),
    "Berukyurosu": ("舞雷龍", "台服"),
    "Doragyurosu": ("冥雷龍", "台服"),
    "Hyujikiki": ("針纏龍", "台服"),
    "Kuarusepusu": ("晶龍", "台服"),
    "Odibatorasu": ("弩岩龍", "台服"),
    "Toridcless": ("照雷鳥", "台服"),
    "Baruragaru": ("噬血龍", "台服"),
    "Mi Ru": ("黑狐龍", "台服"),
    "Disufiroa": ("熾凍龍", "台服"),
    "Shantien": ("天翔龍", "台服"),
    "Elzelion": ("灼零龍", "台服"),
    "Zerureusu": ("輝界龍", "台服"),
    "Meraginasu": ("黑穿龍", "台服"),
    "Diorekkusu": ("雷轟龍", "台服"),
    "Gureadomosu": ("水砦龍", "台服"),
    "Poborubarumu": ("創音龍", "台服"),
    "Varusaburosu": ("炎角龍", "台服"),
    "Zenaserisu": ("裂水龍", "台服"),
    "Keoaruboru": ("焰嶽龍", "台服"),
    "Taikun Zamuza": ("多殼蟹", "台服"),
    "Gougarf": ("鬥獸", "台服"),
    "Guanzorumu": ("帝征龍", "台服"),
    "Aruganosu": ("白銀魚龍", "台服"),
    "Goruganosu": ("黃金魚龍", "台服"),
    "Forokururu": ("華鳳鳥", "台服"),
    "Rebidiora": ("雷極龍", "台服"),
    "Inagami": ("雅翁龍", "台服"),
    "Duremudira": ("皇冰龍", "台服"),
    "Voljang": ("紅蓮獅子", "台服"),
    # wiki 一覽未見穩定條目
    "Bogabadorumu": (None, "找不到"),
    "Hapulubokka": (None, "找不到"),
    "Uruki": (None, "找不到"),
}

# 一併補上台服有、我們缺的 Frontier 魔物（可選入庫）
EXTRA_FROM_TW = [
    ("響狼", "カム・オルガロン", "Kamu Orugaron", "響狼"),
    ("雌響狼", "ノノ・オルガロン", "Nono Orugaron", "雌響狼"),
    ("跳緋獸", "ゴゴモア", "Gogomoa", "跳緋獸"),
    ("冰狐龍", "デュラガウア", "Duragaua", "冰狐龍"),
    ("蠻龍", "グレンゼブル", "Gurenzeburu", "蠻龍"),
    ("極龍", "ルコディオラ", "Rukodiora", "極龍"),
    ("金塵龍", "ガルバダオラ", "Garuba Daora", "金塵龍"),
    ("司銀龍", "ハルドメルグ", "Harudomerugu", "司銀龍"),
    ("浮峰龍", "ヤマクライ", "Yama Kurai", "浮峰龍"),
    ("凍王龍", "トア・テスカトラ", "Toa Tesukatora", "凍王龍"),
    ("傾雷鳥", "ファルノック", "Farunokku", "傾雷鳥"),
]


def main() -> None:
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    have_en = {(r.get("source_en") or "").lower() for r in rows}

    for r in rows:
        r.setdefault("review_flag", "")
        en = (r.get("source_en") or "").strip()
        cat = r.get("category") or ""

        if cat in {"frontier", "frontier_monster"} and en in TW_WIKI:
            zh, note = TW_WIKI[en]
            old = r.get("target_zh_tw") or ""
            r["category"] = "frontier_monster"
            r["frontier_only"] = "Y"
            r["notes"] = note
            if zh is None:
                # 暫留原文片假名／舊譯
                r["review_flag"] = "找不到"
                r["approved"] = "N"
            else:
                r["target_zh_tw"] = zh
                if old != zh:
                    r["review_flag"] = "修改"
                else:
                    r["review_flag"] = "沿用" if r.get("review_flag") != "修改" else "修改"
                # 本次以台服重套：與台服不同過的都標修改（方便你審）
                if old != zh:
                    r["review_flag"] = "修改"
                r["approved"] = "N"
            # JP 修正
            if en == "Forokururu":
                r["source_jp"] = "フォロクルル"
            if en == "Inagami":
                r["source_jp"] = "イナガミ"
            if en == "Voljang":
                r["source_jp"] = "ヴォージャン"
            if en == "Duremudira":
                r["source_jp"] = "ドゥレムディラ"

        elif cat == "frontier_system" or (
            cat == "frontier" and en
            in {
                "GR",
                "G-Rank",
                "Hardcore / HC",
                "Violent Species",
                "Origin Species",
                "Unknown Species",
                "Zenith",
                "Tower",
                "Hunter's Road",
                "Diva",
                "Mezeporta",
            }
        ):
            r["category"] = "frontier_system"
            r["notes"] = "系統"
            r["review_flag"] = ""

        # 略縮其他
        elif cat == "monster":
            r["notes"] = "系列"
        elif cat == "weapon_type":
            r["notes"] = "武器種" if en != "Magnet Spike" else "Frontier 武器"
        elif cat == "system":
            r["notes"] = "系統"
        elif cat == "item":
            r["notes"] = "道具"
        elif cat == "ui":
            r["notes"] = "UI"

        if en in {"Kelbi", "Khezu", "Magnet Spike"}:
            r["approved"] = "Y"
            r["review_flag"] = "你已核准"

    # 補台服有、我們缺的
    n_fmo = sum(1 for r in rows if r.get("category") == "frontier_monster")
    for zh, jp, en, _ in EXTRA_FROM_TW:
        if en.lower() in have_en:
            continue
        n_fmo += 1
        rows.append(
            {
                "id": f"FMO{n_fmo:03d}",
                "category": "frontier_monster",
                "source_jp": jp,
                "source_en": en,
                "target_zh_tw": zh,
                "wilds_ref": "",
                "frontier_only": "Y",
                "register": "ui",
                "display_ok": "pending",
                "fallback_glyph": "",
                "notes": "台服",
                "approved": "N",
                "review_flag": "新增",
            }
        )
        have_en.add(en.lower())

    # 強制：對照台服後仍應審的關鍵修改
    force_mod = {
        "Raviente",
        "Violent Raviente",
        "Duremudira",
        "Voljang",
        "Baruragaru",
        "Silver Hypnocatrice",
        "Gougarf",
        "Pokaradon",
    }
    for r in rows:
        if r.get("source_en") in force_mod and r.get("category") == "frontier_monster":
            if r.get("review_flag") != "找不到":
                r["review_flag"] = "修改"

    rows = rewrite_ids(rows)
    write_terms(rows)
    write_review(rows)
    fm = [r for r in rows if r["category"] == "frontier_monster"]
    print("total", len(rows), "FMO", len(fm))
    print(Counter(r.get("review_flag") or "" for r in fm))


def rewrite_ids(rows: list[dict]) -> list[dict]:
    order = [
        "weapon_type",
        "system",
        "frontier_system",
        "frontier_monster",
        "monster",
        "item",
        "ui",
    ]
    buckets = {k: [] for k in order}
    other = []
    for r in rows:
        (buckets[r["category"]] if r["category"] in buckets else other).append(r)
    counters: Counter = Counter()
    out = []
    for cat in order:
        for r in buckets[cat]:
            counters[cat] += 1
            r = dict(r)
            prefix = {"frontier_system": "FSY", "frontier_monster": "FMO"}.get(
                cat, cat[:3].upper()
            )
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
        "review_flag",
    ]
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_review(rows: list[dict]) -> None:
    by: dict[str, list] = {}
    for r in rows:
        by.setdefault(r["category"], []).append(r)

    mod = [
        r
        for r in by.get("frontier_monster", [])
        if r.get("review_flag") in {"修改", "新增"}
    ]
    miss = [r for r in by.get("frontier_monster", []) if r.get("review_flag") == "找不到"]

    lines = [
        "# 詞語庫審閱",
        "",
        "> 命名優先序：",
        "> 1. **邊境專屬魔物** → 以 [MHFO 台灣 wiki](https://w.atwiki.jp/mhfotw/) 為主",
        "> 2. **真的找不到** → 再查台服；仍無則標「找不到」",
        "> 3. 系列／系統詞 → 玩家常講 ≥ 日文漢字 ≥ 荒野",
        "> 備註已略縮。",
        "",
        f"總詞條：{len(rows)}",
        "",
        "## 請先檢查（修改／新增）",
        "",
        f"{len(mod)} 條",
        "",
        "| EN/JP | 譯名 | 狀態 | 備註 |",
        "|---|---|---|---|",
    ]
    for r in mod:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(
            f"| {src} | {r['target_zh_tw']} | {r['review_flag']} | {r['notes']} |"
        )

    lines += [
        "",
        "## 找不到（台服一覽無條目）",
        "",
        f"{len(miss)} 條",
        "",
        "| EN/JP | 暫定 |",
        "|---|---|",
    ]
    for r in miss:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} |")

    for cat, title, fmo in [
        ("frontier_monster", "邊境魔物（完整）", True),
        ("frontier_system", "Frontier 系統", False),
        ("monster", "系列魔物", False),
        ("weapon_type", "武器種", False),
        ("system", "系統", False),
        ("item", "道具", False),
        ("ui", "UI", False),
    ]:
        if cat not in by:
            continue
        lines += ["", f"## {title}（{len(by[cat])}）", ""]
        if fmo:
            lines += ["| EN/JP | 繁中 | 狀態 | 備註 |", "|---|---|---|---|"]
            for r in by[cat]:
                src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
                lines.append(
                    f"| {src} | {r['target_zh_tw']} | {r.get('review_flag') or '沿用'} | {r['notes']} |"
                )
        else:
            lines += ["| 原文 | 繁中 | ✓ | 備註 |", "|---|---|---|---|"]
            for r in by[cat]:
                src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
                lines.append(
                    f"| {src} | {r['target_zh_tw']} | {r['approved']} | {r['notes']} |"
                )

    REVIEW.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
