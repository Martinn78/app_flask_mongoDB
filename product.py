class Product:
    def __init__(self, name, price, quantify):
        self.name = name
        self.price = price
        self.quantifi = quantify

    def toDBCollection(self):
        return{
            'name' : self.name,
            'price' : self.price,
            'quantify' : self.quantify
        }