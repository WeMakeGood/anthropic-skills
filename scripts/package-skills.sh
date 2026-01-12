#!/bin/bash
#
# Package all skills into individual zip files for distribution.
#
# Usage:
#   ./scripts/package-skills.sh           # Package all skills
#   ./scripts/package-skills.sh my-skill  # Package specific skill
#
# Output goes to dist/ directory.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$REPO_ROOT/skills"
DIST_DIR="$REPO_ROOT/dist"

# Create dist directory if it doesn't exist
mkdir -p "$DIST_DIR"

package_skill() {
    local skill_name="$1"
    local skill_path="$SKILLS_DIR/$skill_name"

    if [[ ! -d "$skill_path" ]]; then
        echo "Error: Skill '$skill_name' not found at $skill_path"
        return 1
    fi

    if [[ ! -f "$skill_path/SKILL.md" ]]; then
        echo "Warning: Skipping '$skill_name' - no SKILL.md found"
        return 0
    fi

    local zip_file="$DIST_DIR/${skill_name}.zip"

    echo "Packaging: $skill_name"

    # Remove existing zip if present
    rm -f "$zip_file"

    # Create zip from skills directory, excluding temp and cache files
    (cd "$SKILLS_DIR" && zip -r "$zip_file" "$skill_name/" \
        -x "*.DS_Store" \
        -x "*__pycache__*" \
        -x "*.pyc" \
        -x "*/tmp/*" \
        -x "*/.git/*" \
        -x "*.log")

    echo "  Created: dist/${skill_name}.zip"
}

# Main logic
if [[ $# -eq 0 ]]; then
    # Package all skills
    echo "Packaging all skills..."
    echo ""

    for skill_dir in "$SKILLS_DIR"/*/; do
        if [[ -d "$skill_dir" ]]; then
            skill_name=$(basename "$skill_dir")
            # Skip hidden directories and non-skill directories
            if [[ "$skill_name" != .* ]] && [[ -f "$skill_dir/SKILL.md" ]]; then
                package_skill "$skill_name"
            fi
        fi
    done

    echo ""
    echo "Done. Packages in dist/:"
    ls -la "$DIST_DIR"/*.zip 2>/dev/null || echo "  (no packages created)"
else
    # Package specific skill(s)
    for skill_name in "$@"; do
        package_skill "$skill_name"
    done
fi
