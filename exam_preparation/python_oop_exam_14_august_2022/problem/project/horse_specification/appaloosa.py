from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        else:
            self.speed = self.MAXIMUM_SPEED
