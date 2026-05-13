# 快速修复 LaTeX 公式转换问题

## 您的情况
- 文件: `叠层成像_相位恢复_FPM_CPM学习指导教程.md`
- 公式数量: 89 个 LaTeX 公式块
- 问题: PDF 转换后公式显示为原始代码而不是被渲染

## 根本原因
Pandoc 在转换 Markdown 到 PDF 时，需要一个 LaTeX 引擎来渲染 `$$...$$` 中的数学公式。
如果没有安装或配置正确，公式会以原始文本形式出现在 PDF 中。

## 最快解决方案（仅需 2 个步骤）

### 第 1 步: 安装 LaTeX 引擎

**Windows 系统** - 打开命令提示符（Command Prompt）或 PowerShell，选择以下任一方式：

#### 方案 A: 使用 Chocolatey (推荐，自动)
```cmd
choco install miktex
```

#### 方案 B: 手动下载安装
访问: https://miktex.org/download
- 下载 Windows Installer
- 运行安装程序，按默认选项安装

#### 方案 C: 使用 TeX Live (完整但更大)
```cmd
choco install texlive
```

**验证安装:**
```cmd
pdflatex --version
```
如果显示版本号，说明安装成功。

### 第 2 步: 使用 Pandoc 转换

确保已安装 Pandoc:
```cmd
choco install pandoc
```

#### 方式 1: 一键转换脚本 (推荐)
```cmd
python convert_markdown_to_pdf.py
```

#### 方式 2: 命令行手动转换
将以下命令保存为 `.bat` 文件或直接执行：

```cmd
pandoc "叠层成像_相位恢复_FPM_CPM学习指导教程.md" ^
  -o "叠层成像_相位恢复_FPM_CPM学习指导教程.pdf" ^
  --pdf-engine=pdflatex ^
  --from=markdown ^
  --toc ^
  --number-sections ^
  -V colorlinks ^
  -V urlcolor=blue
```

## 完全命令说明

```bash
pandoc [输入文件] -o [输出文件] [选项]
```

### 关键选项

| 选项 | 用途 |
|------|------|
| `--pdf-engine=pdflatex` | 👈 **关键**：指定 LaTeX 引擎渲染数学 |
| `--from=markdown` | 输入格式（Markdown） |
| `--toc` | 生成目录 |
| `--number-sections` | 章节编号 |
| `-V colorlinks` | 启用彩色链接 |
| `-V geometry:margin=1in` | 设置 1 英寸页边距 |

## 工作流推荐

编辑完 Markdown 后，运行：
```cmd
# 快速检查公式格式（可选）
python diagnose_formulas.py

# 转换为 PDF
python convert_markdown_to_pdf.py
```

## 排查清单

如果仍有问题，按以下顺序检查：

- [ ] Pandoc 已安装：`pandoc --version`
- [ ] LaTeX 已安装：`pdflatex --version`
- [ ] Markdown 文件编码为 UTF-8（VS Code 右下角检查）
- [ ] 使用了 `--pdf-engine=pdflatex` 参数
- [ ] 文件路径没有特殊字符或空格（如果有，用引号括起来）

## 测试

创建 `test.md` 文件：
```markdown
# 测试

内联公式: $E=mc^2$

显示公式:

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

运行:
```cmd
pandoc test.md -o test.pdf --pdf-engine=pdflatex
```

如果 `test.pdf` 能正确显示公式，您的系统就可以了！

## 需要帮助？

1. 检查 Pandoc 输出是否有错误信息
2. 确认 `pdflatex` 能独立运行
3. 尝试用更简单的 Markdown 文件测试
