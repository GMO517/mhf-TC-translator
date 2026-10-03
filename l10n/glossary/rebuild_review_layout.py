# -*- coding: utf-8 -*-
"""
重整 REVIEW 版面：
- 已審完的邊境專屬 → 移出「請先檢查」，放進正式分類區塊
- 備註文字不改（台服維持台服）
- 待審區只留尚未核准的條目
"""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")


def main() -> None:
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))

    # 使用者：標記台服／邊境相關已審完 → 核准（找不到除外）
    for r in rows:
        cat = r.get("category") or ""
        flag = r.get("review_flag") or ""
        notes = r.get("notes") or ""

        if flag == "找不到" or notes == "找不到":
            r["approved"] = "N"
            r["review_flag"] = "找不到"
            continue

        if cat in {"frontier_monster", "frontier_system"}:
            r["approved"] = "Y"
            # 已歸類，不再掛「修改／新增」待審旗
            r["review_flag"] = ""

        if r.get("source_en") in {"Kelbi", "Khezu", "Magnet Spike"}:
            r["approved"] = "Y"
            r["review_flag"] = ""

    fields = list(rows[0].keys())
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    by: dict[str, list] = defaultdict(list)
    for r in rows:
        by[r["category"]].append(r)

    pending = [r for r in rows if r.get("approved") != "Y"]
    pending_by: dict[str, list] = defaultdict(list)
    for r in pending:
        pending_by[r["category"]].append(r)

    miss = [r for r in rows if r.get("review_flag") == "找不到"]

    lines = [
        "# 詞語庫審閱",
        "",
        "> 命名：系列→荒野／玩家／日文；邊境專屬魔物→[台服 wiki](https://w.atwiki.jp/mhfotw/)",
        "> 辿異種顯示形定稿：`辿異種‧XX`",
        "> **版面：**「請先檢查」只放未審；已審條目在下方分類區塊。",
        "",
        f"總詞條：{len(rows)}　｜　已核准：{sum(1 for r in rows if r['approved']=='Y')}　｜　未審：{len(pending)}",
        "",
        "## 請先檢查（尚未核准）",
        "",
    ]

    if not pending:
        lines.append("（目前沒有未審條目）")
        lines.append("")
    else:
        lines.append(f"{len(pending)} 條")
        lines.append("")
        for cat in sorted(pending_by):
            lines.append(f"### {cat}（{len(pending_by[cat])}）")
            lines.append("")
            lines.append("| 原文 | 建議繁中 | 狀態 | 備註 |")
            lines.append("|---|---|---|---|")
            for r in pending_by[cat]:
                src = " / ".join(x for x in [r.get("source_en"), r.get("source_jp")] if x)
                lines.append(
                    f"| {src} | {r['target_zh_tw']} | {r.get('review_flag') or ''} | {r['notes']} |"
                )
            lines.append("")

    lines += [
        "## 找不到",
        "",
        f"{len(miss)} 條（仍未核准）",
        "",
        "| EN/JP | 暫定 | 備註 |",
        "|---|---|---|",
    ]
    for r in miss:
        src = " / ".join(x for x in [r.get("source_en"), r.get("source_jp")] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} | {r['notes']} |")
    lines.append("")

    lines += [
        "## 辿異種顯示形（已定稿）",
        "",
        "統一：`辿異種‧XX`（例：`辿異種‧火龍`）",
        "",
        "| 不用 | 原因 |",
        "|---|---|",
        "| `XX(辿異)` | 不統一 |",
        "| `辿異種XX`（無點） | 連讀不清 |",
        "",
        "> 個別 UI 爆框再單條縮短，不改全體格式。",
        "",
    ]

    # 正式分類區塊（已審＋未審都列在所屬類，但已審為主體）
    section_specs = [
        ("frontier_system", "Frontier 系統（已歸類）"),
        ("frontier_monster", "邊境魔物（已歸類）"),
        ("monster", "系列魔物"),
        ("weapon_type", "武器種"),
        ("system", "系統"),
        ("item", "道具"),
        ("ui", "UI"),
    ]

    for cat, title in section_specs:
        items = by.get(cat, [])
        if not items:
            continue
        ok = sum(1 for r in items if r.get("approved") == "Y")
        lines += [
            f"## {title}",
            "",
            f"{len(items)} 條（已核准 {ok}）",
            "",
            "| 原文 | 繁中 | ✓ | 備註 |",
            "|---|---|---|---|",
        ]
        for r in items:
            src = " / ".join(x for x in [r.get("source_en"), r.get("source_jp")] if x)
            mark = "Y" if r.get("approved") == "Y" else "N"
            lines.append(f"| {src} | {r['target_zh_tw']} | {mark} | {r['notes']} |")
        lines.append("")

    REVIEW.write_text("\n".join(lines), encoding="utf-8")

    print("approved", Counter(r["approved"] for r in rows))
    print("pending_by_cat:")
    for cat, rs in sorted(pending_by.items()):
        print(f"  {cat}: {len(rs)}")
    print("REVIEW ok")


if __name__ == "__main__":
    main()
