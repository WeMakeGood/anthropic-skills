#!/usr/bin/env python3
"""Generate CPT/ACF configuration from YAML source."""

import json
import re
import sys
from pathlib import Path

# ACF field type mappings
ACF_FIELD_TYPES = {
    "text",
    "textarea",
    "number",
    "range",
    "email",
    "url",
    "password",
    "wysiwyg",
    "oembed",
    "image",
    "file",
    "gallery",
    "select",
    "checkbox",
    "radio",
    "button_group",
    "true_false",
    "link",
    "post_object",
    "page_link",
    "relationship",
    "taxonomy",
    "user",
    "google_map",
    "date_picker",
    "date_time_picker",
    "time_picker",
    "color_picker",
    "message",
    "accordion",
    "tab",
    "group",
    "repeater",
    "flexible_content",
    "clone",
}


def parse_yaml_simple(content: str) -> dict:
    """Parse simple YAML without external dependencies.

    Handles:
    - Top-level keys
    - Lists of dictionaries
    - Nested dictionaries (one level)
    - Simple values
    """
    result = {}
    lines = content.split("\n")

    i = 0
    current_top_key = None
    current_list = None
    current_dict = None

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines and comments
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        # Calculate indentation
        indent = len(line) - len(line.lstrip())

        # Top-level key (no indentation, ends with :)
        if indent == 0 and ":" in line:
            # Save previous list if any
            if current_list is not None and current_top_key:
                if current_dict:
                    current_list.append(current_dict)
                    current_dict = None
                result[current_top_key] = current_list

            key, _, value = line.partition(":")
            current_top_key = key.strip()
            value = value.strip()
            current_list = None
            current_dict = None

            if value:
                result[current_top_key] = value.strip("\"'")
            i += 1
            continue

        # List item at first indent level
        if stripped.startswith("- ") and indent == 2:
            # Save previous dict
            if current_dict and current_list is not None:
                current_list.append(current_dict)

            if current_list is None:
                current_list = []

            # Check if it's a key-value on same line: - key: value
            item_content = stripped[2:].strip()
            if ":" in item_content:
                current_dict = {}
                key, _, value = item_content.partition(":")
                value = value.strip().strip("\"'")
                if value:
                    current_dict[key.strip()] = value
            else:
                # Simple list item
                if current_list is None:
                    current_list = []
                current_list.append(item_content.strip("\"'"))
                current_dict = None
            i += 1
            continue

        # Nested key-value within a list item (indent 4+)
        if indent >= 4 and ":" in line and current_dict is not None:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip().strip("\"'")

            # Check if this starts a nested list
            if not value:
                # Could be start of nested list, peek ahead
                nested_list = []
                j = i + 1
                while j < len(lines):
                    next_line = lines[j]
                    next_stripped = next_line.strip()
                    next_indent = len(next_line) - len(next_line.lstrip())

                    if next_indent <= indent and next_stripped:
                        break
                    if next_stripped.startswith("- "):
                        nested_list.append(next_stripped[2:].strip().strip("\"'"))
                        j += 1
                    elif not next_stripped:
                        j += 1
                    else:
                        break

                if nested_list:
                    current_dict[key] = nested_list
                    i = j
                    continue
            else:
                # Handle boolean-like values
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
                current_dict[key] = value
            i += 1
            continue

        # Nested list item within dict (for fields array)
        if stripped.startswith("- ") and indent >= 4 and current_dict is not None:
            # This is likely a nested list like fields:
            # Find the parent key by looking back
            parent_key = None
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line.endswith(":") and not prev_line.startswith("-"):
                    parent_key = prev_line[:-1].strip()
                    break

            if parent_key:
                if parent_key not in current_dict:
                    current_dict[parent_key] = []

                # Parse the nested dict
                nested_dict = {}
                item_content = stripped[2:].strip()
                if ":" in item_content:
                    k, _, v = item_content.partition(":")
                    v = v.strip().strip("\"'")
                    if v.lower() == "true":
                        v = True
                    elif v.lower() == "false":
                        v = False
                    if v:
                        nested_dict[k.strip()] = v

                # Continue reading nested dict properties
                j = i + 1
                while j < len(lines):
                    next_line = lines[j]
                    next_stripped = next_line.strip()
                    next_indent = len(next_line) - len(next_line.lstrip())

                    if not next_stripped:
                        j += 1
                        continue
                    if next_indent <= indent:
                        break
                    if next_stripped.startswith("- "):
                        break
                    if ":" in next_stripped:
                        k, _, v = next_stripped.partition(":")
                        v = v.strip().strip("\"'")
                        if v.lower() == "true":
                            v = True
                        elif v.lower() == "false":
                            v = False
                        if v:
                            nested_dict[k.strip()] = v
                    j += 1

                if nested_dict:
                    current_dict[parent_key].append(nested_dict)
                i = j
                continue

        i += 1

    # Save final list
    if current_list is not None and current_top_key:
        if current_dict:
            current_list.append(current_dict)
        result[current_top_key] = current_list

    return result


