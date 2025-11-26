from typing import List


class Category:
    """Клас  для определения категории товаров"""

    name: str  # название категории
    description: str  # описание категории
    __products: List  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: List) -> None:
        """Метод для инициализации класса Категория."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: object) -> None:
        """Метод для добавления товара в категорию товаров. Метод принимает объект,
        и записывает его в приватный атрибут списка товаров."""
        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(self) -> str:
        """Гетер который возвращает список товаров в виде строк."""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
