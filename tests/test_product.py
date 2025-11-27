from unittest.mock import patch

import pytest

from src.product import Product


def test_init_product(product_dron):
    assert product_dron.name == "Dron_bot"
    assert product_dron.description == "Now"
    assert product_dron.price == 190.8
    assert product_dron.quantity == 5


def test_new_product(product_new):
    new_p = Product.new_product(product_new)
    assert new_p.name == "Dron_bot"
    assert new_p.description == "Now"
    assert new_p.price == 200
    assert new_p.quantity == 5


def test_new_product_in_list(product_new, product_dron):
    list_products = [product_dron]
    Product.new_product(product_new, list_products)
    assert product_dron.name == "Dron_bot"
    assert product_dron.description == "Now"
    assert product_dron.price == 200
    assert product_dron.quantity == 10


def test_new_product_not_in_list(product_new, existing_product):
    list_products = [existing_product]
    new_p = Product.new_product(product_new, list_products)
    assert new_p.name == "Dron_bot"
    assert new_p.description == "Now"
    assert new_p.price == 200
    assert new_p.quantity == 5


def test_price(existing_product, capsys):
    existing_product.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_price_positive(existing_product):
    existing_product.price = 100
    assert existing_product.price == 100


@patch("builtins.input")
def test_price_confirmation_y(mock_input, product_dron):
    mock_input.return_value = "Y"
    product_dron.price = 100
    assert product_dron.price == 100


@patch("builtins.input")
def test_price_confirmation_n(mock_input, product_dron):
    mock_input.return_value = "w"
    product_dron.price = 100
    assert product_dron.price == 190.8


def test_information_output(product_dron):
    assert str(product_dron) == "Dron_bot, 190.8 руб. Остаток: 5 шт."


def test_total_cost(product_dron, existing_product):
    assert product_dron + existing_product == 954


def test_total_cost_error(product_dron, existing_product):
    with pytest.raises(TypeError):
        product_dron + 100
