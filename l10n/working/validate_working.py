# -*- coding: utf-8 -*-
"""驗證 working CSV：白名單、CP932、placeholder 段數。"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from paths import WORKING, L10N, CSV_DIR, VALIDATE_LOG, ensure_dirs

WHITELIST = L10N / "charset" / "whitelist.txt"

PLACEHOLDER_RE = re.compile(
    r"\{j\}|\{/c\}|\{c\d+\}|\{K[^}]*\}|\{i[^}]*\}|\{u[^}]*\}"
)


def load_allow() -> set[str]:
    return set(WHITELIST.read_text(encoding="utf-8"))


def cp932_ok(s: str) -> bool:
    try:
        s.encode("cp932")
        return True
    except UnicodeEncodeError:
        return False


def ph_counts(s: str) -> dict[str, int]:
    return {
        "j": s.count("{j}"),
        "tokens": len(PLACEHOLDER_RE.findall(s)),
    }


def validate_file(path: Path, allow: set[str]) -> list[str]:
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig", newline="")))
    errs: list[str] = []
    for row in rows:
        src = row.get("source") or ""
        tgt = row.get("target") or ""
        idx = row.get("index", "?")
        # 抽出物本身就有空槽；source 空則允許 target 空
        if not src.strip():
            if tgt.strip():
                errs.append(f"{path.name}#{idx}: source 空但 target 有值")
            continue
        if not tgt.strip():
            errs.append(f"{path.name}#{idx}: target 空白")
            continue
        # 未譯（仍為原文）不檢查漢字白名單
        if tgt == src:
            continue
        missing = sorted({ch for ch in tgt if ch not in allow and not ch.isspace()})
        if missing:
            errs.append(
                f"{path.name}#{idx}: 缺字 {''.join(missing)} | {tgt[:40]}"
            )
        if not cp932_ok(tgt):
            errs.append(f"{path.name}#{idx}: CP932 失敗 | {tgt[:40]}")
        sc, tc = ph_counts(src), ph_counts(tgt)
        if sc["j"] != tc["j"]:
            errs.append(
                f"{path.name}#{idx}: {{j}} 段數 {sc['j']}→{tc['j']}"
            )

    return errs


def main(argv: list[str]) -> int:
    allow = load_allow()
    sections = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
    only = set(argv[1:]) if len(argv) > 1 else None
    ensure_dirs()
    all_errs: list[str] = []
    lines = ["# working 驗證報告", ""]
    for sec in sections:
        if only and sec["id"] not in only:
            continue
        path = CSV_DIR / sec["extracted"]
        if not path.exists():
            all_errs.append(f"缺少 {path.name}")
            lines.append(f"- `{sec['id']}`：缺少 CSV")
            continue
        errs = validate_file(path, allow)
        all_errs.extend(errs)
        lines.append(
            f"- `{sec['id']}`：{'PASS' if not errs else f'FAIL ({len(errs)})'}"
        )
    lines += ["", "## 錯誤", ""]
    if all_errs:
        lines.extend(f"- {e}" for e in all_errs[:100])
    else:
        lines.append("- （無）")
    lines.append("")
    VALIDATE_LOG.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 1 if all_errs else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
