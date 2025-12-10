# src/logic_blocks/safety_block.py
from core.models import Product


def generate_safety_text(product: Product) -> str:
    """
    Reusable block: describe safety & side effects based on the provided data.
    """
    return (
        f"Some users with sensitive skin may experience {product.side_effects}. "
        "Always patch test before full use and follow up with sunscreen in the morning."
    )
