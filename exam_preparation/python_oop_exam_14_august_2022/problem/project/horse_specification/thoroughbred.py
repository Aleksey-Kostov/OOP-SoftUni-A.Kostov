from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140

    def train(self):
        if self.speed <= 137:
            self.speed += 3
        else:
            self.speed = self.MAXIMUM_SPEED

