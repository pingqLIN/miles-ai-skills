# Deep Project Progress Steward Workflow

Use Deep for cross-module, cross-worktree, roadmap, release, architecture, governance, or medium-term progress analysis.

## Steward Ownership

The main Project Progress Steward owns:

- scope and evidence plan
- source-of-truth and conflict decisions
- delegation decisions and boundaries
- risk prioritization and recommendations
- final synthesis and user-facing conclusions

Do not outsource final synthesis or treat an acknowledgement-only, timed-out, or evidence-free subagent response as approval.

## Workflow

1. State `Depth: Deep`, the promotion or routing reason, and the inspected boundaries.
2. Run the shared Evidence Kernel in [evidence-kernel.md](evidence-kernel.md).
3. Build an evidence map of modules, worktrees, milestones, verification surfaces, and governing documents.
4. Decide whether additional tools or bounded subagents materially improve evidence quality.
5. Gather independent evidence, reconcile contradictions, and mark material claims `VERIFIED`, `INFERRED`, or `UNKNOWN`.
6. Synthesize current progress, drift, blockers, risks, dependencies, and prioritized next actions.
7. If update execution is separately authorized, pass the synthesized analysis to [update-files.md](update-files.md).

## Conditional Delegation Contract

Delegation is optional. Proceed without subagents when the main agent can inspect the scope directly with lower coordination cost.

When delegation is justified:

- assign a concrete evidence question, read scope, and deliverable
- keep ownership non-overlapping
- default delegated investigation and review to read-only
- require inspected paths, commands, or execution results
- record assumptions, unknowns, and failed checks
- validate the evidence before using it
- keep integration and final synthesis with the main Steward

Possible non-overlapping roles include:

- repository or worktree evidence investigator
- verification and test-signal investigator
- roadmap, release-note, or documentation-drift investigator
- architecture, governance, or delivery-risk investigator

Use only the roles the evidence plan needs. Do not create a fixed team for every Deep analysis.

## Tool And Authority Boundary

Select the narrowest tools that answer each evidence question. Deep may justify broader read-only inspection or conditional collaboration, but it does not increase mutation or external authority.

Any edit, dependency change, runtime change, merge, push, release, deploy, publication, deletion, or credential operation remains governed by its own user authorization and approval gate. Keep delegated write scopes empty unless a separately authorized execution phase explicitly assigns a bounded mutation.

## Reconciliation Rules

- Prefer canonical project sources over projections and caches.
- Distinguish each worktree and branch instead of flattening them into one status.
- Treat plans and release criteria as intent until execution evidence supports completion.
- Preserve conflicting evidence and explain the recommended resolution.
- Report partial or blocked evidence honestly; do not convert coverage gaps into confident roadmap claims.
