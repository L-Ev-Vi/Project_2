import json

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_dron():
    return Product("Dron_bot", "Now", 190.8, 5)


@pytest.fixture
def category_bakery():
    return Category("bakery", "bakery", [Product("cookie", "cookies", 20, 10), Product("pie", "pies", 50, 5)])


@pytest.fixture
def category_fpv():
    return Category("dron", "new_dron", [Product("Dron_bot", "Now", 190.8, 5), Product("Dron_cinema", "by", 50.0, 3)])


@pytest.fixture
def file_json():
    return json.dumps(
        [
            {
                "name": "Dron",
                "description": "new_dron",
                "products": [{"name": "Dron_bot", "description": "Now", "price": 190.8, "quantity": 5}],
            }
        ]
    )


@pytest.fixture
def category_3():
    return Category("Num", "new_num", [])


@pytest.fixture
def product_new():
    return {"name": "Dron_bot", "description": "Now", "price": 200, "quantity": 5}


@pytest.fixture
def existing_product():
    return Product("cookie", "cookies", 0, 10)
