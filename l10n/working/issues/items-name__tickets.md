# QA: items-name / tickets

- progress_suggestion: translated（子類完；PENDING 已核可；待 QA）
- translation_status: **translated — awaiting_qa**
- batch: `l10n/working/batches/awaiting_qa/batch-items-tickets.json`（n=1927）
- legacy_batches: `batches/legacy/batch-items-tickets-*.json`（已 commit；已在 CSV）
- finish_batch: **OK**（初回 delta 1927）；定稿後 Fixer 再改 CSV 441 列（見 `glossary/DECIDED-tickets.md`；本體若需同步另跑 delta）
- next_untranslated: **無**
- review: `issues/review-items-name__tickets.md`（最終抽看；不擋主線）
- note: **已譯列禁止重翻**；PENDING 票券區已空

## 已保全區段（勿重做）

| 區段 | 產物 | 狀態 |
|---|---|---|
| 票券 A–D | `batches/legacy/batch-items-tickets-*.json` | 已 commit＋CSV |
| 票券全段 | `batches/awaiting_qa/batch-items-tickets.json` | CSV＋finish_batch delta 1927 |
| scratch FINAL | `scratch/tickets-chunk-apply.json` | #15376–16535 已併入 batch |

## blocking / high / low

（子類完成後由 QA Agent 填寫）
