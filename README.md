# Kasparro – Multi-Agent Content Generation System (GlowBoost)

This repo implements a modular, agentic automation system that takes a small product dataset (GlowBoost Vitamin C Serum) and generates three structured JSON content pages:

- `outputs/faq.json`
- `outputs/product_page.json`
- `outputs/comparison_page.json`

The system is built as a multi-agent pipeline with clear agent boundaries, reusable content logic blocks, and a small template engine.

---

## Project Structure

```text
.
├── docs/
│   └── projectdocumentation.md
├── outputs/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
├── src/
│   ├── agents/
│   ├── core/
│   ├── data/
│   ├── logic_blocks/
│   ├── orchestrator/
│   └── templates/
└── venv/ (local virtualenv, not required in repo)
