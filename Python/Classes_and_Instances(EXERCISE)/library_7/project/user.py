def does_book_exist(author, book_name, library):
    return book_name in library.books_available[author]


def get_rented_book_data(book_name, library):
    for username, data in library.rented_books.items():
        for book_n, days_to_ret in data.items():
            if book_n == book_name:
                msg = f"""The book "{book_name}" is already """
                msg += f"rented and will be available in {days_to_ret} days!"
                return msg


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def does_user_have_current_book(self, book_name):
        return book_name in self.books

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if not does_book_exist(author, book_name, library):
            return get_rented_book_data(book_name, library)

        self.books.append(book_name)
        library.books_available[author].remove(book_name)
        library.rented_books[self.username].update({book_name: days_to_return})
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if not self.does_user_have_current_book(book_name):
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)

    def info(self):
        return f"{', '.join(sorted(self.books))}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
