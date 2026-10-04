# -*- coding: utf-8 -*-
"""【step2】只依 terms.csv 重寫 REVIEW.md（不改核准狀態）。

警告：會整檔覆寫 REVIEW.md。有手改時先跑 step3_sync_review_to_csv.py，
禁止直接用本腳本還原覆蓋手改。見 README.md。
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")


def src(r: dict) -> str:
    return " / ".join(x for x in [r.get("source_en"), r.get("source_jp")] if x)


def note_cell(r: dict) -> str:
    """備註欄：保留 notes，並附 review_flag（若有且不同）。"""
    notes = (r.get("notes") or "").strip()
    flag = (r.get("review_flag") or "").strip()
    if flag and flag != notes:
        return f"{flag}｜{notes}" if notes else flag
    return notes or flag


def table(rows: list[dict], *, with_ok: bool = True) -> list[str]:
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
    pending_by: dict[str, list] = defaultdict(list)
    for r in pending:
        pending_by[r["category"]].append(r)

    frontier = by.get("frontier_monster", [])
    series = by.get("monster", [])
    miss = [r for r in rows if (r.get("review_flag") == "找不到") or (r.get("notes") == "找不到")]

    lines = [
        "# 詞語庫審閱",
        "",
        "> 命名：系列→荒野／玩家／日文；邊境專屬魔物→[台服 wiki](https://w.atwiki.jp/mhfotw/)",
        "> 辿異種顯示形定稿：`辿異種‧XX`",
        "> **魔物最終確認：**下方「邊境專屬／系列魔物」含完整備註（台服／系列／找不到…）。",
        "",
        f"總詞條：{len(rows)}　｜　已核准：{sum(1 for r in rows if r['approved']=='Y')}　｜　未審：{len(pending)}",
        "",
        "## 邊境專屬魔物（最終確認）",
        "",
        f"{len(frontier)} 條（已核准 {sum(1 for r in frontier if r.get('approved')=='Y')}）",
        "",
        *table(frontier),
        "",
        "## 系列魔物（最終確認）",
        "",
        f"{len(series)} 條（已核准 {sum(1 for r in series if r.get('approved')=='Y')}）",
        "",
        *table(series),
        "",
        "## 找不到",
        "",
        f"{len(miss)} 條",
        "",
        "| 原文 | 暫定 | 備註 |",
        "|---|---|---|",
    ]
    for r in miss:
        lines.append(f"| {src(r)} | {r['target_zh_tw']} | {note_cell(r)} |")
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
        "## 請先檢查（尚未核准・非魔物）",
        "",
    ]

    non_monster_pending = {
        k: v
        for k, v in pending_by.items()
        if k not in {"frontier_monster", "monster"}
    }
    if not non_monster_pending:
        lines.append("（無）")
        lines.append("")
    else:
        n = sum(len(v) for v in non_monster_pending.values())
        lines.append(f"{n} 條")
        lines.append("")
        for cat in sorted(non_monster_pending):
            lines.append(f"### {cat}（{len(non_monster_pending[cat])}）")
            lines.append("")
            lines.append("| 原文 | 建議繁中 | 狀態 | 備註 |")
            lines.append("|---|---|---|---|")
            for r in non_monster_pending[cat]:
                lines.append(
                    f"| {src(r)} | {r['target_zh_tw']} | {r.get('review_flag') or ''} | {r.get('notes') or ''} |"
                )
            lines.append("")

    section_specs = [
        ("frontier_system", "Frontier 系統（已歸類）"),
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
            lines.append(f"| {src(r)} | {r['target_zh_tw']} | {r.get('approved') or 'N'} | {note_cell(r)} |")
        lines.append("")

    REVIEW.write_text("\n".join(lines), encoding="utf-8")
    print(f"REVIEW written: frontier={len(frontier)} series={len(series)} pending_non_monster={sum(len(v) for v in non_monster_pending.values())}")


if __name__ == "__main__":
    main()
