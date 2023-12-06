from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name):
        super().__init__(name, 25)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
