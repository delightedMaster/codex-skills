# Academic Report PPT Skill (学术报告 PPT 智能生成 Skill)

<p align="center">
  <b>简体中文</b> | <a href="README_EN.md">English</a>
</p>

[![Skill: academic-report-ppt](https://img.shields.io/badge/Skill-academic--report--ppt-244D70.svg)](#)
[![Format: Native PPTX](https://img.shields.io/badge/Output-Native%20PPTX-D04423.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

专为 AI Agent（OpenAI Codex、ChatGPT、Claude、Google Antigravity 等）打造的高品质学术演示文稿制作 Skill。适用于文献汇报、组会进展、开题报告、中期检查及毕业答辩。

摒弃浮夸的大色块与无意义装饰，采用**白底、深灰正文、深蓝重点**的高信息密度科研版式，确保核心讲解直接呈现在页面上，并精细控制中英文字体、段落缩进、专业表格与科研图表。

---

## ✨ 核心特性

- 🎓 **高信息密度与严谨学术排版**：
  - 白底深灰正文（#222222）、深蓝主题与重点强调（#244D70），无冗余图标、无大面积装饰色块、无机械卡片堆叠。
  - 核心论据与推断直接完整展现在页面上，不强行压缩成碎片化关键词，亦不将核心讲解藏入备注页。
- 📐 **规范的中西文字体体系与层次**：
  - 中文正文与标题采用**微软雅黑**，西文与数字采用 **Arial**，保留标准科学符号、上下标及公式字体。
  - 清晰的字号梯度：主标题 28–30 pt，正文 18–20 pt，图表与表格标签 ≥ 16 pt。中文说明段落严格首行缩进 2 字符。
- 📊 **原生可编辑图表与科研证据**：
  - 数据图表、流程示意图与对比表格保持 Office 原生矢量与可编辑格式。
  - 支持将 LaTeX 表达式无损转换为原生可编辑公式；对论文原始高分辨率图版保留图注并建立清晰的对应图解。
- 🔍 **全流程质量自检机制（内置 Audit 脚本）**：
  - 配套 Python 质量审核工具（`scripts/audit_pptx.py`），自动化扫描检测字号阶梯、正文重叠、表格对齐与未替换的占位符。

---

## 📂 仓库目录结构

```text
codex-skills/
├── SKILL.md                                 # Skill 核心 Prompt 指令与生成逻辑规范
├── agents/
│   └── openai.yaml                          # OpenAI / Codex 交互界面与默认启动 Prompt 配置
├── assets/
│   └── academic-report-reference.pptx       # 官方三页样稿（标题页、单图实证页、两列对比页标准排版）
├── references/
│   ├── academic-content.md                  # 学术文本组织逻辑：事实结论、实证推断与论证结构
│   ├── figures-charts.md                    # 科研图表、流式图与公式选择及标注规范
│   ├── layout-typography.md                 # 版式排版、留白法则、字号字阶与中英混合规范
│   └── production-qa.md                     # 生成流程、渲染验证与交付清单
└── scripts/
    └── audit_pptx.py                        # PPTX 交付前自动化合规性审计脚本
```

---

## 🚀 安装与使用指南

### 1. 在 Codex / ChatGPT Agent 中使用
将本仓库克隆或导入至 Agent 工作区技能目录（如 `.codex/skills/` 或相应技能路径），并在任务中直接唤起：
```text
请使用 $academic-report-ppt 根据我的文献材料制作一份开题汇报 PPT，采用简洁高信息密度版式，将主要讲解写在页面上。
```

### 2. 在 Antigravity / Claude Code / CLI 中使用
将本仓库目录挂载至 Skills 配置文件夹，Agent 即可自动识别 `SKILL.md` 中的 Frontmatter 元数据：
```yaml
---
name: academic-report-ppt
description: 制作和改写可编辑的中英文学术报告 PPTX，适用于文献汇报、组会进展、开题、中期和答辩...
---
```

### 3. 运行 PPTX 质量合规性审计
在生成或修改 PPTX 后，可运行内置检查脚本对输出文件进行合规性验证：
```bash
python scripts/audit_pptx.py path/to/your_presentation.pptx
```
脚本将自动输出每一页的字号阶梯分布、表格居中状态、文本框重叠情况与异常占位符报告。

---

## 📜 许可证

本项目采用 [MIT 许可证](LICENSE)。欢迎在学术汇报、课题研讨与教学场景中自由使用和改进。
