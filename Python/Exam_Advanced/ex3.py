def list_manipulator(numbers, *args):
    add_or_remove, beginning_or_end, other_numbers = args[0], args[1], args[2:]

    if add_or_remove == "add":
        if beginning_or_end == "beginning":
            for i in range(len(other_numbers) - 1, -1, -1):
                numbers.insert(0, other_numbers[i])

        elif beginning_or_end == "end":
            for i in range(len(other_numbers)):
                numbers.insert(len(numbers), other_numbers[i])

    elif add_or_remove == "remove":
        if beginning_or_end == "beginning":
            if other_numbers:
                for _ in range(other_numbers[0]):
                    numbers.pop(0)
            else:
                numbers.pop(0)

        elif beginning_or_end == "end":
            if other_numbers:
                for _ in range(other_numbers[0]):
                    numbers.pop()
            else:
                numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
