# -*- coding: utf-8 -*-
"""將譯文回寫 mhfdat（compress+encrypt），再同步本體。

預設／建議：只回寫「本批」index（--batch），避免每批重寫累積數百列。
全量同步：--all-changed（僅必要時）。
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from paths import WORKING, ROOT, CSV_DIR, STATE_FILE, WRITEBACK_LOG, ensure_dirs

FTH = ROOT / "tools" / "FrontierTextHandler"
DATA = ROOT / "l10n" / "data"
CLIENT_BIN = ROOT / "client" / "MHFCT4.1" / "dat" / "mhfdat.bin"
BACKUP_ROOT = ROOT / "_backup"
STATE = STATE_FILE
PY = sys.executable
SECTIONS = {s["id"]: s for s in json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))}


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


def load_csv_rows(sec_id: str) -> dict[str, dict]:
    path = CSV_DIR / SECTIONS[sec_id]["extracted"]
    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    return {r["index"]: r for r in rows}


def rows_from_batch(batch_path: Path) -> tuple[str, list[dict]]:
    if not batch_path.is_absolute():
        batch_path = WORKING / batch_path
    data = json.loads(batch_path.read_text(encoding="utf-8"))
    sec_id = data["section_id"]
    by_idx = load_csv_rows(sec_id)
    out: list[dict] = []
    for t in data.get("translations", []):
        idx = str(t["index"])
        if idx not in by_idx:
            raise SystemExit(f"batch 含未知 index {idx}")
        row = by_idx[idx]
        src = row.get("source") or ""
        tgt = (t.get("target") or row.get("target") or "").strip()
        # 以 working CSV 為準（已套用過 charset）
        tgt = (row.get("target") or tgt).strip()
        if not tgt or tgt == src:
            continue
        out.append({"index": idx, "source": src, "target": tgt})
    return sec_id, out


def rows_all_changed(sec_id: str) -> list[dict]:
    by_idx = load_csv_rows(sec_id)
    out = []
    for r in by_idx.values():
        src = r.get("source") or ""
        tgt = r.get("target") or ""
        if tgt.strip() and tgt != src:
            out.append({"index": r["index"], "source": src, "target": tgt})
    return out


def import_rows(sec_id: str, changed: list[dict], work: Path) -> tuple[bool, str]:
    sec = SECTIONS[sec_id]
    if not changed:
        return True, f"- `{sec_id}`：無列可寫，略過"
    print(f"import {sec_id} n={len(changed)} (delta)", flush=True)
    dest_csv = work / "output" / sec["extracted"]
    with dest_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["index", "source", "target"])
        w.writeheader()
        w.writerows(changed)
    r = run_fth(
        [
            "--csv-to-bin",
            f"output/{sec['extracted']}",
            "data/mhfdat.bin",
            "--xpath",
            sec["xpath"],
            "--compress",
            "--encrypt",
        ],
        cwd=work,
    )
    combined = (r.stdout or "") + "\n" + (r.stderr or "")
    print(combined[-500:], flush=True)
    if r.returncode != 0 or "Found 0 translations" in combined:
        return False, f"- `{sec_id}`：IMPORT FAIL\n```\n{combined[-800:]}\n```"
    modified = work / "output" / "mhfdat-modified.bin"
    if not modified.exists():
        return False, f"- `{sec_id}`：找不到 mhfdat-modified.bin"
    shutil.copy2(modified, work / "data" / "mhfdat.bin")
    return True, f"- `{sec_id}`：OK（delta {len(changed)} 列）"


def save_state(sec_id: str, indexes: list[str], after: str) -> None:
    state = {}
    if STATE.exists():
        state = json.loads(STATE.read_text(encoding="utf-8"))
    done = set(state.get(sec_id, {}).get("indexes", []))
    done.update(indexes)
    state[sec_id] = {
        "indexes": sorted(done, key=lambda x: int(x) if x.isdigit() else x),
        "count": len(done),
        "sha256": after,
        "updated": datetime.now().isoformat(timespec="seconds"),
    }
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="回寫 mhfdat（建議 --batch）")
    ap.add_argument(
        "--batch",
        action="append",
        default=[],
        help="本批 JSON（可重複）。只回寫該批 index",
    )
    ap.add_argument(
        "--all-changed",
        action="store_true",
        help="回寫該 section 全部已譯列（慢；少用）",
    )
    ap.add_argument(
        "sections",
        nargs="*",
        help="搭配 --all-changed 的 section id",
    )
    args = ap.parse_args(argv[1:])

    if not args.batch and not args.all_changed:
        print(
            "請指定 --batch batches/batch-xxx.json（建議）\n"
            "或 --all-changed <section-id…>（全量，慢）",
            file=sys.stderr,
        )
        return 2

    ensure_backup()
    if not CLIENT_BIN.exists():
        raise SystemExit(f"缺少本體 bin：{CLIENT_BIN}")
    ensure_dirs()

    work = WORKING / f"_writeback_work_{os.getpid()}"
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    (work / "data").mkdir()
    (work / "output").mkdir()
    shutil.copy2(DATA / "mhfdat.bin", work / "data" / "mhfdat.bin")
    before = sha256(work / "data" / "mhfdat.bin")

    log = [
        "# 回寫報告",
        "",
        f"- 時間：{datetime.now().isoformat(timespec='seconds')}",
        f"- 模式：{'batch-delta' if args.batch else 'all-changed'}",
        f"- 回寫前 SHA256：`{before}`",
        "",
    ]
    ok = True
    written_idx: dict[str, list[str]] = {}

    jobs: list[tuple[str, list[dict]]] = []
    for bp in args.batch:
        sec_id, rows = rows_from_batch(Path(bp))
        jobs.append((sec_id, rows))
    if args.all_changed:
        for sec_id in args.sections or list(SECTIONS):
            jobs.append((sec_id, rows_all_changed(sec_id)))

    for sec_id, rows in jobs:
        good, line = import_rows(sec_id, rows, work)
        log.append(line)
        if not good:
            ok = False
            break
        written_idx.setdefault(sec_id, []).extend(r["index"] for r in rows)

    after = sha256(work / "data" / "mhfdat.bin")
    log += ["", f"- 回寫後 SHA256：`{after}`", ""]

    if not ok:
        WRITEBACK_LOG.write_text("\n".join(log), encoding="utf-8")
        print("\n".join(log), flush=True)
        shutil.rmtree(work, ignore_errors=True)
        return 2

    if after == before:
        log.append("- 警告：雜湊未變（可能未寫入）")
        WRITEBACK_LOG.write_text("\n".join(log), encoding="utf-8")
        print("\n".join(log), flush=True)
        shutil.rmtree(work, ignore_errors=True)
        return 3

    shutil.copy2(work / "data" / "mhfdat.bin", DATA / "mhfdat.bin")
    shutil.copy2(work / "data" / "mhfdat.bin", CLIENT_BIN)
    for sec_id, idxs in written_idx.items():
        save_state(sec_id, idxs, after)
    log.append(f"- 已同步：`l10n/data/mhfdat.bin` 與 `{CLIENT_BIN}`")
    WRITEBACK_LOG.write_text("\n".join(log + [""]), encoding="utf-8")
    print("\n".join(log), flush=True)
    shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
