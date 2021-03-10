books = input().split("&")
command = input()
while command != "Done":
    command = command.split(" | ")
    if command[0] == "Add Book":
        insert_book_start = command[1]
        if insert_book_start not in books:
            books.insert(0, insert_book_start)
    elif command[0] == "Take Book":
        taken_book = command[1]
        if taken_book in books:
            books.remove(taken_book)
    elif command[0] == "Swap Books":
        first_swapped_book = command[1]
        second_swapped_book = command[2]
        first_swapped_book_index = 0
        second_swapped_book_index = 0

        for i1 in range(len(books)):
            if books[i1] == first_swapped_book:
                first_swapped_book_index = i1
                break
        for i2 in range(len(books)):
            if books[i2] == second_swapped_book:
                second_swapped_book_index = i2
                break

        if first_swapped_book in books and second_swapped_book in books:
            books[first_swapped_book_index], books[second_swapped_book_index] = books[second_swapped_book_index], books[first_swapped_book_index]

    elif command[0] == "Insert Book":
        insert_book_end = command[1]
        books.insert(len(books), insert_book_end)
    elif command[0] == "Check Book":
        index = int(command[1])
        if 0 < index < len(books):
            print(books[index])
    command = input()
print(", ".join(books))