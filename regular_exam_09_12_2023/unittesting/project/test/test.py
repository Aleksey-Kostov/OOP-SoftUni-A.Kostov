from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("London")

    def test_init(self):
        self.assertEqual("London", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_len_name_setter_is_equal_to_3(self):
        with self.assertRaises(ValueError)as ve:
            self.station.name = "Bon"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_len_name_setter_is_less_than_3(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Bo"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        expected = deque(["Test1"])
        self.station.new_arrival_on_board("Test1")
        self.assertEqual(expected, self.station.arrival_trains)
        expected = deque(["Test1", "Test2"])
        self.station.new_arrival_on_board("Test2")
        self.assertEqual(expected, self.station.arrival_trains)

    def test_train_has_arrived_with_diff_train_info(self):
        expected = deque(["Test1", "Test2"])
        self.station.arrival_trains = deque(["Test1", "Test2"])
        self.assertEqual(expected, self.station.arrival_trains)
        expected2 = "There are other trains to arrive before Test5."
        self.assertEqual(expected2, self.station.train_has_arrived("Test5"))

    def test_train_has_arrived(self):
        self.station.arrival_trains = deque(["Test1", "Test2"])
        expected = "Test1 is on the platform and will leave in 5 minutes."
        self.assertEqual(expected, self.station.train_has_arrived("Test1"))
        expected1 = deque(["Test2"])
        expected2 = deque(["Test1"])
        self.assertEqual(expected1, self.station.arrival_trains)
        self.assertEqual(expected2, self.station.departure_trains)

    def test_train_has_left(self):
        self.station.departure_trains = deque(["Test1", "Test2"])
        self.assertTrue(self.station.train_has_left("Test1"))
        self.assertFalse(self.station.train_has_left("Test5"))


if __name__ == '__main__':
    main()
