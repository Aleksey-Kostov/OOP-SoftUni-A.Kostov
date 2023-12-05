from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    TYPE_OF_DELICACY = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    TYPE_OF_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.TYPE_OF_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        obj_delicacy = self.TYPE_OF_DELICACY[type_delicacy](name, price)
        if obj_delicacy.name in [d.name for d in self.delicacies]:
            raise Exception(f"{obj_delicacy.name} already exists!")
        self.delicacies.append(obj_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        obj_booth = self.TYPE_OF_BOOTHS[type_booth](booth_number, capacity)
        if type_booth not in self.TYPE_OF_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        if obj_booth.booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {obj_booth.booth_number} already exists!")
        self.booths.append(obj_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        find_booth = next((b for b in self.booths if b.is_reserved is False and number_of_people <= b.capacity), None)
        if find_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        find_booth.reserve(number_of_people)
        return f"Booth {find_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        obj_booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        obj_delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if obj_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if obj_delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        obj_booth.delicacy_orders.append(obj_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        obj_booth = next(b for b in self.booths if b.booth_number == booth_number)
        get_bill = obj_booth.price_for_reservation + sum(d.price for d in obj_booth.delicacy_orders)
        self.income += get_bill
        obj_booth.delicacy_orders = []
        obj_booth.is_reserved = False
        obj_booth.price_for_reservation = 0.0
        return (f"Booth {booth_number}:\n"
                f"Bill: {get_bill:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
