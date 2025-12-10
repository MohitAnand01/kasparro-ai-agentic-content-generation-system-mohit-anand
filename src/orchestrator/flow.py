# src/orchestrator/flow.py
import json
from pathlib import Path

from data.product_input import GLOWBOOST_PRODUCT_RAW
from agents.parser_agent import ParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.content_planner_agent import ContentPlannerAgent
from agents.page_assembler_agent import PageAssemblerAgent
from templates.faq_template import build_faq_page


class Orchestrator:
    """
    Orchestrator: defines and runs the multi-agent automation flow.

    Flow:
      1. ParserAgent             -> parse raw product data into internal models
      2. QuestionGeneratorAgent  -> generate categorized user questions
      3. ContentPlannerAgent     -> turn questions + product data into FAQ items
      4. PageAssemblerAgent      -> assemble product + comparison pages via templates
      5. FAQ template            -> build FAQ page from FAQ items
      6. Write all outputs as JSON files into outputs/
    """

    def __init__(self, outputs_dir: str = "outputs"):
        self.outputs_dir = Path(outputs_dir)
        self.outputs_dir.mkdir(parents=True, exist_ok=True)

        # Initialize agents
        self.parser_agent = ParserAgent()
        self.question_agent = QuestionGeneratorAgent()
        self.content_planner = ContentPlannerAgent()
        self.page_assembler = PageAssemblerAgent()

    def run(self):
        # Step 1: Parse raw product into internal model
        print("📥 Step 1: Parsing raw product data...")
        context = self.parser_agent.parse(GLOWBOOST_PRODUCT_RAW)

        # Step 2: Generate categorized user questions
        print("❓ Step 2: Generating categorized questions...")
        context = self.question_agent.generate_questions(context)
        print(f"   → Generated {len(context.generated_questions)} questions.")

        # Step 3: Use logic blocks to build FAQ items
        print("🧩 Step 3: Building FAQ items using logic blocks...")
        context = self.content_planner.build_faqs(context)
        print(f"   → Built {len(context.faqs)} FAQ items.")

        # Step 4: Assemble product & comparison pages via templates
        print("📄 Step 4: Assembling product & comparison pages...")
        context = self.page_assembler.assemble_pages(context)

        # Step 5: Build FAQ page structure via FAQ template
        print("💾 Step 5: Building FAQ page JSON and saving outputs...")
        faq_json = build_faq_page(context)
        product_json = context.product_page_data
        comparison_json = context.comparison_page_data

        # Step 6: Write all JSON outputs
        self._write_json("faq.json", faq_json)
        self._write_json("product_page.json", product_json)
        self._write_json("comparison_page.json", comparison_json)

    def _write_json(self, filename: str, data):
        path = self.outputs_dir / filename
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✔ Wrote {path}")
