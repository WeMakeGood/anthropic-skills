#!/usr/bin/env python3
"""
Count tokens in context library modules and calculate agent budgets.
"""

import os
import sys
import re
import yaml
from pathlib import Path


def estimate_tokens(text: str) -> int:
    """Estimate tokens (roughly 0.75 words per token for English)."""
    words = len(text.split())
    return int(words / 0.75)


def parse_frontmatter(content: str) -> tuple:
    """Extract YAML frontmatter and body from markdown."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2]
                return frontmatter, body
            except yaml.YAMLError:
                pass
    return {}, content


def analyze_module(filepath: Path) -> dict:
    """Analyze a single module file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        return {
            'path': str(filepath),
            'name': filepath.stem,
            'module_id': frontmatter.get('module_id', filepath.stem),
            'module_name': frontmatter.get('module_name', filepath.stem),
            'tier': frontmatter.get('tier', 'unknown'),
            'tokens': estimate_tokens(content),
            'error': None
        }
    except Exception as e:
        return {
            'path': str(filepath),
            'name': filepath.stem,
            'error': str(e)
        }


def analyze_agent(filepath: Path) -> dict:
    """Analyze an agent definition file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        modules = frontmatter.get('modules', {})
        all_modules = []
        for tier_modules in modules.values():
            if isinstance(tier_modules, list):
                all_modules.extend(tier_modules)

        return {
            'path': str(filepath),
            'name': frontmatter.get('agent_name', filepath.stem),
            'modules': all_modules,
            'stated_tokens': frontmatter.get('estimated_tokens'),
            'error': None
        }
    except Exception as e:
        return {
            'path': str(filepath),
            'name': filepath.stem,
            'error': str(e)
        }


def find_modules(library_dir: Path) -> list:
    """Find all module files in library."""
    modules = []
    for subdir in ['foundation', 'shared', 'specialized']:
        subpath = library_dir / subdir
        if subpath.exists():
            modules.extend(subpath.glob('*.md'))
    return modules


def main():
    if len(sys.argv) < 2:
        print("Usage: count_tokens.py <library_dir> [agents_dir]")
        print("  library_dir: Path to library/ folder with modules")
        print("  agents_dir: Optional path to agents/ folder")
        sys.exit(1)

    library_dir = Path(sys.argv[1])
    agents_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not library_dir.exists():
        print(f"Error: Library directory '{library_dir}' not found")
        sys.exit(1)

    # Analyze modules
    module_files = find_modules(library_dir)
    modules = {}

    print("Token Count Report")
    print("==================")
    print()
    print("MODULES")
    print("-" * 60)
    print(f"{'Module ID':<20} {'Tier':<15} {'Tokens':>10}")
    print("-" * 60)

    total_tokens = 0
    for mf in sorted(module_files):
        result = analyze_module(mf)
        if result.get('error'):
            print(f"{result['name']:<20} ERROR: {result['error']}")
        else:
            modules[result['module_id']] = result
            print(f"{result['module_id']:<20} {result['tier']:<15} {result['tokens']:>10}")
            total_tokens += result['tokens']

    print("-" * 60)
    print(f"{'TOTAL':<35} {total_tokens:>10}")
    print()

    # Analyze agents if provided
    if agents_dir and agents_dir.exists():
        agent_files = list(agents_dir.glob('*.md'))

        if agent_files:
            print("AGENT TOKEN BUDGETS")
            print("-" * 70)
            print(f"{'Agent':<30} {'Tokens':>10} {'% of 20K':>10} {'Status':>10}")
            print("-" * 70)

            TOKEN_LIMIT = 20000

            for af in sorted(agent_files):
                agent = analyze_agent(af)
                if agent.get('error'):
                    print(f"{agent['name']:<30} ERROR: {agent['error']}")
                    continue

                # Calculate actual tokens from modules
                agent_tokens = 0
                missing_modules = []
                for mod_id in agent['modules']:
                    # Try to match module by ID or filename
                    matched = False
                    for mid, mdata in modules.items():
                        if mid == mod_id or mdata['name'] == mod_id:
                            agent_tokens += mdata['tokens']
                            matched = True
                            break
                    if not matched:
                        missing_modules.append(mod_id)

                pct = (agent_tokens / TOKEN_LIMIT) * 100
                status = "OK" if agent_tokens < TOKEN_LIMIT else "OVER"
                if pct > 80:
                    status = "WARN" if status == "OK" else status

                print(f"{agent['name']:<30} {agent_tokens:>10} {pct:>9.1f}% {status:>10}")

                if missing_modules:
                    print(f"  Missing: {', '.join(missing_modules)}")

            print("-" * 70)
            print()
            print("Status: OK = under 80%, WARN = 80-100%, OVER = exceeds limit")

    else:
        print("No agents directory provided. Run with agents path to check budgets:")
        print(f"  python count_tokens.py {library_dir} ./agents")


if __name__ == '__main__':
    main()
