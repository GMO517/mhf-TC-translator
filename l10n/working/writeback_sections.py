# -*- coding: utf-8 -*-
"""將 working CSV 回寫 mhfdat（compress+encrypt），再同步本體。"""
from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

WORKING = Path(__file__).resolve().parent
ROOT = WORKING.parents[1]
FTH = ROOT / "tools" / "FrontierTextHandler"
DATA = ROOT / "l10n" / "data"
CLIENT_BIN = ROOT / "client" / "MHFCT4.1" / "dat" / "mhfdat.bin"
BACKUP_ROOT = ROOT / "_backup"
CSV_DIR = WORKING / "csv"
REPORTS = WORKING / "reports"
PY = sys.executable


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_backup() -> None:
    if not any(BACKUP_ROOT.glob("*/")):
        raise SystemExit(f"缺少備份目錄：{BACKUP_ROOT}")


def run_fth(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [PY, str(FTH / "main.py"), *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def main(argv: list[str]) -> int:
    ensure_backup()
    if not CLIENT_BIN.exists():
        raise SystemExit(f"缺少本體 bin：{CLIENT_BIN}")
    sections = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
    only = set(argv[1:]) if len(argv) > 1 else None
    work = WORKING / "_writeback_work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    (work / "data").mkdir()
    (work / "output").mkdir()

    src_bin = DATA / "mhfdat.bin"
    shutil.copy2(src_bin, work / "data" / "mhfdat.bin")
    before = sha256(work / "data" / "mhfdat.bin")

    log = [
        "# 回寫報告",
        "",
        f"- 時間：{datetime.now().isoformat(timespec='seconds')}",
        f"- 回寫前 SHA256：`{before}`",
        "",
    ]
    ok = True
    for sec in sections:
        if only and sec["id"] not in only:
            continue
        if sec["bin"] != "mhfdat.bin":
            log.append(f"- `{sec['id']}`：略過（非 mhfdat）")
            continue
        csv_path = CSV_DIR / sec["extracted"]
        if not csv_path.exists():
            log.append(f"- `{sec['id']}`：缺少 CSV → FAIL")
            ok = False
            continue
        # 僅當有「不同於 source」的譯文才回寫該 section
        rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig", newline="")))
        changed = sum(
            1
            for r in rows
            if (r.get("target") or "").strip()
            and (r.get("target") or "") != (r.get("source") or "")
        )
        if changed == 0:
            log.append(f"- `{sec['id']}`：無譯文變更，略過")
            continue
        dest_csv = work / "output" / csv_path.name
        shutil.copy2(csv_path, dest_csv)
        r = run_fth(
            [
                "--csv-to-bin",
                f"output/{csv_path.name}",
                "data/mhfdat.bin",
                "--xpath",
                sec["xpath"],
                "--compress",
                "--encrypt",
            ],
            cwd=work,
        )
        if r.returncode != 0:
            ok = False
            log.append(f"- `{sec['id']}`：IMPORT FAIL rc={r.returncode}")
            log.append("```")
            log.append((r.stdout or "")[-500])
            log.append((r.stderr or "")[-500])
            log.append("```")
            continue
        log.append(f"- `{sec['id']}`：OK（變更 {changed} 列）")

    after_path = work / "data" / "mhfdat.bin"
    after = sha256(after_path)
    log += ["", f"- 回寫後 SHA256：`{after}`", ""]
    if not ok:
        REPORTS.mkdir(parents=True, exist_ok=True)
        (REPORTS / "writeback.md").write_text("\n".join(log), encoding="utf-8")
        print("\n".join(log))
        return 2

    shutil.copy2(after_path, DATA / "mhfdat.bin")
    shutil.copy2(after_path, CLIENT_BIN)
    log.append(f"- 已同步：`l10n/data/mhfdat.bin` 與 `{CLIENT_BIN}`")
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "writeback.md").write_text("\n".join(log + [""]), encoding="utf-8")
    print("\n".join(log))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