def generate_field_key(group_key: str, field_name: str) -> str:
    """Generate ACF-style field key."""
    return f"field_{group_key}_{field_name}"


def generate_group_key(group_name: str) -> str:
    """Generate ACF-style group key."""
    clean_name = group_name.lower().replace(" ", "_").replace("-", "_")
    return f"group_{clean_name}"


def validate_field_type(field_type: str) -> bool:
    """Check if field type is valid ACF type."""
    return field_type.lower() in ACF_FIELD_TYPES


def generate_markdown_spec(config: dict) -> str:
    """Generate human-readable markdown specification."""
    lines = ["# Custom Post Types and Fields Specification", ""]

    # Custom Post Types
    if "post_types" in config:
        lines.append("## Custom Post Types")
        lines.append("")

        for cpt in config["post_types"]:
            lines.append(f"### {cpt.get('plural', cpt.get('slug', 'Unknown'))}")
            lines.append(f"- **Slug:** {cpt.get('slug', '')}")
            lines.append(f"- **Singular:** {cpt.get('singular', '')}")
            lines.append(f"- **Plural:** {cpt.get('plural', '')}")
            lines.append(f"- **Public:** {'Yes' if cpt.get('public', True) else 'No'}")
            lines.append(f"- **Has Archive:** {'Yes' if cpt.get('has_archive', True) else 'No'}")
            if cpt.get("archive_slug"):
                lines.append(f"  (/{cpt['archive_slug']}/)")
            supports = cpt.get("supports", ["title", "editor", "thumbnail"])
            if isinstance(supports, list):
                lines.append(f"- **Supports:** {', '.join(supports)}")
            if cpt.get("menu_icon"):
                lines.append(f"- **Menu Icon:** {cpt['menu_icon']}")
            lines.append("")

    # Taxonomies
    if "taxonomies" in config:
        lines.append("## Custom Taxonomies")
        lines.append("")

        for tax in config["taxonomies"]:
            lines.append(f"### {tax.get('name', 'Unknown')}")
            lines.append(f"- **Slug:** {tax.get('slug', '')}")
            post_types = tax.get('post_types', [])
            if isinstance(post_types, list):
                lines.append(f"- **Applies to:** {', '.join(post_types)}")
            lines.append(f"- **Hierarchical:** {'Yes' if tax.get('hierarchical', True) else 'No'}")
            terms = tax.get("terms", [])
            if terms and isinstance(terms, list):
                lines.append(f"- **Terms:** {', '.join(terms)}")
            lines.append("")

    # ACF Field Groups
    if "field_groups" in config:
        lines.append("## ACF Field Groups")
        lines.append("")

        for group in config["field_groups"]:
            lines.append(f"### {group.get('title', 'Unknown')}")
            lines.append(f"**Location:** {group.get('location', '')}")
            lines.append("")
            lines.append("| Field Name | Field Type | Required | Notes |")
            lines.append("|------------|------------|----------|-------|")

            for field in group.get("fields", []):
                required = "yes" if field.get("required", False) else "no"
                notes = field.get("notes", "")
                lines.append(f"| {field.get('name', '')} | {field.get('type', '')} | {required} | {notes} |")

            lines.append("")

    return "\n".join(lines)


