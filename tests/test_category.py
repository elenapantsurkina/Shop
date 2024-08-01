import pytest
from src.product import Product
from src.category import Category


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert first_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_init2(first_category, second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert second_category.products == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"

def test_add_product():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category.add_product(product)
    assert category.product_count == 9
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_products_property():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product1)
    category.add_product(product2)
    products_str = category.products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str
