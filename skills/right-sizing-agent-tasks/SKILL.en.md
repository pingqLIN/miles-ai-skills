---
name: right-sizing-agent-tasks
description: Use when preparing or revising a broad, repetitive, or multi-phase task before execution, especially when context, tokens, agent calls, file reads, or validation effort appear disproportionate to one verified outcome.
---

# Right-Sizing Agent Tasks

## Core Principle

Optimize for **minimum total inference cost per verified outcome**, not merely for a shorter prompt. This is a task-preparation Skill, not an execution policy that must be loaded for every run. Never reduce user authorization, security boundaries, ownership controls, rollback requirements, evidence requirements, or acceptance criteria.

## Transform the Task

Classify each requirement first:

| Class | Action |
|---|---|
| `KEEP` | Required to achieve the outcome or verify it safely |
| `REFERENCE` | Already governed by an applicable Skill, `AGENTS.md`, Task Contract, or formal specification; reference the authority instead of copying it |
| `CONDITIONAL` | Execute only when an observable trigger is satisfied |
| `DEFER` | Valuable, but not required for the current verified outcome |
| `DELETE` | Duplicate background, no action, and no acceptance impact |

Then rewrite the request as **TASK-LITE** with exactly five sections:

1. **Outcome** — One terminal outcome; do not silently reinterpret the user's goal.
2. **Scope** — Exact repository/targets, in-scope items, out-of-scope items, and stop triggers.
3. **Method** — Minimum read set, minimum mutation, and necessary preflight; reference general policy instead of copying it in full.
4. **Acceptance** — Affected tests, the nearest regression guard, diff hygiene, and explicit PASS/BLOCK conditions.
5. **Report** — Status, changes, verification, deferred items, and blockers; do not restate the prompt.

## Keep One Task or Split

**Keep one task** when work shares repository state, preflight, root-cause evidence, or an integration decision and splitting would duplicate file reads or reasoning.

**Split** when outcomes can be verified independently, authority or workspace is separate, there is no execution dependency, and splitting does not duplicate substantial context.

Do not split sessions merely to make the prompt look shorter.

## Execution Budget

- Use Lead-only execution by default.
- Delegate only when the work is bounded, low-ambiguity, requires minimal context, can be independently verified, and has clearly positive ROI.
- Keep architecture, cross-file integration, security judgment, dirty-change ownership, and final acceptance with the Lead.
- Treat a full test suite, broad inventory, or complete runtime matrix as conditional by default; run it only when the changed surface, risk, or acceptance criteria require it.
- If token, model, or reasoning usage is not observable, report `not observable`; do not invent savings.
- After TASK-LITE is sufficient, do not list this Skill as an executor dependency. Reload it only when a scope trigger requires re-scoping.

## Non-Negotiable Boundaries

Task reduction must never:

- Remove safety, authorization, evidence, rollback, or destructive-operation gates.
- Downgrade a failure or infer PASS from `NOT VERIFIED`.
- Move a required repair into a follow-up item.
- Replace integration judgment that requires full context with lower-cost subagents.
- Expand the task into opportunistic refactoring, migration, or repository-wide governance work.

## Project Relationships

This Skill is a task-preparation policy, not a Lead Agent runtime component. When used with Lead Agent Control Plane, use this Skill first to produce or revise TASK-LITE; then let the project's own intake, authority, routing, and acceptance contracts control execution. Project rules remain the execution-time authority.

For maintenance, integration, or review of this boundary, read [references/project-relationships.md](references/project-relationships.md). For behavioral pressure testing, read [references/pressure-tests.md](references/pressure-tests.md).

## Common Mistakes

- Splitting sessions to shorten text while duplicating preflight, file reads, and root-cause reasoning.
- Deleting prompt text without reducing the actual read, mutation, or validation surface.
- Copying general policy into every task instead of referencing the governing authority.
- Running unrelated full-suite validation unconditionally because it feels safer.

## Required Output

```text
DECISION: KEEP_SINGLE | SPLIT | BLOCK
TASK-LITE: <ready-to-run prompt>
PRESERVED: <non-negotiable requirements>
DEFERRED: <items>
REENTRY TRIGGERS: <observable conditions that require re-scoping>
SAVINGS PROXIES: <removed duplication, bounded reads/tests/agent calls>
```

Claim token savings only when they were actually measured. Otherwise, report only observable proxies.