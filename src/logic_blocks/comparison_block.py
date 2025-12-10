# src/logic_blocks/comparison_block.py
from typing import Dict, Any
from core.models import Product, FictionalProduct


def compare_products(base: Product, other: FictionalProduct) -> Dict[str, Any]:
    """
    Reusable block: build a structured comparison between the base product
    and a fictional comparison product (Product B).
    """
    return {
        "base_product": {
            "name": base.name,
            "ingredients": base.key_ingredients,
            "benefits": base.benefits,
            "price": base.price,
        },
        "other_product": {
            "name": other.name,
            "ingredients": other.key_ingredients,
            "benefits": other.benefits,
            "price": other.price,
        },
        "comparison_points": [
            {
                "aspect": "Ingredients",
                "base": ", ".join(base.key_ingredients),
                "other": ", ".join(other.key_ingredients),
            },
            {
                "aspect": "Benefits",
                "base": ", ".join(base.benefits),
                "other": ", ".join(other.benefits),
            },
            {
                "aspect": "Price",
                "base": base.price,
                "other": other.price,
            },
        ],
    }
