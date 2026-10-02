---
name: maintain-project-updates
description: Govern a software project's current progress through evidence-backed shallow or deep analysis, identify its execution stage and next implementable step, and maintain status, roadmap, changelog, or release-readiness notes when authorized. Use for project maintain or project progress checks, development status reports, execution-stage or implementation-readiness checks, requests to resume unfinished development toward a usable application, cross-module or cross-worktree progress reviews, roadmap and release readiness, next-action advice, documentation drift checks, and project update maintenance. For deciding whether a proposed change belongs on the current path, an isolated branch/worktree, a new project, research, or deferral, use advise-project-direction instead.
metadata:
  runtime_support_files: true
---

# Maintain Project Updates

## Operating Contract

Use one skill with two analysis depths and one shared Evidence Kernel.

- `shallow`: complete a local, bounded, short-horizon progress review as the calling agent. Do not delegate or spawn subagents.
- `deep`: act as the Project Progress Steward for cross-boundary or medium-horizon analysis. Use additional tools or bounded subagents only when justified.
- Keep analysis depth independent from authority. Deep analysis never grants permission to edit, stage, commit, merge, push, release, deploy, access credentials, or publish.
- Keep analysis, presentation, and update execution separate. Produce a read-only assessment unless the request separately authorizes file updates.
- Do not use this skill as automated release, merge, push, or deployment machinery or as a general-purpose product manager.

## Paired Skill Routing

This skill is paired with `$advise-project-direction` so project evaluation requests can be redirected without merging their responsibilities. If the request is primarily to decide whether a proposed change should stay on the current path, use an isolated branch/worktree, become a new project, require research, or defer before implementation—not to establish the project's current progress—stop this route and recommend `$advise-project-direction`. Carry forward any verified progress evidence already gathered, but let that skill own the project-boundary classification and continuation route.

## Execution-Stage Trigger

When the user asks to confirm the execution stage, continue unfinished development, or reach a usable application, treat that as an execution-seeking request rather than ending with a status report. Establish the current verified stage, the nearest usable outcome, the next bounded implementation step, and its acceptance check. Distinguish local implementation, provider or runtime execution, and release or deployment; evidence for one does not establish another.

If the user has authorized that bounded step and its applicable gates pass, continue the work through the appropriate engineering workflow. If a material product choice or gated action remains, finish the reviewable local preparation first, then prompt for the exact missing decision or approval. State what can proceed now and what remains blocked. A progress check alone never grants execution authority.

## Route The Depth

Default to `shallow` when the question is limited to one repository or worktree, a small task or procedure, a local status check, or a near-term next step that the calling agent can verify directly.

Choose `deep` when the user explicitly requests it or when the assessment materially spans any of these boundaries:

- multiple modules, repositories, branches, or worktrees
- roadmap, release, architecture, or medium-term progress planning
- conflicting sources of truth that cannot be reconciled locally
- several independent verification domains that benefit from bounded parallel inspection
- blockers or risks whose impact crosses ownership, delivery, or governance boundaries

Announce the selected depth and the evidence boundary in one sentence. Do not interpret an elaborate output format alone as a reason to choose Deep.

## Run The Shared Evidence Kernel

Run the same kernel before either workflow:

1. Lock the repository, branch/worktree, instruction scope, time horizon, and requested mutation boundary.
2. Run `scripts/audit_project_progress.py` for a local project when feasible.
3. Inspect the highest-signal files and execution results directly.
4. Compare code, Git history and worktree state, tests/build/runtime signals, project docs, update files, and the user's stated goal.
5. Classify material claims as `VERIFIED`, `INFERRED`, or `UNKNOWN`.
6. Identify progress, drift, blockers, risks, and evidence-backed next actions.

Read [references/evidence-kernel.md](references/evidence-kernel.md) for evidence ordering, source comparison, and claim standards. Treat the audit script as a starting map, never as the final analysis.

## Execute The Selected Workflow

### Shallow

Read [references/shallow-workflow.md](references/shallow-workflow.md). Complete the analysis yourself as the calling agent. You may use appropriate local tools, but you must not delegate, spawn subagents, or invoke agent-based review from the Shallow route.

If Shallow evidence crosses a Deep boundary, stop expanding the Shallow analysis, state the promotion trigger, and promote the analysis to Deep only when the request and runtime permit. Promotion changes depth, not authority. Never delegate first and label the route Deep afterward.

### Deep

Read [references/deep-steward-workflow.md](references/deep-steward-workflow.md). The main Project Progress Steward owns scope, evidence reconciliation, risk decisions, recommendations, and final synthesis.

Tool or subagent orchestration is conditional, not mandatory. Delegate only when the work is independently verifiable, bounded, non-overlapping, and worth the coordination cost. Record the reason and ownership for each delegation, validate returned evidence, and keep final synthesis with the main agent.

## Apply The Mutation Boundary

Do not infer write authority from either depth.

- For read-only progress or recommendation requests, report findings or an exact update proposal without editing files.
- For authorized update maintenance, run the Git pre-edit gate and follow [references/update-files.md](references/update-files.md).
- Keep public release notes separate from private plans, timelines, research, and implementation priorities.
- Do not stage, commit, merge, push, release, deploy, publish, rewrite history, delete, or access credentials unless the user separately authorizes that exact action and applicable governance gates pass.

After any authorized update, run the smallest high-signal verification and report changed files, preserved pre-existing work, uncommitted state, rollback path, and residual risk.

## Report The Result

Adapt the presentation to the request rather than forcing a universal report schema. Always make these points recoverable:

- selected depth and inspected scope
- evidence-backed current state and progress
- drift, blockers, risks, and unknowns
- prioritized next actions
- the current execution stage, nearest usable outcome, and next acceptance check when execution continuation was requested
- update proposal or executed changes, when applicable
- verification performed and remaining limitations

Lead with the project state and the most useful next move. Do not present plans, stale TODO text, or unexecuted checks as verified progress.
