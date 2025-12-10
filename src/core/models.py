# src/core/models.py
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Product:
    """
    Represents the base product (GlowBoost Vitamin C Serum).
    """
    name: str
    concentration: str
    skin_types: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str


@dataclass
class FictionalProduct:
    """
    Represents the fictional comparison product (Product B).
    """
    name: str
    key_ingredients: List[str]
    benefits: List[str]
    price: str


@dataclass
class Question:
    """
    Represents a user question with a specific category.
    Example categories: Informational, Usage, Safety, Purchase, Comparison.
    """
    category: str
    text: str


@dataclass
class FAQItem:
    """
    A single FAQ entry, pairing a question with an answer.
    """
    question: str
    answer: str


@dataclass
class PageContext:
    """
    Shared context object passed between agents in the pipeline.
    """
    base_product: Product
    fictional_product: FictionalProduct
    generated_questions: List[Question]
    faqs: List[FAQItem]
    product_page_data: Dict[str, Any]
    comparison_page_data: Dict[str, Any]
