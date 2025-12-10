content: |
  # 📘 Multi-Agent Content Generation System — Technical Documentation
  ### Kasparro AI Engineer Challenge  
  ### Author: Mohit Anand  

  ---

  # 1. Overview

  This document provides a complete technical explanation of the **Multi-Agent Content Generation System** developed for the Kasparro AI Engineer Challenge.

  The system takes a small raw dataset describing **GlowBoost Vitamin C Serum** and automatically generates three structured machine-readable JSON pages:

  - `product_page.json`
  - `faq.json`
  - `comparison_page.json`

  The solution uses:

  - A multi-agent architecture  
  - Reusable logic blocks  
  - Page templates  
  - A shared PageContext data model  
  - A pipeline orchestrator  

  This documentation explains the workflow, components, architecture, diagrams, and execution steps in detail.

  ---

  # 2. High-Level Architecture

  ```mermaid
  flowchart TD

  A[Raw Product Input] --> B[Parser Agent]
  B -->|Creates PageContext| C[Question Generation Agent]
  C -->|Generates Questions| D[Content Planner Agent]
  D -->|Creates FAQ Items| E[Page Assembler Agent]
  E -->|Templates + Logic Blocks| F[JSON Generator]

  F --> G1[product_page.json]
  F --> G2[faq.json]
  F --> G3[comparison_page.json]
3. Folder Structure
css
Copy code
src/
│
├── agents/
│   ├── parser_agent.py
│   ├── question_generator_agent.py
│   ├── content_planner_agent.py
│   └── page_assembler_agent.py
│
├── core/
│   └── models.py
│
├── data/
│   └── product_input.py
│
├── logic_blocks/
│   ├── benefits_block.py
│   ├── comparison_block.py
│   ├── safety_block.py
│   └── usage_block.py
│
├── orchestrator/
│   └── flow.py
│
├── templates/
│   ├── product_template.py
│   ├── faq_template.py
│   └── comparison_template.py
│
└── main.py
4. Components Explained
4.1 Raw Product Data
Located in:
src/data/product_input.py

Contains fields:

product_name

concentration

skin_type

key_ingredients

benefits

how_to_use

side_effects

price

This raw dictionary is the input to the system.

4.2 ParserAgent
Responsibilities:

Converts raw product dictionary into internal models (Product, FictionalProduct)

Initializes PageContext with:

base product

fictional product

empty lists for questions and FAQs

empty product & comparison page structures

Output: PageContext passed to next agent.

4.3 QuestionGeneratorAgent
Responsibilities:

Generates customer-style questions

Covers categories: informational, usage, safety, purchase, comparison

Populates context.generated_questions

4.4 ContentPlannerAgent
Responsibilities:

Converts questions into FAQ items

Uses logic blocks to generate consistent answers

Writes FAQ objects into context.faqs

4.5 PageAssemblerAgent
Responsibilities:

Invokes page templates to create:

product page

comparison page

FAQ page

Fills:

context.product_page_data

context.comparison_page_data

5. Logic Blocks
Block	Description
benefits_block.py	Generates benefits summary
usage_block.py	Produces usage instructions
safety_block.py	Generates safety notes
comparison_block.py	Compares GlowBoost vs fictional product

6. Templates Layer
Template	Purpose
product_template.py	Builds product description page
faq_template.py	Builds FAQ page
comparison_template.py	Builds product comparison page

7. Orchestrator (Pipeline Controller)
File: src/orchestrator/flow.py

Pipeline Steps
Parse raw product → PageContext

Generate categorized questions

Create FAQ items

Assemble product & comparison pages

Generate FAQ page

Write JSON files

Output directory:
pgsql
Copy code
outputs/
│── product_page.json
│── faq.json
│── comparison_page.json
8. Running the Pipeline
Run:

bash
Copy code
python src/main.py
This executes the full pipeline from parsing → FAQ → templates → JSON output.

9. Output Summary
product_page.json
Contains:

product details

benefits summary

usage instructions

safety information

price

faq.json
Contains 5+ structured FAQ items.

comparison_page.json
Contains:

GlowBoost summary

Fictional product summary

Comparison points (ingredients, benefits, price)

10. Sequence Diagram
mermaid
Copy code
sequenceDiagram
    participant Input as Raw Product Data
    participant Parser as ParserAgent
    participant QAgent as QuestionGeneratorAgent
    participant Planner as ContentPlannerAgent
    participant Assembler as PageAssemblerAgent
    participant JSON as Output Writer

    Input->>Parser: Raw product data
    Parser->>QAgent: PageContext(base_product)
    QAgent->>Planner: Generated questions
    Planner->>Assembler: FAQ items
    Assembler->>JSON: Final JSON pages
11. Conclusion
This system meets all Kasparro challenge requirements:

✔ Multi-agent modular architecture
✔ Logic block–powered content generation
✔ Template-based page assembly
✔ Generates Product, FAQ, and Comparison JSON pages
✔ Professional folder structure & documentation
✔ Easy to extend or upgrade

The system is ready for future enhancements such as API endpoints, LLM integration, or UI display.
