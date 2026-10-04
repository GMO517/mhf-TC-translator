# -*- coding: utf-8 -*-
"""建立 MHF PC 可顯示字白名單（JIS X 0208 ＋ 可列印 ASCII）。"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).with_name("whitelist.txt")
README = Path(__file__).with_name("README.md")


def jis_ku_ten_to_sjis(ku: int, ten: int) -> bytes:
    """JIS X 0208 區點（1..94）→ Shift_JIS 雙位元組。"""
    row = ku + 0x20
    cell = ten + 0x20
    if row < 0x5F:
        b1 = ((row + 1) >> 1) + 0x70
    else:
        b1 = ((row + 1) >> 1) + 0xB0
    if row & 1:
        b2 = cell + 0x1F
        if b2 >= 0x7F:
            b2 += 1
    else:
        b2 = cell + 0x7E
    return bytes([b1, b2])


def jisx0208_chars() -> set[str]:
    chars: set[str] = set()
    for ku in range(1, 95):
        for ten in range(1, 95):
            try:
                s = jis_ku_ten_to_sjis(ku, ten).decode("cp932")
            except UnicodeDecodeError:
                continue
            if len(s) == 1:
                chars.add(s)
    return chars


def main() -> None:
    chars = jisx0208_chars() | {chr(i) for i in range(0x20, 0x7F)}
    ordered = sorted(chars, key=lambda c: (0 if ord(c) < 128 else 1, ord(c)))
    OUT.write_text("".join(ordered), encoding="utf-8")
    print(f"whitelist chars={len(ordered)} -> {OUT}")

    README.write_text(
        f"""# 字型／編碼閘門（Phase 0.5）

## 結論

現行 CT4.1／日系客戶端：

- **編碼**：CP932（Windows Shift-JIS）
- **繪字**：內嵌點陣 ≈ **JIS X 0208** + 可列印 ASCII  
  （FrontierTextHandler `docs/translation-format.md`）

台服當年 Big5／系統 TTF **不能**直接當本體白名單。

## 檔案

| 檔 | 用途 |
|---|---|
| `whitelist.txt` | 全部允許字元連成一字串（**{len(ordered)}** 字） |
| `fallback_map.csv` | 禁字 → 建議替換 |
| `check_glossary.py` | 更新詞語庫 `display_ok`／`fallback_glyph` |
| `build_whitelist.py` | 重建白名單 |

## 使用

```bash
python build_whitelist.py
python check_glossary.py
```

- `display_ok=Y`：繁中每字皆在白名單，且可 CP932 編碼  
- `display_ok=N`：有缺字；若 fallback 有對應則填 `fallback_glyph`
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
