#!/usr/bin/env python3
"""Find pages without clear CTAs."""

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


def has_cta_section(content: str) -> bool:
    """Check if content has a CTA section in the body."""
    # Look for common CTA patterns
    patterns = [
        r"##\s*Take Action",
        r"##\s*Get Started",
        r"##\s*Call to Action",
        r"##\s*Next Steps",
        r"\{\{button:",
        r"cta_primary:",
    ]
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False


def find_orphaned_pages(project_path: Path) -> list[dict]:
    """Find content files without clear CTAs."""
    orphans = []
    content_dir = project_path / "content"

    if not content_dir.exists():
        return orphans

    for md_file in content_dir.rglob("*.md"):
        content = md_file.read_text()
        frontmatter = extract_frontmatter(content)

        title = frontmatter.get("title", md_file.stem)
        has_frontmatter_cta = bool(frontmatter.get("cta_primary"))
        has_body_cta = has_cta_section(content)

        if not has_frontmatter_cta and not has_body_cta:
            rel_path = str(md_file.relative_to(project_path))
            orphans.append(
                {
                    "file_path": rel_path,
                    "title": title,
                    "issue": "No CTA in frontmatter or body",
                }
            )
        elif not has_frontmatter_cta:
            rel_path = str(md_file.relative_to(project_path))
            orphans.append(
                {
                    "file_path": rel_path,
                    "title": title,
                    "issue": "No cta_primary in frontmatter (has body CTA)",
                }
            )

    return orphans


def main():
    if len(sys.argv) < 2:
        print("Usage: python find_orphans.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    orphans = find_orphaned_pages(project_path)

    print(f"Scanning for orphaned pages: {project_path}")
    print("-" * 40)

    if orphans:
        # Create _validation directory if needed
        validation_dir = project_path / "_validation"
        validation_dir.mkdir(exist_ok=True)

        # Write CSV
        csv_path = validation_dir / "orphaned-pages.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["file_path", "title", "issue"])
            writer.writeheader()
            writer.writerows(orphans)

        print(f"\nFound {len(orphans)} page(s) without clear CTAs:")
        for orphan in orphans:
            print(f"  - {orphan['file_path']}: {orphan['issue']}")

        print(f"\nResults written to: {csv_path}")
    else:
        print("\nAll pages have clear CTAs.")


if __name__ == "__main__":
    main()
