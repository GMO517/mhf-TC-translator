# AOCI-CODE（本專案用法）

> 用途：給 Agent 一份**可 git 版控**的倉庫認知索引，減少每輪重讀腳本／管線。  
> 正式規範以 `AGENTS.md` 的 AOCI 區塊與 MCP 工具為準。

## 為什麼加

本倉庫翻譯規則／腳本／CSV 路徑多。AOCI 把「工程檔職責」收成高密度索引，適合：

- 改 `l10n/working/*.py`、writeback／validate 管線
- 新開對話時快速接上「怎麼跑、哪裡是真相」
- **不是**用來取代 `terms.csv`／子類 review 的譯文審核

## 本機路徑

| 項 | 路徑 |
|---|---|
| CLI | `tools/aoci/aoci.exe` |
| Cursor MCP | `.cursor/mcp.json` → server `aoci` |
| 索引骨架 | `aoci.txt`／`aoci.meta.txt`／`aoci.code.txt` |
| 治理／基線 | `.aoci/config.json`、`.aoci/baseline.json` |

## Agent 最短用法

1. **重啟 Cursor**（讓 MCP 載入 `aoci`）
2. 工程任務開場：先 `aoci_rules`，需要全貌時再 `aoci_overview`
3. 改完受管檔且穩定後：呼叫一次 `aoci_maintain`（不必每次小改都叫）
4. 純翻譯 CSV／review 填表：可不走 AOCI

## 人工 CLI

```powershell
# 狀態
.\tools\aoci\aoci.exe --repo E:\MHF status

# 重扫基線（檔案集合大變時）
.\tools\aoci\aoci.exe --repo E:\MHF scan

# 本機面板（可選）
.\tools\aoci\aoci.exe --repo E:\MHF ui --detach --json
```

## 注意

- 本體 `client/MHFCT4.1/`、bin、備份已由 production scope／gitignore 排除，勿硬塞進索引。
- 首次完整索引需 Agent 依 Guide 分批寫 Entry（骨架＋scan 已就緒；Entries 尚未填滿屬正常）。
- 下載快取在 `tools/aoci-code/`（不上庫）；執行檔以 `tools/aoci/aoci.exe` 為準。
