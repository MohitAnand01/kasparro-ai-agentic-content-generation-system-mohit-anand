# src/agents/content_planner_agent.py
from core.models import PageContext, FAQItem
from logic_blocks.benefits_block import generate_benefits_text
from logic_blocks.usage_block import generate_usage_text
from logic_blocks.safety_block import generate_safety_text


class ContentPlannerAgent:
    """
    Agent 3: Uses logic blocks to convert generated questions into FAQ items.
    """

    def build_faqs(self, context: PageContext) -> PageContext:
        faqs = []
        p = context.base_product

        for q in context.generated_questions:
            if q.category == "Informational":
                text_lower = q.text.lower()
                if "what is" in text_lower:
                    answer = (
                        f"{p.name} is a serum with {p.concentration}, "
                        f"formulated for {', '.join(p.skin_types)} skin."
                    )
                elif "key ingredients" in text_lower:
                    answer = f"It contains: {', '.join(p.key_ingredients)}."
                elif "skin types" in text_lower:
                    answer = f"It is suitable for {', '.join(p.skin_types)} skin."
                else:
                    answer = generate_benefits_text(p)

            elif q.category == "Usage":
                answer = generate_usage_text(p)

            elif q.category == "Safety":
                answer = generate_safety_text(p)

            elif q.category == "Purchase":
                answer = f"The serum is priced at {p.price}."

            elif q.category == "Comparison":
                # In FAQ, keep comparison answers high-level; detailed comparison is in comparison page
                answer = generate_benefits_text(p)

            else:
                answer = generate_benefits_text(p)

            faqs.append(FAQItem(question=q.text, answer=answer))

        context.faqs = faqs
        return context
