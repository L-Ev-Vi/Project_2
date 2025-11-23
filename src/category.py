from typing import List


class Category:
    """Клас  для определения категории товаров"""

    name: str  # название категории
    description: str  # описание категории
    _products: List  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, _products: List) -> None:
        """Метод для инициализации класса Категория."""
        self.name = name
        self.description = description
        self._products = _products

        Category.category_count += 1
        Category.product_count += len(_products)

    def add_product(self, product: object) -> None:
        """Метод для добавления товара в категорию товаров. Метод принимает объект,
        и записывает его в приватный атрибут списка товаров."""
        self._products.append(product)

        Category.product_count += 1

    @property
    def products(self) -> str:
        """Гетер который возвращает список товаров в виде строк."""
        product_str = ""
        for product in self._products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
