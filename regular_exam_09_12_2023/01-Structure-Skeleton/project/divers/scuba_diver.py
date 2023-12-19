from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    CURRENT_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        percent_time_to_catch = 0.3 * time_to_catch
        if self.oxygen_level < percent_time_to_catch:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= percent_time_to_catch
            self.oxygen_level = int(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = 540
