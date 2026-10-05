# 防具翻譯待裁定（主線不停；最後一併處理）

> 產生：2026-10-04 自動化主流程  
> 規則：疑問不中斷套用／QA；僅記錄於此。

## 方針衝突／待確認

| ID | 主題 | 現況處置 | 待裁定 |
|---|---|---|---|
| Q-01 | 字庫無「卡」 | 專名改可／伽等可顯示字 | 是否補字庫「卡」 |
| Q-02 | Gate4 TODO 條目含任務／劇情 | 本輪先清防具五部位至可回寫 | 是否立刻開任務說明 |
| Q-03 | QA `truncate` 對合法短系列名（輝／翼／灰／蝶兜／龍皮）亦標 | 2026-10-05 triage：121 筆多為誤報；真截斷已修 | 是否放寬腳本閾值 |
| Q-04 | 高頻 ZP 專名短音譯（Charis／Miriam…） | 已依片假名對照短音譯入典 | 人審抽樣是否改義譯 |
| Q-05 | `風`（Wind）與鋼龍裝混用 | 字典有 wind＝風、kushala＝鋼龍；複合「Kushala バダル」未整段命中則保留舊譯 | 複合日英混名規則 |

## 回寫前檢查清單（自動填）

- [x] Gate0 round-trip（既有 PASS，見 TODO）
- [x] Gate0.5 charset／fallback
- [x] `_backup/20261004-armor/mhfdat.bin` 存在
- [~] blocking／high：2026-10-05 QA 後 truncate 121／need_semantic 196／long_phon 1（見 `qa-armors.md`；未清零）
- [x] 詞庫優先：`terms_lookup`→series-dict→套用

## 追加疑問

| ID | 主題 | 現況處置 |
|---|---|---|
| Q-06 | QA 未清零即 Gate4 回寫 | 依使用者口令推進；殘項留本檔＋qa-transliteration |
| Q-07 | need_semantic 高計數 | 2026-10-05 已由 1242→196；殘色尾／Star／True 見 ISSUE-002 |

## 備註

主流程日誌見 `l10n/working/logs/`；全量 QA 見 `qa-transliteration.md`。
