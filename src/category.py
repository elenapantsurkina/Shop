from src.product import Product
from src.smartphone import Smartphone
from src.exceptions import ZeroProduct


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
            try:
                if product.quantity == 0:
                    raise ZeroProduct("Нельзя внести товар с нулевым количеством")
            except ZeroProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
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

    def middle_price(self):
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0
