# -*- coding: utf-8 -*-
"""將詞語庫精確命中填入 working CSV；未命中 target=source。"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from paths import WORKING, L10N, CSV_DIR, LOGS, ensure_dirs

GLOSSARY = L10N / "glossary" / "terms.csv"
EXTRACTED = L10N / "extracted"


def load_glossary(categories: set[str]) -> dict[str, dict]:
    rows = list(csv.DictReader(GLOSSARY.open(encoding="utf-8-sig", newline="")))
    out: dict[str, dict] = {}
    for r in rows:
        if r.get("approved") != "Y":
            continue
        if r.get("category") not in categories:
            continue
        en = (r.get("source_en") or "").strip()
        if not en:
            continue
        key = en.lower()
        if key in out:
            continue
        disp = (r.get("fallback_glyph") or r.get("target_zh_tw") or "").strip()
        if not disp:
            continue
        out[key] = {
            "id": r["id"],
            "ideal": (r.get("target_zh_tw") or "").strip(),
            "display": disp,
            "notes": r.get("notes") or "",
        }
    return out


def apply_one(section: dict) -> dict:
    cats = set(section["categories"])
    gloss = load_glossary(cats)
    src_csv = EXTRACTED / section["extracted"]
    if not src_csv.exists():
        raise FileNotFoundError(src_csv)
    rows = list(csv.DictReader(src_csv.open(encoding="utf-8-sig", newline="")))
    fields = list(rows[0].keys()) if rows else ["index", "source", "target"]
    hits: list[str] = []
    for row in rows:
        src = (row.get("source") or "").strip()
        # CSV 可能帶引號包住的來源；DictReader 已去引號
        key = src.lower()
        if key in gloss:
            g = gloss[key]
            row["target"] = g["display"]
            hits.append(
                f"| {row.get('index')} | {src} | {g['ideal']} | {g['display']} | {g['id']} |"
            )
        else:
            # 未命中：暫留原文，避免回寫空白
            row["target"] = src

    ensure_dirs()
    out_csv = CSV_DIR / section["extracted"]
    # FTH detect_translation_format 見首欄須為精確「index」；不可寫 BOM
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    report = [
        f"# {section['id']} 詞庫套用",
        "",
        f"- xpath: `{section['xpath']}`",
        f"- categories: {', '.join(sorted(cats))}",
        f"- 總列：{len(rows)}",
        f"- 命中：{len(hits)}",
        "",
        "| index | source | 理想繁中 | 顯示形 | term_id |",
        "|---|---|---|---|---|",
        *(hits if hits else ["| （無） | | | | |"]),
        "",
    ]
    (LOGS / f"{section['id']}-apply.md").write_text("\n".join(report), encoding="utf-8")
    return {
        "id": section["id"],
        "rows": len(rows),
        "hits": len(hits),
        "csv": str(out_csv),
    }


def main(argv: list[str]) -> int:
    sections = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
    only = set(argv[1:]) if len(argv) > 1 else None
    ensure_dirs()
    summary = ["# 詞庫套用總覽", ""]
    for sec in sections:
        if only and sec["id"] not in only:
            continue
        info = apply_one(sec)
        print(f"{info['id']}: hits={info['hits']}/{info['rows']}")
        summary.append(f"- `{info['id']}`：命中 {info['hits']}／{info['rows']}")
    summary.append("")
    (LOGS / "apply-summary.md").write_text("\n".join(summary), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
