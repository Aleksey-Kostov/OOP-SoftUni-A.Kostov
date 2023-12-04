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
        obj_robot = self._check_object(robot_name, self.robots)
        obj_service = self._check_object(service_name, self.services)
        if obj_robot.EXPECTED_TYPE_SERVICE != obj_service.__class__.__name__:
            return "Unsuitable service."
        if len(obj_service.robots) >= obj_service.capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(obj_robot)
        obj_service.robots.append(obj_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        object_service = self._check_object(service_name, self.services)
        robot = [r for r in object_service.robots if r.name == robot_name]
        if not robot:
            raise Exception("No such robot in this service!")
        object_robot = robot[0]
        object_service.robots.remove(object_robot)
        self.robots.append(object_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        obj_service = self._check_object(service_name, self.services)
        [r.eating() for r in obj_service.robots]
        return f"Robots fed: {len(obj_service.robots)}."

    def service_price(self, service_name: str):
        obj_service = self._check_object(service_name, self.services)
        total_price = sum([r.price for r in obj_service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([s.details() for s in self.services])

    @staticmethod
    def _check_object(name_obj, collection):
        return next((o for o in collection if o.name == name_obj), None)

    # def _check_capacity(self):
    #     return next((s for s in self.services if s.capacity > len(s.robots)), None)
    #
    # def _check_service(self, robot_name):
    #     return next((r for r in self.services if r.name == robot_name), None)
