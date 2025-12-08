from src.order import Order


def test_init_order(order1):
    assert order1._Order__id == 1
    assert order1._Order__name_product == "Samsung Galaxy S23 Ultra"
    assert order1.description == "256GB, Серый цвет, 200MP камера"
    assert order1._Order__price == 180000.0
    assert order1.quantity == 1

    assert (
        order1.products
        == "Заказ №1, Товар: Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, в количестве: 1 шт., "
        "стоимостью: 180000.0\n"
    )

    assert order1._Order__ID_ORDER == 2
    assert order1._Order__order_count == 1
    assert order1._Order__number_products_sold == 1

    order1.add_product("Samsung Galaxy S23 Ultra", 180000.0, 2)
    assert (
        order1.products
        == "Заказ №1, Товар: Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, в количестве: 3 шт., "
        "стоимостью: 540000.0\n"
    )
    assert order1._Order__ID_ORDER == 2
    assert order1._Order__order_count == 1
    assert order1._Order__number_products_sold == 3


def test_order_add_product_error_name(order1, capsys):
    order1.add_product("Iphone 15", 210000.0, 2)
    captured = capsys.readouterr()
    assert captured.out == (
        "Для товара Iphone 15 необходимо сформировать отдельный заказ\n" "Обработка добавления товара завершена.\n"
    )


def test_init_order_message(capsys):
    Order("Samsung Galaxy S23 Ultra", "Серый цвет", 180000.0, 1)
    captured = capsys.readouterr()
    assert captured.out == ("Товар добавлен.\n" "Обработка добавления товара завершена.\n")


def test_init_order_error_message(capsys):
    Order("Samsung Galaxy S23 Ultra", "Серый цвет", 180000.0, 0)
    captured = capsys.readouterr()
    assert captured.out == (
        "Попытка добавить товар с нулевым количеством\n" "Обработка добавления товара завершена.\n"
    )


def test_order_add_product_error_quantity(order1, capsys):
    order1.add_product("Samsung Galaxy S23 Ultra", 180000.0, 0)
    captured = capsys.readouterr()
    assert captured.out == ("Не указанно количество товара\n" "Обработка добавления товара завершена.\n")
