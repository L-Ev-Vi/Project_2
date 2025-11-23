from src.product import Product


def test_init_product(product_dron):
    assert product_dron.name == "Dron_bot"
    assert product_dron.description == "Now"
    assert product_dron._price == 190.8
    assert product_dron.quantity == 5


def test_new_product(product_new):
    new_p = Product.new_product(product_new)
    assert new_p.name == "Dron_bot"
    assert new_p.description == "Now"
    assert new_p._price == 200
    assert new_p.quantity == 5

def test_new_product_in_list(product_new,product_dron):
    list_products = [product_dron]
    Product.new_product(product_new, list_products)
    assert product_dron.name == "Dron_bot"
    assert product_dron.description == "Now"
    assert product_dron._price == 200
    assert product_dron.quantity == 10

def test_new_product_not_in_list(product_new,existing_product):
    list_products = [existing_product]
    new_p = Product.new_product(product_new, list_products)
    assert new_p.name == "Dron_bot"
    assert new_p.description == "Now"
    assert new_p._price == 200
    assert new_p.quantity == 5

def test_price(existing_product, capsys):
    existing_product.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"

def test_price_positive(existing_product):
    existing_product.price = 100
    assert existing_product._price == 100

