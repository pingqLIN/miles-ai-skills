# Miles AI Skills Registry

A small, portable, and verifiable collection of reusable AI Agent Skills maintained by Miles / `pingqLIN`.

The repository keeps **canonical Skill definitions separate from runtime-specific routing, model selection, and execution policy**. Each Skill is intended to be reviewable as a bounded behavior module rather than as an opaque agent configuration.

> Traditional Chinese: [README.zh-TW.md](README.zh-TW.md)

## Skills

| Skill | Purpose | Version | Status | Language files |
|---|---|---:|---|---|
| [JING JING Clarifier](skills/jing-jing-clarifier/SKILL.en.md) | Refines Traditional Chinese text, reduces unnecessary Chinese-English mixing, and protects technical literals. | 1.1.0 | Stable | [English](skills/jing-jing-clarifier/SKILL.en.md) · [繁中](skills/jing-jing-clarifier/SKILL.md) |
| [Right-Sizing Agent Tasks](skills/right-sizing-agent-tasks/SKILL.en.md) | Converts broad or repetitive work into a bounded TASK-LITE while preserving safety, authority, evidence, and acceptance gates. | 1.0.0 | Stable | [English](skills/right-sizing-agent-tasks/SKILL.en.md) · [繁中](skills/right-sizing-agent-tasks/SKILL.md) |

The registry metadata is maintained in [`registry/index.yaml`](registry/index.yaml).

## Language and version policy

- `SKILL.md` remains the canonical Traditional Chinese definition for the current registry Skill version.
- `SKILL.en.md` is the English semantic companion for the same Skill version.
- Translation must preserve behavior, safety boundaries, protected literals, required output contracts, and acceptance semantics.
- A language-only synchronization does not imply a new behavioral Skill release. Behavioral changes should update the Skill version in [`registry/index.yaml`](registry/index.yaml) and then synchronize both language files.

## Repository structure

```text
miles-ai-skills/
├── .github/workflows/       # CI validation workflows
├── registry/
│   └── index.yaml           # Canonical registry metadata and language mapping
├── scripts/
│   └── validate-registry.py # Repository integrity validator
├── skills/
│   ├── jing-jing-clarifier/
│   │   ├── SKILL.md         # Canonical Traditional Chinese definition
│   │   └── SKILL.en.md      # English semantic companion
│   └── right-sizing-agent-tasks/
│       ├── SKILL.md         # Canonical Traditional Chinese definition
│       ├── SKILL.en.md      # English semantic companion
│       └── references/      # Supporting evidence and pressure tests
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

## Relationship to runtime systems

Skills in this repository define reusable behavior and task policy. Runtime-specific concerns—such as model routing, executor selection, active installation state, or project-level authority—belong to the consuming runtime or project unless a Skill explicitly defines otherwise.

For example, `right-sizing-agent-tasks` can prepare a bounded TASK-LITE before execution, while the related `lead-agent-control-plane` project remains responsible for execution-time intake, authority, routing, evidence review, and final acceptance.

## License and provenance

This repository does not currently declare one repository-wide license. License and provenance are tracked per Skill in [`registry/index.yaml`](registry/index.yaml) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

The registry and provenance notes contain the current per-Skill license status and upstream attribution. One Skill has an identified upstream license while another remains explicitly `unknown`; consult those source files before reuse or redistribution.

Do not infer a repository-wide license from an individual Skill's license.