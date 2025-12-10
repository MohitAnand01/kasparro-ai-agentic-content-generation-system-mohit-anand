# src/logic_blocks/benefits_block.py
from core.models import Product


def generate_benefits_text(product: Product) -> str:
    """
    Reusable block: turn product.benefits into a short benefits sentence.
    """
    benefits = ", ".join(product.benefits)
    return f"The serum helps with {benefits}."
