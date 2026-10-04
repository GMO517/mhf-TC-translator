# -*- coding: utf-8 -*-
"""完成一批：驗證 section → delta 回寫 → 印出建議 commit 檔案。

用法:
  python finish_batch.py batches/batch-items-tickets.json
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from paths import WORKING, CATALOGS, STATE_FILE, WRITEBACK_LOG

PY = sys.executable


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("用法: finish_batch.py batches/batch-xxx.json")
        return 2
    batch = Path(argv[1])
    if not batch.is_absolute():
        batch = WORKING / batch
    data = json.loads(batch.read_text(encoding="utf-8"))
    sec_id = data["section_id"]
    n = len(data.get("translations", []))
    print(f"finish {batch.name} section={sec_id} n={n}", flush=True)

    r1 = subprocess.run(
        [PY, str(WORKING / "validate_working.py"), sec_id], cwd=WORKING
    )
    if r1.returncode != 0:
        return r1.returncode

    r2 = subprocess.run(
        [PY, str(WORKING / "writeback_sections.py"), "--batch", str(batch)],
        cwd=WORKING,
    )
    if r2.returncode != 0:
        return r2.returncode

    catalog = CATALOGS / "ITEMS-TRANSLATED.md"
    print(
        "\n建議 commit 檔案:\n"
        f"  {batch}\n"
        f"  l10n/working/csv/（對應 section）\n"
        f"  {WRITEBACK_LOG}\n"
        f"  {STATE_FILE}\n"
        f"  {catalog}（若有改）\n",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
