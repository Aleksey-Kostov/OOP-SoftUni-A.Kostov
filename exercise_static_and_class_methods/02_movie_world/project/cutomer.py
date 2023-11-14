from typing import List
from project.dvd import DVD


class Costumer:
    def __init__(self, name: str, age: int, costumer_id: int):
        self.name = name
        self.age = age
        self.id = costumer_id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        dvd_names = ", ".join([d.name for d in self.rented_dvds])
        return (f"{id}: {self.name} of age {self.age} has {len(self.rented_dvds)}"
                f" rented DVD's ({dvd_names})")
