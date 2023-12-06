from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(50)

    def test_init(self):
        self.assertEqual(50, self.store.books_limit)
        self.store.availability_in_store_by_book_titles = {"Book": 1, "Book2": 2, "Book3": 3}
        self.assertEqual({"Book": 1, "Book2": 2, "Book3": 3}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_setter_books_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -1

        self.assertEqual(f"Books limit of -1 is not valid", str(ve.exception))

    def test_len__(self):
        self.store.availability_in_store_by_book_titles = {"Book": 1, "Book2": 2, "Book3": 3}
        self.assertEqual(6, self.store.__len__())

    def test_receive_book_if_there_is_not_enough_space_in_the_bookstore(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Book", 60)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_if_there_is_enough_space_in_the_bookstore(self):
        self.store.availability_in_store_by_book_titles = {"Book": 1, "Book2": 2}
        self.store.receive_book("Book", 1)
        self.assertEqual({"Book": 2, "Book2": 2}, self.store.availability_in_store_by_book_titles)

        self.store.availability_in_store_by_book_titles = {"Book": 1, "Book2": 2}
        self.store.receive_book("Test", 1)
        self.assertEqual({"Book": 1, "Book2": 2, "Test": 1}, self.store.availability_in_store_by_book_titles)

        self.assertEqual("2 copies of Test are available in the bookstore.", self.store.receive_book("Test", 1))

        self.store.receive_book("Test", 1)

        self.assertEqual("4 copies of Test are available in the bookstore.", self.store.receive_book("Test", 1))

    def test_sell_book_if_the_book_is_not_available_in_the_bookstore(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Test", 2)
        self.assertEqual("Book Test doesn't exist!", str(ex.exception))

    def test_sell_book_if_there_is_not_enough_copies_of_that_book_to_sell(self):
        self.store.availability_in_store_by_book_titles = {"Book": 1, "Book2": 2}
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book", 2)
        self.assertEqual("Book has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_if_can_sell_successfully(self):
        self.store.availability_in_store_by_book_titles = {"Book": 3, "Book2": 2}
        sell = self.store.sell_book("Book", 1)
        self.assertEqual({"Book": 2, "Book2": 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(1, self.store.total_sold_books)
        self.assertEqual("Sold 1 copies of Book", sell)

        sell = self.store.sell_book("Book", 1)
        self.assertEqual({"Book": 1, "Book2": 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(2, self.store.total_sold_books)
        self.assertEqual("Sold 1 copies of Book", sell)

    def test_str__(self):
        self.store.availability_in_store_by_book_titles = {"Book": 3}
        sell = self.store.sell_book("Book", 1)
        result = "Total sold books: 1\nCurrent availability: 2\n - Book: 2 copies"
        self.assertEqual(result, str(self.store))
        self.assertEqual({"Book": 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("Sold 1 copies of Book", sell)


if __name__ == '__main__':
    main()
