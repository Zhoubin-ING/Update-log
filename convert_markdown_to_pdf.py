#!/usr/bin/env python3
"""
Markdown to PDF converter with proper LaTeX math support.
This script converts Markdown files to PDF while correctly rendering LaTeX formulas.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_pandoc():
    """Check if Pandoc is installed."""
    try:
        result = subprocess.run(['pandoc', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Pandoc found")
            return True
    except FileNotFoundError:
        print("✗ Pandoc not found")
        return False

def check_latex():
    """Check if LaTeX is installed."""
    try:
        result = subprocess.run(['pdflatex', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ LaTeX (pdflatex) found")
            return True
    except FileNotFoundError:
        print("✗ LaTeX not found")
        return False

def convert_md_to_pdf(md_file, pdf_file):
    """
    Convert Markdown to PDF using Pandoc with proper math rendering.
    
    Args:
        md_file: Path to input Markdown file
        pdf_file: Path to output PDF file
    """
    if not os.path.exists(md_file):
        print(f"Error: File {md_file} not found")
        return False
    
    # Pandoc command with math support
    cmd = [
        'pandoc',
        md_file,
        '-o', pdf_file,
        '--pdf-engine=pdflatex',  # Use pdflatex for math rendering
        '--from=markdown+tex_math_double_backslash',  # Parse LaTeX math
        '--to=pdf',
        '--variable=geometry:margin=1in',  # Set margins
        '--variable=fontsize:11pt',
        '--toc',  # Table of contents
        '--number-sections',  # Number sections
        '-V', 'colorlinks',  # Colored links
        '-V', 'urlcolor=blue',
    ]
    
    print(f"Converting {md_file} to {pdf_file}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✓ Successfully created {pdf_file}")
            return True
        else:
            print(f"✗ Conversion failed")
            print("STDERR:", result.stderr)
            print("STDOUT:", result.stdout)
            return False
            
    except subprocess.TimeoutExpired:
        print("✗ Conversion timeout (exceeded 5 minutes)")
        return False
    except Exception as e:
        print(f"✗ Error during conversion: {e}")
        return False

def main():
    """Main function."""
    print("=" * 60)
    print("Markdown to PDF Converter with LaTeX Math Support")
    print("=" * 60)
    
    # Check requirements
    print("\nChecking requirements...")
    pandoc_ok = check_pandoc()
    latex_ok = check_latex()
    
    if not pandoc_ok:
        print("\n✗ Pandoc is required but not installed")
        print("  Install via: choco install pandoc")
        return 1
    
    if not latex_ok:
        print("\n✗ LaTeX is required but not installed")
        print("  Install via: choco install miktex OR choco install texlive")
        return 1
    
    print("\n✓ All requirements met!\n")
    
    # Find and convert all Markdown files
    script_dir = Path(__file__).parent
    md_files = list(script_dir.glob("*.md"))
    
    if not md_files:
        print(f"No Markdown files found in {script_dir}")
        return 1
    
    for md_file in md_files:
        if md_file.name == "README.md":
            continue
        
        pdf_file = md_file.with_suffix(".pdf")
        print(f"\nProcessing: {md_file.name}")
        
        success = convert_md_to_pdf(str(md_file), str(pdf_file))
        
        if not success:
            return 1
    
    print("\n" + "=" * 60)
    print("✓ All conversions completed successfully!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())
