# -*- coding: utf-8 -*-
"""詞語庫查表：展開 source_en 的「／」別名與獨立縮寫列；全專案共用。"""
from __future__ import annotations

import csv
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TERMS = ROOT / "glossary" / "terms.csv"

# 防具級別 GS≠武器種大劍：查系列名時排除
BLOCK_AS_SERIES = {
    "gs",
    "ls",
    "sns",
    "db",
    "ds",
    "hm",
    "hh",
    "lbg",
    "hbg",
    "bow",
    "sa",
    "gl",
    "saf",
    "ms",
    "great sword",
    "long sword",
}


@lru_cache(maxsize=1)
def load_alias_map(*, include_weapons: bool = False) -> dict[str, str]:
    """key=小寫英文（含縮寫）→ 顯示用繁中。"""
    out: dict[str, str] = {}
    for r in csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")):
        if r.get("approved") != "Y":
            continue
        zh = (r.get("fallback_glyph") or r.get("target_zh_tw") or "").strip()
        if not zh:
            continue
        cat = r.get("category") or ""
        if not include_weapons and cat == "weapon_type":
            continue
        en = (r.get("source_en") or "").strip()
        if not en:
            continue
        for piece in re.split(r"\s*/\s*", en):
            piece = re.sub(r"\([^)]*\)", "", piece).strip()
            if not piece:
                continue
            key = piece.lower().rstrip(".")
            if not include_weapons and key in BLOCK_AS_SERIES:
                continue
            out[key] = zh
            # 無點變體：W.Espi → w.espi 已有；亦存 w espi？不
            if "." in key:
                out[key.replace(".", "")] = zh
    return out


def lookup(en: str, *, include_weapons: bool = False) -> str | None:
    if not en:
        return None
    m = load_alias_map(include_weapons=include_weapons)
    k = en.strip().lower().rstrip(".")
    if k in m:
        return m[k]
    k2 = k.replace(" ", "")
    return m.get(k2)
