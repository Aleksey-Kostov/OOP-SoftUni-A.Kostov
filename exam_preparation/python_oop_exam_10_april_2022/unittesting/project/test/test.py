from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Mark", 1985, 50.6)

    def test_initialize(self):
        self.assertEqual("Mark", self.movie.name)
        self.assertEqual(1985, self.movie.year)
        self.assertEqual(50.6, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_with_happy_end(self):
        self.movie.actors = ["Kevin", "Jon", "Eddy"]
        self.movie.add_actor("Ivan")
        expected = ["Kevin", "Jon", "Eddy", "Ivan"]
        self.assertEqual(expected, self.movie.actors)

    def test_add_actor_with_name_in_actors(self):
        self.movie.actors = ["Kevin", "Jon", "Eddy"]
        expected = self.movie.add_actor("Kevin")
        self.assertEqual("Kevin is already added in the list of actors!", expected)

    def test___gt__when_rating_is_bigger_from_other_rating(self):
        other = Movie("Donev", 2003, 40.2)
        expected = self.movie.__gt__(other)
        self.assertEqual('"Mark" is better than "Donev"', expected)

    def test_test___gt__when_other_rating_is_bigger(self):
        other = Movie("Donev", 2003, 100.53)
        expected = self.movie.__gt__(other)
        self.assertEqual('"Donev" is better than "Mark"', expected)

    def test_represent(self):
        self.movie.actors = ["Kevin", "Jon", "Eddy"]
        expected = f"Name: Mark\n" \
                   f"Year of Release: 1985\n" \
                   f"Rating: 50.60\n" \
                   f"Cast: Kevin, Jon, Eddy"
        self.assertEqual(expected, str(self.movie))


if __name__ == '__main__':
    main()
