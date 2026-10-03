# -*- coding: utf-8 -*-
"""補漏：辿異種及相關用語（台服 wiki 用字）。"""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

ADDITIONS = [
    {
        "category": "frontier_system",
        "source_jp": "辿異種",
        "source_en": "Teni / Transcendent",
        "target_zh_tw": "辿異種",
        "notes": "台服",
        "review_flag": "新增",
    },
    {
        "category": "frontier_system",
        "source_jp": "辿異スキル",
        "source_en": "Teni Skill",
        "target_zh_tw": "辿異技能",
        "notes": "台服",
        "review_flag": "新增",
    },
    {
        "category": "frontier_system",
        "source_jp": "辿異武器",
        "source_en": "Teni Weapon",
        "target_zh_tw": "辿異武器",
        "notes": "台服",
        "review_flag": "新增",
    },
    {
        "category": "frontier_system",
        "source_jp": "辿異防具",
        "source_en": "Teni Armor",
        "target_zh_tw": "辿異防具",
        "notes": "台服",
        "review_flag": "新增",
    },
    {
        "category": "frontier_system",
        "source_jp": "辿異クエスト",
        "source_en": "Teni Quest",
        "target_zh_tw": "辿異任務",
        "notes": "台服",
        "review_flag": "新增",
    },
    {
        "category": "frontier_system",
        "source_jp": "発達部位",
        "source_en": "Developed Part",
        "target_zh_tw": "發達部位",
        "notes": "台服",
        "review_flag": "新增",
    },
]


def main() -> None:
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    have_jp = {r.get("source_jp") or "" for r in rows}

    for a in ADDITIONS:
        if a["source_jp"] in have_jp:
            print("skip", a["source_jp"])
            continue
        rows.append(
            {
                "id": "",
                "category": a["category"],
                "source_jp": a["source_jp"],
                "source_en": a["source_en"],
                "target_zh_tw": a["target_zh_tw"],
                "wilds_ref": "",
                "frontier_only": "Y",
                "register": "system",
                "display_ok": "pending",
                "fallback_glyph": "",
                "notes": a["notes"],
                "approved": "N",
                "review_flag": a["review_flag"],
            }
        )
        print("add", a["source_jp"], "=>", a["target_zh_tw"])
        have_jp.add(a["source_jp"])

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

    out = []
    counters: Counter = Counter()
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
        w.writerows(out)

    # 更新 REVIEW
    text = REVIEW.read_text(encoding="utf-8")
    fsy = [r for r in out if r["category"] == "frontier_system"]
    block_lines = [
        "## Frontier 系統（含種別名）",
        "",
        "| 原文 | 繁中 | ✓ | 狀態 | 備註 |",
        "|---|---|---|---|---|",
    ]
    for r in fsy:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        block_lines.append(
            f"| {src} | {r['target_zh_tw']} | {r['approved']} | {r.get('review_flag') or ''} | {r['notes']} |"
        )
    block_lines.append("")
    new_fsy = "\n".join(block_lines)

    text2 = re.sub(
        r"## Frontier 系統.*?(?=\n## |\Z)", new_fsy, text, count=1, flags=re.S
    )
    if text2 == text:
        text2 = re.sub(
            r"## frontier_system.*?(?=\n## |\Z)", new_fsy, text, count=1, flags=re.S
        )
    text2 = re.sub(r"總詞條：\d+", f"總詞條：{len(out)}", text2, count=1)

    note = (
        "> **補漏：**「辿異種」及辿異技能／武器／防具／任務／發達部位已加入 "
        "（先前種別名表漏列，非遊戲無此概念）。"
        "台服：[辿異種](https://w.atwiki.jp/mhfotw/pages/1992.html)"
    )
    if "辿異種" not in text2.split("## 請先檢查")[0]:
        text2 = text2.replace("> 備註已略縮。", "> 備註已略縮。\n" + note)

    # 在請先檢查表前插入辿異新增列
    teni_rows = [
        r
        for r in out
        if r.get("review_flag") == "新增"
        and (
            "辿異" in (r.get("source_jp") or "")
            or r.get("source_jp") == "発達部位"
        )
    ]
    if teni_rows and "| Teni / Transcendent" not in text2:
        insert = ["| Teni / Transcendent / 辿異種 | 辿異種 | 新增 | 台服 |"]
        for r in teni_rows:
            if r["source_jp"] == "辿異種":
                continue
            src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
            insert.append(
                f"| {src} | {r['target_zh_tw']} | 新增 | {r['notes']} |"
            )
        text2 = text2.replace(
            "| EN/JP | 譯名 | 狀態 | 備註 |\n|---|---|---|---|",
            "| EN/JP | 譯名 | 狀態 | 備註 |\n|---|---|---|---|\n" + "\n".join(insert),
        )

    REVIEW.write_text(text2, encoding="utf-8")
    print("total", len(out))
    print("frontier_system:", [r["target_zh_tw"] for r in fsy])


if __name__ == "__main__":
    main()
