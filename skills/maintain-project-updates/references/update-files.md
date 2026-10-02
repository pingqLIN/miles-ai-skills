# Project Update Executor

Use this reference only after Shallow or Deep analysis has produced an evidence-backed result and the request separately authorizes update execution. Analysis depth does not authorize file mutation.

## Executor Boundary

Before editing:

1. Confirm the exact update target and whether it is public, publishable, private, or local-only.
2. Run the repository Git pre-edit gate and preserve pre-existing user work.
3. Confirm that editing is inside the requested scope. For a read-only request, provide an exact proposal instead.
4. Keep staging, committing, merging, pushing, releasing, deploying, and publishing outside this executor unless separately authorized.
5. Plan the smallest verification and a rollback path.

## File Selection

Use the most specific existing convention first:

- Release history: `CHANGELOG.md`, `RELEASE_NOTES.md`
- Current engineering status: `STATUS.md`, `PROJECT_STATUS.md`, `docs/status.md`
- Planning or roadmap: `ROADMAP.md`, `docs/roadmap.md`
- Decisions: `docs/adr/`, `DECISIONS.md`, `docs/decisions.md`
- Local/private operational notes: `.project-updates/status.md`

If no convention exists and the content includes private planning, timelines, internal research, or implementation priorities, prefer `.project-updates/status.md` and add `.project-updates/` to `.git/info/exclude`.

Use a tracked publishable file only when the user explicitly wants a public project update or the repository already treats that file as public-facing.

## Suggested Status Entry

```markdown
## YYYY-MM-DD

### Snapshot
- Branch:
- Worktree:
- Verification:

### Progress
- Completed:
- In progress:
- Not started:

### Risks And Blockers
-

### Recommended Next Actions
1.
2.
3.

### Evidence
-
```

Adapt this shape to the existing project convention. Do not force it when another authoritative format exists.

## Maintenance Rules

- Preserve existing headings and chronology.
- Add a new dated entry instead of rewriting old history unless correcting stale or false information.
- Keep recommendations tied to evidence.
- Separate public release notes from private implementation plans.
- Update the authoritative file first, then any required Traditional Chinese companion.
- Do not turn an `INFERRED` or `UNKNOWN` conclusion into a completed-status claim.

## Verification And Report

Run the smallest high-signal check for the edited format and affected workflow. Report:

- files changed
- the state the update now represents
- pre-existing changes preserved
- verification performed
- uncommitted state and rollback path
- residual risks or follow-up checkpoints
