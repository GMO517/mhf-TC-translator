# 離線 round-trip 結果

- 時間：2026-10-04T08:25:07
- Python：C:\Users\GMO\AppData\Local\Programs\Python\Python312\python.exe
- FTH：E:\MHF\tools\FrontierTextHandler

| xpath | bin | 抽出 | 回寫 | SHA256 一致 | 備註 |
|---|---|---|---|---|---|
| `dat/weapons/melee/name` | mhfdat.bin | OK | OK | Y | strings=OK; reextract=OK; hash=same |
| `dat/weapons/ranged/name` | mhfdat.bin | OK | OK | Y | strings=OK; reextract=OK; hash=same |
| `dat/items/name` | mhfdat.bin | OK | OK | Y | strings=OK; reextract=OK; hash=same |
| `dat/armors/head` | mhfdat.bin | OK | OK | Y | strings=OK; reextract=OK; hash=same |
| `dat/armors/body` | mhfdat.bin | OK | OK | Y | strings=OK; reextract=OK; hash=same |
| `dat/monsters/description` | mhfdat.bin | OK | OK | Y | strings=OK; reextract=OK; hash=same |

**總評：PASS（離線）**

> 雜湊不一致時，若「可再抽出」仍算工具鏈可用（壓縮／加密容器可能非位元穩定）。
> 進遊戲 smoke 另做，不是本腳本範圍。
