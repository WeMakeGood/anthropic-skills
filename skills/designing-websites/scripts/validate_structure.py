#!/usr/bin/env python3
"""Validate website project folder structure is complete."""

import sys
from pathlib import Path


def validate_structure(project_path: Path) -> tuple[bool, list[str]]:
    """Validate project has required structure."""
    errors = []
    warnings = []

    # Required folders
    required_folders = [
        "strategy",
        "templates",
        "content",
        "content/pages",
    ]

    # Required files
    required_files = [
        "strategy/calls-to-action.md",
        "strategy/audience-analysis.md",
        "sitemap.md",
    ]

    # Check folders
    for folder in required_folders:
        folder_path = project_path / folder
        if not folder_path.exists():
            errors.append(f"Missing required folder: {folder}/")
        elif not folder_path.is_dir():
            errors.append(f"Expected folder but found file: {folder}")

    # Check files
    for file in required_files:
        file_path = project_path / file
        if not file_path.exists():
            errors.append(f"Missing required file: {file}")

    # Check for at least one content file
    content_pages = project_path / "content" / "pages"
    if content_pages.exists():
        md_files = list(content_pages.glob("*.md"))
        if not md_files:
            warnings.append("No content files found in content/pages/")

    # Optional but recommended
    optional_folders = ["forms", "cpts", "globals", "_validation"]
    for folder in optional_folders:
        if not (project_path / folder).exists():
            warnings.append(f"Optional folder not found: {folder}/")

    return len(errors) == 0, errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_structure.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    valid, errors, warnings = validate_structure(project_path)

    print(f"Validating: {project_path}")
    print("-" * 40)

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if valid and not warnings:
        print("\nStructure is complete.")
    elif valid:
        print(f"\nStructure valid with {len(warnings)} warning(s).")
    else:
        print(f"\nStructure invalid: {len(errors)} error(s).")
        sys.exit(1)


if __name__ == "__main__":
    main()
