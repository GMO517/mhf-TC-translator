# MHF 繁中翻譯（私服客戶端）

Monster Hunter Frontier 用戶端文字繁中化工程。遊戲本體不上庫。  
預設分支：`main`。

## 目錄

```text
.
├── client/                 # 本體父層
│   └── MHFCT4.1/           # 本體（gitignore，需自行放置）
├── l10n/                   # 抽出物、詞語庫、翻譯工作區
├── tools/                  # FrontierTextHandler / ReFrontier（本機 clone）
├── docs/
│   ├── TODO.md             # 代辦 Source of Truth
│   └── STYLE.md            # 風格規範
└── _backup/                # 本機備份（gitignore）
```

## 開始前

1. 閱讀 `docs/TODO.md`、`docs/STYLE.md`
2. 確認本體在 `client/MHFCT4.1/`
3. 翻譯流程：`docs/agent-translation-playbook.md` → `docs/plans/l10n-orchestration.md`

## 工具

- [FrontierTextHandler](https://github.com/Houmgaor/FrontierTextHandler)
- [ReFrontier](https://github.com/mhvuze/ReFrontier)
