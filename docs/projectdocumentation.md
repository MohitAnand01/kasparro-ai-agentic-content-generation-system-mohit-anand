# Multi-Agent Content Generation System — GlowBoost Vitamin C Serum

## Problem Statement

Design and implement a modular, agentic automation system that takes a small, fixed product dataset (GlowBoost Vitamin C Serum) and automatically generates multiple structured, machine-readable content pages — specifically:

- FAQ Page (with at least 5 Q&A items)
- Product Description Page
- Comparison Page (GlowBoost vs a fictional Product B)

The system must:

- Use only the given product data (no external research or knowledge).
- Be built as a multi-agent system, not a single monolithic script.
- Produce clean JSON outputs suitable for downstream consumption. :contentReference[oaicite:1]{index=1}  


## Solution Overview

The solution is implemented as a **multi-agent pipeline** with clear responsibilities, reusable logic blocks, and a small template engine. It takes the raw product data for GlowBoost Vitamin C Serum, transforms it into an internal model, generates categorized questions, converts them into FAQ items, and finally assembles three JSON pages:

- `faq.json`
- `product_page.json`
- `comparison_page.json`

High-level flow:

1. **ParserAgent** converts the raw product input into strongly-typed internal models.
2. **QuestionGeneratorAgent** generates at least 15 user questions across categories (Informational, Usage, Safety, Purchase, Comparison).
3. **ContentPlannerAgent** uses reusable logic blocks to convert questions into FAQ items.
4. **PageAssemblerAgent** applies templates to assemble the Product Page and Comparison Page.
5. A FAQ template consumes the FAQ items to build `faq.json`.
6. The **Orchestrator** coordinates all agents and writes the final JSON files to the `outputs/` directory.


## Scopes & Assumptions

- **Single product input**  
  The pipeline is designed around one product instance (GlowBoost Vitamin C Serum), but the internal models and agents can operate on any product with the same schema.

- **No external knowledge**  
  All generated content is derived strictly from the provided dataset:
  - product name  
  - concentration  
  - skin types  
  - key ingredients  
  - benefits  
  - how to use  
  - side effects  
  - price :contentReference[oaicite:2]{index=2}  

- **Fictional Product B**  
  Product B is a fictional but structured product, defined inside the parser agent for comparison purposes only (name, ingredients, benefits, price).

- **System boundaries**  
  - No UI / frontend is included.
  - No database or external APIs are used.
  - The system runs as a local Python CLI pipeline.

- **Outputs**  
  JSON outputs are written to `./outputs` and are treated as the final machine-readable pages for this assignment.


## System Design

### 1. Architecture Overview

The system is structured as:

- **Core models** (`core.models`)
  - `Product`, `FictionalProduct`, `Question`, `FAQItem`, `PageContext`
- **Agents** (`agents.*`)
  - Each agent has a single responsibility and defined inputs/outputs.
- **Logic blocks** (`logic_blocks.*`)
  - Pure functions that encapsulate reusable content logic.
- **Templates** (`templates.*`)
  - Page definitions that use logic blocks and context to build JSON structures.
- **Orchestrator** (`orchestrator.flow.Orchestrator`)
  - Coordinates the agent execution order and writes outputs.

A minimal orchestration diagram (Mermaid):

```mermaid
flowchart TD

    A[Raw Product Data] --> B[ParserAgent]
    B --> C[QuestionGeneratorAgent]
    C --> D[ContentPlannerAgent]
    D --> E[PageAssemblerAgent]
    D --> F[FAQ Template]
    E --> G[Product Page Template]
    E --> H[Comparison Page Template]

    F --> I[faq.json]
    G --> J[product_page.json]
    H --> K[comparison_page.json]
