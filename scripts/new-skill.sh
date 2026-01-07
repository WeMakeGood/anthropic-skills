#!/bin/bash
#
# Create a new skill from template
# Usage: ./new-skill.sh <skill-name>
#

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$REPO_ROOT/skills"
TEMPLATE_FILE="$REPO_ROOT/templates/SKILL.template.md"

# Validate skill name
validate_name() {
    local name="$1"

    # Check length
    if [[ ${#name} -gt 64 ]]; then
        echo -e "${RED}Error:${NC} Skill name exceeds 64 characters"
        exit 1
    fi

    # Check format
    if ! echo "$name" | grep -qE '^[a-z0-9-]+$'; then
        echo -e "${RED}Error:${NC} Skill name must contain only lowercase letters, numbers, and hyphens"
        exit 1
    fi

    # Check reserved words
    if echo "$name" | grep -qiE '(anthropic|claude)'; then
        echo -e "${RED}Error:${NC} Skill name cannot contain reserved words: 'anthropic', 'claude'"
        exit 1
    fi
}

# Convert hyphenated name to title case
to_title_case() {
    echo "$1" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1'
}

# Main
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <skill-name>"
    echo ""
    echo "Creates a new skill directory with SKILL.md from template."
    echo ""
    echo "Arguments:"
    echo "  skill-name    Lowercase name with hyphens (e.g., 'pdf-processing')"
    echo ""
    echo "Examples:"
    echo "  $0 pdf-processing"
    echo "  $0 analyzing-spreadsheets"
    echo "  $0 code-review"
    exit 1
fi

SKILL_NAME="$1"

# Validate the name
validate_name "$SKILL_NAME"

# Check if skill already exists
SKILL_DIR="$SKILLS_DIR/$SKILL_NAME"
if [[ -d "$SKILL_DIR" ]]; then
    echo -e "${RED}Error:${NC} Skill '$SKILL_NAME' already exists at $SKILL_DIR"
    exit 1
fi

# Check template exists
if [[ ! -f "$TEMPLATE_FILE" ]]; then
    echo -e "${RED}Error:${NC} Template not found at $TEMPLATE_FILE"
    exit 1
fi

# Create skill directory
mkdir -p "$SKILL_DIR"

# Generate title from name
SKILL_TITLE=$(to_title_case "$SKILL_NAME")

# Copy and customize template
sed -e "s/{{SKILL_NAME}}/$SKILL_NAME/g" \
    -e "s/{{SKILL_TITLE}}/$SKILL_TITLE/g" \
    "$TEMPLATE_FILE" > "$SKILL_DIR/SKILL.md"

echo -e "${GREEN}Created skill:${NC} $SKILL_DIR"
echo ""
echo "Next steps:"
echo "  1. Edit $SKILL_DIR/SKILL.md"
echo "  2. Update the description to explain what the skill does and when to use it"
echo "  3. Add instructions in the body of SKILL.md"
echo "  4. Validate with: ./scripts/validate-skill.sh $SKILL_DIR"
echo "  5. Test locally via .claude/skills/ symlink"
