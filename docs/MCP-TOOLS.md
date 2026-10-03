# 可協助「代辦不忘」的 MCP 工具（Web 搜尋摘要）

結論：**倉庫內 Markdown 代辦（`docs/TODO.md`）仍是最穩的 Source of Truth**；MCP 可選加強，不取代本檔。

## 較推薦（依本專案）

| 工具 | 連結 | 適合原因 | 注意 |
|------|------|----------|------|
| **Todokit** | https://github.com/j0hanz/todokit-mcp-server | 本機 JSON 持久化待辦、輕量、原子寫入 | 與 `docs/TODO.md` 可能雙源，需約定「以誰為準」 |
| **mcp-cursor-taskmaster** | https://github.com/notbnull/mcp-cursor-taskmaster | 專案內 `.taskmaster/`、階層任務、記憶檢索 | 需設 `--project-dir`；偏重 |
| **Anchor** | https://glama.ai/mcp/servers/thewillmoss/anchor-mcp | 跨 Agent 共用 active task／plans／memory（`.anchor/`） | 適合多工具切換時 |
| **Task Guardian** | https://github.com/jalbarrang/task-guardian-mcp | `.task/` 檔案型任務、相依關係 | Cursor 整合導向 |

## 記憶／知識庫向（可選）

| 工具 | 連結 | 用途 |
|------|------|------|
| MegaMemory | https://github.com/0xK3vin/megamemory | 專案概念圖＋語意搜尋（`.megamemory/`） |
| project-memory-mcp | https://github.com/pnientiedt/project-memory-mcp | 決策／進度 Markdown 記憶，偏離線 |
| Context Manager | https://github.com/tejpalvirk/contextmanager | 跨 session 知識圖 |

## 本專案採用策略

1. **必備（已落地）**：`docs/TODO.md` + `.cursor/rules/mhf-l10n.mdc`（alwaysApply）
2. **可選下一步**：若跨很多 session 仍漏狀態，再裝 **Todokit** 或 **Anchor**，並規定 MCP 狀態變更後必須同步改 `docs/TODO.md`
3. **暫不優先**：GitHub Projects MCP（私服本地工程，Issue 板非必要）
