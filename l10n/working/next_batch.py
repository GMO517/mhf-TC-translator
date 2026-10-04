# -*- coding: utf-8 -*-
"""列出下一批判譯候選（target==source 且 source 非空）。"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from paths import WORKING, CSV_DIR, SCRATCH, ensure_dirs

SECTIONS = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
SEC_BY_ID = {s["id"]: s for s in SECTIONS}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("用法: next_batch.py <section-id> [limit=200]")
        return 2
    sec_id = argv[1]
    # 預設 200：減少 subagent／回寫／commit 次數（固定開銷）以省 token
    limit = int(argv[2]) if len(argv) > 2 else 200
    sec = SEC_BY_ID[sec_id]
    rows = list(
        csv.DictReader((CSV_DIR / sec["extracted"]).open(encoding="utf-8", newline=""))
    )
    pending = []
    for r in rows:
        src = (r.get("source") or "").strip()
        tgt = r.get("target") or ""
        if not src:
            continue
        if tgt != src:
            continue
        # 略過純符號占位
        if set(src) <= set("－-—_*."):
            continue
        pending.append({"index": r["index"], "source": src})
        if len(pending) >= limit:
            break
    ensure_dirs()
    out = {
        "section_id": sec_id,
        "xpath": sec["xpath"],
        "pending_total_estimate": sum(
            1
            for r in rows
            if (r.get("source") or "").strip()
            and (r.get("target") or "") == (r.get("source") or "")
        ),
        "batch": pending,
    }
    path = SCRATCH / f"next-{sec_id}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {path} n={len(pending)} pending≈{out['pending_total_estimate']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
