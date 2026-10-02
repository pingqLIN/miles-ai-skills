# Third Party Notices

## JING JING Clarifier

This skill is derived from and adapted from existing work associated with:

- `pingqLIN/UniText`
- `chinese-writing-clarifier` (historical source name/reference)

The current `pingqLIN/UniText` repository contains an MIT License. The JING JING Clarifier adaptation retains provenance here while simplifying the skill into a client-neutral canonical definition.

Material changes in v1.1.0 include:

- Removed model-availability and runtime-selection guidance from the skill body.
- Removed the `full` and `general` variants in favor of one canonical skill.
- Reworked terminology handling around semantic editing and protected literals.
- Added repository integrity and Agent Skills specification conformance checks.

If a separately identifiable upstream repository for `chinese-writing-clarifier` is later established, its exact source and license requirements should be recorded here before incorporating additional material from it.

## Right-Sizing Agent Tasks

The canonical package in this repository was imported from the owner's local
`browser-governance-task-right-sizing/right-sizing-agent-tasks` authoring
package. No separate third-party upstream or license grant was identified at
import time; the registry therefore records its license as `unknown` rather
than inferring one from another Skill or repository.

## Advise Project Direction

This package was synchronized from the owner's local Codex Skill installation,
which identifies `pingqLIN/UniText` as its upstream governance source. No
separate third-party upstream or license grant was identified at synchronization
time, so the registry records its license as `unknown`.

The published package removes UniText runtime-projection metadata while
preserving the portable Skill behavior and its paired routing relationship with
`maintain-project-updates`.

## Maintain Project Updates

This package was synchronized from the owner's local Codex Skill installation,
which identifies `pingqLIN/UniText` as its upstream governance source. No
separate third-party upstream or license grant was identified at synchronization
time, so the registry records its license as `unknown`.

The published package removes UniText runtime-projection metadata while
preserving the portable Skill behavior, support files, and its paired routing
relationship with `advise-project-direction`.
