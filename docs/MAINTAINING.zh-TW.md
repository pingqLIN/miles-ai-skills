# Miles AI Skills 維護說明

> 本文件供 repository maintainer 作業使用，不是公開 Skill 檢索入口。檔案仍儲存於公開 repository，不得紀錄憑證、私密計畫、machine-only evidence 或其他敏感資料。

## 資料邊界

- 每個 Skill 只能有一個 authoritative upstream。
- 本 repository 儲存可攜式的發布 package，不收錄 runtime projection wrapper、cache 或特定機器證據。
- `README.md` 與 `README.zh-TW.md` 主要服務外部使用者檢索、比較與選用 Skill；維護流程留在本文件。

## 新增或同步 Skill

1. 確認 authoritative upstream，複製前檢查 license、provenance 與敏感內容。
2. 將完整、可攜式的 package 複製到 `skills/<skill-id>/`，排除 runtime-only 與 machine-only 內容。
3. 在 `registry/index.yaml` 新增或更新唯一條目，包含 version、status、license、path、`canonical_locale`、`localized_files` 與重要 relationships。
4. 可用性、行為、provenance 或 license 變更時，同步更新兩份 README 與 `THIRD_PARTY_NOTICES.md`。
5. 執行 repository validator 與 Skill validator，審查限定範圍的 diff，再透過 pull request 發布本次 package 與 metadata。

## 狀態判定

將下列狀態分開記錄，不得互相代替：

- `SOURCE_PRESENT`：authoritative source 存在且已檢視。
- `PUBLISHED`：可攜式 package 已進入 repository 目標分支。
- `INSTALLED`：檔案已放入目標 runtime 的 Skill 位置。
- `LOADED`：runtime 已實際載入該 Skill。
- `RUNTIME_ACCEPTED`：新 session 或真實任務已驗證路由與行為。

Git push、PR merge 或檔案安裝只能證明對應狀態，不能單獨證明 runtime acceptance。
