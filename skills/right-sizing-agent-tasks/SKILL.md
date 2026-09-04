---
name: right-sizing-agent-tasks
description: Use when preparing or revising a broad, repetitive, or multi-phase task before execution, especially when context, tokens, agent calls, file reads, or validation effort appear disproportionate to one verified outcome.
---

# Right-Sizing Agent Tasks

## Core Principle

最佳化 **minimum total inference cost per verified outcome**，不是單純縮短 prompt。這是 task-preparation Skill，不是每次執行都必須載入的 execution policy。不得縮減使用者授權、security boundary、ownership、rollback、evidence 或 acceptance criteria。

## Transform the Task

先把每個要求分類：

| Class | Action |
|---|---|
| `KEEP` | 完成 outcome 或安全驗收不可缺少 |
| `REFERENCE` | 已由適用的 Skill、AGENTS、Task Contract 或正式規格管理；只引用 authority |
| `CONDITIONAL` | 只有可觀察 trigger 成立才執行 |
| `DEFER` | 有價值但不是本次 verified outcome 所需 |
| `DELETE` | 重複背景、無 action、無 acceptance impact |

接著重寫為 **TASK-LITE**，固定五段：

1. **Outcome** — 一個 terminal outcome；不可暗中改寫使用者目標。
2. **Scope** — exact repo／targets、in-scope、out-of-scope、stop triggers。
3. **Method** — 最小 read set、最小 mutation、必要 preflight；通用政策只引用，不複製全文。
4. **Acceptance** — affected tests、最接近的 regression guard、diff hygiene、明確 PASS／BLOCK 條件。
5. **Report** — status、changes、verification、deferred／blockers；不得重述 prompt。

## Keep One Task or Split

**Keep one task**：共用 repo state、preflight、root-cause evidence 或 integration decision；拆分會重複讀檔與推理。

**Split**：outcomes 可獨立驗證、authority／workspace 分離、互不依賴，且拆分不會複製大量 context。

不要只為讓 prompt 看起來較短而拆 session。

## Execution Budget

- Lead-only by default。
- 只在 bounded、低 ambiguity、最小 context、可獨立驗證且 ROI 明顯為正時 delegate。
- Architecture、cross-file integration、security judgment、dirty-change ownership 與 final acceptance 留給 Lead。
- Full suite、廣泛 inventory、完整 runtime matrix 預設為 conditional；只有 changed surface、風險或 acceptance 需要時執行。
- Token／model／reasoning usage 不可觀察時寫 `not observable`，不得猜測節省量。
- TASK-LITE 產生後，不要把本 Skill 列為 executor dependency；只有 scope trigger 成立、必須重新縮編時才重新載入。

## Non-Negotiable Boundaries

不得用 task reduction：

- 移除安全、權限、證據、rollback 或 destructive-operation gates；
- 將 failure 降級、把 `NOT VERIFIED` 推論為 PASS；
- 把必要修復轉成 follow-up；
- 以低價 subagents 取代需要完整 context 的整合判斷；
- 擴張成順手重構、migration 或全域治理專案。

## Project Relationships

本 Skill 是 task-preparation policy，不是 Lead Agent runtime component。當它與 Lead Agent Control Plane 搭配時，先用本 Skill 產生或修訂 TASK-LITE，再由專案自己的 intake、authority、routing 與 acceptance contracts 執行；專案規則仍是執行期 authority。

如需維護、整合或審查這項關係，讀取 [references/project-relationships.md](references/project-relationships.md)。如需 behavioral pressure testing，讀取 [references/pressure-tests.md](references/pressure-tests.md)。

## Common Mistakes

- 為縮短文字而拆 session，卻重複 preflight、讀檔與 root-cause reasoning。
- 只刪 prompt 句子，沒有縮小 read／mutation／validation surface。
- 把通用政策全文搬進每個任務，而不是引用 authority。
- 因 full suite「比較安心」而無條件執行 unrelated validation。

## Required Output

```text
DECISION: KEEP_SINGLE | SPLIT | BLOCK
TASK-LITE: <ready-to-run prompt>
PRESERVED: <non-negotiable requirements>
DEFERRED: <items>
REENTRY TRIGGERS: <observable conditions that require re-scoping>
SAVINGS PROXIES: <removed duplication, bounded reads/tests/agent calls>
```

只有實際量測時才能宣稱 token savings；否則只報告 proxies。
