# -*- coding: utf-8 -*-
"""對譯文套用白名單／fallback_map，回傳可顯示形或錯誤。"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOW = set((ROOT / "charset" / "whitelist.txt").read_text(encoding="utf-8"))


def load_fallback() -> dict[str, str]:
    path = ROOT / "charset" / "fallback_map.csv"
    out: dict[str, str] = {}
    for r in csv.DictReader(path.open(encoding="utf-8-sig", newline="")):
        frm, to = r.get("from") or "", r.get("to") or ""
        if frm and to and frm not in out:
            out[frm] = to
    return out


FB = load_fallback()


def to_display(text: str) -> tuple[str, list[str]]:
    """回傳 (顯示形, 仍缺字列表)。"""
    parts: list[str] = []
    missing: list[str] = []
    for ch in text:
        if ch in ALLOW or ch.isspace():
            parts.append(ch)
            continue
        if ch in FB and all(c in ALLOW or c.isspace() for c in FB[ch]):
            parts.append(FB[ch])
        else:
            parts.append(ch)
            if ch not in missing:
                missing.append(ch)
    out = "".join(parts)
    try:
        out.encode("cp932")
    except UnicodeEncodeError:
        if "CP932" not in missing:
            missing.append("CP932")
    still = [c for c in out if c not in ALLOW and not c.isspace()]
    # 去重
    uniq: list[str] = []
    for c in still:
        if c not in uniq:
            uniq.append(c)
    return out, uniq
