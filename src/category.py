from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []      # сделали категорию приватной

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):       # геттер выводит список товаров в виде строк в заданном формате
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток {product.quantity} шт.\n"
        return products_str
