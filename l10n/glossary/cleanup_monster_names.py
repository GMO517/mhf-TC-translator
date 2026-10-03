# -*- coding: utf-8 -*-
"""修正明顯不佳的 Frontier 魔物譯名，並重寫 REVIEW。"""
import csv
from collections import Counter
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

FIX = {
    "Kuarusepusu": ("嵐氣龍", "Frontier；譯名待你再核"),
    "Meraginasu": ("黑穿龍", "Frontier"),
    "Voljang": ("爆狼龍", "Frontier；譯名待你再核"),
    "Zenaserisu": ("天彗龍ゼナ", "Frontier；譯名待你再核"),
    "Keoaruboru": ("焦炎王龍", "Frontier；譯名待你再核"),
    "Hapulubokka": ("河童蛙", "Frontier"),
    "Uruki": ("烏魯基", "Frontier 小怪"),
    "Gougarf": ("剛猿狐", "Frontier"),
    "Guanzorumu": ("戰帝龍", "Frontier"),
    "Disufiroa": ("迪斯菲羅亞", "Frontier 煌黑龍系；簡稱可再議"),
    "Mi Ru": ("密爾", "Frontier"),
    "Poborubarumu": ("霧海龍", "Frontier；譯名待你再核"),
    "Aruganosu": ("銀火龍（阿魯）", "Frontier 對龍；待核"),
    "Goruganosu": ("金火龍（戈魯）", "Frontier 對龍；待核"),
    "Forokururu": ("風彩鳥", "Frontier"),
    "Rebidiora": ("雷轟龍", "Frontier"),
    "Bogabadorumu": ("爆鎚龍", "Frontier"),
    "Inagami": ("雲羊鹿", "Frontier"),
    "Anorupatisu": ("冰鯊龍", "Frontier"),
    "Elzelion": ("雙極龍", "Frontier"),
    "Eruzerion": ("雙極龍", "Frontier"),
    "Zenaserisu": ("天塞龍", "Frontier；譯名待你再核"),
}

DROP_EN = {"Unknown", "Farunakk", "Albino"}  # 占位／不確定詞綴先拿掉


def main() -> None:
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    out = []
    for r in rows:
        en = r.get("source_en") or ""
        if en in DROP_EN:
            continue
        if en in FIX:
            zh, note = FIX[en]
            r["target_zh_tw"] = zh
            r["notes"] = f"MHF 擴充；{note}"
        out.append(r)

    # 去重 source_en（同英文保留 approved=Y 或先出現）
    best = {}
    order = []
    for r in out:
        k = (r["category"], (r.get("source_en") or "").lower())
        if k not in best:
            best[k] = r
            order.append(k)
        else:
            if r.get("approved") == "Y" and best[k].get("approved") != "Y":
                best[k] = r

    uniq = [best[k] for k in order]

    # 重編 id
    counters: Counter = Counter()
    final = []
    for r in uniq:
        counters[r["category"]] += 1
        r = dict(r)
        r["id"] = f"{r['category'][:3].upper()}{counters[r['category']]:03d}"
        final.append(r)

    fields = list(final[0].keys())
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(final)

    by = {}
    for r in final:
        by.setdefault(r["category"], []).append(r)
    lines = [
        "# 詞語庫審閱",
        "",
        "> 本體名稱多為英文；繁中以台灣慣用＋《荒野》為準；`frontier_only=Y` 為 MHF 特有。",
        "> 已核准：`approved=Y`。請優先審 **frontier／monster** 區塊（含大量 MHF 特有魔物）。",
        "",
        f"總詞條：{len(final)}",
        "",
        "## 你已手改並標記核准",
        "",
        "| 原文 | 繁中 |",
        "|---|---|",
        "| Kelbi | 精靈鹿 |",
        "| Khezu | 奇怪龍 |",
        "| Magnet Spike | 磁斬槌 |",
        "",
    ]
    # frontier 與 monster 放前面方便審
    for cat in ["frontier", "monster", "weapon_type", "system", "item", "ui"]:
        if cat not in by:
            continue
        lines.append(f"## {cat}（{len(by[cat])}）")
        lines.append("")
        lines.append("| 原文(EN/JP) | 建議繁中 | Frontier | approved | 備註 |")
        lines.append("|---|---|---|---|---|")
        for r in by[cat]:
            src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
            lines.append(
                f"| {src} | {r['target_zh_tw']} | {r['frontier_only']} | {r['approved']} | {r['notes']} |"
            )
        lines.append("")

    REVIEW.write_text("\n".join(lines), encoding="utf-8")
    print("total", len(final))
    print("frontier", counters["frontier"], "monster", counters["monster"])
    print("approved_Y", sum(1 for r in final if r["approved"] == "Y"))


if __name__ == "__main__":
    main()
