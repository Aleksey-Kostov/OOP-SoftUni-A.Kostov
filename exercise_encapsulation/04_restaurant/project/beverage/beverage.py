from project.product import Product


class Belverage(Product):
    def __init__(self, milliliters: float, name, price):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters


