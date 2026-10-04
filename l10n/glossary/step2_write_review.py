# -*- coding: utf-8 -*-
"""【step2】只依 terms.csv 重寫 REVIEW.md。

會整檔覆寫。有手改時務必先跑 step3。見 README.md。
版面：頂部待審進度摘要 + 各分類完整表（含已核准，不拆兩套表）。
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

SECTIONS = [
    ("frontier_monster", "邊境專屬魔物"),
    ("monster", "系列魔物"),
    ("frontier_system", "Frontier 系統"),
    ("weapon_type", "武器種"),
    ("system", "系統"),
    ("item", "道具"),
    ("ui", "UI"),
]


def src(r: dict) -> str:
    return " / ".join(x for x in [r.get("source_en"), r.get("source_jp")] if x)


def note_cell(r: dict) -> str:
    notes = (r.get("notes") or "").strip()
    flag = (r.get("review_flag") or "").strip()
    if flag and flag != notes:
        return f"{flag}｜{notes}" if notes else flag
    return notes or flag


def table(rows: list[dict]) -> list[str]:
    lines = [
        "| # | 原文 | 繁中 | ✓ | 備註 |",
        "|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        ok = r.get("approved") or "N"
        lines.append(f"| {i} | {src(r)} | {r['target_zh_tw']} | {ok} | {note_cell(r)} |")
    return lines


def main() -> None:
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    by: dict[str, list] = defaultdict(list)
    for r in rows:
        by[r["category"]].append(r)

    pending = [r for r in rows if r.get("approved") != "Y"]
    approved_n = sum(1 for r in rows if r.get("approved") == "Y")
    miss = [
        r
        for r in rows
        if (r.get("review_flag") == "找不到") or (r.get("notes") == "找不到")
    ]

    lines = [
        "# 詞語庫審閱",
        "",
        "> **主檔就是本檔。** 改繁中／✓ 後跑 `step3_sync_review_to_csv.py` 回寫 CSV。",
        "> 命名：系列→荒野／玩家／日文；邊境專屬→[台服 wiki](https://w.atwiki.jp/mhfotw/)",
        "> 辿異種顯示形：`辿異種‧XX`",
        "",
        f"總詞條：{len(rows)}　｜　已核准：{approved_n}　｜　未審：{len(pending)}",
        "",
        "## 待審進度",
        "",
        "| 分類 | 未審 | 已核准 | 合計 |",
        "|---|---:|---:|---:|",
    ]
    for cat, title in SECTIONS:
        items = by.get(cat, [])
        if not items:
            continue
        ok = sum(1 for r in items if r.get("approved") == "Y")
        lines.append(f"| {title} | {len(items) - ok} | {ok} | {len(items)} |")
    lines += ["", f"找不到標記：{len(miss)} 條", ""]

    for cat, title in SECTIONS:
        items = by.get(cat, [])
        if not items:
            continue
        ok = sum(1 for r in items if r.get("approved") == "Y")
        lines += [
            f"## {title}",
            "",
            f"{len(items)} 條（已核准 {ok}／未審 {len(items) - ok}）",
            "",
            *table(items),
            "",
        ]

    lines += [
        "## 找不到",
        "",
        f"{len(miss)} 條",
        "",
        "| # | 原文 | 繁中 | ✓ | 備註 |",
        "|---|---|---|---|---|",
    ]
    for i, r in enumerate(miss, 1):
        lines.append(
            f"| {i} | {src(r)} | {r['target_zh_tw']} | {r.get('approved') or 'N'} | {note_cell(r)} |"
        )
    lines += [
        "",
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

    REVIEW.write_text("\n".join(lines), encoding="utf-8")
    print(
        "REVIEW rewritten:",
        f"total={len(rows)}",
        f"pending={len(pending)}",
        f"weapons={len(by.get('weapon_type', []))}",
    )


if __name__ == "__main__":
    main()
