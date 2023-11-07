from project.food.food import Food


class Desert(Food):
    def __init__(self, calories: float):
        super().__init__(grams, name, price)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories
