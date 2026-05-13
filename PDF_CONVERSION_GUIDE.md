# Markdown to PDF 转换指南 - LaTeX 公式修复

## 问题说明
Markdown 中的 LaTeX 数学公式（使用 `$$...$$` 格式）在转换为 PDF 时显示为原始代码而不是被渲染。

## 解决方案

### 步骤 1: 安装必要工具

#### Windows 用户 (使用 Chocolatey)：

```bash
# 安装 Pandoc
choco install pandoc

# 安装 LaTeX (选择一个)
# 选项 1: MiKTeX (更轻量)
choco install miktex

# 或选项 2: TeX Live (功能完整)
choco install texlive
```

#### 如果没有 Chocolatey:
1. 访问 https://pandoc.org/installing.html 下载 Pandoc
2. 访问 https://miktex.org/download 下载 MiKTeX

### 步骤 2: 验证安装

```bash
pandoc --version
pdflatex --version
```

### 步骤 3: 使用提供的转换工具

#### 方法 A: 直接运行批处理文件
```bash
convert.bat
```

#### 方法 B: 手动运行 Python 脚本
```bash
python convert_markdown_to_pdf.py
```

#### 方法 C: 使用 Pandoc 命令行 (推荐用于单个文件)
```bash
pandoc "叠层成像_相位恢复_FPM_CPM学习指导教程.md" ^
  -o "叠层成像_相位恢复_FPM_CPM学习指导教程.pdf" ^
  --pdf-engine=pdflatex ^
  --from=markdown+tex_math_double_backslash ^
  --toc ^
  --number-sections ^
  -V colorlinks ^
  -V urlcolor=blue ^
  -V geometry:margin=1in
```

## Pandoc 关键参数说明

| 参数 | 说明 |
|------|------|
| `--pdf-engine=pdflatex` | 使用 pdflatex 引擎正确渲染数学公式 |
| `--from=markdown+tex_math_double_backslash` | 启用 LaTeX 数学解析 |
| `--toc` | 生成目录 |
| `--number-sections` | 对章节进行编号 |
| `-V colorlinks` | 启用彩色链接 |
| `-V geometry:margin=1in` | 设置页边距 |

## 常见问题

### Q: 仍然显示 LaTeX 原始代码?
A: 
1. 确认已安装 LaTeX (运行 `pdflatex --version`)
2. 检查 Markdown 文件中公式的格式是否正确
3. 查看 Markdown 中是否混合使用了 `$$` 和 `\[` 等多种格式

### Q: 转换很慢?
A: 第一次转换会很慢（LaTeX 需要初始化），后续转换会更快。

### Q: 公式中有特殊符号显示不正确?
A: 确保 Markdown 文件保存为 UTF-8 编码。

## 快速测试

创建一个简单的测试文件 `test.md`:
```markdown
# Test Formula

This is an inline formula: $E=mc^2$

This is a display formula:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

然后运行:
```bash
pandoc test.md -o test.pdf --pdf-engine=pdflatex
```

如果生成的 PDF 能正确显示公式，那么您的系统配置是正确的。

## 脚本文件说明

- `convert_markdown_to_pdf.py`: Python 脚本，自动检查依赖并转换所有 Markdown 文件
- `convert.bat`: Windows 批处理文件，简化运行
