# -*- coding: utf-8 -*-
"""【step3】以 REVIEW.md 為準，只更新 terms.csv 的繁中（不改 REVIEW）。日常審完後跑。見 README.md。"""
from __future__ import annotations

import csv
import re
from pathlib import Path

REVIEW = Path(__file__).with_name("REVIEW.md")
TERMS = Path(__file__).with_name("terms.csv")


def parse_review_zh() -> dict[str, str]:
    """src_en（斜線前）→ 繁中；同一 EN 以檔案中先出現為準。"""
    text = REVIEW.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line or "原文" in line:
            continue
        if line.startswith("| #"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 3:
            continue
        if parts[0].isdigit():
            src, zh = parts[1], parts[2]
        else:
            src, zh = parts[0], parts[1]
        if src in {"原文", "EN/JP"} or zh in {"繁中", "建議繁中", "暫定"}:
            continue
        en = src.split("/")[0].strip()
        if en and en not in out:
            out[en] = zh
    return out


def main() -> None:
    zh_map = parse_review_zh()
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    n = 0
    for r in rows:
        en = (r.get("source_en") or "").strip()
        # Nibelsnarf / Hapulubokka 這種複合 EN：逐段比對
        keys = [en] if en else []
        if " / " in en:
            keys = [p.strip() for p in en.split("/") if p.strip()]
            keys.insert(0, en)
        hit = None
        for k in keys:
            if k in zh_map:
                hit = zh_map[k]
                break
            # Hapulubokka 在 REVIEW 可能只剩 Nibelsnarf 開頭
            for rk, rz in zh_map.items():
                if k and (k in rk or rk in k):
                    hit = rz
                    break
            if hit:
                break
        if hit and r["target_zh_tw"] != hit:
            print(f"{r['id']} {en}: {r['target_zh_tw']} -> {hit}")
            r["target_zh_tw"] = hit
            n += 1

    fields = list(rows[0].keys())
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"synced {n} rows from REVIEW -> CSV")


if __name__ == "__main__":
    main()
