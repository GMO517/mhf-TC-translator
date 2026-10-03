# -*- coding: utf-8 -*-
"""
將 Frontier 魔物拆出獨立區塊，套用玩家最常用中文名（日文別名／台服 wiki／華語社群），
縮短備註，並標記「修改／找不到」。
"""
from __future__ import annotations

import csv
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

# 系統／地名等（非魔物）— 留在 frontier_system
SYSTEM_EN = {
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

# 命名優先序：玩家常講 ≥ 日文漢字別名（有則可直接用，竜→龍）≥ 找不到
# value: (zh, note_short, found)
# note 只寫短來源標籤
PLAYER_NAMES: dict[str, tuple[str, str, bool]] = {
    # 棘龍系（玩家／台服＝日文漢字）
    "Espinas": ("棘龍", "玩家", True),
    "Orange Espinas": ("棘茶龍", "玩家", True),
    "White Espinas": ("棘白龍", "玩家", True),
    "Hypnocatrice": ("眠鳥", "玩家", True),
    "Breeding Season Hypnoc": ("蒼眠鳥", "日文", True),
    "Silver Hypnocatrice": ("蒼白眠鳥", "日文", True),
    "Pariapuria": ("吞龍", "玩家", True),
    "Raviente": ("拉維克", "玩家", True),
    "Violent Raviente": ("猛狂拉維克", "玩家", True),
    "Akura Vashimu": ("尾晶蠍", "玩家", True),
    "Akura Jebia": ("灰晶蠍", "玩家", True),
    "Anorupatisu": ("暴鋸龍", "日文", True),
    "Pokara": ("凍海獸", "日文", True),
    "Pokaradon": ("波卡拉頓", "玩家", True),
    "Midogaron": ("爆狼", "日文", True),
    "Giaorugu": ("冰獰龍", "日文", True),
    "Abiorugu": ("獰龍", "日文", True),
    "Gasurabazura": ("怒貌龍", "日文", True),
    "Berukyurosu": ("舞雷龍", "玩家", True),
    "Doragyurosu": ("冥雷龍", "日文", True),
    "Hyujikiki": ("針纏龍", "日文", True),
    "Kuarusepusu": ("晶龍", "日文", True),
    "Odibatorasu": ("弩岩龍", "日文", True),
    "Toridcless": ("照雷鳥", "日文", True),
    "Baruragaru": ("喰血龍", "日文", True),
    "Mi Ru": ("黑狐龍", "日文", True),
    "Disufiroa": ("熾凍龍", "日文", True),
    "Shantien": ("天翔龍", "日文", True),
    "Elzelion": ("灼零龍", "日文", True),
    "Zerureusu": ("輝界龍", "日文", True),
    "Meraginasu": ("黑穿龍", "日文", True),
    "Diorekkusu": ("雷轟龍", "日文", True),
    "Gureadomosu": ("水砦龍", "日文", True),
    "Poborubarumu": ("創音龍", "日文", True),
    "Varusaburosu": ("炎角龍", "日文", True),
    "Zenaserisu": ("裂水龍", "日文", True),
    "Keoaruboru": ("焰嶽龍", "日文", True),
    "Taikun Zamuza": ("多殼蟹", "日文", True),
    "Gougarf": ("鬪獸", "日文", True),
    "Guanzorumu": ("帝征龍", "日文", True),
    "Aruganosu": ("白銀魚龍", "日文", True),
    "Goruganosu": ("黃金魚龍", "日文", True),
    "Forokururu": ("華鳳鳥", "日文", True),
    "Rebidiora": ("雷極龍", "日文", True),
    "Inagami": ("雅翁龍", "日文", True),
    "Bogabadorumu": ("爆霧龍", "日文", True),
    "Duremudira": ("天廊番人", "通稱", True),
    "Voljang": ("ヴォージャン", "找不到", False),
    "Hapulubokka": ("ハプルボッカ", "找不到", False),
    "Uruki": ("ウルクムルク", "找不到", False),
}


def load_rows() -> list[dict]:
    with TERMS.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def split_and_update(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        r = dict(r)
        en = (r.get("source_en") or "").strip()
        cat = r.get("category") or ""

        # Zenith 系統詞綴與魔物無關：系統列保留；魔物偵測重複 Zenith 丟掉
        if cat == "frontier" and en == "Zenith" and "詞綴" in (r.get("notes") or ""):
            continue

        if cat == "frontier":
            if en in SYSTEM_EN or en.startswith("Hardcore"):
                r["category"] = "frontier_system"
                r["notes"] = "Frontier 系統"
                r["review_flag"] = ""
            elif en in PLAYER_NAMES:
                zh, note, found = PLAYER_NAMES[en]
                old = r.get("target_zh_tw") or ""
                r["category"] = "frontier_monster"
                r["target_zh_tw"] = zh
                r["frontier_only"] = "Y"
                r["wilds_ref"] = ""
                if not found:
                    r["notes"] = note
                    r["review_flag"] = "找不到"
                    r["approved"] = "N"
                elif old != zh:
                    r["notes"] = note
                    r["review_flag"] = "修改"
                    r["approved"] = "N"  # 暫不核准，等你檢查
                else:
                    r["notes"] = note
                    r["review_flag"] = "沿用"
                # 修正錯誤日文對照
                if en == "Forokururu":
                    r["source_jp"] = "フォロクルル"
                if en == "Inagami":
                    r["source_jp"] = "イナガミ"
                if en == "Voljang":
                    r["source_jp"] = "ヴォージャン"
            else:
                # 未對表的 frontier 列：若像魔物則進 monster 區並標找不到
                if en and en not in SYSTEM_EN:
                    r["category"] = "frontier_monster"
                    r["notes"] = "未查到慣用名"
                    r["review_flag"] = "找不到"
                else:
                    r["category"] = "frontier_system"
                    r["notes"] = "Frontier 系統"
                    r["review_flag"] = ""
        else:
            r["review_flag"] = r.get("review_flag") or ""

        # 使用者已核准的三條保留
        if en in {"Kelbi", "Khezu", "Magnet Spike"} and r.get("approved") == "Y":
            r["review_flag"] = "你已核准"

        out.append(r)
    return out


def rewrite_ids(rows: list[dict]) -> list[dict]:
    from collections import Counter

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
        if r["category"] in buckets:
            buckets[r["category"]].append(r)
        else:
            other.append(r)
    counters: Counter = Counter()
    final = []
    for cat in order:
        for r in buckets[cat]:
            counters[cat] += 1
            r = dict(r)
            prefix = {
                "frontier_system": "FSY",
                "frontier_monster": "FMO",
            }.get(cat, cat[:3].upper())
            r["id"] = f"{prefix}{counters[cat]:03d}"
            final.append(r)
    for r in other:
        counters[r["category"]] += 1
        r = dict(r)
        r["id"] = f"{r['category'][:3].upper()}{counters[r['category']]:03d}"
        final.append(r)
    return final


def write_terms(rows: list[dict]) -> None:
    # review_flag 寫入 notes 前綴，避免改 CSV schema 太大；同時另存 flag 欄
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
        for r in rows:
            flag = r.get("review_flag") or ""
            note = r.get("notes") or ""
            # notes 保持短：來源；flag 獨立欄
            if flag and flag not in {"", "沿用", "你已核准"}:
                # 修改／找不到已在 flag
                pass
            w.writerow({k: r.get(k, "") for k in fields})


def write_review(rows: list[dict]) -> None:
    by: dict[str, list] = {}
    for r in rows:
        by.setdefault(r["category"], []).append(r)

    mod = [r for r in by.get("frontier_monster", []) if r.get("review_flag") == "修改"]
    miss = [r for r in by.get("frontier_monster", []) if r.get("review_flag") == "找不到"]

    lines = [
        "# 詞語庫審閱",
        "",
        "> 無官中時優先序：**玩家常講 ≥ 日文漢字別名**（有漢字可直接用，竜→龍）。",
        "> 參考：[nenaiko](https://wikiwiki.jp/nenaiko/%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC)／[台服 wiki](https://w.atwiki.jp/mhfotw/pages/22.html)／[華語雜談](https://cowlevel.net/article/1921207)",
        "",
        f"總詞條：{len(rows)}",
        "",
        "## 請你優先檢查：本次修改的邊境魔物",
        "",
        f"共 {len(mod)} 條（狀態＝修改）。",
        "",
        "| EN / JP | 新譯名 | 備註 |",
        "|---|---|---|",
    ]
    for r in mod:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} | {r['notes']} |")

    lines += [
        "",
        "## 找不到穩定中文慣用名",
        "",
        f"共 {len(miss)} 條（暫留日文片假名／學名）。",
        "",
        "| EN / JP | 暫定 | 備註 |",
        "|---|---|---|",
    ]
    for r in miss:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} | {r['notes']} |")

    # frontier_system
    lines += ["", "## frontier_system（系統／地名）", ""]
    lines.append("| 原文 | 繁中 | 備註 |")
    lines.append("|---|---|---|")
    for r in by.get("frontier_system", []):
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} | {r['notes']} |")

    # frontier_monster full
    lines += ["", "## frontier_monster（邊境魔物）", ""]
    lines.append("| EN / JP | 玩家常用繁中 | 狀態 | 備註 |")
    lines.append("|---|---|---|---|")
    for r in by.get("frontier_monster", []):
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        flag = r.get("review_flag") or "沿用"
        lines.append(f"| {src} | {r['target_zh_tw']} | {flag} | {r['notes']} |")

    # other cats compact
    for cat in ["monster", "weapon_type", "system", "item", "ui"]:
        if cat not in by:
            continue
        lines += ["", f"## {cat}（{len(by[cat])}）", ""]
        lines.append("| 原文 | 繁中 | approved | 備註 |")
        lines.append("|---|---|---|---|")
        for r in by[cat]:
            src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
            lines.append(
                f"| {src} | {r['target_zh_tw']} | {r['approved']} | {r['notes']} |"
            )

    REVIEW.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = rewrite_ids(split_and_update(load_rows()))
    write_terms(rows)
    write_review(rows)
    fm = [r for r in rows if r["category"] == "frontier_monster"]
    print("total", len(rows))
    print("frontier_monster", len(fm))
    print("修改", sum(1 for r in fm if r.get("review_flag") == "修改"))
    print("找不到", sum(1 for r in fm if r.get("review_flag") == "找不到"))
    print("沿用", sum(1 for r in fm if r.get("review_flag") == "沿用"))


if __name__ == "__main__":
    main()
