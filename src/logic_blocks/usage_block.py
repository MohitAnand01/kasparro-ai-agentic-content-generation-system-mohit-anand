# src/logic_blocks/usage_block.py
from core.models import Product


def generate_usage_text(product: Product) -> str:
    """
    Reusable block: describe how to use the serum, combining usage + skin types.
    """
    return (
        f"{product.how_to_use} "
        f"It is designed for {', '.join(product.skin_types)} skin."
    )
