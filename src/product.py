class Product:
    name: str
    description: str
    price: round(2)
    quatity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
