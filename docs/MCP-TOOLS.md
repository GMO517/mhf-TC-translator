# MCP 方針（子規範）

> **父規範**：`docs/agent-translation-playbook.md`。  
> **主流程**：`docs/plans/l10n-orchestration.md`。本檔只管 MCP；**日常翻譯禁止**為 feedback／確認而停主線。

## 結論

**不要再裝待辦／記憶類 MCP**（Todokit、Taskmaster、Anchor、MegaMemory 等）。  
進度只寫：`progress.md`（分類）＋`TODO.md`（工程 Gate）。禁止第三進度源。

## 已有 MCP

| MCP | 用途 | 邊界 |
|-----|------|------|
| `interactive_feedback` | **僅**真正閘門：大改規則、本體方針衝突、使用者明示要審 | **日常翻譯推進不必呼叫**；MCP 不可用時直接依父規範續做 |
| `context7` | 函式庫文件（本專案幾乎用不到） | 勿為查 FTH／MHF 硬繞 |
| Cursor `TodoWrite` | 單 session 輔助勾選 | 跨 session 以 `TODO.md`／`progress.md` 為準 |

## 禁止

- 為「不忘代辦」再裝第二套 todo／memory MCP  
- 同一進度寫 MCP JSON + Markdown 卻不同步  
- 用 feedback／確認輪詢取代 PHASE3 的「不必每步問下一步」
