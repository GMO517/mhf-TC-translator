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
# 全形拉丁後接片假名（含・）；用於半翻警告
HALF_TRANSLATE_RE = re.compile(r"[Ａ-Ｚａ-ｚ]+[\u30A0-\u30FF]+")
KATA_LETTER_RE = re.compile(r"[\u30A1-\u30FA\u30FC]")
KATA_ANY_RE = re.compile(r"[\u30A1-\u30FA\u30FC]")
HAN_RE = re.compile(r"[\u4e00-\u9fff]")
ASCII_WORD_RE = re.compile(r"[A-Za-z]{2,}")


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


def is_half_translate(src: str, tgt: str) -> bool:
    """英源＋譯文出現全形拉丁黏片假名 → 半翻（原文已是日文形者不計）。"""
    if not ASCII_WORD_RE.search(src):
        return False
    m = HALF_TRANSLATE_RE.search(tgt)
    if not m:
        return False
    return bool(KATA_LETTER_RE.search(m.group(0)))


def is_kata_han_mix(tgt: str) -> bool:
    """片假名與漢字同時出現 → 不合格混寫。"""
    return bool(KATA_ANY_RE.search(tgt) and HAN_RE.search(tgt))


def validate_file(path: Path, allow: set[str]) -> tuple[list[str], list[str]]:
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig", newline="")))
    errs: list[str] = []
    half_warns: list[str] = []
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
        if is_half_translate(src, tgt):
            half_warns.append(
                f"{path.name}#{idx}: 半翻（全形字母＋片假名）| {tgt[:40]} → 見 glossary/PENDING.md"
            )
        elif is_kata_han_mix(tgt):
            half_warns.append(
                f"{path.name}#{idx}: 片假名混中文 | {tgt[:40]} → 見 glossary/PENDING.md"
            )

    return errs, half_warns


def main(argv: list[str]) -> int:
    allow = load_allow()
    sections = json.loads((WORKING / "sections.json").read_text(encoding="utf-8"))
    only = set(argv[1:]) if len(argv) > 1 else None
    ensure_dirs()
    all_errs: list[str] = []
    all_half: list[str] = []
    lines = ["# working 驗證報告", ""]
    for sec in sections:
        if only and sec["id"] not in only:
            continue
        path = CSV_DIR / sec["extracted"]
        if not path.exists():
            all_errs.append(f"缺少 {path.name}")
            lines.append(f"- `{sec['id']}`：缺少 CSV")
            continue
        errs, half = validate_file(path, allow)
        all_errs.extend(errs)
        all_half.extend(half)
        note = ""
        if half:
            note = f"；半翻警告 {len(half)}"
        lines.append(
            f"- `{sec['id']}`：{'PASS' if not errs else f'FAIL ({len(errs)})'}{note}"
        )
    lines += ["", "## 錯誤", ""]
    if all_errs:
        lines.extend(f"- {e}" for e in all_errs[:100])
    else:
        lines.append("- （無）")
    lines += ["", "## 半翻／片假名混中文警告（暫不致 FAIL；應列入 PENDING，子類完成後回修）", ""]
    if all_half:
        lines.extend(f"- {e}" for e in all_half[:80])
        if len(all_half) > 80:
            lines.append(f"- …另有 {len(all_half) - 80} 筆")
    else:
        lines.append("- （無）")
    lines.append("")
    text = "\n".join(lines)
    VALIDATE_LOG.write_text(text, encoding="utf-8")
    out = getattr(sys.stdout, "buffer", None)
    if out is not None:
        out.write((text + "\n").encode("utf-8", errors="replace"))
        out.flush()
    else:
        print(text)
    return 1 if all_errs else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
