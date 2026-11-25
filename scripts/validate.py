"""Validate the published skill packages, Markdown paths, and eval inventory."""

import json
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FRONTMATTER = re.compile(r"---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n(.+)\Z", re.DOTALL)
INLINE_LINK = re.compile(r"\]\(([^\s)]+)\)")


def package_errors(root):
    errors = []
    catalog = set()
    skills = root / "skills"
    for folder in sorted(skills.iterdir()):
        if not folder.is_dir() or folder.is_symlink():
            errors.append(f"{folder.name}: expected a real skill directory")
            continue
        catalog.add(folder.name)
        source = folder / "SKILL.md"
        if not source.is_file():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        data = source.read_text(encoding="utf-8")
        match = FRONTMATTER.fullmatch(data)
        if not match:
            errors.append(f"{folder.name}: expected required plain-scalar frontmatter and body")
            continue
        name, description, body = match.groups()
        if name != folder.name or len(name) > 64 or not SLUG.fullmatch(name):
            errors.append(f"{folder.name}: invalid name or directory mismatch")
        # This repository deliberately uses a small, unquoted YAML subset.
        if (not 1 <= len(description) <= 1024 or not description[0].isalpha()
                or ": " in description or " #" in description or description.endswith(":")
                or description.lower() in {"true", "false", "yes", "no", "on", "off", "null"}):
            errors.append(f"{folder.name}: invalid description for repository YAML subset")
        if not body.strip() or len(data.splitlines()) > 120:
            errors.append(f"{folder.name}: missing body or exceeds 120-line repository budget")
    if not catalog:
        errors.append("empty skill catalog")
    return catalog, errors


def path_errors(root):
    errors = []
    for directory in (root, root / "skills", root / "docs", root / "examples"):
        sources = directory.glob("*.md") if directory == root else directory.rglob("*.md")
        for source in sorted(sources):
            relative = source.relative_to(root)
            if source.is_symlink() or not source.resolve().is_relative_to(root):
                errors.append(f"{relative}: Markdown source must remain in the distribution")
                continue
            boundary = root / "skills" / relative.parts[1] if relative.parts[0] == "skills" else root
            for destination in INLINE_LINK.findall(source.read_text(encoding="utf-8")):
                if destination.startswith("https://") or destination.startswith("#"):
                    continue
                target = destination.split("#", 1)[0]
                resolved = (source.parent / target).resolve()
                if (":" in target or "\\" in target or not resolved.is_relative_to(boundary)
                        or not resolved.exists()):
                    errors.append(f"{relative}: invalid or missing local destination {destination}")
    return errors


def check_case(root, case, catalog):
    if set(case) != {"id", "skill", "prompt", "inputs", "criteria"}:
        raise ValueError("unexpected scenario fields")
    if not SLUG.fullmatch(case["id"]) or case["skill"] not in catalog or not case["prompt"].strip():
        raise ValueError("invalid scenario identity, skill, or prompt")
    if not isinstance(case["inputs"], list) or not case["inputs"]:
        raise ValueError("missing scenario inputs")
    fixtures = root / "examples" / "synthetic-project"
    for item in case["inputs"]:
        path = PurePosixPath(item)
        resolved = (root / item).resolve()
        if (path.is_absolute() or ".." in path.parts or "\\" in item or ":" in item
                or not resolved.is_relative_to(fixtures) or not resolved.is_file()):
            raise ValueError(f"{case['id']}: invalid synthetic input path")
    criteria = case["criteria"]
    if not isinstance(criteria, list) or len(criteria) < 2:
        raise ValueError(f"{case['id']}: insufficient rubric")
    seen = set()
    for criterion in criteria:
        if (set(criterion) != {"id", "observable", "critical"}
                or not SLUG.fullmatch(criterion["id"]) or criterion["id"] in seen
                or type(criterion["critical"]) is not bool or not criterion["observable"].strip()):
            raise ValueError(f"{case['id']}: invalid criterion")
        seen.add(criterion["id"])
    if not any(criterion["critical"] for criterion in criteria):
        raise ValueError(f"{case['id']}: mark at least one critical criterion")


def check_manifest(root, catalog):
    data = json.loads((root / "evals/scenarios.json").read_text(encoding="utf-8"))
    if set(data) != {"version", "cases"} or type(data["version"]) is not int or data["version"] != 1:
        raise ValueError("invalid scenario manifest version or fields")
    counts = dict.fromkeys(catalog, 0)
    seen = set()
    for case in data["cases"]:
        check_case(root, case, catalog)
        if case["id"] in seen:
            raise ValueError(f"duplicate scenario ID {case['id']}")
        seen.add(case["id"])
        counts[case["skill"]] += 1
    if any(count < 2 for count in counts.values()):
        raise ValueError("provide at least two scenarios per skill")
    return len(seen)


def main():
    try:
        catalog, errors = package_errors(ROOT)
        errors.extend(path_errors(ROOT))
        total = check_manifest(ROOT, catalog)
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(catalog)} skill packages, Markdown destinations, and {total} eval cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
