# Miles AI Skills Registry

Miles / `pingqLIN` 維護的小型、可攜、可驗證 AI Agent Skills 集合。

本 repository 將 **canonical Skill 定義** 與 runtime-specific routing、模型選擇及執行政策分離。每個 Skill 都應能作為範圍明確、可審查的行為模組，而不是不透明的 Agent 設定集合。

> English: [README.md](README.md)

## Skills

| Skill | 用途 | 版本 | 狀態 | 語言檔案 |
|---|---|---:|---|---|
| [JING JING Clarifier](skills/jing-jing-clarifier/SKILL.md) | 修訂繁體中文文本、減少不必要的中英混寫，並保護技術精準字串。 | 1.1.0 | Stable | [繁中](skills/jing-jing-clarifier/SKILL.md) · [English](skills/jing-jing-clarifier/SKILL.en.md) |
| [Right-Sizing Agent Tasks](skills/right-sizing-agent-tasks/SKILL.md) | 將寬廣或重複任務整理成 bounded TASK-LITE，同時保留安全、authority、evidence 與 acceptance gates。 | 1.0.0 | Stable | [繁中](skills/right-sizing-agent-tasks/SKILL.md) · [English](skills/right-sizing-agent-tasks/SKILL.en.md) |

Registry metadata 維護於 [`registry/index.yaml`](registry/index.yaml)。

## 語言與版本政策

- `SKILL.md` 保持為目前 registry 所記錄的 Skill 版本的 canonical 繁體中文定義。
- `SKILL.en.md` 為相同 Skill 版本的英文語意對等 companion。
- 翻譯必須維持原有行為、安全邊界、protected literals、required output contract 與 acceptance semantics。
- 僅同步語言版本不代表新的行為版本。若 Skill 行為有變更，應更新 [`registry/index.yaml`](registry/index.yaml) 中的 Skill version，並同步兩種語言檔案。

## Repository Structure

```text
miles-ai-skills/
├── .github/workflows/       # CI validation workflows
├── registry/
│   └── index.yaml           # Canonical registry metadata 與語言 mapping
├── scripts/
│   └── validate-registry.py # Repository integrity validator
├── skills/
│   ├── jing-jing-clarifier/
│   │   ├── SKILL.md         # Canonical 繁體中文定義
│   │   └── SKILL.en.md      # 英文語意對等 companion
│   └── right-sizing-agent-tasks/
│       ├── SKILL.md         # Canonical 繁體中文定義
│       ├── SKILL.en.md      # 英文語意對等 companion
│       └── references/      # Supporting evidence 與 pressure tests
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

## 與 Runtime Systems 的責任邊界

本 repository 內的 Skill 定義 reusable behavior 與 task policy。模型 routing、executor selection、實際安裝／啟用狀態與 project-level authority 等 runtime-specific concerns，除非 Skill 明確定義，否則由 consuming runtime 或專案負責。

例如 `right-sizing-agent-tasks` 可在執行前產生 bounded TASK-LITE；相關的 `lead-agent-control-plane` 專案仍負責 execution-time intake、authority、routing、evidence review 與 final acceptance。

## License and provenance

本 repository 目前**沒有宣告單一 repository-wide license**。各 Skill 的 license 與 provenance 分別記錄於 [`registry/index.yaml`](registry/index.yaml) 與 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。

Registry 與 provenance notes 記錄目前各 Skill 的 license 狀態及 upstream attribution。其中一項 Skill 已有可識別的 upstream license，另一項則明確標記為 `unknown`；重用或重新散布前應以這兩份來源檔案為準。

不得由單一 Skill 的 license 推論整個 repository 的授權條款。