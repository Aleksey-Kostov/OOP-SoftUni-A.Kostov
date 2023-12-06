from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSES_VALID_TYPE = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    JOCKEYS = {"Jockey": Jockey}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.HORSES_VALID_TYPE:
            return
        horse_obj = self.HORSES_VALID_TYPE[horse_type](horse_name, horse_speed)
        if horse_obj.name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")
        self.horses.append(horse_obj)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        # jockey_obj = self.JOCKEYS["Jockey"](jockey_name, age)
        jockey_obj = Jockey(jockey_name, age)
        if jockey_obj.name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(jockey_obj)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race_obj = HorseRace(race_type)
        if race_obj.race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(race_obj)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        last_horse_obj = next((h for h in self.horses[::-1]
                               if h.__class__.__name__ == horse_type and not h.is_taken), None)
        jokey_obj = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jokey_obj is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if last_horse_obj is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jokey_obj.horse:
            return f"Jockey {jockey_name} already has a horse."
        if last_horse_obj and jokey_obj:
            jokey_obj.horse = last_horse_obj
            last_horse_obj.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {last_horse_obj.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jokey_obj = next((j for j in self.jockeys if j.name == jockey_name), None)
        get_race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if get_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jokey_obj is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jokey_obj.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jokey_obj in get_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        get_race.jockeys.append(jokey_obj)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jokey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return (f"The winner of the {race_type} race, with a speed of "
                f"{winner_jokey.horse.speed}km/h is {winner_jokey.name}! Winner's horse: {winner_jokey.horse.name}.")
