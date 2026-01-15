#!/usr/bin/env python3
"""Find all content requiring user input."""

import csv
import re
import sys
from pathlib import Path


def find_placeholders_in_file(file_path: Path, project_path: Path) -> list[dict]:
    """Find placeholder patterns in a file."""
    issues = []
    content = file_path.read_text()
    rel_path = str(file_path.relative_to(project_path))
    lines = content.split("\n")

    for line_num, line in enumerate(lines, 1):
        # Find {{needs-input: ...}}
        needs_input = re.finditer(r"\{\{needs-input:\s*([^}]+)\}\}", line)
        for match in needs_input:
            issues.append(
                {
                    "file_path": rel_path,
                    "line_number": line_num,
                    "type": "needs-input",
                    "content": match.group(1).strip(),
                }
            )

        # Find {{placeholder: ...}}
        placeholders = re.finditer(r"\{\{placeholder:\s*([^}]+)\}\}", line)
        for match in placeholders:
            issues.append(
                {
                    "file_path": rel_path,
                    "line_number": line_num,
                    "type": "placeholder",
                    "content": match.group(1).strip(),
                }
            )

        # Find {{verify ...}} blocks (just the opening tag)
        verify_blocks = re.finditer(r"\{\{verify:\s*([^}]+)\}\}", line)
        for match in verify_blocks:
            issues.append(
                {
                    "file_path": rel_path,
                    "line_number": line_num,
                    "type": "verify",
                    "content": match.group(1).strip(),
                }
            )

    return issues


def find_all_placeholders(project_path: Path) -> list[dict]:
    """Find all placeholders in the project."""
    all_issues = []

    # Scan all markdown files
    for md_file in project_path.rglob("*.md"):
        # Skip _validation folder
        if "_validation" in str(md_file):
            continue
        issues = find_placeholders_in_file(md_file, project_path)
        all_issues.extend(issues)

    return all_issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python find_placeholders.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    issues = find_all_placeholders(project_path)

    print(f"Scanning for placeholders: {project_path}")
    print("-" * 40)

    if issues:
        # Create _validation directory if needed
        validation_dir = project_path / "_validation"
        validation_dir.mkdir(exist_ok=True)

        # Write CSV
        csv_path = validation_dir / "placeholders.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["file_path", "line_number", "type", "content"]
            )
            writer.writeheader()
            writer.writerows(issues)

        # Group by type
        needs_input = [i for i in issues if i["type"] == "needs-input"]
        placeholders = [i for i in issues if i["type"] == "placeholder"]
        verify = [i for i in issues if i["type"] == "verify"]

        if needs_input:
            print(f"\nNeeds input ({len(needs_input)}):")
            for issue in needs_input[:5]:
                print(f"  - {issue['file_path']}:{issue['line_number']}: {issue['content']}")
            if len(needs_input) > 5:
                print(f"  ... and {len(needs_input) - 5} more")

        if placeholders:
            print(f"\nPlaceholders ({len(placeholders)}):")
            for issue in placeholders[:5]:
                print(f"  - {issue['file_path']}:{issue['line_number']}: {issue['content']}")
            if len(placeholders) > 5:
                print(f"  ... and {len(placeholders) - 5} more")

        if verify:
            print(f"\nNeeds verification ({len(verify)}):")
            for issue in verify[:5]:
                print(f"  - {issue['file_path']}:{issue['line_number']}: {issue['content']}")
            if len(verify) > 5:
                print(f"  ... and {len(verify) - 5} more")

        print(f"\nTotal: {len(issues)} item(s) requiring attention")
        print(f"Results written to: {csv_path}")
    else:
        print("\nNo placeholders or items needing input found.")


if __name__ == "__main__":
    main()
