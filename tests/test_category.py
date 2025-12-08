import pytest


def test_init_category(category_bakery, category_fpv):
    assert category_bakery.name == "bakery"
    assert category_bakery.description == "bakery"

    assert category_bakery.category_count == 2
    assert category_fpv.category_count == 2

    assert category_bakery.product_count == 4
    assert category_fpv.product_count == 4


def test_add_product(category_3, product_dron):
    assert category_3.product_count == 4
    category_3.add_product(product_dron)
    assert category_3.product_count == 5


def test_product(category_bakery):
    assert category_bakery.products == "cookie, 20 руб. Остаток: 10 шт.\npie, 50 руб. Остаток: 5 шт.\n"


def test_displaying_information_about_category(category_fpv):
    assert str(category_fpv) == "dron, количество продуктов: 8 шт."


def test_add_product_error(category_3, category_fpv):
    with pytest.raises(TypeError):
        category_3.add_product(category_fpv)


def test_middle_price_error(category_3):
    assert category_3.middle_price() == 0.0


def test_middle_price(category_fpv):
    assert category_fpv.middle_price() == 138


def test_add_product_error_quantity(category_3, quantity_is_zero, capsys):
    category_3.add_product(quantity_is_zero)
    captured = capsys.readouterr()
    assert captured.out == (
        "Попытка добавить товар с нулевым количеством\n" "Обработка добавления товара завершена.\n"
    )


def test_error_when_adding_a_product(my_exceptions, capsys):
    print(my_exceptions)
    captured = capsys.readouterr()
    assert captured.out == "Общая ошибка при добавлении товара\n"
