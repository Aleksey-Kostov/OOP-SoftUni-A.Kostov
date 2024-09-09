from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_TYPE_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_TYPE_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_TYPE_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        if diver_name in [d.name for d in self.divers]:
            return f"{diver_name} is already a participant."
        diver = self.VALID_TYPE_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_TYPE_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        if fish_name in [f.name for f in self.fish_list]:
            return f"{fish_name} is already permitted."
        fish = self.VALID_TYPE_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue is True:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky is True:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."
        if diver.oxygen_level == 0:
            diver.has_health_issue = True

    def health_recovery(self):
        divers = [d for d in self.divers if d.has_health_issue is True]
        if divers:
            for d in divers:
                d.has_health_issue = False
                d.oxygen_level = d.CURRENT_OXYGEN_LEVEL
        return f"Divers recovered: {len(divers)}"

    def diver_catch_report(self, diver_name: str):
        result = []
        diver = next((d for d in self.divers if diver_name == d.name), None)
        if diver:
            result = [f.fish_details() for f in diver.catch]
            result = "\n".join(result)
        return f"**{diver_name} Catch Report**\n{result}"

    def competition_statistics(self):
        result = []
        sorted_divers = sorted(self.divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        if sorted_divers:
            for d in sorted_divers:
                if d.has_health_issue is False:
                    result.append(str(d))

        result = "\n".join(result)
        return f"**Nautical Catch Challenge Statistics**\n{result}"

