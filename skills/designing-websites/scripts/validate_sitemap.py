#!/usr/bin/env python3
"""Cross-reference sitemap with content files."""

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


def extract_sitemap_pages(sitemap_content: str) -> set[str]:
    """Extract page slugs from sitemap."""
    slugs = set()
    # Match patterns like (/path/) or (/path/subpath/)
    pattern = r"\((/[^)]*)\)"
    for match in re.finditer(pattern, sitemap_content):
        slug = match.group(1).rstrip("/")
        if slug:
            slugs.add(slug)
    return slugs


def get_content_slugs(project_path: Path) -> dict[str, str]:
    """Get all content file slugs mapped to file paths."""
    slugs = {}
    content_dir = project_path / "content"

    if not content_dir.exists():
        return slugs

    for md_file in content_dir.rglob("*.md"):
        content = md_file.read_text()
        frontmatter = extract_frontmatter(content)
        slug = frontmatter.get("slug", "")
        if slug:
            slug = slug.rstrip("/")
            slugs[slug] = str(md_file.relative_to(project_path))

    return slugs


def validate_sitemap(project_path: Path) -> tuple[list, list, list]:
    """Validate sitemap against content files."""
    sitemap_path = project_path / "sitemap.md"

    if not sitemap_path.exists():
        return [], [], ["sitemap.md not found"]

    sitemap_content = sitemap_path.read_text()
    sitemap_slugs = extract_sitemap_pages(sitemap_content)
    content_slugs = get_content_slugs(project_path)

    # Pages in sitemap but no content file
    missing_content = []
    for slug in sitemap_slugs:
        if slug not in content_slugs:
            missing_content.append(slug)

    # Content files not in sitemap
    orphaned_content = []
    for slug, path in content_slugs.items():
        if slug not in sitemap_slugs:
            orphaned_content.append(f"{slug} ({path})")

    return sorted(missing_content), sorted(orphaned_content), []


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_sitemap.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    missing_content, orphaned_content, errors = validate_sitemap(project_path)

    print(f"Validating sitemap: {project_path}")
    print("-" * 40)

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    if missing_content:
        print(f"\nPages in sitemap without content files ({len(missing_content)}):")
        for slug in missing_content:
            print(f"  - {slug}")

    if orphaned_content:
        print(f"\nContent files not in sitemap ({len(orphaned_content)}):")
        for item in orphaned_content:
            print(f"  - {item}")

    if not missing_content and not orphaned_content:
        print("\nSitemap and content files are in sync.")
    else:
        total = len(missing_content) + len(orphaned_content)
        print(f"\nFound {total} discrepancy(ies).")


if __name__ == "__main__":
    main()
