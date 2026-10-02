#!/usr/bin/env python3
"""Collect lightweight project-progress signals for an agent status review."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".nuxt",
    ".cache",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "out",
    "coverage",
    "__pycache__",
    "target",
    ".idea",
    ".vscode",
    ".clean",
    ".tmp",
    ".del",
}

TEXT_EXTENSIONS = {
    ".c",
    ".cc",
    ".cfg",
    ".conf",
    ".cs",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".html",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".kt",
    ".lock",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".rs",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}

UPDATE_NAME_RE = re.compile(
    r"(readme|change[-_ ]?log|release|status|progress|roadmap|todo|decision|adr|plan)",
    re.IGNORECASE,
)
TODO_RE = re.compile(r"\b(TODO|FIXME|HACK|XXX|BUG)\b[:\s-]*(.*)", re.IGNORECASE)


@dataclass
class TodoHit:
    path: str
    line: int
    tag: str
    text: str


def run_git(root: Path, args: list[str]) -> tuple[int, str]:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        return 127, "git not found"
    return completed.returncode, completed.stdout.strip() or completed.stderr.strip()


def git_root(start: Path) -> Path | None:
    code, output = run_git(start, ["rev-parse", "--show-toplevel"])
    if code == 0 and output:
        return Path(output).resolve()
    return None


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def iter_files(root: Path, max_files: int) -> Iterable[Path]:
    seen = 0
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            seen += 1
            if seen > max_files:
                return
            yield Path(current_root) / name


def is_text_candidate(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    return path.name in {"Dockerfile", "Makefile", "Justfile", "Procfile"}


def read_text(path: Path, max_bytes: int = 250_000) -> str | None:
    try:
        if path.stat().st_size > max_bytes:
            return None
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def find_update_docs(root: Path, max_files: int) -> list[str]:
    docs: list[str] = []
    for path in iter_files(root, max_files):
        if path.suffix.lower() not in {".md", ".txt", ".rst", ".adoc"}:
            continue
        relative = rel(path, root)
        if UPDATE_NAME_RE.search(relative):
            docs.append(relative)
    return sorted(docs)


def find_manifests(root: Path) -> list[str]:
    names = {
        "package.json",
        "pnpm-lock.yaml",
        "yarn.lock",
        "package-lock.json",
        "pyproject.toml",
        "requirements.txt",
        "poetry.lock",
        "Pipfile",
        "Cargo.toml",
        "go.mod",
        "pom.xml",
        "build.gradle",
        "composer.json",
        "Gemfile",
        "Makefile",
        "Justfile",
    }
    found: list[str] = []
    for name in names:
        path = root / name
        if path.exists():
            found.append(name)
    return sorted(found)


def find_tests(root: Path) -> dict[str, object]:
    dirs = [name for name in ["test", "tests", "__tests__", "spec", "e2e"] if (root / name).exists()]
    workflows = sorted(rel(path, root) for path in (root / ".github" / "workflows").glob("*") if path.is_file()) if (root / ".github" / "workflows").exists() else []
    scripts: dict[str, str] = {}
    package_json = root / "package.json"
    text = read_text(package_json)
    if text:
        try:
            package = json.loads(text)
            raw_scripts = package.get("scripts", {})
            if isinstance(raw_scripts, dict):
                scripts = {k: str(v) for k, v in raw_scripts.items() if any(term in k.lower() for term in ["test", "lint", "build", "check"])}
        except json.JSONDecodeError:
            scripts = {}
    return {"directories": dirs, "workflows": workflows, "package_scripts": scripts}


def find_todos(root: Path, max_files: int, limit: int) -> list[TodoHit]:
    hits: list[TodoHit] = []
    for path in iter_files(root, max_files):
        if not is_text_candidate(path):
            continue
        text = read_text(path, max_bytes=150_000)
        if text is None:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            match = TODO_RE.search(line)
            if not match:
                continue
            hits.append(TodoHit(rel(path, root), idx, match.group(1).upper(), match.group(2).strip()))
            if len(hits) >= limit:
                return hits
    return hits


def git_info(root: Path) -> dict[str, object]:
    info: dict[str, object] = {"is_git": False}
    repo_root = git_root(root)
    if repo_root is None:
        return info

    info["is_git"] = True
    info["repo_root"] = str(repo_root)
    for key, args in {
        "branch": ["branch", "--show-current"],
        "head": ["rev-parse", "--short", "HEAD"],
        "status": ["status", "--short", "--branch"],
        "recent_commits": ["log", "--oneline", "--decorate", "-n", "5"],
    }.items():
        code, output = run_git(repo_root, args)
        info[key] = output if code == 0 else ""

    git_dir_code, git_dir = run_git(repo_root, ["rev-parse", "--git-dir"])
    active_ops: list[str] = []
    if git_dir_code == 0 and git_dir:
        git_path = Path(git_dir)
        if not git_path.is_absolute():
            git_path = repo_root / git_path
        markers = {
            "merge": "MERGE_HEAD",
            "rebase": "rebase-merge",
            "apply-rebase": "rebase-apply",
            "cherry-pick": "CHERRY_PICK_HEAD",
            "revert": "REVERT_HEAD",
        }
        for label, marker in markers.items():
            if (git_path / marker).exists():
                active_ops.append(label)
    info["active_operations"] = active_ops
    return info


def collect(root: Path, max_files: int, todo_limit: int) -> dict[str, object]:
    resolved = root.resolve()
    repo_root = git_root(resolved) or resolved
    return {
        "root": str(repo_root),
        "git": git_info(repo_root),
        "manifests": find_manifests(repo_root),
        "tests": find_tests(repo_root),
        "update_docs": find_update_docs(repo_root, max_files),
        "todo_hits": [asdict(hit) for hit in find_todos(repo_root, max_files, todo_limit)],
    }


def markdown_report(data: dict[str, object]) -> str:
    git = data.get("git", {})
    assert isinstance(git, dict)
    tests = data.get("tests", {})
    assert isinstance(tests, dict)

    lines = [
        "# Project Progress Audit",
        "",
        f"- Root: `{data.get('root')}`",
        f"- Git repo: `{git.get('is_git')}`",
    ]
    if git.get("is_git"):
        lines.extend(
            [
                f"- Branch: `{git.get('branch') or '(detached or unknown)'}`",
                f"- HEAD: `{git.get('head')}`",
                f"- Active operations: `{', '.join(git.get('active_operations') or []) or 'none'}`",
                "",
                "## Git Status",
                "",
                "```text",
                str(git.get("status") or ""),
                "```",
                "",
                "## Recent Commits",
                "",
                "```text",
                str(git.get("recent_commits") or ""),
                "```",
            ]
        )

    lines.extend(["", "## Project Signals", ""])
    for key in ["manifests", "update_docs"]:
        values = data.get(key, [])
        assert isinstance(values, list)
        lines.append(f"- {key.replace('_', ' ').title()}: {', '.join(f'`{v}`' for v in values) if values else 'none found'}")

    lines.extend(["", "## Test Signals", ""])
    lines.append(f"- Test directories: {', '.join(f'`{v}`' for v in tests.get('directories', [])) or 'none found'}")
    lines.append(f"- CI workflows: {', '.join(f'`{v}`' for v in tests.get('workflows', [])) or 'none found'}")
    scripts = tests.get("package_scripts", {})
    if isinstance(scripts, dict) and scripts:
        lines.append("- Package scripts:")
        for name, command in scripts.items():
            lines.append(f"  - `{name}`: `{command}`")
    else:
        lines.append("- Package scripts: none found")

    todo_hits = data.get("todo_hits", [])
    assert isinstance(todo_hits, list)
    lines.extend(["", "## TODO/FIXME Signals", ""])
    if todo_hits:
        for hit in todo_hits:
            assert isinstance(hit, dict)
            text = str(hit.get("text") or "").strip()
            suffix = f" - {text}" if text else ""
            lines.append(f"- `{hit.get('path')}:{hit.get('line')}` {hit.get('tag')}{suffix}")
    else:
        lines.append("- none found")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect project progress signals.")
    parser.add_argument("--root", default=".", help="Project directory to inspect.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--max-files", type=int, default=4000)
    parser.add_argument("--todo-limit", type=int, default=50)
    args = parser.parse_args()

    data = collect(Path(args.root), args.max_files, args.todo_limit)
    if args.format == "json":
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(markdown_report(data), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
