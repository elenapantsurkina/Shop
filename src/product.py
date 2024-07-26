class Product:
    name: str
    description: str
    price: round(1)
    quatity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
