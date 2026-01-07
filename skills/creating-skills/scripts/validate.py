#!/usr/bin/env python3
"""
Validate an Agent Skill against the specification.

Usage:
    python validate.py <skill-path>
    python validate.py --all <skills-directory>

Validates:
- SKILL.md exists
- YAML frontmatter present and valid
- name field: format, length, reserved words
- description field: length, third person, no XML
- SKILL.md line count (warning if >500)
- File references exist
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, Optional


class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, msg: str):
        self.errors.append(msg)
        print(f"ERROR: {msg}")

    def warning(self, msg: str):
        self.warnings.append(msg)
        print(f"WARNING: {msg}")

    def success(self, msg: str):
        print(f"OK: {msg}")

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0


def extract_frontmatter(content: str) -> Optional[Dict[str, str]]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None

    lines = content.split("\n")
    end_index = None

    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index is None:
        return None

    frontmatter = {}
    for line in lines[1:end_index]:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip("\"'")
            frontmatter[key] = value

    return frontmatter


def validate_name(name: str, folder_name: str, result: ValidationResult):
    """Validate the name field."""
    if not name:
        result.error("Missing required field: name")
        return

    # Length check
    if len(name) > 64:
        result.error(f"name exceeds 64 characters ({len(name)} chars)")

    # Format check
    if not re.match(r"^[a-z0-9-]+$", name):
        result.error("name must contain only lowercase letters, numbers, and hyphens")

    # Reserved words
    if re.search(r"(anthropic|claude)", name, re.IGNORECASE):
        result.error("name cannot contain reserved words: 'anthropic', 'claude'")

    # XML tags
    if re.search(r"<[^>]+>", name):
        result.error("name cannot contain XML tags")

    # Match folder name
    if name != folder_name:
        result.warning(f"name '{name}' does not match folder name '{folder_name}'")

    if len(name) <= 64 and re.match(r"^[a-z0-9-]+$", name):
        result.success(f"name: {name}")


def validate_description(description: str, result: ValidationResult):
    """Validate the description field."""
    if not description:
        result.error("Missing required field: description")
        return

    # Length check
    if len(description) > 1024:
        result.error(f"description exceeds 1024 characters ({len(description)} chars)")

    # XML tags
    if re.search(r"<[^>]+>", description):
        result.error("description cannot contain XML tags")

    # First/second person (warning)
    bad_patterns = [
        r"\bI can\b",
        r"\bI will\b",
        r"\bI am\b",
        r"\byou can\b",
        r"\byou will\b",
        r"\byou are\b",
        r"\bwe can\b",
        r"\bwe will\b",
    ]
    for pattern in bad_patterns:
        if re.search(pattern, description, re.IGNORECASE):
            result.warning(
                f"description should use third person (found pattern matching '{pattern}')"
            )
            break

    result.success(f"description present ({len(description)} chars)")


def validate_skill(skill_path: Path) -> ValidationResult:
    """Validate a single skill."""
    result = ValidationResult()
    skill_name = skill_path.name
    skill_md = skill_path / "SKILL.md"

    print()
    print("=" * 50)
    print(f"Validating: {skill_name}")
    print("=" * 50)

    # Check SKILL.md exists
    if not skill_md.exists():
        result.error(f"SKILL.md not found in {skill_path}")
        return result
    result.success("SKILL.md exists")

    # Read content
    content = skill_md.read_text()

    # Check frontmatter
    frontmatter = extract_frontmatter(content)
    if frontmatter is None:
        result.error("SKILL.md must start with YAML frontmatter (---)")
        return result
    result.success("YAML frontmatter present")

    # Validate fields
    validate_name(frontmatter.get("name", ""), skill_name, result)
    validate_description(frontmatter.get("description", ""), result)

    # Line count
    line_count = len(content.split("\n"))
    if line_count > 500:
        result.warning(f"SKILL.md has {line_count} lines (recommended: under 500)")
    else:
        result.success(f"SKILL.md line count: {line_count}")

    # Check for Windows paths
    if re.search(r"\\[a-zA-Z]", content):
        result.warning("Possible Windows-style paths detected (use forward slashes)")

    # Check file references exist
    md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for link_text, link_path in md_links:
        if link_path.startswith("http"):
            continue
        ref_path = skill_path / link_path
        if not ref_path.exists():
            result.warning(f"Referenced file not found: {link_path}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Validate Agent Skills")
    parser.add_argument("path", help="Path to skill directory or --all flag")
    parser.add_argument(
        "--all", action="store_true", help="Validate all skills in directory"
    )
    args = parser.parse_args()

    path = Path(args.path)

    if args.all:
        # Validate all skills in directory
        if not path.is_dir():
            print(f"ERROR: {path} is not a directory")
            sys.exit(1)

        total = 0
        passed = 0
        failed = 0

        for skill_dir in sorted(path.iterdir()):
            if skill_dir.is_dir() and not skill_dir.name.startswith("."):
                total += 1
                result = validate_skill(skill_dir)
                if result.passed:
                    passed += 1
                else:
                    failed += 1

        print()
        print("=" * 50)
        print("SUMMARY")
        print("=" * 50)
        print(f"Total:  {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

        sys.exit(0 if failed == 0 else 1)

    else:
        # Validate single skill
        if not path.is_dir():
            print(f"ERROR: {path} is not a directory")
            sys.exit(1)

        result = validate_skill(path)

        print()
        if result.errors:
            print(f"FAILED: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
            sys.exit(1)
        elif result.warnings:
            print(f"PASSED with warnings: {len(result.warnings)} warning(s)")
            sys.exit(0)
        else:
            print("PASSED: All checks passed")
            sys.exit(0)


if __name__ == "__main__":
    main()
