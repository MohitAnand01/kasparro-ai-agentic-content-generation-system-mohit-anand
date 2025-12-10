# src/agents/question_generator_agent.py
from typing import List
from core.models import PageContext, Question


class QuestionGeneratorAgent:
    """
    Agent 2: Generates categorized user questions based only on known fields.
    Produces at least 15 questions across categories.
    """

    def generate_questions(self, context: PageContext) -> PageContext:
        p = context.base_product
        questions: List[Question] = []

        # Informational
        questions.append(Question("Informational", f"What is {p.name}?"))
        questions.append(Question("Informational", "What are the key ingredients in this serum?"))
        questions.append(Question("Informational", "Which skin types is this serum suitable for?"))

        # Usage
        questions.append(Question("Usage", "How do I use this serum in my routine?"))
        questions.append(Question("Usage", "Can I use this serum every morning?"))
        questions.append(Question("Usage", "Should I apply this before or after moisturizer?"))

        # Safety
        questions.append(Question("Safety", "Is this serum safe for sensitive skin?"))
        questions.append(Question("Safety", "Are there any side effects I should expect?"))
        questions.append(Question("Safety", "Can I use this serum along with sunscreen?"))

        # Purchase
        questions.append(Question("Purchase", "What is the price of this serum?"))
        questions.append(Question("Purchase", "Is this serum good for daily use at its price point?"))

        # Comparison
        questions.append(Question("Comparison", "How does this serum compare to other Vitamin C serums?"))
        questions.append(Question("Comparison", "Does this serum offer brightening benefits?"))
        questions.append(Question("Comparison", "Is this serum better for oily or combination skin?"))
        questions.append(Question("Comparison", "How do this serum’s ingredients compare to another product?"))

        context.generated_questions = questions
        return context
