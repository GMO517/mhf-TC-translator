# -*- coding: utf-8 -*-
"""將 batches/batch-*.json 譯文合併進 working CSV。

JSON 形狀：
{
  "section_id": "items-name",
  "translations": [{"index": "7", "target": "回復藥"}, ...]
}
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from charset_apply import to_display
from paths import WORKING, CSV_DIR

SECTIONS = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
SEC_BY_ID = {s["id"]: s for s in SECTIONS}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("用法: apply_batch_json.py batches/batch-xxx.json")
        return 2
    batch_path = Path(argv[1])
    if not batch_path.is_absolute():
        batch_path = WORKING / batch_path
    data = json.loads(batch_path.read_text(encoding="utf-8"))
    sec_id = data["section_id"]
    sec = SEC_BY_ID[sec_id]
    csv_path = CSV_DIR / sec["extracted"]
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8", newline="")))
    by_idx = {r["index"]: r for r in rows}
    ok = fail = 0
    errors: list[str] = []
    for t in data.get("translations", []):
        idx = str(t["index"])
        raw = (t.get("target") or "").strip()
        if idx not in by_idx:
            errors.append(f"缺 index {idx}")
            fail += 1
            continue
        disp, miss = to_display(raw)
        if miss:
            errors.append(f"{idx}: 缺字 {''.join(miss)} | {raw}")
            fail += 1
            continue
        by_idx[idx]["target"] = disp
        ok += 1
    fields = list(rows[0].keys())
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"applied ok={ok} fail={fail} -> {csv_path}")
    for e in errors[:30]:
        print("ERR", e)
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
