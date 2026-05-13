#!/usr/bin/env python3
"""
Diagnostic script to identify LaTeX formula issues in Markdown files.
"""

import re
from pathlib import Path

def find_formula_issues(md_file):
    """Analyze Markdown file for formula formatting issues."""
    print(f"\nAnalyzing: {md_file}")
    print("=" * 60)
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Count different formula formats
    display_formulas = len(re.findall(r'\$\$', content))
    inline_formulas = len(re.findall(r'(?<!\$)\$(?!\$)[^\$]*\$(?!\$)', content))
    backslash_bracket = len(re.findall(r'\\\[', content))
    backslash_paren = len(re.findall(r'\\\(', content))
    
    print(f"Display formulas ($$...$$):    {display_formulas // 2}")
    print(f"Inline formulas ($...$):      {inline_formulas}")
    print(f"LaTeX display (\\[...\\]):     {backslash_bracket}")
    print(f"LaTeX inline (\\(...\\)):      {backslash_paren}")
    
    # Look for potential issues
    issues = []
    in_code_block = False
    in_display_formula = False
    
    for i, line in enumerate(lines, 1):
        # Check for code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            continue
        
        # Check for display formula markers
        if '$$' in line:
            count = line.count('$$')
            if count % 2 == 1:
                in_display_formula = not in_display_formula
        
        # Check for potential issues
        if '$$$' in line:
            issues.append(f"Line {i}: Triple $$$$ detected (might be typo)")
        
        # Check for mixed formatting
        if '$$' in line and '\[' in line:
            issues.append(f"Line {i}: Mixed $$ and \\[ formatters")
        
        # Check for incomplete formulas
        if re.search(r'\$[^$]*$', line) and not in_display_formula:
            if '$$' not in line:
                issues.append(f"Line {i}: Unclosed $ formula")
    
    if not issues:
        print("\n✓ No obvious formatting issues detected")
    else:
        print(f"\n⚠ Found {len(issues)} potential issues:")
        for issue in issues[:10]:  # Show first 10
            print(f"  - {issue}")
    
    # Show sample formulas
    print("\nSample formulas found:")
    formula_count = 0
    for i, line in enumerate(lines, 1):
        if '$$' in line or (re.search(r'\$[^$]+\$', line) and '$$' not in line):
            print(f"  Line {i}: {line.strip()[:80]}")
            formula_count += 1
            if formula_count >= 5:
                break
    
    return len(issues) == 0

def main():
    """Main diagnostic function."""
    print("=" * 60)
    print("LaTeX Formula Diagnostic Tool")
    print("=" * 60)
    
    md_files = list(Path('.').glob('*.md'))
    md_files = [f for f in md_files if f.name != 'README.md']
    
    if not md_files:
        print("No Markdown files found")
        return
    
    all_ok = True
    for md_file in md_files:
        ok = find_formula_issues(md_file)
        all_ok = all_ok and ok
    
    print("\n" + "=" * 60)
    if all_ok:
        print("✓ All files appear to be correctly formatted")
    else:
        print("⚠ Some files may have formatting issues")
    print("=" * 60)

if __name__ == "__main__":
    main()
