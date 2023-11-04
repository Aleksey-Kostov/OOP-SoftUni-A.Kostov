from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.add_user_not_reg(user)
                user.books.append(book_name)
                self.rented_books[user.username][book_name] = days_to_return
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username_key, book_info_dict in self.rented_books.items(): # TODO
            for book, days in book_info_dict.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in' \
                            f' {days} days!'

    def return_book(self, author:str, book_name:str, user: User):
        if book_name in user.books:
            self.rented_books[user.username].pop(book_name)
            self.books_available[author].append(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"

    def add_user_not_reg(self, user: User):
        for user_rec in self.user_records:
            if user_rec.user_id == user.user_id:
                return
        self.user_records.append(user)
        self.rented_books[user.username] = {}