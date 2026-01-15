#!/usr/bin/env python3
"""Generate completion status report."""

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


def count_sitemap_entries(project_path: Path) -> int:
    """Count pages defined in sitemap."""
    sitemap_path = project_path / "sitemap.md"
    if not sitemap_path.exists():
        return 0

    content = sitemap_path.read_text()
    # Count slug patterns like (/path/)
    matches = re.findall(r"\((/[^)]+)\)", content)
    return len(matches)


def count_content_files(project_path: Path) -> dict:
    """Count content files by type."""
    counts = {"pages": 0, "posts": 0, "cpts": {}}
    content_dir = project_path / "content"

    if not content_dir.exists():
        return counts

    # Count pages
    pages_dir = content_dir / "pages"
    if pages_dir.exists():
        counts["pages"] = len(list(pages_dir.glob("*.md")))

    # Count posts
    posts_dir = content_dir / "posts"
    if posts_dir.exists():
        counts["posts"] = len(list(posts_dir.glob("*.md")))

    # Count CPT content
    for item in content_dir.iterdir():
        if item.is_dir() and item.name not in ["pages", "posts"]:
            counts["cpts"][item.name] = len(list(item.glob("*.md")))

    return counts


def count_forms(project_path: Path) -> tuple[int, int]:
    """Count forms specified vs referenced."""
    forms_dir = project_path / "forms"
    specified = 0
    if forms_dir.exists():
        specified = len(list(forms_dir.glob("*.md")))

    # Count form references in content
    referenced = set()
    for md_file in project_path.rglob("*.md"):
        if "forms" in str(md_file):
            continue
        content = md_file.read_text()
        form_refs = re.findall(r"\{\{form:\s*([^|}]+)", content)
        referenced.update(f.strip() for f in form_refs)

    return specified, len(referenced)


def count_placeholders(project_path: Path) -> dict:
    """Count placeholder patterns."""
    counts = {"needs_input": 0, "placeholder": 0, "verify": 0}

    for md_file in project_path.rglob("*.md"):
        if "_validation" in str(md_file):
            continue
        content = md_file.read_text()
        counts["needs_input"] += len(re.findall(r"\{\{needs-input:", content))
        counts["placeholder"] += len(re.findall(r"\{\{placeholder:", content))
        counts["verify"] += len(re.findall(r"\{\{verify:", content))

    return counts


def count_pending_links(project_path: Path) -> int:
    """Count pending internal links."""
    count = 0
    for md_file in project_path.rglob("*.md"):
        if "_validation" in str(md_file):
            continue
        content = md_file.read_text()
        # Links with # as href
        count += len(re.findall(r"\]\(#\)", content))
        # Template syntax with url=#
        count += len(re.findall(r"url\s*=\s*#", content))

    return count


def check_strategy_complete(project_path: Path) -> dict:
    """Check if strategy documents are complete."""
    strategy_dir = project_path / "strategy"
    status = {
        "calls-to-action.md": False,
        "audience-analysis.md": False,
        "conversion-strategy.md": False,
    }

    if strategy_dir.exists():
        for name in status:
            file_path = strategy_dir / name
            if file_path.exists():
                content = file_path.read_text()
                # Check if file has content beyond frontmatter
                body = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)
                status[name] = len(body.strip()) > 50

    return status


def generate_checklist(project_path: Path) -> str:
    """Generate the completion checklist."""
    lines = ["# Project Completion Checklist", ""]

    # Strategy status
    lines.append("## Strategy Documents")
    strategy = check_strategy_complete(project_path)
    for name, complete in strategy.items():
        status = "x" if complete else " "
        lines.append(f"- [{status}] {name}")
    lines.append("")

    # Sitemap status
    lines.append("## Architecture")
    sitemap_exists = (project_path / "sitemap.md").exists()
    sitemap_entries = count_sitemap_entries(project_path)
    lines.append(f"- [{'x' if sitemap_exists else ' '}] sitemap.md ({sitemap_entries} entries)")

    templates_dir = project_path / "templates"
    template_count = len(list(templates_dir.glob("*.md"))) if templates_dir.exists() else 0
    lines.append(f"- [{'x' if template_count > 0 else ' '}] templates/ ({template_count} templates)")
    lines.append("")

    # Content status
    lines.append("## Content Files")
    content = count_content_files(project_path)
    lines.append(f"- Pages: {content['pages']} of {sitemap_entries} sitemap entries")
    lines.append(f"- Posts: {content['posts']}")
    for cpt_name, cpt_count in content["cpts"].items():
        lines.append(f"- {cpt_name}: {cpt_count}")
    lines.append("")

    # Forms status
    lines.append("## Forms")
    specified, referenced = count_forms(project_path)
    lines.append(f"- Specified: {specified}")
    lines.append(f"- Referenced in content: {referenced}")
    if referenced > specified:
        lines.append(f"- **Warning:** {referenced - specified} referenced form(s) not specified")
    lines.append("")

    # Validation issues
    lines.append("## Validation Issues")
    placeholders = count_placeholders(project_path)
    pending_links = count_pending_links(project_path)

    total_issues = sum(placeholders.values()) + pending_links
    if total_issues == 0:
        lines.append("- No validation issues found")
    else:
        if placeholders["needs_input"] > 0:
            lines.append(f"- Needs input: {placeholders['needs_input']}")
        if placeholders["placeholder"] > 0:
            lines.append(f"- Placeholders: {placeholders['placeholder']}")
        if placeholders["verify"] > 0:
            lines.append(f"- Needs verification: {placeholders['verify']}")
        if pending_links > 0:
            lines.append(f"- Pending links: {pending_links}")
    lines.append("")

    # Summary
    lines.append("## Summary")
    strategy_complete = all(strategy.values())
    content_complete = content["pages"] >= sitemap_entries if sitemap_entries > 0 else False
    forms_complete = specified >= referenced

    if strategy_complete and content_complete and forms_complete and total_issues == 0:
        lines.append("**Status: COMPLETE**")
    else:
        lines.append("**Status: IN PROGRESS**")
        if not strategy_complete:
            lines.append("- [ ] Complete strategy documents")
        if not content_complete:
            lines.append(f"- [ ] Create {sitemap_entries - content['pages']} more page(s)")
        if not forms_complete:
            lines.append(f"- [ ] Specify {referenced - specified} more form(s)")
        if total_issues > 0:
            lines.append(f"- [ ] Resolve {total_issues} validation issue(s)")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_checklist.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    checklist = generate_checklist(project_path)

    # Create _validation directory if needed
    validation_dir = project_path / "_validation"
    validation_dir.mkdir(exist_ok=True)

    # Write checklist
    checklist_path = validation_dir / "checklist.md"
    checklist_path.write_text(checklist)

    print(checklist)
    print(f"\nChecklist written to: {checklist_path}")


if __name__ == "__main__":
    main()