def generate_acf_json(config: dict) -> list:
    """Generate ACF Pro JSON import format."""
    field_groups = []

    if "field_groups" not in config:
        return field_groups

    for group in config["field_groups"]:
        group_key = generate_group_key(group.get("title", "unknown"))

        acf_fields = []
        for field in group.get("fields", []):
            field_type = field.get("type", "text").lower()

            if not validate_field_type(field_type):
                print(f"Warning: Unknown field type '{field_type}' for field '{field.get('name', '')}'")

            acf_field = {
                "key": generate_field_key(group_key, field.get("name", "")),
                "label": field.get("label", field.get("name", "").replace("_", " ").title()),
                "name": field.get("name", ""),
                "type": field_type,
                "required": 1 if field.get("required", False) else 0,
            }

            # Add type-specific properties
            if field_type == "select" and "choices" in field:
                choices = field["choices"]
                if isinstance(choices, list):
                    acf_field["choices"] = {c: c for c in choices}

            if field_type in ["textarea", "wysiwyg"]:
                acf_field["rows"] = field.get("rows", 4)

            if field_type == "number":
                if "min" in field:
                    acf_field["min"] = field["min"]
                if "max" in field:
                    acf_field["max"] = field["max"]

            if field.get("instructions"):
                acf_field["instructions"] = field["instructions"]

            acf_fields.append(acf_field)

        # Build location rules
        location = group.get("location", "")
        location_rules = []

        if location.startswith("post_type:"):
            post_type = location.replace("post_type:", "").strip()
            location_rules = [[{"param": "post_type", "operator": "==", "value": post_type}]]
        elif location.startswith("page_template:"):
            template = location.replace("page_template:", "").strip()
            location_rules = [[{"param": "page_template", "operator": "==", "value": template}]]
        else:
            # Assume it's a post type slug
            location_rules = [[{"param": "post_type", "operator": "==", "value": location}]]

        acf_group = {
            "key": group_key,
            "title": group.get("title", ""),
            "fields": acf_fields,
            "location": location_rules,
            "menu_order": group.get("menu_order", 0),
            "position": group.get("position", "normal"),
            "style": group.get("style", "default"),
            "label_placement": "top",
            "instruction_placement": "label",
            "active": True,
        }

        field_groups.append(acf_group)

    return field_groups


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_cpt_spec.py <yaml_file_or_project_path>")
        print("")
        print("If given a YAML file, generates spec.md and acf-export.json from it.")
        print("If given a project path, looks for cpts/source.yaml.")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    # Determine source file and output directory
    if input_path.suffix in [".yaml", ".yml"]:
        source_file = input_path
        output_dir = input_path.parent
    else:
        # Assume project directory
        source_file = input_path / "cpts" / "source.yaml"
        output_dir = input_path / "cpts"

    if not source_file.exists():
        print(f"Error: Source file not found: {source_file}")
        print("")
        print("Create a YAML file with this structure:")
        print("---")
        print("post_types:")
        print("  - slug: team-member")
        print("    singular: Team Member")
        print("    plural: Team Members")
        print("field_groups:")
        print("  - title: Team Member Details")
        print("    location: team-member")
        print("    fields:")
        print("      - name: job_title")
        print("        type: text")
        print("        required: true")
        sys.exit(1)

    # Load config using simple parser
    content = source_file.read_text()
    config = parse_yaml_simple(content)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate markdown spec
    spec_content = generate_markdown_spec(config)
    spec_path = output_dir / "spec.md"
    spec_path.write_text(spec_content)
    print(f"Generated: {spec_path}")

    # Generate ACF JSON
    acf_data = generate_acf_json(config)
    json_path = output_dir / "acf-export.json"
    with open(json_path, "w") as f:
        json.dump(acf_data, f, indent=2)
    print(f"Generated: {json_path}")

    print("")
    print("Done! Review the generated files and import acf-export.json into WordPress.")


if __name__ == "__main__":
    main()
