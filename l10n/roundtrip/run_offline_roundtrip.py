# -*- coding: utf-8 -*-
"""離線 round-trip：抽出 → 原樣回寫（compress+encrypt）→ 雜湊比對。

不需開遊戲。結果寫入本目錄 RESULT.md。
"""
from __future__ import annotations

import csv
import hashlib
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FTH = ROOT / "tools" / "FrontierTextHandler"
DATA = ROOT / "l10n" / "data"
OUT = Path(__file__).resolve().parent
PY = sys.executable

# MVP 已抽出的 xpath（對應 mhfdat / mhfpac）
SECTIONS = [
    ("dat/weapons/melee/name", "mhfdat.bin"),
    ("dat/weapons/ranged/name", "mhfdat.bin"),
    ("dat/items/name", "mhfdat.bin"),
    ("dat/armors/head", "mhfdat.bin"),
    ("dat/armors/body", "mhfdat.bin"),
    ("dat/monsters/description", "mhfdat.bin"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run_fth(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    cmd = [PY, str(FTH / "main.py"), *args]
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main() -> int:
    work = OUT / "work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    (work / "data").mkdir()
    (work / "output").mkdir()

    # 複製會動到的 bin
    bins = sorted({b for _, b in SECTIONS})
    for b in bins:
        src = DATA / b
        if not src.exists():
            print(f"MISSING {src}")
            return 1
        shutil.copy2(src, work / "data" / b)

    results: list[str] = [
        f"# 離線 round-trip 結果",
        "",
        f"- 時間：{datetime.now().isoformat(timespec='seconds')}",
        f"- Python：{PY}",
        f"- FTH：{FTH}",
        "",
        "| xpath | bin | 抽出 | 回寫 | SHA256 一致 | 備註 |",
        "|---|---|---|---|---|---|",
    ]

    ok_all = True
    for xpath, bin_name in SECTIONS:
        print(f"== {xpath} ==")
        bin_path = work / "data" / bin_name
        before = sha256(bin_path)

        # 抽出到 work/output（FTH 預設寫 output/）
        # 使用 --xpath；工作目錄設 work，並把 data 放對
        r1 = run_fth(["--xpath", xpath, f"data/{bin_name}"], cwd=work)
        extract_ok = r1.returncode == 0
        if not extract_ok:
            print(r1.stdout)
            print(r1.stderr)
            results.append(f"| `{xpath}` | {bin_name} | FAIL | - | - | extract rc={r1.returncode} |")
            ok_all = False
            continue

        # 找剛產出的 csv
        csvs = list((work / "output").glob("*.csv"))
        # 取最新修改
        csvs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        if not csvs:
            results.append(f"| `{xpath}` | {bin_name} | FAIL | - | - | no csv |")
            ok_all = False
            continue
        csv_path = csvs[0]

        # 原樣回寫：把 target 填成 source，強制走重建路徑
        rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig", newline="")))
        if not rows:
            results.append(f"| `{xpath}` | {bin_name} | FAIL | - | - | empty csv |")
            ok_all = False
            continue
        fields = list(rows[0].keys())
        for row in rows:
            if not (row.get("target") or "").strip():
                row["target"] = row.get("source") or ""
        with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        sources = [row.get("source") or "" for row in rows]

        out_bin = work / "data" / f"rt-{bin_name}"
        shutil.copy2(bin_path, out_bin)
        r2 = run_fth(
            [
                "--csv-to-bin",
                str(csv_path.relative_to(work)).replace("\\", "/"),
                str(out_bin.relative_to(work)).replace("\\", "/"),
                "--xpath",
                xpath,
                "--compress",
                "--encrypt",
            ],
            cwd=work,
        )
        import_ok = r2.returncode == 0
        if not import_ok:
            print(r2.stdout)
            print(r2.stderr)
            results.append(
                f"| `{xpath}` | {bin_name} | OK | FAIL | - | import rc={r2.returncode} |"
            )
            ok_all = False
            continue

        after = sha256(out_bin)
        same = after == before

        # 再抽出，比對字串內容（比雜湊更關鍵）
        # 清掉舊 csv 以免抓錯檔
        for old in (work / "output").glob("*.csv"):
            old.unlink()
        r3 = run_fth(
            ["--xpath", xpath, str(out_bin.relative_to(work)).replace("\\", "/")],
            cwd=work,
        )
        reextract_ok = r3.returncode == 0
        strings_ok = False
        if reextract_ok:
            csvs2 = sorted(
                (work / "output").glob("*.csv"),
                key=lambda p: p.stat().st_mtime,
                reverse=True,
            )
            if csvs2:
                rows2 = list(
                    csv.DictReader(csvs2[0].open(encoding="utf-8-sig", newline=""))
                )
                sources2 = [row.get("source") or "" for row in rows2]
                strings_ok = sources2 == sources

        note = (
            f"strings={'OK' if strings_ok else 'DIFF'}; "
            f"reextract={'OK' if reextract_ok else 'FAIL'}; "
            f"hash={'same' if same else 'diff'}"
        )
        pass_row = extract_ok and import_ok and reextract_ok and strings_ok
        if not pass_row:
            ok_all = False
        results.append(
            f"| `{xpath}` | {bin_name} | OK | {'OK' if import_ok else 'FAIL'} | "
            f"{'Y' if same else 'N'} | {note} |"
        )

        # 還原 data 內原 bin，避免下一 section 用到已改檔
        shutil.copy2(DATA / bin_name, bin_path)

    results += [
        "",
        f"**總評：{'PASS（離線）' if ok_all else 'FAIL'}**",
        "",
        "> 雜湊不一致時，若「可再抽出」仍算工具鏈可用（壓縮／加密容器可能非位元穩定）。",
        "> 進遊戲 smoke 另做，不是本腳本範圍。",
        "",
    ]
    (OUT / "RESULT.md").write_text("\n".join(results), encoding="utf-8")
    print("\n".join(results))
    return 0 if ok_all else 2


if __name__ == "__main__":
    raise SystemExit(main())
