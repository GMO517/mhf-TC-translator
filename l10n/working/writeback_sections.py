# -*- coding: utf-8 -*-
"""將 working CSV 回寫 mhfdat（compress+encrypt），再同步本體。

只把 target≠source 的列寫成精簡 CSV 給 FTH，避免整表 1 萬多列拖慢。
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
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
    print("FTH:", " ".join(args), flush=True)
    return subprocess.run(
        [PY, str(FTH / "main.py"), *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def changed_rows(csv_path: Path) -> list[dict]:
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8", newline="")))
    out = []
    for r in rows:
        src = r.get("source") or ""
        tgt = r.get("target") or ""
        if tgt.strip() and tgt != src:
            out.append({"index": r["index"], "source": src, "target": tgt})
    return out


def main(argv: list[str]) -> int:
    ensure_backup()
    if not CLIENT_BIN.exists():
        raise SystemExit(f"缺少本體 bin：{CLIENT_BIN}")
    sections = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
    only = set(argv[1:]) if len(argv) > 1 else None
    work = WORKING / f"_writeback_work_{os.getpid()}"
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
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
        changed = changed_rows(csv_path)
        if not changed:
            log.append(f"- `{sec['id']}`：無譯文變更，略過")
            print(f"skip {sec['id']}", flush=True)
            continue
        print(f"import {sec['id']} n={len(changed)}", flush=True)
        dest_csv = work / "output" / csv_path.name
        with dest_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["index", "source", "target"])
            w.writeheader()
            w.writerows(changed)
        # 每次以目前 work/data 的 bin 為輸入；FTH 產物在 output/*-modified.bin
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
        combined = (r.stdout or "") + "\n" + (r.stderr or "")
        print(combined[-600:], flush=True)
        if r.returncode != 0 or "Found 0 translations" in combined:
            ok = False
            log.append(f"- `{sec['id']}`：IMPORT FAIL rc={r.returncode}")
            log.append("```")
            log.append(combined[-800:])
            log.append("```")
            continue
        modified = work / "output" / "mhfdat-modified.bin"
        if not modified.exists():
            ok = False
            log.append(f"- `{sec['id']}`：找不到 {modified.name}")
            continue
        shutil.copy2(modified, work / "data" / "mhfdat.bin")
        log.append(f"- `{sec['id']}`：OK（變更 {len(changed)} 列）")
        print(f"ok {sec['id']} -> data/mhfdat.bin", flush=True)

    after_path = work / "data" / "mhfdat.bin"
    after = sha256(after_path)
    log += ["", f"- 回寫後 SHA256：`{after}`", ""]
    REPORTS.mkdir(parents=True, exist_ok=True)
    if not ok:
        (REPORTS / "writeback.md").write_text("\n".join(log), encoding="utf-8")
        print("\n".join(log), flush=True)
        shutil.rmtree(work, ignore_errors=True)
        return 2

    if after == before:
        log.append("- 警告：雜湊未變（可能未寫入）")
        print("WARN hash unchanged", flush=True)
        (REPORTS / "writeback.md").write_text("\n".join(log), encoding="utf-8")
        shutil.rmtree(work, ignore_errors=True)
        return 3

    shutil.copy2(after_path, DATA / "mhfdat.bin")
    shutil.copy2(after_path, CLIENT_BIN)
    log.append(f"- 已同步：`l10n/data/mhfdat.bin` 與 `{CLIENT_BIN}`")
    (REPORTS / "writeback.md").write_text("\n".join(log + [""]), encoding="utf-8")
    print("\n".join(log), flush=True)
    shutil.rmtree(work, ignore_errors=True)
    return 0



if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
