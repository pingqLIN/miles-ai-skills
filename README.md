# Miles AI Skills Registry

A small, portable, and verifiable collection of reusable AI Agent Skills maintained by Miles / `pingqLIN`.

The repository keeps **canonical Skill definitions separate from runtime-specific routing, model selection, and execution policy**. Each Skill is intended to be reviewable as a bounded behavior module rather than as an opaque agent configuration.

> Traditional Chinese: [README.zh-TW.md](README.zh-TW.md)

## Skills

| Skill | Purpose | Version | Status | Language files |
|---|---|---:|---|---|
| [JING JING Clarifier](skills/jing-jing-clarifier/SKILL.en.md) | Refines Traditional Chinese text, reduces unnecessary Chinese-English mixing, and protects technical literals. | 1.1.0 | Stable | [English](skills/jing-jing-clarifier/SKILL.en.md) · [繁中](skills/jing-jing-clarifier/SKILL.md) |
| [Right-Sizing Agent Tasks](skills/right-sizing-agent-tasks/SKILL.en.md) | Converts broad or repetitive work into a bounded TASK-LITE while preserving safety, authority, evidence, and acceptance gates. | 1.0.0 | Stable | [English](skills/right-sizing-agent-tasks/SKILL.en.md) · [繁中](skills/right-sizing-agent-tasks/SKILL.md) |
| [Advise Project Direction](skills/advise-project-direction/SKILL.md) | Decides the project and execution boundary for a proposed change before implementation. | 1.0.0 | Stable | [English](skills/advise-project-direction/SKILL.md) |
| [Maintain Project Updates](skills/maintain-project-updates/SKILL.md) | Establishes current project progress, execution readiness, and the next evidence-backed step. | 1.0.0 | Stable | [English](skills/maintain-project-updates/SKILL.md) |

The registry metadata is maintained in [`registry/index.yaml`](registry/index.yaml).

## Language and version policy

- `SKILL.md` is the canonical package entrypoint. Its locale is declared by `canonical_locale` in the registry rather than assumed from the filename.
- Localized semantic companions use a locale suffix such as `SKILL.en.md`; every available language file is declared under `localized_files`.
- Translation must preserve behavior, safety boundaries, protected literals, required output contracts, and acceptance semantics.
- A language-only synchronization does not imply a new behavioral Skill release. Behavioral changes should update the Skill version in [`registry/index.yaml`](registry/index.yaml) and then synchronize every declared language file.

## Repository structure

```text
miles-ai-skills/
├── .github/workflows/       # CI validation workflows
├── registry/
│   └── index.yaml           # Canonical registry metadata and language mapping
├── scripts/
│   └── validate-registry.py # Repository integrity validator
├── skills/
│   └── <skill-id>/
│       ├── SKILL.md         # Canonical package entrypoint
│       ├── agents/          # Optional UI metadata and invocation policy
│       ├── references/      # Optional supporting instructions
│       └── scripts/         # Optional deterministic helpers
├── THIRD_PARTY_NOTICES.md   # Attribution and provenance notes
├── README.zh-TW.md          # Traditional Chinese repository landing page
└── README.md                # English repository landing page
```

## Validation

This repository uses two validation layers:

1. **Repository integrity** — `scripts/validate-registry.py` checks that `registry/index.yaml`, Skill directories, and canonical `SKILL.md` frontmatter remain consistent.
2. **Specification conformance** — CI uses a pinned Agent Skills `skills-ref` reference implementation to run `skills-ref validate`. The reference implementation is a compatibility check, not the repository's only production validator.

Run the local integrity check with:

```bash
python scripts/validate-registry.py
```

A successful integrity check verifies registry structure and canonical frontmatter consistency. It does **not** prove that a Skill was discovered, invoked, or accepted by a particular runtime.

## Adding or synchronizing a Skill

1. Identify one authoritative upstream and inspect its license, provenance, and private or machine-specific content before copying anything.
2. Copy the complete portable package to `skills/<skill-id>/`. Exclude runtime projection wrappers, credentials, private plans, caches, and machine-only evidence.
3. Add or update exactly one entry in `registry/index.yaml`, including version, status, license, path, `canonical_locale`, `localized_files`, and material relationships.
4. Update both repository landing pages and `THIRD_PARTY_NOTICES.md` when availability, behavior, provenance, or license status changes.
5. Run the repository validator and the Skill validator, review the scoped diff, then commit and push only the intended package and metadata.

Treat source presence, publication, installation, loading, and runtime acceptance as separate states. A successful repository push establishes publication only.

## Relationship to runtime systems

Skills in this repository define reusable behavior and task policy. Runtime-specific concerns—such as model routing, executor selection, active installation state, or project-level authority—belong to the consuming runtime or project unless a Skill explicitly defines otherwise.

For example, `right-sizing-agent-tasks` can prepare a bounded TASK-LITE before execution, while the related `lead-agent-control-plane` project remains responsible for execution-time intake, authority, routing, evidence review, and final acceptance.

`advise-project-direction` and `maintain-project-updates` are a paired routing set, not a merged workflow. The former owns project-boundary decisions before implementation; the latter owns current-state, readiness, and project-update maintenance. Each redirects misrouted requests to the other without auto-invoking it or expanding mutation authority.

## License and provenance

This repository does not currently declare one repository-wide license. License and provenance are tracked per Skill in [`registry/index.yaml`](registry/index.yaml) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

The registry and provenance notes contain the current per-Skill license status and upstream attribution. Some Skills remain explicitly `unknown`; consult those source files before reuse or redistribution.

Do not infer a repository-wide license from an individual Skill's license.
