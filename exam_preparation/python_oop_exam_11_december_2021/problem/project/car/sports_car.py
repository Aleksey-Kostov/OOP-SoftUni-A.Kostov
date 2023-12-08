from project.car.car import Car


class SportsCar(Car):
    @property
    def min_speed(self):
        return 400

    @property
    def max_speed(self):
        return 600
