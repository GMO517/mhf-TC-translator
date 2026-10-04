# 詞語庫建置過程紀錄（已退役腳本）

以下腳本曾用於從初稿擴到現況，**成果已併入 `terms.csv`／`REVIEW.md`**，不再保留可執行檔。

| 舊檔 | 做過什麼 |
|---|---|
| `expand_monsters.py` | 擴充 MHF／Frontier 魔物詞條；同步早期 REVIEW 手改 |
| `cleanup_monster_names.py` | 修正明顯不佳的 Frontier 譯名 |
| `apply_frontier_monster_names.py` | 依玩家常講／日文漢字別名套用邊境魔物譯名 |
| `apply_tw_wiki_names.py` | 對照 [台服 wiki 魔物一覽](https://w.atwiki.jp/mhfotw/pages/22.html) 套名；找不到標註 |
| `shorten_notes_and_apply.py` | 備註略縮（台服／系列／系統…）並重寫 REVIEW |
| `add_teni_terms.py` | 補辿異種／技能／武器／防具／任務／發達部位 |
| `add_teni_monsters.py` | 補個別「辿異種‧XX」魔物條 |
| `rebuild_review_layout.py` | 已審邊境條目移出待審區、核准旗標重整（曾整檔覆寫 REVIEW） |
| `restore_user_review_edits.py` | 從 Cursor 本機歷史救回被腳本蓋掉的 REVIEW 手改（一次性） |

定稿後管線只留 `README.md` 的 step1～3。
