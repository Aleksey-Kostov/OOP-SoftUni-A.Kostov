from project.car.car import Car


class MuscleCar(Car):
    @property
    def min_speed(self):
        return 250

    @property
    def max_speed(self):
        return 450
