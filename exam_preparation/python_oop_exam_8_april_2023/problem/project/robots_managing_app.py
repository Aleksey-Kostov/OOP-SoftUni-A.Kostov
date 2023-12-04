from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_TYPE_SERVICE = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_TYPE_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_TYPE_SERVICE:
            raise Exception("Invalid service type!")
        valid_type = self.VALID_TYPE_SERVICE[service_type](name)
        self.services.append(valid_type)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_TYPE_ROBOTS:
            raise Exception("Invalid robot type!")
        valid_type_robot = self.VALID_TYPE_ROBOTS[robot_type](name, kind, price)
        self.robots.append(valid_type_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        if self._check_robots(robot_name) is None:
            return "Unsuitable service."
        if self._check_capacity() is None:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot_name)
        self.VALID_TYPE_SERVICE[service_name].robots.append(robot_name)

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        pass

    def service_price(self, service_name: str):
        pass

    def __str__(self):
        pass

    def _check_robots(self, name_robot):
        return next((r for r in self.robots if name_robot == r.EXPECTED_TYPE_SERVICE), None)

    def _check_capacity(self):
        return next((s for s in self.services if s.capacity <= len(s.robots)), None)
