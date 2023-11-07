class Coffee:
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, caffeine: float):
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
