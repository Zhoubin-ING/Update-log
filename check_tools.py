#!/usr/bin/env python3
"""
Check if all required tools are installed for LaTeX formula rendering.
"""

import subprocess
import sys

def check_tool(name, commands):
    """Check if a tool is installed."""
    for cmd in commands:
        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )
            if result.returncode == 0:
                print(f"✓ {name} 已安装")
                return True
        except:
            pass
    
    print(f"✗ {name} 未安装")
    return False

def main():
    print("=" * 70)
    print("LaTeX 公式渲染系统检查")
    print("=" * 70 + "\n")
    
    # Check requirements
    pandoc_ok = check_tool(
        "Pandoc",
        [
            "pandoc --version",
            "where pandoc"
        ]
    )
    
    latex_ok = check_tool(
        "LaTeX (pdflatex)",
        [
            "pdflatex --version",
            "where pdflatex"
        ]
    )
    
    python_ok = check_tool(
        "Python 3",
        [
            "python --version",
            "where python"
        ]
    )
    
    print("\n" + "=" * 70)
    
    if pandoc_ok and latex_ok:
        print("✓ 所有依赖都已安装！")
        print("\n可以运行: python convert_simple.py")
        return 0
    else:
        print("✗ 缺少必要的工具")
        print("\n请安装:")
        if not pandoc_ok:
            print("  - Pandoc: choco install pandoc")
        if not latex_ok:
            print("  - LaTeX:  choco install miktex")
        print("\n安装后重试此检查脚本。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
