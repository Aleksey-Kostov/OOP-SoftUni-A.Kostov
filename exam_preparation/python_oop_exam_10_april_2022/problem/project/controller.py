from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE_TYPES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *player: Player):
        for player in self.players:
            if player in self.players:
                return
        self.players.append(player)
        return f"Successfully added: {', '.join([p.name for p in self.players])}"

    def add_supply(self, *supply: Supply):
        for s in supply:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player_obj = next((p for p in self.players if p.name == player_name), None)
        if sustenance_type not in self.VALID_SUSTENANCE_TYPES or not player_obj:
            return
        if player_obj.stamina == 100:
            return f"{player_name} have enough stamina."
        supplies_obj = next((s for s in self.supplies[::-1] if s.__class__.__name__ == sustenance_type), None)
        if sustenance_type == "Food" and supplies_obj:
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink" and supplies_obj:
            raise Exception("There are no drink supplies left!")
        if supplies_obj:
            player_obj._sustain_player(supplies_obj)
            self.supplies.remove(supplies_obj)
            return f"{player_name} sustained successfully with {supplies_obj.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one_obj = next((p for p in self.players if p.name == first_player_name), None)
        player_two_obj = next((p for p in self.players if p.name == second_player_name), None)
        self._check_if_the_players_cannot_duel(player_one_obj, player_two_obj)
        self._reduce_stamina(player_one_obj, player_two_obj)
        if self._stamina_set(player_one_obj, player_two_obj) is not None:
            return self._stamina_set(player_one_obj, player_two_obj)
        if self._get_winner(player_one_obj, player_two_obj) is not None:
            return self._get_winner(player_one_obj, player_two_obj)

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []
        for p in self.players:
            result.append("\n".join(p.__str__()))
        for s in self.supplies:
            result.append("\n".join(s.details()))
        return result



    @staticmethod
    def _reduce_stamina(player_one, player_two):
        if player_one.stamina < player_two.stamina:
            player_two.stamina -= player_one.stamina / 2
        elif player_one.stamina > player_two.stamina:
            player_one.stamina -= player_two.stamina / 2

    @staticmethod
    def _stamina_set(player_one, player_two):
        winner_name = ""
        if player_one.stamina <= 0:
            player_one.stamina = 0
            winner_name = player_two.name
            return f"Winner: {winner_name}"
        if player_two.stamina <= 0:
            player_two.stamina = 0
            winner_name = player_one.name
            return f"Winner: {winner_name}"

    @staticmethod
    def _get_winner(player_one, player_two):
        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_one.name}"
        elif player_two.stamina > player_one.stamina:
            return f"Winner: {player_two.name}"
    @staticmethod
    def _check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 100:
                result.append(f"Player {player.name} does not have enough stamina.")
        return "\n".join(result)
