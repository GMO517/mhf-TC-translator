# -*- coding: utf-8 -*-
"""依白名單更新 terms.csv 的 display_ok／fallback_glyph。"""
from __future__ import annotations

import csv
from pathlib import Path

CHARSET = Path(__file__).resolve().parent
TERMS = CHARSET.parent / "glossary" / "terms.csv"
WHITELIST = CHARSET / "whitelist.txt"
FALLBACK = CHARSET / "fallback_map.csv"
REPORT = CHARSET / "glossary_display_report.md"


def load_whitelist() -> set[str]:
    text = WHITELIST.read_text(encoding="utf-8")
    return set(text)


def load_fallback() -> dict[str, str]:
    rows = list(csv.DictReader(FALLBACK.open(encoding="utf-8-sig", newline="")))
    out: dict[str, str] = {}
    for r in rows:
        frm = r.get("from") or ""
        to = r.get("to") or ""
        if frm and to and frm not in out:
            out[frm] = to
    return out


def cp932_ok(s: str) -> bool:
    try:
        s.encode("cp932")
        return True
    except UnicodeEncodeError:
        return False


def apply_fallback(text: str, allow: set[str], fb: dict[str, str]) -> str:
    parts: list[str] = []
    for ch in text:
        if ch in allow:
            parts.append(ch)
        elif ch in fb and all(c in allow for c in fb[ch]):
            parts.append(fb[ch])
        else:
            parts.append(ch)
    return "".join(parts)


def analyze(text: str, allow: set[str], fb: dict[str, str]) -> tuple[str, str, list[str]]:
    """回傳 display_ok, fallback_glyph, 缺字列表。

    理想繁中可顯示 → Y、無 fallback。
    套用 fallback 後可顯示 → Y、寫入 fallback_glyph。
    仍有缺字 → N。
    """
    missing: list[str] = []
    for ch in text:
        if ch not in allow and ch not in missing:
            missing.append(ch)

    if not missing and cp932_ok(text):
        return "Y", "", []

    suggestion = apply_fallback(text, allow, fb)
    if (
        suggestion
        and all(c in allow for c in suggestion)
        and cp932_ok(suggestion)
    ):
        return "Y", suggestion, missing

    still: list[str] = []
    for ch in suggestion:
        if ch not in allow and ch not in still:
            still.append(ch)
    return "N", suggestion if suggestion != text else "", still or missing


def main() -> None:
    if not WHITELIST.exists():
        raise SystemExit("先跑 build_whitelist.py")
    allow = load_whitelist()
    fb = load_fallback()
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    fields = list(rows[0].keys())

    ok_n = bad_n = 0
    bad_samples: list[str] = []
    fb_samples: list[str] = []
    for r in rows:
        zh = r.get("target_zh_tw") or ""
        display, glyph, miss = analyze(zh, allow, fb)
        r["display_ok"] = display
        r["fallback_glyph"] = glyph
        if display == "Y":
            ok_n += 1
            if glyph and len(fb_samples) < 50:
                fb_samples.append(f"| {r['id']} | {zh} | {glyph} |")
        else:
            bad_n += 1
            if len(bad_samples) < 40:
                miss_s = "".join(miss)
                bad_samples.append(
                    f"| {r['id']} | {zh} | {miss_s} | {glyph or '—'} |"
                )

    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    report = [
        "# 詞語庫 display_ok 報告",
        "",
        f"- 白名單字數：{len(allow)}",
        f"- 可顯示（Y）：{ok_n}",
        f"- 有缺字（N）：{bad_n}",
        "",
        "## 暫用形（日後可能再修）",
        "",
        "| 主題 | 詞條 | 現況 | 備註 |",
        "|---|---|---|---|",
        "| 陷阱 | ITE014／ITE015 | 落穴罠／麻痺罠 | 暫用「罠」；可能改回陷阱系 |",
        "| 鐮 | MON007／MON041 | 鐮蟹→顯示鎌蟹 | 暫用「鎌」fallback |",
        "| 剝取 | SYS049 | 剝取→顯示剥取 | 暫用「剥」fallback |",
        "| 貓／喵 | FSY042 | 理想「貓」→顯示「猫」 | 「喵」無字形，改「貓」 |",
        "",
        "## 仍缺字（N）",
        "",
        "| id | 繁中 | 缺字 | fallback 建議 |",
        "|---|---|---|---|",
        *(bad_samples if bad_samples else ["| （無） | | | |"]),
        "",
        "## 使用 fallback_glyph 的詞條",
        "",
        "| id | 理想繁中 | 顯示形 |",
        "|---|---|---|",
        *(fb_samples if fb_samples else ["| （無） | | |"]),
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"display_ok Y={ok_n} N={bad_n} -> {TERMS}")
    print(f"report -> {REPORT}")


if __name__ == "__main__":
    main()
