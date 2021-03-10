numbers_dictionary = {}

try:
    while True:
        line = input()
        if line == "Search":
            break
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number

    while True:
        line = input()
        if line == "Remove":
            break

        searched = line
        print(numbers_dictionary[searched])

    while True:
        line = input()
        if line == "End":
            break
        searched = line
        del numbers_dictionary[searched]

except ValueError:
    print("The variable number must be an integer")

except KeyError:
    print("Number does not exist in dictionary")

print(numbers_dictionary)
