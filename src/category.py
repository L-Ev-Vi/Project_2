from typing import List


class Category:
    """Клас  для определения категории товаров"""

    name: str  # название категории
    description: str  # описание категории
    products: List  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: List) -> None:
        """Метод для инициализации класса Категория."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
