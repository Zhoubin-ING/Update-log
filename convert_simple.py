#!/usr/bin/env python3
"""
Simple one-click Markdown to PDF converter with LaTeX support.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_conversion():
    """Run the conversion."""
    
    # The markdown file to convert
    md_file = "叠层成像_相位恢复_FPM_CPM学习指导教程.md"
    pdf_file = "叠层成像_相位恢复_FPM_CPM学习指导教程.pdf"
    
    if not os.path.exists(md_file):
        print(f"错误: 找不到文件 {md_file}")
        return False
    
    # Pandoc command with proper LaTeX math support
    cmd = [
        "pandoc",
        md_file,
        "-o", pdf_file,
        "--pdf-engine=pdflatex",  # Key parameter for math rendering
        "--from=markdown",
        "--to=pdf",
        "--toc",  # Table of contents
        "--number-sections",  # Section numbers
        "-V", "colorlinks",
        "-V", "urlcolor=blue",
        "-V", "geometry:margin=1in",
    ]
    
    print("=" * 70)
    print("Markdown to PDF 转换（支持 LaTeX 公式）")
    print("=" * 70)
    print(f"\n输入文件: {md_file}")
    print(f"输出文件: {pdf_file}")
    print(f"\n执行命令:")
    print(" ".join(cmd))
    print("\n" + "-" * 70)
    print("转换中... 请稍候")
    print("-" * 70 + "\n")
    
    try:
        # Run pandoc
        result = subprocess.run(cmd, timeout=300)
        
        if result.returncode == 0:
            print("\n" + "=" * 70)
            print("✓ 转换成功！")
            print(f"PDF 文件已生成: {pdf_file}")
            print("=" * 70)
            return True
        else:
            print("\n" + "=" * 70)
            print("✗ 转换失败")
            print("=" * 70)
            print("\n可能的原因:")
            print("1. Pandoc 未安装，请运行: choco install pandoc")
            print("2. LaTeX 引擎未安装，请运行: choco install miktex")
            print("3. 文件不存在或无读取权限")
            return False
            
    except subprocess.TimeoutExpired:
        print("\n✗ 转换超时（超过 5 分钟）")
        return False
    except FileNotFoundError:
        print("\n✗ Pandoc 未找到")
        print("请先安装 Pandoc: choco install pandoc")
        return False
    except Exception as e:
        print(f"\n✗ 错误: {e}")
        return False

if __name__ == "__main__":
    success = run_conversion()
    sys.exit(0 if success else 1)
