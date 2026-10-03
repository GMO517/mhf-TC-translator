# -*- coding: utf-8 -*-
"""套用邊境魔物譯名＋全庫備註略縮＋重寫 REVIEW。"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import apply_frontier_monster_names as afm

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

# 非魔物區塊：統一短備註
NOTE_BY_CAT = {
    "weapon_type": "武器種",
    "system": "系統",
    "item": "道具",
    "ui": "UI",
    "monster": "系列魔物",
    "frontier_system": "Frontier 系統",
    "npc": "NPC",
    "place": "地名",
}


def shorten_non_frontier(rows: list[dict]) -> None:
    for r in rows:
        cat = r.get("category") or ""
        en = r.get("source_en") or ""
        if cat == "frontier_monster":
            continue
        if cat in NOTE_BY_CAT:
            # 特例保留極短提示
            if en == "Magnet Spike":
                r["notes"] = "Frontier 武器"
            elif cat == "monster":
                r["notes"] = "系列"
            elif cat == "frontier_system":
                r["notes"] = "系統"
            else:
                r["notes"] = NOTE_BY_CAT[cat]
        else:
            # 其他：截斷
            n = (r.get("notes") or "").strip()
            r["notes"] = n[:12] if n else ""


def main() -> None:
    rows = afm.load_rows()
    # 若尚無 review_flag 欄，補上
    for r in rows:
        r.setdefault("review_flag", "")

    rows = afm.rewrite_ids(afm.split_and_update(rows))
    shorten_non_frontier(rows)

    # 已核准三條
    for r in rows:
        if r.get("source_en") in {"Kelbi", "Khezu", "Magnet Spike"}:
            r["approved"] = "Y"
            r["review_flag"] = "你已核准"
            if r["source_en"] == "Kelbi":
                r["target_zh_tw"] = "精靈鹿"
                r["notes"] = "系列"
            elif r["source_en"] == "Khezu":
                r["target_zh_tw"] = "奇怪龍"
                r["notes"] = "系列"
            else:
                r["target_zh_tw"] = "磁斬槌"
                r["notes"] = "Frontier 武器"

    afm.write_terms(rows)
    write_review_compact(rows)

    fm = [r for r in rows if r["category"] == "frontier_monster"]
    print("total", len(rows))
    print(
        "FMO",
        len(fm),
        "修改",
        sum(1 for r in fm if r.get("review_flag") == "修改"),
        "找不到",
        sum(1 for r in fm if r.get("review_flag") == "找不到"),
    )


def write_review_compact(rows: list[dict]) -> None:
    by: dict[str, list] = {}
    for r in rows:
        by.setdefault(r["category"], []).append(r)

    mod = [r for r in by.get("frontier_monster", []) if r.get("review_flag") == "修改"]
    miss = [r for r in by.get("frontier_monster", []) if r.get("review_flag") == "找不到"]

    lines = [
        "# 詞語庫審閱",
        "",
        "> 優先序：**玩家常講 ≥ 日文漢字**（竜→龍）。備註已略縮。",
        "> 參考：nenaiko／台服 wiki／華語社群",
        "",
        f"總詞條：{len(rows)}",
        "",
        "## 請先檢查：邊境魔物（本次修改）",
        "",
        f"{len(mod)} 條",
        "",
        "| EN/JP | 新譯名 | 備註 |",
        "|---|---|---|",
    ]
    for r in mod:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} | {r['notes']} |")

    lines += [
        "",
        "## 找不到",
        "",
        f"{len(miss)} 條",
        "",
        "| EN/JP | 暫定 |",
        "|---|---|",
    ]
    for r in miss:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        lines.append(f"| {src} | {r['target_zh_tw']} |")

    sections = [
        ("frontier_monster", "邊境魔物（完整）", True),
        ("frontier_system", "Frontier 系統", False),
        ("monster", "系列魔物", False),
        ("weapon_type", "武器種", False),
        ("system", "系統", False),
        ("item", "道具", False),
        ("ui", "UI", False),
    ]
    for cat, title, is_fmo in sections:
        if cat not in by:
            continue
        lines += ["", f"## {title}（{len(by[cat])}）", ""]
        if is_fmo:
            lines.append("| EN/JP | 繁中 | 狀態 | 備註 |")
            lines.append("|---|---|---|---|")
            for r in by[cat]:
                src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
                lines.append(
                    f"| {src} | {r['target_zh_tw']} | {r.get('review_flag') or '沿用'} | {r['notes']} |"
                )
        else:
            lines.append("| 原文 | 繁中 | ✓ | 備註 |")
            lines.append("|---|---|---|---|")
            for r in by[cat]:
                src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
                lines.append(
                    f"| {src} | {r['target_zh_tw']} | {r['approved']} | {r['notes']} |"
                )

    REVIEW.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
