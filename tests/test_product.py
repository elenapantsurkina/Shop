
from src.product import Product


def test_product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_new_product(product_dict):
    product = Product.new_product(product_dict)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_info_price(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = 100
    assert product.price == 100

def test_product_str(product):
    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."

def test_product_add(product1, product2):
    assert product1 + product2 == 2580000
