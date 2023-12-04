from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Georgi", 25, 100.00)

    def test_init(self):
        self.assertEqual("Georgi", self.player.name)
        self.assertEqual(25, self.player.age)
        self.assertEqual(100.00, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_setter_name_if_len_name_is_equal_2(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Go"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_setter_name_if_len_name_is_less_from_2_simbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "G"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_setter_age_with_less_than_18(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_with_append(self):
        self.player.add_new_win("Sofia")
        self.assertEqual(["Sofia"], self.player.wins)
        self.assertEqual("Sofia has been already added to the list of wins!", self.player.add_new_win("Sofia"))

    def test___lt___with_less_than_points_to_player_2(self):
        self.player2 = TennisPlayer("Toni", 23, 200.00)

        self.assertEqual(f"{self.player2.name} is a top seeded player and he/she is better "
                         f"than {self.player.name}", self.player.__lt__(self.player2))

    def test___lt___with_less_than_points_to_player_1(self):
        self.player2 = TennisPlayer("Toni", 23, 90)

        self.assertEqual(f"{self.player.name} is a better player than {self.player2.name}",
                         self.player.__lt__(self.player2))

    def test_str(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023', 'FO 2022']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023, FO 2022')


if __name__ == '__main__':
    main()
