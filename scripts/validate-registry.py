#!/usr/bin/env python3
"""Validate registry/index.yaml against canonical skill directories."""
import sys
from pathlib import Path

import yaml


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    registry_file = root / "registry" / "index.yaml"
    skills_dir = root / "skills"
    errors: list[str] = []

    if not registry_file.is_file():
        print(f"[CRITICAL] Missing registry file: {registry_file}", file=sys.stderr)
        raise SystemExit(1)

    try:
        data = yaml.safe_load(registry_file.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        print(f"[CRITICAL] Failed to parse {registry_file}: {exc}", file=sys.stderr)
        raise SystemExit(1)

    entries = data.get("skills", [])
    if not isinstance(entries, list) or not entries:
        errors.append("registry/index.yaml must declare a non-empty 'skills' list")
        entries = []

    seen_ids: set[str] = set()
    registered_dirs: set[Path] = set()

    for item in entries:
        if not isinstance(item, dict):
            errors.append(f"Registry entry must be a mapping: {item!r}")
            continue

        skill_id = item.get("id")
        skill_path = item.get("path")
        if not isinstance(skill_id, str) or not skill_id or not isinstance(skill_path, str) or not skill_path:
            errors.append(f"Registry entry missing valid 'id' or 'path': {item!r}")
            continue

        if skill_id in seen_ids:
            errors.append(f"Duplicate skill ID: {skill_id!r}")
        seen_ids.add(skill_id)

        target_dir = root / skill_path
        if not target_dir.is_dir():
            errors.append(f"Registry path does not exist: {skill_path}")
            continue
        registered_dirs.add(target_dir.resolve())

        if target_dir.name != skill_id:
            errors.append(f"Directory name {target_dir.name!r} != registry ID {skill_id!r}")

        skill_md = target_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"Missing SKILL.md: {skill_path}")
            continue

        try:
            content = skill_md.read_text(encoding="utf-8")
            if not content.startswith("---\n"):
                errors.append(f"Missing YAML frontmatter: {skill_md.relative_to(root)}")
                continue
            parts = content.split("---", 2)
            if len(parts) < 3:
                errors.append(f"Malformed YAML frontmatter: {skill_md.relative_to(root)}")
                continue
            frontmatter = yaml.safe_load(parts[1]) or {}
            if not isinstance(frontmatter, dict):
                errors.append(f"Frontmatter must be a mapping: {skill_md.relative_to(root)}")
                continue
            fm_name = frontmatter.get("name")
            if fm_name != skill_id:
                errors.append(
                    f"Frontmatter name {fm_name!r} != registry ID {skill_id!r}: "
                    f"{skill_md.relative_to(root)}"
                )
        except Exception as exc:
            errors.append(f"Failed to parse {skill_md.relative_to(root)}: {exc}")

    if not skills_dir.is_dir():
        errors.append("Missing skills directory")
    else:
        for disk_skill in skills_dir.iterdir():
            if disk_skill.is_dir() and disk_skill.resolve() not in registered_dirs:
                errors.append(
                    f"Unregistered skill directory: {disk_skill.relative_to(root)}"
                )

    if errors:
        print(f"[VALIDATION FAILED] {len(errors)} error(s):", file=sys.stderr)
        for index, error in enumerate(errors, 1):
            print(f"  {index}. {error}", file=sys.stderr)
        raise SystemExit(1)

    print("Repository and registry integrity checks passed.")


if __name__ == "__main__":
    main()
