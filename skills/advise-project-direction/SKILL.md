---
name: advise-project-direction
description: Decide whether a proposed change in an existing project should continue on the current path, use an isolated branch/worktree, become a new project, require research, or defer. Use only when the user explicitly asks for this project-boundary or execution-direction decision before implementation; do not use for ordinary planning, code design, bug fixes, status, or general discussion. For current progress, status, readiness, or project-update maintenance, use maintain-project-updates instead. After classifying, recommend—but never auto-invoke—the narrowest applicable next skill or workflow.
---

# Advise Project Direction

## Operating Stance

Act as an independent project advisor before execution. Do not jump directly into coding, patching, planning a single component, or defending the current implementation. Give advice based on the whole project direction, including product purpose, engineering process, user-specific environment constraints, and market/promotion implications when relevant.

This skill makes a direction decision, then gives a bounded continuation route. A route is a recommendation only: it does not invoke another skill, authorize mutation, create a branch or worktree, or start an execution loop. The user must explicitly choose or invoke the recommended next workflow when its own trigger requires that.

Use high or extra-high reasoning effort when the runtime lets you choose model settings. If model settings are not controllable, state that the advisory pass should be treated as high-stakes reasoning and compensate by gathering stronger evidence before answering.

## Trigger Boundary

Use this skill only when the user explicitly needs a decision between the current project path, an isolated implementation path, a separate product, more research, or deferral before work begins. Typical requests ask whether a proposal belongs in the current branch, needs a worktree, changes the product boundary, has enough evidence, or should wait for a later milestone.

Do not use it for ordinary implementation planning, code design, bug fixing, status reporting, general brainstorming, or a request that already has an unambiguous scoped execution path. In those cases, use normal task handling or the narrowly matching skill instead.

## Paired Skill Routing

This skill is paired with `$maintain-project-updates` so project evaluation requests can be redirected without merging their responsibilities. If the request is primarily to establish current progress, reconcile code, Git, tests, runtime, and project documents, assess roadmap or release readiness, or maintain project-update files—not to decide a proposed change's project or execution boundary—stop this route and recommend `$maintain-project-updates`. Carry forward any verified evidence already gathered, but let that skill choose its Shallow or Deep workflow and preserve its separate mutation boundary.

## Required Context Refresh

Before answering, recheck the project's core materials. Prefer the closest repo-local sources, then workspace/global sources:

- instruction files: `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, docs index, project briefs
- current state: `git status --short --branch`, recent commits, active branch/worktree, open plans or task state
- product intent: purpose, target user, success criteria, non-goals, deployment/distribution assumptions
- process history: decision logs, roadmap or local planning notes, verification logs, unresolved issues
- current request: what the user wants to think about before acting

If the project is not a Git repo or the core materials are missing, say that clearly and base the answer on the available files rather than inventing certainty.

## Advisory Workflow

1. Identify the user's idea or concern in one sentence.
2. Summarize the project baseline from fresh evidence: purpose, goal, current progress, and relevant constraints.
3. Classify the idea:
   - `current-path`: fits the current branch/project and can proceed now
   - `branch-first`: plausible but risky enough to isolate in a branch/worktree
   - `new-project`: materially changes product identity, audience, runtime, ownership, or distribution
   - `research-first`: needs evidence before implementation
   - `defer`: useful but not aligned with the current milestone
4. State confidence and the material unknowns. Do not promote missing evidence into certainty.
5. Explain why, using project-wide reasoning rather than only the local component.
6. Recommend the next action, continuation route, and smallest verification gate before execution.

## Second-Stage Continuation Routing

Give exactly one primary continuation route. Keep it proportional to the decision and do not recommend a tool merely because it is available.

### `current-path`

- For a simple, already-scoped change, recommend normal implementation in the current project; do not add workflow overhead.
- When the user wants a reviewed small/medium/large execution contract, recommend `$dev-workflow-scale-planner`.
- When the user wants an implementation plan or explicit review gates before execution, recommend `$plan-first-execution`.
- Recommend `$project-development-loop` only when the user explicitly asks for continuous, time-boxed, overnight, or repeated autonomous maintenance in an existing codebase. Never imply that this classification alone authorizes that loop.

### `branch-first`

- First give a lightweight isolation record: reason for isolation, base ref, intended branch/worktree boundary, affected areas, and the condition for merging back.
- If the work is still ambiguous or needs a reviewed design before isolation, recommend `$plan-first-execution`; if the user wants a scaled execution contract, recommend `$dev-workflow-scale-planner`.
- Do not invent a dedicated branch tool when none is available. Creation of the branch or worktree follows the repository's Git safety rules and requires the normal explicit approval path for local mutation.
- If the isolated scope is actually a small, low-risk edit, say so and prefer `current-path` instead of overcomplicating the work.

### `new-project`

- Recommend a project-boundary brief before implementation: product premise, target user, runtime or operating environment, data ownership, distribution or publication model, non-goals, and success criteria.
- If the question is specifically whether the new system can be operated primarily by AI agents, optionally recommend `$ai-first-readiness-review` after the boundary is defined.
- Do not recommend `$project-development-loop`: it excludes greenfield bootstrap. Do not imply that a generic research skill exists when local evidence does not identify one.

### `research-first`

- Provide an evidence plan: hypothesis or decision question, known facts, unknowns, sources to inspect, decision threshold, and the condition that allows the work to return to a direction decision.
- Use read-only project evidence or focused external research first. Recommend a specialized skill only when its boundary matches the evidence gap: `$ai-first-readiness-review` for AI-agent operability, or `$ai-runtime-governance` for installed developer-tool and host-configuration questions.
- Do not route directly to implementation until the threshold is met or the user explicitly accepts the residual uncertainty.

### `defer`

- Give a bounded defer record: why it is out of scope, which milestone or condition makes it relevant again, where the decision should be retained, and a review or expiry trigger.
- Do not recommend an execution, planning, or autonomous-loop skill by default.

## Routing Constraints

- Recommendations are not implicit skill invocation, approval, or authorization to mutate the repository.
- Respect the recommended skill's own trigger boundary and availability. If it is unavailable, state the workflow outcome it would provide rather than fabricating a substitute tool.
- Prefer the narrowest next step. A simple `current-path` change usually needs no second skill.
- Never use a continuation route to bypass Git safety, approval gates, research evidence, or project-local instructions.

## Branch And New-Project Boundary

Recommend a separate branch/worktree when the idea changes implementation strategy but preserves the same product identity and acceptance criteria. Recommend a new project when it changes the core product premise, target user, operational environment, data ownership, compliance boundary, business model, marketing surface, or distribution channel.

When the recommendation differs from the user's implied direction, say so plainly and offer the safer boundary first.

## Answer Shape

Keep the answer concise and decision-oriented:

- `Recommendation`: current-path, branch-first, new-project, research-first, or defer
- `Evidence`: project facts checked before answering
- `Confidence and unknowns`: what is verified, inferred, or still missing
- `Reasoning`: why this fits or conflicts with the project as a whole
- `Next step`: one practical action before coding
- `Continuation route`: one recommended mode, skill, or no-tool path; why it fits; and any explicit user action required
- `Verification gate`: what must be true before committing to the direction
