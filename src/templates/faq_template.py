# src/templates/faq_template.py
from typing import Dict, Any
from core.models import PageContext


def build_faq_page(context: PageContext) -> Dict[str, Any]:
    """
    Creates the FAQ page structure using:
        - product_name
        - first 5 FAQ items (requirement)
    """

    return {
        "product_name": context.base_product.name,
        "faqs": [
            {"question": faq.question, "answer": faq.answer}
            for faq in context.faqs[:5]  # take minimum 5 FAQs
        ],
    }
