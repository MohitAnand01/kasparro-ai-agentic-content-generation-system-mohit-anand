# src/agents/parser_agent.py
from typing import Dict
import core.models as models  # import the module, not individual names


class ParserAgent:
    """
    Agent 1: Converts raw product data into structured internal models.
    """

    def parse(self, raw_product: Dict):
        # Build the base Product object
        product = models.Product(
            name=raw_product["product_name"],
            concentration=raw_product["concentration"],
            skin_types=raw_product["skin_type"],
            key_ingredients=raw_product["key_ingredients"],
            benefits=raw_product["benefits"],
            how_to_use=raw_product["how_to_use"],
            side_effects=raw_product["side_effects"],
            price=raw_product["price"],
        )

        # Define structured fictional Product B for comparison
        fictional_b = models.FictionalProduct(
            name="RadiantShield Vitamin C Complex",
            key_ingredients=["Vitamin C", "Niacinamide"],
            benefits=["Brightening", "Evens skin tone"],
            price="₹899",
        )

        # Initial empty context that later agents will fill
        return models.PageContext(
            base_product=product,
            fictional_product=fictional_b,
            generated_questions=[],
            faqs=[],
            product_page_data={},
            comparison_page_data={},
        )
