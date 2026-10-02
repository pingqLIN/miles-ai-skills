# Shared Evidence Kernel

Use this kernel for both Shallow and Deep analysis. Depth changes breadth and coordination, not the meaning of evidence.

## 1. Lock Scope

Identify:

- repository root and applicable instruction files
- branch, HEAD, worktree state, and active Git operations
- requested time horizon and project boundary
- whether the request is read-only or separately authorizes update execution
- sources the user considers authoritative

Do not silently widen the project, time horizon, or mutation scope.

## 2. Collect A Starting Map

For a local project, run:

```bash
python /path/to/maintain-project-updates/scripts/audit_project_progress.py --root . --format markdown
```

Use JSON only when another local tool needs structured input:

```bash
python /path/to/maintain-project-updates/scripts/audit_project_progress.py --root . --format json
```

The collector finds Git state, recent commits, common manifests and test signals, update documents, and bounded TODO/FIXME signals. It does not prove feature completeness, test success, release readiness, or document accuracy.

## 3. Inspect Direct Evidence

Read the highest-signal artifacts identified by the map. Prefer:

1. current source and configuration
2. executed tests, builds, runtime checks, or CI results
3. current Git status, diff, history, and worktree topology
4. canonical project specifications, decisions, and release criteria
5. status, roadmap, changelog, and planning files
6. user-stated goals and constraints

Plans and TODO text describe intent until implementation or execution evidence confirms them. A configured test command is not a passing test. A generated or runtime projection is not the authoring source unless project governance says so.

## 4. Compare Sources Of Truth

Check for contradictions across:

- code versus docs
- committed history versus the current worktree
- test declarations versus actual results
- roadmap/status claims versus implemented behavior
- canonical source versus generated, installed, cached, or deployed projections
- the user's current goal versus older plans

When sources conflict, name the conflict and preserve the distinction instead of silently selecting the convenient source.

## 5. Classify Claims

Use these labels for material conclusions:

- `VERIFIED`: supported by inspected source, authoritative documents, or actual execution output.
- `INFERRED`: a reasoned interpretation tied to named evidence.
- `UNKNOWN`: missing, inaccessible, stale, conflicting, or untested.

Do not promote `UNKNOWN` to `VERIFIED`. State what evidence or authorization would resolve an important unknown.

## 6. Derive Progress And Actions

Separate:

- completed and verified work
- in-progress or dirty work
- unstarted or unsupported claims
- documentation or projection drift
- blockers and risks
- recommended actions ordered by risk and leverage

Keep recommendations downstream of evidence. Avoid inventing precise completion percentages unless the project defines a trustworthy measurement model.

## 7. Preserve Safety

Run read-only evidence collection by default. Do not install dependencies, start or restart services, run migrations, change ports, edit files, or contact external systems merely to make the evidence set look complete. Use the applicable approval gate when a stronger verification step would mutate runtime or external state.
