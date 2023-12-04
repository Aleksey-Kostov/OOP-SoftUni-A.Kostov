from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    EXPECTED_TYPE_SERVICE = "MainService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9)

    def eating(self):
        self.weight += 3
