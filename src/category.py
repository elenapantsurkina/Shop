from src.product import Product

from src.smartphone import Smartphone


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []  # сделали категорию приватной

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def total_product(self):
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        total_quatity = self.total_product()
        return f"{self.name}, количество продуктов: {total_quatity} шт."

    @property
    def products(self):  # геттер выводит список товаров в виде строк в заданном формате
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str
