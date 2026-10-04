# -*- coding: utf-8 -*-
"""一鍵：套用詞庫 + 驗證。"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

WORKING = Path(__file__).resolve().parent
PY = sys.executable


def main(argv: list[str]) -> int:
    args = argv[1:]
    r1 = subprocess.run(
        [PY, str(WORKING / "apply_glossary_section.py"), *args], cwd=WORKING
    )
    if r1.returncode != 0:
        return r1.returncode
    r2 = subprocess.run(
        [PY, str(WORKING / "validate_working.py"), *args], cwd=WORKING
    )
    return r2.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
