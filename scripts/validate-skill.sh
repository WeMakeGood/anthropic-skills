#!/bin/bash
#
# Validate Agent Skills against the specification
# Usage: ./validate-skill.sh <skill-path> | --all
#

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$REPO_ROOT/skills"

# Validation counters
ERRORS=0
WARNINGS=0

log_error() {
    echo -e "${RED}ERROR:${NC} $1"
    ((ERRORS++))
}

log_warning() {
    echo -e "${YELLOW}WARNING:${NC} $1"
    ((WARNINGS++))
}

log_success() {
    echo -e "${GREEN}OK:${NC} $1"
}

log_info() {
    echo -e "INFO: $1"
}

# Extract YAML frontmatter value
get_frontmatter_value() {
    local file="$1"
    local key="$2"

    # Extract content between --- markers and get the value
    sed -n '/^---$/,/^---$/p' "$file" | grep "^${key}:" | sed "s/^${key}:[[:space:]]*//" | sed 's/^["'\'']//' | sed 's/["'\'']$//'
}

# Check if frontmatter exists
has_frontmatter() {
    local file="$1"
    head -1 "$file" | grep -q '^---$'
}

# Validate a single skill
validate_skill() {
    local skill_path="$1"
    local skill_name="$(basename "$skill_path")"
    local skill_md="$skill_path/SKILL.md"

    echo ""
    echo "=========================================="
    echo "Validating: $skill_name"
    echo "=========================================="

    # Check SKILL.md exists
    if [[ ! -f "$skill_md" ]]; then
        log_error "SKILL.md not found in $skill_path"
        return 1
    fi
    log_success "SKILL.md exists"

    # Check frontmatter exists
    if ! has_frontmatter "$skill_md"; then
        log_error "SKILL.md must start with YAML frontmatter (---)"
        return 1
    fi
    log_success "YAML frontmatter present"

    # Validate name field
    local name=$(get_frontmatter_value "$skill_md" "name")
    if [[ -z "$name" ]]; then
        log_error "Missing required field: name"
    else
        # Check name length (max 64 chars)
        if [[ ${#name} -gt 64 ]]; then
            log_error "name exceeds 64 characters (${#name} chars)"
        fi

        # Check name format (lowercase, numbers, hyphens only)
        if ! echo "$name" | grep -qE '^[a-z0-9-]+$'; then
            log_error "name must contain only lowercase letters, numbers, and hyphens"
        fi

        # Check for reserved words
        if echo "$name" | grep -qiE '(anthropic|claude)'; then
            log_error "name cannot contain reserved words: 'anthropic', 'claude'"
        fi

        # Check name matches folder name
        if [[ "$name" != "$skill_name" ]]; then
            log_warning "name '$name' does not match folder name '$skill_name'"
        fi

        # Check for XML tags
        if echo "$name" | grep -qE '<[^>]+>'; then
            log_error "name cannot contain XML tags"
        fi

        if [[ $ERRORS -eq 0 ]] || [[ ${#name} -le 64 ]]; then
            log_success "name: $name"
        fi
    fi

    # Validate description field
    local description=$(get_frontmatter_value "$skill_md" "description")
    if [[ -z "$description" ]]; then
        log_error "Missing required field: description"
    else
        # Check description is non-empty
        if [[ ${#description} -eq 0 ]]; then
            log_error "description cannot be empty"
        fi

        # Check description length (max 1024 chars)
        if [[ ${#description} -gt 1024 ]]; then
            log_error "description exceeds 1024 characters (${#description} chars)"
        fi

        # Check for XML tags
        if echo "$description" | grep -qE '<[^>]+>'; then
            log_error "description cannot contain XML tags"
        fi

        # Check for first/second person (warning only)
        if echo "$description" | grep -qiE '\b(I can|I will|you can|you will)\b'; then
            log_warning "description should use third person (avoid 'I can', 'you can', etc.)"
        fi

        log_success "description present (${#description} chars)"
    fi

    # Check SKILL.md line count
    local line_count=$(wc -l < "$skill_md" | tr -d ' ')
    if [[ $line_count -gt 500 ]]; then
        log_warning "SKILL.md has $line_count lines (recommended: under 500)"
    else
        log_success "SKILL.md line count: $line_count"
    fi

    # Check for Windows-style paths
    if grep -qE '\\[a-zA-Z]' "$skill_md"; then
        log_warning "Possible Windows-style paths detected (use forward slashes)"
    fi

    # Summary
    echo ""
    if [[ $ERRORS -gt 0 ]]; then
        echo -e "${RED}FAILED:${NC} $ERRORS error(s), $WARNINGS warning(s)"
        return 1
    elif [[ $WARNINGS -gt 0 ]]; then
        echo -e "${YELLOW}PASSED with warnings:${NC} $WARNINGS warning(s)"
        return 0
    else
        echo -e "${GREEN}PASSED:${NC} All checks passed"
        return 0
    fi
}

# Validate all skills
validate_all() {
    local total=0
    local passed=0
    local failed=0

    echo "Validating all skills in $SKILLS_DIR"

    for skill_dir in "$SKILLS_DIR"/*/; do
        if [[ -d "$skill_dir" ]]; then
            # Reset counters for each skill
            ERRORS=0
            WARNINGS=0

            ((total++))
            if validate_skill "$skill_dir"; then
                ((passed++))
            else
                ((failed++))
            fi
        fi
    done

    echo ""
    echo "=========================================="
    echo "SUMMARY"
    echo "=========================================="
    echo "Total:  $total"
    echo -e "${GREEN}Passed: $passed${NC}"
    if [[ $failed -gt 0 ]]; then
        echo -e "${RED}Failed: $failed${NC}"
        exit 1
    fi
}

# Main
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <skill-path> | --all"
    echo ""
    echo "Options:"
    echo "  <skill-path>  Path to a skill directory to validate"
    echo "  --all         Validate all skills in the skills/ directory"
    exit 1
fi

if [[ "$1" == "--all" ]]; then
    validate_all
else
    ERRORS=0
    WARNINGS=0
    validate_skill "$1"
    exit $?
fi
