# Miles AI Skills Registry

Miles / `pingqLIN` 維護的小型、可攜、可驗證 AI Agent Skills 集合。

本 repository 將 **canonical Skill 定義** 與 runtime-specific routing、模型選擇及執行政策分離。每個 Skill 都應能作為範圍明確、可審查的行為模組，而不是不透明的 Agent 設定集合。

> English: [README.md](README.md)

## Skills

| Skill | 用途 | 版本 | 狀態 | 語言檔案 |
|---|---|---:|---|---|
| [JING JING Clarifier](skills/jing-jing-clarifier/SKILL.md) | 修訂繁體中文文本、減少不必要的中英混寫，並保護技術精準字串。 | 1.1.0 | Stable | [繁中](skills/jing-jing-clarifier/SKILL.md) · [English](skills/jing-jing-clarifier/SKILL.en.md) |
| [Right-Sizing Agent Tasks](skills/right-sizing-agent-tasks/SKILL.md) | 將寬廣或重複任務整理成 bounded TASK-LITE，同時保留安全、authority、evidence 與 acceptance gates。 | 1.0.0 | Stable | [繁中](skills/right-sizing-agent-tasks/SKILL.md) · [English](skills/right-sizing-agent-tasks/SKILL.en.md) |
| [Advise Project Direction](skills/advise-project-direction/SKILL.md) | 在實作前判定提案的專案邊界與執行方向。 | 1.0.0 | Stable | [English](skills/advise-project-direction/SKILL.md) |
| [Maintain Project Updates](skills/maintain-project-updates/SKILL.md) | 建立專案當前進度、執行就緒度與下一個有證據支持的步驟。 | 1.0.0 | Stable | [English](skills/maintain-project-updates/SKILL.md) |

Registry metadata 維護於 [`registry/index.yaml`](registry/index.yaml)。

## 語言與版本政策

- `SKILL.md` 是 canonical package entrypoint；其語系由 registry 的 `canonical_locale` 宣告，不由檔名推定。
- 其他語系的語意對等 companion 使用 `SKILL.en.md` 等 locale suffix，並全數列於 `localized_files`。
- 翻譯必須維持原有行為、安全邊界、protected literals、required output contract 與 acceptance semantics。
- 僅同步語言版本不代表新的行為版本。若 Skill 行為有變更，應更新 [`registry/index.yaml`](registry/index.yaml) 中的 Skill version，並同步所有已宣告的語言檔案。

## Repository Structure

```text
miles-ai-skills/
├── .github/workflows/       # CI validation workflows
├── registry/
│   └── index.yaml           # Canonical registry metadata 與語言 mapping
├── scripts/
│   └── validate-registry.py # Repository integrity validator
├── skills/
│   └── <skill-id>/
│       ├── SKILL.md         # Canonical package entrypoint
│       ├── agents/          # Optional UI metadata 與 invocation policy
│       ├── references/      # Optional supporting instructions
│       └── scripts/         # Optional deterministic helpers
├── THIRD_PARTY_NOTICES.md   # Attribution 與 provenance notes
├── README.zh-TW.md          # 繁體中文 repository landing page
└── README.md                # 英文 repository landing page
```

## Validation

本 repository 採兩層驗證：

1. **Repository integrity** — `scripts/validate-registry.py` 檢查 `registry/index.yaml`、Skill 目錄與 canonical `SKILL.md` frontmatter 是否一致。
2. **Specification conformance** — CI 使用固定版本的 Agent Skills `skills-ref` reference implementation 執行 `skills-ref validate`。該 reference implementation 是規格相容性檢查，不是本 repository 唯一的 production validator。

本機 integrity check：

```bash
python scripts/validate-registry.py
```

Integrity check 通過只代表 registry 結構與 canonical frontmatter 一致；**不代表**特定 runtime 已發現、載入、呼叫或驗收該 Skill。

## 新增或同步 Skill

1. 先確認唯一 authoritative upstream，複製前檢查 license、provenance，以及是否含有私密或僅適用單機的內容。
2. 將完整、可攜式的 package 複製到 `skills/<skill-id>/`；排除 runtime projection wrapper、憑證、私密計畫、cache 與 machine-only evidence。
3. 在 `registry/index.yaml` 新增或更新唯一條目，包含 version、status、license、path、`canonical_locale`、`localized_files` 與重要 relationships。
4. 可用性、行為、provenance 或 license 變更時，同步更新兩份 README 與 `THIRD_PARTY_NOTICES.md`。
5. 執行 repository validator 與 Skill validator，審查限定範圍的 diff，再只 commit 與 push 本次 package 與 metadata。

將 source presence、publication、installation、loading 與 runtime acceptance 視為不同狀態。Git repository push 成功只證明已發布。

## 與 Runtime Systems 的責任邊界

本 repository 內的 Skill 定義 reusable behavior 與 task policy。模型 routing、executor selection、實際安裝／啟用狀態與 project-level authority 等 runtime-specific concerns，除非 Skill 明確定義，否則由 consuming runtime 或專案負責。

例如 `right-sizing-agent-tasks` 可在執行前產生 bounded TASK-LITE；相關的 `lead-agent-control-plane` 專案仍負責 execution-time intake、authority、routing、evidence review 與 final acceptance。

`advise-project-direction` 與 `maintain-project-updates` 是一組雙向路由，不是合併後的單一工作流。前者負責實作前的專案邊界決策；後者負責當前狀態、執行就緒度與專案更新維護。兩者可將誤路由的請求導向對方，但不會自動呼叫對方或擴張修改權限。

## License and provenance

本 repository 目前**沒有宣告單一 repository-wide license**。各 Skill 的 license 與 provenance 分別記錄於 [`registry/index.yaml`](registry/index.yaml) 與 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。

Registry 與 provenance notes 記錄目前各 Skill 的 license 狀態及 upstream attribution。部分 Skill 仍明確標記為 `unknown`；重用或重新散布前應以這兩份來源檔案為準。

不得由單一 Skill 的 license 推論整個 repository 的授權條款。
