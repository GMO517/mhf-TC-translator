# -*- coding: utf-8 -*-
"""
補上個別辿異種魔物詞條。
顯示形建議採台服「辿異種‧XX」；另在 notes 註短形備援。
來源：https://w.atwiki.jp/mhfotw/pages/1992.html
"""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

TERMS = Path(__file__).with_name("terms.csv")
REVIEW = Path(__file__).with_name("REVIEW.md")

# (jp_base, en_base, zh_base) — 台服魔物本名
TENI_MONSTERS = [
    ("ドドブランゴ", "Dodoblanco / Blangonga", "雪獅子王"),
    ("ミドガロン", "Midogaron", "爆狼"),
    ("ヒプノック", "Hypnocatrice", "眠鳥"),
    ("ガノトトス", "Plesioth", "水龍"),
    ("リオレウス", "Rathalos", "火龍"),
    ("フルフル", "Khezu", "電龍"),  # 台服對フルフル稱電龍；系列詞你已核奇怪龍→辿異用台服
    ("ティガレックス", "Tigrex", "轟龍"),
    ("エスピナス", "Espinas", "棘龍"),
    ("ヒュジキキ", "Hyujikiki", "針纏龍"),
    ("ダイミョウザザミ", "Daimyo Hermitaur", "大名蟹"),
    ("アクラ・ヴァシム", "Akura Vashimu", "尾晶蠍"),
    ("ギアオルグ", "Giaorugu", "冰獰龍"),
    ("ルコディオラ", "Rukodiora", "極龍"),
    ("イナガミ", "Inagami", "雅翁龍"),
]


def main() -> None:
    rows = list(csv.DictReader(TERMS.open(encoding="utf-8-sig", newline="")))
    have = {
        (r.get("source_jp") or "")
        for r in rows
        if r.get("category") == "frontier_monster"
    }

    for jp, en, zh in TENI_MONSTERS:
        sjp = f"辿異種{jp}"
        if sjp in have or f"辿異種‧{zh}" in {
            r.get("target_zh_tw") for r in rows if "辿異" in (r.get("target_zh_tw") or "")
        }:
            # 以 jp 鍵去重
            if any(r.get("source_jp") == sjp for r in rows):
                print("skip", sjp)
                continue
        rows.append(
            {
                "id": "",
                "category": "frontier_monster",
                "source_jp": sjp,
                "source_en": f"Teni {en}",
                "target_zh_tw": f"辿異種‧{zh}",
                "wilds_ref": "",
                "frontier_only": "Y",
                "register": "ui",
                "display_ok": "pending",
                "fallback_glyph": "",
                "notes": "台服；短形可XX(辿異)",
                "approved": "N",
                "review_flag": "新增",
            }
        )
        print("add", f"辿異種‧{zh}")

    # 重編 id
    order = [
        "weapon_type",
        "system",
        "frontier_system",
        "frontier_monster",
        "monster",
        "item",
        "ui",
    ]
    buckets = {k: [] for k in order}
    other = []
    for r in rows:
        (buckets[r["category"]] if r["category"] in buckets else other).append(r)
    out = []
    c: Counter = Counter()
    for cat in order:
        for r in buckets[cat]:
            c[cat] += 1
            r = dict(r)
            prefix = {"frontier_system": "FSY", "frontier_monster": "FMO"}.get(
                cat, cat[:3].upper()
            )
            r["id"] = f"{prefix}{c[cat]:03d}"
            out.append(r)
    for r in other:
        c[r["category"]] += 1
        r = dict(r)
        r["id"] = f"{r['category'][:3].upper()}{c[r['category']]:03d}"
        out.append(r)

    fields = [
        "id",
        "category",
        "source_jp",
        "source_en",
        "target_zh_tw",
        "wilds_ref",
        "frontier_only",
        "register",
        "display_ok",
        "fallback_glyph",
        "notes",
        "approved",
        "review_flag",
    ]
    with TERMS.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)

    # REVIEW：更新總數、在請先檢查插入辿異魔物、重寫 frontier_monster 段頭說明
    text = REVIEW.read_text(encoding="utf-8")
    text = re.sub(r"總詞條：\d+", f"總詞條：{len(out)}", text, count=1)

    teni_mon = [
        r
        for r in out
        if r.get("category") == "frontier_monster"
        and (r.get("source_jp") or "").startswith("辿異種")
    ]
    insert_lines = []
    for r in teni_mon:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        insert_lines.append(
            f"| {src} | {r['target_zh_tw']} | 新增 | {r['notes']} |"
        )
    if insert_lines and "辿異種‧火龍" not in text:
        text = text.replace(
            "| EN/JP | 譯名 | 狀態 | 備註 |\n|---|---|---|---|",
            "| EN/JP | 譯名 | 狀態 | 備註 |\n|---|---|---|---|\n"
            + "\n".join(insert_lines),
        )

    # 命名建議區塊
    tip = (
        "\n## 辿異種顯示形（建議）\n\n"
        "| 場景 | 建議 | 原因 |\n"
        "|---|---|---|\n"
        "| 詞語庫／圖鑑／任務標題 | `辿異種‧火龍` | 台服 wiki 寫法，語意清楚 |\n"
        "| 超短 UI／爆框時備援 | `火龍(辿異)` | 較短；半形括號省寬 |\n"
        "| 不要用 | `辿異種火龍`（無分隔） | 連讀易糊 |\n\n"
        "> **字數會影響**：遊戲 UI 有顯示寬限制（CJK 多半算 2）。"
        "正式形先用 `辿異種‧XX`；回寫時再用行寬驗證決定是否改短形。\n"
    )
    if "## 辿異種顯示形" not in text:
        # 插在找不到段之後
        if "## 找不到" in text:
            parts = text.split("## 找不到", 1)
            # 找到下一個 ## 之後插入 tip 在找不到段結束後
            rest = parts[1]
            m = re.search(r"\n## ", rest)
            if m:
                text = (
                    parts[0]
                    + "## 找不到"
                    + rest[: m.start()]
                    + tip
                    + rest[m.start() :]
                )
            else:
                text = parts[0] + "## 找不到" + rest + tip
        else:
            text = text.replace(f"總詞條：{len(out)}\n", f"總詞條：{len(out)}\n{tip}")

    # 重寫 frontier_monster 完整表（保持與 CSV 同步）
    fmo = [r for r in out if r["category"] == "frontier_monster"]
    block = [
        "## 邊境魔物（完整）",
        "",
        f"（{len(fmo)}）",
        "",
        "| EN/JP | 繁中 | 狀態 | 備註 |",
        "|---|---|---|---|",
    ]
    for r in fmo:
        src = " / ".join(x for x in [r["source_en"], r["source_jp"]] if x)
        block.append(
            f"| {src} | {r['target_zh_tw']} | {r.get('review_flag') or '沿用'} | {r['notes']} |"
        )
    block.append("")
    new_block = "\n".join(block)
    text2 = re.sub(
        r"## 邊境魔物（完整）.*?(?=\n## |\Z)", new_block, text, count=1, flags=re.S
    )
    if text2 == text:
        text2 = re.sub(
            r"## frontier_monster.*?(?=\n## |\Z)", new_block, text, count=1, flags=re.S
        )

    REVIEW.write_text(text2, encoding="utf-8")
    print("total", len(out), "teni_monsters", len(teni_mon))


if __name__ == "__main__":
    main()
