from typing import List


class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name):
        pass

    def unregister_animal(self, animal_name):
        pass

    def info(self):
        pass
