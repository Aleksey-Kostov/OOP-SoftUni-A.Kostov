from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPES:
            return
        if model in [c.model for c in self.cars]:
            raise Exception(f"Car {model} is already created!")
        car_obj = self.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(car_obj)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        driver_obj = Driver(driver_name)
        self.drivers.append(driver_obj)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [r.name for r in self.races]:
            raise Exception(f"Driver {race_name} is already created!")
        race_obj = Race(race_name)
        self.races.append(race_obj)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        find_driver = next((d for d in self.drivers if d.name == driver_name), None)
        if find_driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        last_car_type = next((c for c in self.cars[::-1] if c.__class__.__name__ == car_type and not c.is_taken), None)
        if last_car_type is None:
            raise Exception(f"Car {car_type} could not be found!")
        if last_car_type and find_driver.car is not None:
            old_model = find_driver.car.model
            new_model = last_car_type.model
            find_driver.car.is_taken = False
            last_car_type.is_taken = True
            find_driver.car = last_car_type
            return f"Driver {find_driver.name} changed his car from {old_model} to {new_model}."
        if find_driver.car is None:
            find_driver.car = last_car_type
            last_car_type.is_taken = True
            return f"Driver {driver_name} chose the car {last_car_type.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver_obj = next((d for d in self.drivers if d.name == driver_name), None)
        race_obj = next((r for r in self.races if race_name == r.name), None)
        if race_obj is None:
            raise Exception(f"Race {race_name} could not be found!")
        if driver_obj is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver_obj and driver_obj.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver_obj and race_obj and driver_obj.car is not None:
            race_obj.drivers.append(driver_obj)
            return f"Driver {driver_name} added in {race_name} race."
        if driver_obj in race_obj.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

    def start_race(self, race_name: str):
        race_obj = next((r for r in self.races if r.name == race_name), None)
        if race_obj is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race_obj.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        if len(race_obj.drivers) >= 3:
            sorted_result = sorted(race_obj.drivers, key=lambda x: -x.car.speed_limit)
            for result in sorted_result[:3]:
                increase = [d.number_of_wins + 1 for d in result]
                return (f"Driver {result.drivers.name} wins the {race_name} race with a "
                        f"speed of {result.drivers.speed_limit}.")




