book_she_search = input()
library_capacity = int(input())
books = ""
counter = 0

while book_she_search != books and counter < library_capacity:
    books = input()
    counter += 1

if book_she_search == books:
    counter -= 1
    print(f"You checked {counter} books and found it.")

elif books != book_she_search or counter > library_capacity:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")

