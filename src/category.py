from typing import List

from src.base_category_order import BaseCategoryOrder
from src.product import Product


class Category(BaseCategoryOrder):
    """Клас  для определения категории товаров"""

    name: str  # название категории
    description: str  # описание категории
    __products: List  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: List) -> None:
        """Метод для инициализации объекта-класса Категория."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Магический метод, который отображает информацию, об общем количестве товаров на складе, для пользователей"""
        quantity_stock = 0
        for product in self.__products:
            quantity_stock += product.quantity
        return f"{self.name}, количество продуктов: {quantity_stock} шт."

    def add_product(self, product: object) -> None:
        """Метод для добавления товара в категорию товаров. Метод принимает объект,
        и записывает его в приватный атрибут списка товаров."""
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(self) -> str:
        """Гетер который возвращает список товаров в виде строк."""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.__str__()}\n"
        return product_str
