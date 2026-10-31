# Academic Report PPT Skill

<p align="center">
  <a href="README.md">简体中文</a> | <b>English</b>
</p>

[![Skill: academic-report-ppt](https://img.shields.io/badge/Skill-academic--report--ppt-244D70.svg)](#)
[![Format: Native PPTX](https://img.shields.io/badge/Output-Native%20PPTX-D04423.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An intelligent presentation generation skill designed for AI agents (OpenAI Codex, ChatGPT, Claude, Google Antigravity, etc.). Specially tailored for literature seminars, research group updates, thesis proposals, midterm reviews, and graduation defenses.

Moving away from flashy decorative blocks and superficial animations, it adopts a **clean white background, charcoal gray text, and navy blue accents** with high information density, ensuring essential explanations and scientific arguments are presented directly on the slides with meticulous typographic control.

---

## ✨ Highlights & Features

- 🎓 **High Information Density & Scholarly Layout**:
  - Crisp white background (#FFFFFF), readable charcoal body text (#222222), and focused navy blue accents (#244D70).
  - Eliminates distracting icon bloat, decorative cards, and artificial text fragmentation. Core explanations and evidence live directly on the slide rather than being hidden in presenter notes.
- 📐 **Rigorous Typography & Font Hierarchy**:
  - Uses **Microsoft YaHei** for Chinese text and **Arial** for Western characters and numerals, preserving standard scientific notation, subscripts/superscripts, and equation fonts.
  - Defined typographic scale: Slide Title at 28–30 pt, Body Text at 18–20 pt, Chart/Table labels ≥ 16 pt.
- 📊 **Native Editable Charts & Scientific Figures**:
  - Generates native Office charts, data tables, and structural diagrams rather than flat screenshots.
  - Converts LaTeX equations into native editable Office equation objects while preserving high-resolution paper figures with structured figure captions.
- 🔍 **Automated Pre-Delivery Audit Script**:
  - Includes a Python verification script (`scripts/audit_pptx.py`) that audits font hierarchy, shape collisions, table alignments, and placeholder residue before delivery.

---

## 📂 Repository Structure

```text
codex-skills/
├── SKILL.md                                 # Core agent prompt instructions and slide generation rules
├── agents/
│   └── openai.yaml                          # OpenAI / Codex agent interface and default prompt definition
├── assets/
│   └── academic-report-reference.pptx       # 3-slide golden reference (Title, Single Figure, 2-Column Comparison)
├── references/
│   ├── academic-content.md                  # Academic argumentation structure, evidence synthesis & citations
│   ├── figures-charts.md                    # Data charts, flowcharts, paper figures & equation conventions
│   ├── layout-typography.md                 # Spacing, visual balance, font scales & bilingual typography
│   └── production-qa.md                     # Step-by-step production workflow and verification checklist
└── scripts/
    └── audit_pptx.py                        # Automated presentation compliance and QA audit script
```

---

## 🚀 Installation & Usage

### 1. Codex / ChatGPT Agents
Clone or mount this repository into your agent's skill path (e.g. `.codex/skills/`), then invoke directly:
```text
Please use $academic-report-ppt to create an editable academic presentation based on my research paper, keeping a clean, high-density layout with primary explanations directly on the slides.
```

### 2. Antigravity / Claude Code / CLI Agents
Mount this directory under your skills root. The agent will discover the frontmatter metadata in `SKILL.md`:
```yaml
---
name: academic-report-ppt
description: 制作和改写可编辑的中英文学术报告 PPTX，适用于文献汇报、组会进展、开题、中期和答辩...
---
```

### 3. Run Quality Audit
After generating or modifying a `.pptx` file, run the automated auditor:
```bash
python scripts/audit_pptx.py path/to/your_presentation.pptx
```
The script will output font size distributions, shape overlaps, and placeholder warnings for each slide.

---

## 📜 License

Distributed under the [MIT License](LICENSE). Feel free to use, adapt, and build upon this skill for academic research and education.
