# -*- coding: utf-8 -*-
"""【step3】以 REVIEW.md 為準，回寫 terms.csv 的繁中與核准（不改 REVIEW 版面）。見 README.md。"""
from __future__ import annotations

import csv
from pathlib import Path

REVIEW = Path(__file__).with_name("REVIEW.md")
TERMS = Path(__file__).with_name("terms.csv")


def parse_review() -> dict[str, tuple[str, str | None]]:
    """en → (繁中, approved 或 None)。同一 EN 以檔案中先出現為準。"""
    text = REVIEW.read_text(encoding="utf-8")
    out: dict[str, tuple[str, str | None]] = {}
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line or "原文" in line:
            continue
        if line.startswith("| #"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 3:
            continue
        approved = None
        if parts[0].isdigit():
            # # | 原文 | 繁中 | ✓ | 備註
            src, zh = parts[1], parts[2]
            if len(parts) >= 4 and parts[3] in {"Y", "N"}:
                approved = parts[3]
        else:
            # 原文 | 繁中 | … 
            src, zh = parts[0], parts[1]
            if len(parts) >= 3 and parts[2] in {"Y", "N"}:
                approved = parts[2]
            elif len(parts) >= 3 and parts[2] == "已核准":
                approved = "Y"
        if src in {"原文", "EN/JP"} or zh in {"繁中", "建議繁中", "暫定"}:
            continue
        en = src.split("/")[0].strip()
        if en and en not in out:
            out[en] = (zh, approved)
    return out


def match_zh(en: str, zh_map: dict[str, tuple[str, str | None]]) -> tuple[str, str | None] | None:
    if not en:
        return None
    if en in zh_map:
        return zh_map[en]
    keys = [p.strip() for p in en.split("/") if p.strip()] if "/" in en else [en]
    for k in keys:
        if k in zh_map:
            return zh_map[k]
    for rk, rv in zh_map.items():
        for k in keys:
            if k and (k in rk or rk in k):
                return rv
    return None


def main() -> None:
    zh_map = parse_review()
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    n_zh = n_ok = 0
    for r in rows:
        en = (r.get("source_en") or "").strip()
        hit = match_zh(en, zh_map)
        if not hit:
            continue
        zh, approved = hit
        if zh and r["target_zh_tw"] != zh:
            print(f"zh {r['id']} {en}: {r['target_zh_tw']} -> {zh}")
            r["target_zh_tw"] = zh
            n_zh += 1
        if approved and r.get("approved") != approved:
            print(f"ok {r['id']} {en}: {r.get('approved')} -> {approved}")
            r["approved"] = approved
            if approved == "Y":
                r["review_flag"] = ""
            n_ok += 1

    fields = list(rows[0].keys())
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"synced zh={n_zh} approved={n_ok} from REVIEW -> CSV")


if __name__ == "__main__":
    main()
