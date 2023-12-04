from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        return f"""{self.name} Secondary Service:
Robots: {self._get_names()}"""
