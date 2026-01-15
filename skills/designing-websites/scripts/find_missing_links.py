#!/usr/bin/env python3
"""Find all pending and broken internal links."""

import csv
import re
import sys
from pathlib import Path


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown file without external dependencies."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    current_key = None
    current_list = None

    for line in match.group(1).split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List item
        if stripped.startswith("- ") and current_key:
            if current_list is None:
                current_list = []
                frontmatter[current_key] = current_list
            current_list.append(stripped[2:].strip().strip("\"'"))
        # Key: value pair
        elif ":" in line and not line.startswith(" ") and not line.startswith("\t"):
            key, _, value = line.partition(":")
            current_key = key.strip()
            value = value.strip().strip("\"'")
            current_list = None
            if value:
                frontmatter[current_key] = value

    return frontmatter


def get_all_slugs(project_path: Path) -> set[str]:
    """Get all content slugs in the project."""
    slugs = set()
    content_dir = project_path / "content"

    if content_dir.exists():
        for md_file in content_dir.rglob("*.md"):
            content = md_file.read_text()
            frontmatter = extract_frontmatter(content)
            slug = frontmatter.get("slug", "")
            if slug:
                slugs.add(slug.rstrip("/"))

    return slugs


def find_links_in_file(file_path: Path, project_path: Path, valid_slugs: set) -> list[dict]:
    """Find problematic links in a file."""
    issues = []
    content = file_path.read_text()
    rel_path = str(file_path.relative_to(project_path))
    lines = content.split("\n")

    for line_num, line in enumerate(lines, 1):
        # Find markdown links: [text](url)
        md_links = re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", line)
        for match in md_links:
            link_text = match.group(1)
            href = match.group(2)

            # Pending URL (just #)
            if href == "#":
                issues.append(
                    {
                        "file_path": rel_path,
                        "line_number": line_num,
                        "link_text": link_text,
                        "href": href,
                        "issue": "pending",
                    }
                )
            # Internal link (starts with /)
            elif href.startswith("/") and not href.startswith("//"):
                clean_href = href.rstrip("/").split("#")[0].split("?")[0]
                if clean_href and clean_href not in valid_slugs:
                    issues.append(
                        {
                            "file_path": rel_path,
                            "line_number": line_num,
                            "link_text": link_text,
                            "href": href,
                            "issue": "broken",
                        }
                    )

        # Find template syntax with url=#
        template_links = re.finditer(r"\{\{[^}]*url\s*=\s*#[^}]*\}\}", line)
        for match in template_links:
            issues.append(
                {
                    "file_path": rel_path,
                    "line_number": line_num,
                    "link_text": "(template)",
                    "href": "#",
                    "issue": "pending",
                }
            )

    return issues


def find_missing_links(project_path: Path) -> list[dict]:
    """Find all missing links in the project."""
    all_issues = []
    valid_slugs = get_all_slugs(project_path)

    # Scan all markdown files
    for md_file in project_path.rglob("*.md"):
        # Skip _validation folder
        if "_validation" in str(md_file):
            continue
        issues = find_links_in_file(md_file, project_path, valid_slugs)
        all_issues.extend(issues)

    return all_issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python find_missing_links.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    issues = find_missing_links(project_path)

    print(f"Scanning for missing links: {project_path}")
    print("-" * 40)

    if issues:
        # Create _validation directory if needed
        validation_dir = project_path / "_validation"
        validation_dir.mkdir(exist_ok=True)

        # Write CSV
        csv_path = validation_dir / "missing-links.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["file_path", "line_number", "link_text", "href", "issue"]
            )
            writer.writeheader()
            writer.writerows(issues)

        # Group by issue type
        pending = [i for i in issues if i["issue"] == "pending"]
        broken = [i for i in issues if i["issue"] == "broken"]

        if pending:
            print(f"\nPending links ({len(pending)}):")
            for issue in pending[:10]:
                print(f"  - {issue['file_path']}:{issue['line_number']} [{issue['link_text']}]")
            if len(pending) > 10:
                print(f"  ... and {len(pending) - 10} more")

        if broken:
            print(f"\nBroken internal links ({len(broken)}):")
            for issue in broken[:10]:
                print(
                    f"  - {issue['file_path']}:{issue['line_number']} [{issue['link_text']}]({issue['href']})"
                )
            if len(broken) > 10:
                print(f"  ... and {len(broken) - 10} more")

        print(f"\nResults written to: {csv_path}")
    else:
        print("\nNo missing or broken links found.")


if __name__ == "__main__":
    main()
