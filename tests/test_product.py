def test_init_product(product_dron):
    assert product_dron.name == "Dron_bot"
    assert product_dron.description == "Now"
    assert product_dron.price == 190.8
    assert product_dron.quantity == 5
