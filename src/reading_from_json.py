import json
import os

from src.category import Category
from src.product import Product


def reading_from_json(file: str = "./data/products.json") -> None:
    """Функция извлечения данных из json файла для создания экземпляров класса. Функция принимает путь к json файлу,
    и возвращает словари с данными по категориям и товарам, но это не точно!"""

    path = os.path.abspath(file)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for i, category in enumerate(data):
        name_category = f"category{i + 1}"
        globals()[name_category] = Category(
            category["name"], category["description"], [Product(**position) for position in category["products"]]
        )


# Не знаю точно, что должно являться результатом функции,
# но использование глобальных переменных в пространстве имён скорее всего не лучший вариант,
# возможно стоит выводить результат в виде словаря.

# Проверка создания объектов классов Category и Product
# if __name__ == "__main__":
#
#     reading_from_json()
#
#     print(category1.name)
#     print(category1.description)
#     print(len(category1.products))
#     print(category1.products)
#     print('-------')
#     for product in category1.products:
#         print(product.name)
#         print(product.description)
#         print(product.price)
#         print(product.quantity)
#         print('-------')
#     print(category1.category_count)
#     print(category1.product_count)
#     print('-------')
#     print(category2.name)
#     print(category2.description)
#     print(len(category2.products))
#     print(category2.products)
#     print('-------')
#     for product in category2.products:
#         print(product.name)
#         print(product.description)
#         print(product.price)
#         print(product.quantity)
#         print('-------')
#     print(Category.category_count)
#     print(Category.product_count)
