import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def product_dron():
    return Product('Dron_bot', 'Now', 190.8, 5)


@pytest.fixture
def category_bakery():
    return Category('bakery', 'bakery', [
        Product('cookie', 'cookies', 20, 10),
        Product('pie', 'pies', 50, 5)])

@pytest.fixture
def category_fpv():
    return Category('dron', 'new_dron', [
        Product('Dron_bot', 'Now', 190.8, 5),
        Product('Dron_cinema', 'by', 50.0, 3)])
