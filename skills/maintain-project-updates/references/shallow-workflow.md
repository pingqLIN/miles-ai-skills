# Shallow Progress Workflow

Use Shallow for bounded, local, short-horizon progress questions that the calling agent can verify directly.

## Hard Boundary

Complete Shallow as the calling agent.

- Do not delegate.
- Do not spawn subagents.
- Do not invoke agent-based reviewers or parallel agent work.
- Do not use an output format, task size label, or desire for speed to bypass this boundary.

Local read-only tools, repository commands, and directly available project checks remain allowed when they fit the request and governance rules.

## Workflow

1. State `Depth: Shallow` and lock one clear repository/worktree and near-term question.
2. Run the shared Evidence Kernel in [evidence-kernel.md](evidence-kernel.md).
3. Inspect the smallest set of direct artifacts needed to resolve the question.
4. Reconcile local code, Git, verification, and update-document evidence.
5. Report the current state, important drift or risk, and a short ordered set of next actions.
6. If update execution is authorized, hand the analysis to the separate update executor in [update-files.md](update-files.md).

## Promotion Boundary

Promote to Deep when the evidence reveals:

- a material dependency on another module, repository, branch, or worktree
- roadmap, release, architecture, or medium-term planning implications
- conflicting canonical and projection states that require wider reconciliation
- multiple independent verification domains that cannot be handled safely as one local pass
- blockers or risks that cross ownership or governance boundaries

Stop the Shallow expansion before delegation. State the trigger and the new evidence boundary. Continue as Deep only when the request and runtime permit; otherwise report the promotion recommendation and the unresolved scope.

Promotion does not grant edit, merge, push, deploy, publish, deletion, or credential authority.
