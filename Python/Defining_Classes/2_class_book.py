from dataclasses import dataclass


class Book1:
    def __init__(self, book_name, author, pages):
        self.name = book_name
        self.author = author
        self.pages = pages


@dataclass
class Book2:
    name: str
    author: str
    pages: int


# Book1
book = Book1("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

print('\n*\n' )

# Book2
book = Book2("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

