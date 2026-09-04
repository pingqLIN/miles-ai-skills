# Project Relationships

## Canonical Skill and projections

- Canonical distributable package: `pingqLIN/miles-ai-skills`, path `skills/right-sizing-agent-tasks`.
- Installed Codex projection: `$CODEX_HOME/skills/right-sizing-agent-tasks`.
- Historical authoring package: local `browser-governance-task-right-sizing/right-sizing-agent-tasks`; retained as provenance, not runtime authority.

The canonical package is the maintained source for installation. An installed copy proves filesystem installation only; active discovery or invocation needs separate runtime evidence.

## Lead Agent Control Plane

Related project: `lead-agent-control-plane`.

Relationship:

1. `right-sizing-agent-tasks` prepares or revises a broad request into a bounded TASK-LITE before execution.
2. Lead Agent Control Plane owns execution-time intake, Lead binding, authority checks, workspace preflight, routing, evidence review, and terminal acceptance.
3. The Skill may recommend `KEEP_SINGLE`, `SPLIT`, or `BLOCK`, but it does not dispatch Workers, mutate project runtime state, or establish project completion.
4. The project may implement compatible right-sizing rules directly. Those project rules remain authoritative inside that repository and do not make this Skill a runtime dependency.

## Integration boundary

Use the Skill when task scope is broad, repetitive, multi-phase, or disproportionately expensive. Do not reload it after a sufficient TASK-LITE exists unless an observable re-entry trigger requires re-scoping.

When either side changes, review the shared boundary: single terminal outcome, authority/workspace separation, delegation ROI, acceptance ownership, and the distinction between package installation and active runtime invocation.
