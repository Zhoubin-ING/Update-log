# LaTeX 公式转换问题修复说明

## 问题总结
您的 Markdown 文件 `叠层成像_相位恢复_FPM_CPM学习指导教程.md` 中的 89 个 LaTeX 公式在转换为 PDF 时显示为原始代码。

## 根本原因
Pandoc 需要 LaTeX 引擎（如 pdflatex）来渲染数学公式。如果没有安装或没有正确配置，公式就会以原始形式出现。

## 快速解决 (3 步)

### 步骤 1️⃣ : 检查系统
```cmd
python check_tools.py
```

### 步骤 2️⃣ : 安装缺失的工具
如果检查结果显示缺少工具，请安装：

```cmd
# 安装 Pandoc
choco install pandoc

# 安装 LaTeX (选一个)
choco install miktex
```

### 步骤 3️⃣ : 转换 Markdown 到 PDF
```cmd
python convert_simple.py
```

完成！您应该会看到一个新的 PDF 文件，其中公式已正确渲染。

---

## 详细文档

### 📋 文件说明

| 文件 | 用途 |
|------|------|
| `QUICK_FIX.md` | 详细的快速修复指南 |
| `PDF_CONVERSION_GUIDE.md` | 完整的 Pandoc 使用指南 |
| `check_tools.py` | 检查系统依赖 ✅ |
| `convert_simple.py` | 一键转换脚本 ✅ |
| `convert_markdown_to_pdf.py` | 高级转换脚本（支持多文件） |
| `diagnose_formulas.py` | 诊断 Markdown 公式格式 |
| `convert.bat` | Windows 批处理脚本 |

### 🔧 工具要求

| 工具 | 用途 | 下载 |
|------|------|------|
| Pandoc | Markdown 转 PDF | [链接](https://pandoc.org/installing.html) |
| LaTeX (MiKTeX) | 渲染数学公式 | [链接](https://miktex.org/download) |
| Python 3 | 运行转换脚本 | 通常已安装 |

### 📝 Pandoc 关键参数

对 Markdown 到 PDF 的转换最关键的参数是：

```
--pdf-engine=pdflatex    # 指定使用 pdflatex 引擎（必须）
--from=markdown          # 输入格式
--toc                    # 生成目录
--number-sections        # 章节编号
```

### 🧪 测试转换

如果转换失败，可以用简单的测试文件验证：

1. 创建 `test.md`:
```markdown
# 测试

$$E = mc^2$$
```

2. 运行:
```cmd
pandoc test.md -o test.pdf --pdf-engine=pdflatex
```

如果 `test.pdf` 能正确显示公式，说明系统配置正确。

### ❓ 常见问题

**Q: 显示 "Pandoc not found"**
- A: 安装 Pandoc: `choco install pandoc`

**Q: "pdflatex not found"**
- A: 安装 LaTeX: `choco install miktex`

**Q: 转换很慢**
- A: 第一次会很慢（LaTeX 初始化），后续会快很多

**Q: 公式仍然是原始代码**
- A: 确保使用了 `--pdf-engine=pdflatex` 参数

---

## 下一步

1. ✅ 运行 `python check_tools.py` 检查依赖
2. ✅ 安装缺失的工具
3. ✅ 运行 `python convert_simple.py` 生成 PDF
4. ✅ 检查 PDF 中的公式是否正确渲染

祝您使用愉快！🎉
