from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, caffeine: float, milliliters: float, name, price):
        super().__init__(milliliters, name, price)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
