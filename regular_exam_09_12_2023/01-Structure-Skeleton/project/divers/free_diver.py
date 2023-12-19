from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    CURRENT_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, 120)

    def miss(self, time_to_catch: int):
        percent_time_to_catch = 0.6 * time_to_catch
        if self.oxygen_level < percent_time_to_catch:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= percent_time_to_catch
            self.oxygen_level = round(self.oxygen_level, 0)

    def renew_oxy(self):
        self.oxygen_level = 120
