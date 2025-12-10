# src/templates/comparison_template.py
from typing import Dict, Any
from core.models import PageContext
from logic_blocks.comparison_block import compare_products


def build_comparison_page(context: PageContext) -> Dict[str, Any]:
    """
    Builds the comparison page using:
      - base product (GlowBoost)
      - fictional product B
      - reusable comparison logic block
    """
    p = context.base_product
    b = context.fictional_product

    comparison_data = compare_products(p, b)

    return {
        "title": f"{p.name} vs {b.name}",
        **comparison_data,
    }
