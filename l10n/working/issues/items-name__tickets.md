# QA: items-name / tickets

- progress_suggestion: （子類未譯完，尚不進全量 QA）
- translation_status: **partial — in_progress**
- active_batch: `l10n/working/batches/active/batch-items-tickets.json`
- legacy_batches: `batches/legacy/batch-items-tickets-a.json` … `-d.json`（已 commit；已在 CSV）
- csv_verify_active: 158/158（#4856–5772 段）與 batch 一致（2026-10-04）
- next_untranslated: **#6018** `Parin WhtTea Tkt`
- note: 整類票券清完前不要宣告 translated；**已譯列禁止重翻**

## 已保全區段（勿重做）

| 區段 | 產物 | 狀態 |
|---|---|---|
| 票券 A–D | `batches/legacy/batch-items-tickets-*.json` | 已 commit＋CSV |
| 票券續段（原 E，已去字母） | `batches/active/batch-items-tickets.json` | CSV＋delta 回寫；見保全 commit |

## blocking / high / low

（子類完成後由 QA Agent 填寫）
