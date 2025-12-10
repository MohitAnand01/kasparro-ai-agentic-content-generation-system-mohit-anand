# src/templates/product_template.py
from typing import Dict, Any
from core.models import PageContext
from logic_blocks.benefits_block import generate_benefits_text
from logic_blocks.usage_block import generate_usage_text
from logic_blocks.safety_block import generate_safety_text


def build_product_page(context: PageContext) -> Dict[str, Any]:
    """
    Builds the product description page using:
        - core product fields
        - reusable logic blocks
    """

    p = context.base_product

    return {
        "name": p.name,
        "concentration": p.concentration,
        "skin_types": p.skin_types,
        "key_ingredients": p.key_ingredients,
        "benefits_summary": generate_benefits_text(p),
        "usage_instructions": generate_usage_text(p),
        "safety_information": generate_safety_text(p),
        "price": p.price,
    }
