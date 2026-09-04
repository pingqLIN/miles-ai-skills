# Miles AI Skills Registry

個人 Agent Skills Registry 與 canonical skill definitions。

目前以小型、可攜、可驗證的 Skill 定義為主；Runtime routing、模型選擇與其他執行環境政策不放入 Skill 本體。

## Available Skills

| Skill | Category | Status |
|---|---|---|
| JING JING Clarifier | 繁體中文文本修訂 | Stable |
| Right-Sizing Agent Tasks | Agent 治理／任務縮編 | Stable |

## Project Relationships

`right-sizing-agent-tasks` 是 `lead-agent-control-plane` 的前置 task-preparation policy：Skill 負責將寬廣或重複的需求整理成 TASK-LITE；Lead Agent 專案負責 execution-time intake、authority、routing、evidence 與 final acceptance。兩者相容但不互相取代，也不把 Skill 安裝狀態視為專案 runtime acceptance。

## Repository Structure

```text
miles-ai-skills/
├── .github/workflows/       # CI validation workflows
├── registry/
│   └── index.yaml           # Canonical Skills registry index
├── scripts/
│   └── validate-registry.py # Repository integrity validator
├── skills/
│   ├── jing-jing-clarifier/
│   │   └── SKILL.md         # Canonical skill definition (v1.1.0)
│   └── right-sizing-agent-tasks/
│       ├── SKILL.md
│       └── references/      # Pressure tests and project relationship record
├── THIRD_PARTY_NOTICES.md   # Attribution and upstream provenance tracking
└── README.md
```

## Validation

本 repository 採雙層驗證：

1. **Repository Integrity**：`scripts/validate-registry.py` 檢查 `registry/index.yaml`、Skill 目錄與 `SKILL.md` frontmatter 是否一致。
2. **Specification Conformance**：CI 使用固定 commit 的 Agent Skills `skills-ref` reference implementation 執行 `skills-ref validate`。`skills-ref` 僅作規格相容性參考，不是本 repository 唯一的 production validator。

## License and provenance

`JING JING Clarifier` 的已知來源包含 `pingqLIN/UniText`；其目前 repository `LICENSE` 為 MIT License。衍生來源與 attribution 細節記錄於 `THIRD_PARTY_NOTICES.md`。
