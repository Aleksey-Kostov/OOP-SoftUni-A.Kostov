from project.supply.supply import Supply


class Player:
    COLLECTION = []
    def __init__(self, name: str, age: int, stamina: int):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name not valid!")
        if value in self.COLLECTION:
            raise Exception(f"Name {value} is already used!")
        self.COLLECTION.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if  value > 100 or value < 0:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def _sustain_player(self, supply: Supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


