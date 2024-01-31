class Product:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def getb(self):
        return self.__b


product = Product(1, 2)
print(product.b)
    