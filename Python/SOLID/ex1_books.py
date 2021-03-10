from abc import ABC, abstractmethod


class Book:
    def __init__(self,
                 title,
                 author,
                 total_pages,
                 description):

        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.description = description


class LibraryStorage:
    pass


class Library:
    def __init__(self,
                 name: str,
                 location: str,
                 books: dict):
        """
        Books = {'author': {book: quantity, ...}, ...}
        """

        self.name = name
        self.location = location
        self.books = books
        self.storage = set()

    @staticmethod
    def __does_obj_already_exist(obj, storage) -> bool:
        return obj in storage

    def add_book(self, book: Book) -> str:
        book_author = book.author
        author_books = self.books[book_author]

        if Library.__does_obj_already_exist(book, author_books):
            self.books[book_author][book] += 1
            return f"The amount of book '{book.title}'" \
                   f" successfully increased!"
        else:
            self.books[book_author][book] = 1
            return f"New book with title {book.title}" \
                   f" was successfully added to the library!"

    def add_storage(self, storage: LibraryStorage):
        self.storage.add(storage)


class User(ABC):
    @abstractmethod
    def __init__(self,
                 user_name: str,
                 password: str,
                 email: str):

        self.__user_name = user_name
        self.__password = password
        self.__email = email

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @user_name.setter
    def user_name(self, new_value):
        self.__user_name = new_value

    @password.setter
    def password(self, new_value):
        self.__password = new_value

    @email.setter
    def email(self, new_value):
        self.__email = new_value


class Manger(User):
    def __init__(self,
                 user_name: str,
                 password: str,
                 email: str):

        super().__init__(user_name, password, email)


class Reader(User):
    def __init__(self,
                 user_name: str,
                 password: str,
                 email: str):

        super().__init__(user_name, password, email)
        self.current_book = None
        self.start_page = 0

    def __has_reader_chosen_a_book(self):
        return self.current_book

    def read_book(self, book: Book):
        self.current_book = book

    def change_page_with_custom_amount(self, page):
        if not self.__has_reader_chosen_a_book():
            return "Please choose a book to read!"

        if page <= self.current_book.total_pages:
            self.start_page = page
