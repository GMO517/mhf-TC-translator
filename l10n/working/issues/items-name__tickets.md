# QA: items-name / tickets

- progress_suggestion: （子類未譯完，尚不進全量 QA）
- translation_status: **partial — in_progress**
- active_batch: `l10n/working/batches/active/batch-items-tickets.json`
- legacy_batches: `batches/legacy/batch-items-tickets-a.json` … `-d.json`（已 commit；已在 CSV）
- csv_verify_active: 累積至 **#8915**（約 638 筆在 active JSON；含手修 Ohai／綠茶／HRP／深紅・白ＧＳ）
- next_untranslated: **#9092** `Baro K Tkt`
- note: 整類票券清完前不要宣告 translated；**已譯列禁止重翻**

## 已保全區段（勿重做）

| 區段 | 產物 | 狀態 |
|---|---|---|
| 票券 A–D | `batches/legacy/batch-items-tickets-*.json` | 已 commit＋CSV |
| 票券續推（#4856 起累積） | `batches/active/batch-items-tickets.json` | CSV＋多次 delta；下一 #9092 |

## blocking / high / low

（子類完成後由 QA Agent 填寫）
