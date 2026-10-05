# l10n/working 目錄結構

工作流：[`docs/agent-translation-playbook.md`](../docs/agent-translation-playbook.md) → [`docs/plans/l10n-orchestration.md`](../docs/plans/l10n-orchestration.md)。指令：`PIPELINE.md`。  
**已譯文以 `csv/` 為準；待審看 `issues/queue.md`。禁止因目錄搬家而重翻。**

| 目錄 | 用途 |
|------|------|
| `csv/` | 譯文工作 CSV（UTF-8 無 BOM）＝主真相 |
| `batches/active/` | 進行中語意批次 JSON |
| `batches/awaiting_qa/` | 已譯待獨立 QA 的批次（溯源；勿重做） |
| `batches/legacy/` | 歷史流水號歸檔 |
| `state/` | `writeback-state.json` |
| `logs/` | validate／writeback／apply 日誌 |
| `catalogs/` | 一覽（如 `ITEMS-TRANSLATED.md`） |
| `scratch/` | 本機暫態腳本／中間檔（gitignore；勿當審面） |
| `_backup/` 等 | 本機備份／verify／writeback 殘渣（gitignore） |
| `issues/` | 隊列與審閱（見 `issues/queue.md`）；武器請開 `issues/weapons/README.md` |
| `paths.py` | 路徑契約 |

舊 `reports/` 已廢止，勿再寫入。
