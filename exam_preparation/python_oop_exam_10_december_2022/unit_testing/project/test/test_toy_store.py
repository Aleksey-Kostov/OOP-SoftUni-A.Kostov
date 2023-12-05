from project.toy_store import ToyStore

from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toy = ToyStore()

    def test_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

    def test_add_toy_if_shelf_not_in_toy_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("R", "Test")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_if_toy_name_not_in_toy_shelf(self):
        with self.assertRaises(Exception) as ex1:
            self.toy.add_toy("A", "Test")
            self.toy.add_toy("A", "Test")

        self.assertEqual("Toy is already in shelf!", str(ex1.exception))

    def test_add_toy_if_toy_shelf_in_but_name_is_diff(self):
        with self.assertRaises(Exception) as ex2:
            self.toy.add_toy("A", "Test")
            self.toy.add_toy("A", "Test2")

        self.assertEqual("Shelf is already taken!", str(ex2.exception))

    def test_add_toy_with_happy_case(self):
        self.toy.add_toy("A", "Test")
        self.assertEqual({
            "A": "Test",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

        self.assertEqual(f"Toy:Test placed successfully!", self.toy.add_toy("B", "Test"))

    def test_remove_toy_rise_exception_if_shelf_not_in_shelf_dict(self):
        with self.assertRaises(Exception) as ex3:
            self.toy.remove_toy("R", "Test")
        self.assertEqual("Shelf doesn't exist!", str(ex3.exception))

    def test_remove_toy_rise_exception_if_name_is_not_equal(self):
        with self.assertRaises(Exception) as ex4:
            self.toy.add_toy("A", "Test")
            self.toy.remove_toy("A", "Test2")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex4.exception))

    def test_remove_toy_with_happy_case(self):
        self.toy.add_toy("A", "Test")
        self.toy.remove_toy("A", "Test")
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)
        self.toy.add_toy("A", "Test")

        self.assertEqual("Remove toy:Test successfully!", self.toy.remove_toy("A", "Test"))


if __name__ == '__main__':
    main()
