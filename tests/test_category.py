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
