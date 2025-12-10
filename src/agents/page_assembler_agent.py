# src/agents/page_assembler_agent.py
from core.models import PageContext
from templates.faq_template import build_faq_page
from templates.product_template import build_product_page
from templates.comparison_template import build_comparison_page


class PageAssemblerAgent:
    """
    Agent 4: Applies templates to build final JSON-ready page structures.
    """

    def assemble_pages(self, context: PageContext) -> PageContext:
        # Build product and comparison page structures
        context.product_page_data = build_product_page(context)
        context.comparison_page_data = build_comparison_page(context)
        return context

    def build_faq_page(self, context: PageContext):
        # FAQ page is built separately from FAQs already attached to context
        return build_faq_page(context)
