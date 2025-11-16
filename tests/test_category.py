def test_init_category(category_bakery, category_fpv):
    assert category_bakery.name == "bakery"
    assert category_bakery.description == "bakery"
    assert len(category_bakery.products) == 2

    assert category_bakery.category_count == 2
    assert category_fpv.category_count == 2

    assert category_bakery.product_count == 4
    assert category_fpv.product_count == 4
