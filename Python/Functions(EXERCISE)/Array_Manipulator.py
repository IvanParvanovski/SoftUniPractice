import sys
main_list = input().split()


def max_odd(main_list):
    check = False
    biggest_odd_num = -sys.maxsize
    biggest_odd_index = -sys.maxsize
    for index in range(len(main_list)):
        element = int(main_list[index])
        if element >= biggest_odd_num and element % 2 != 0:
            check = True
            biggest_odd_num = element
            biggest_odd_index = index
    if check:
        return biggest_odd_index
    else:
        print("No matches")


def max_even(main_list):
    check = False
    biggest_even_num = -sys.maxsize
    biggest_even_index = -sys.maxsize
    for index in range(len(main_list)):
        element = int(main_list[index])
        if element >= biggest_even_num and element % 2 == 0:
            check = True
            biggest_even_num = element
            biggest_even_index = index
    if check:
        return biggest_even_index
    else:
        print("No matches")


def min_odd(main_list):
    check = False
    min_odd_num = sys.maxsize
    min_odd_index = sys.maxsize
    for index in range(len(main_list)):
        element = int(main_list[index])
        if element <= min_odd_num and element % 2 != 0:
            check = True
            min_odd_num = element
            min_odd_index = index
    if check:
        return min_odd_index
    else:
        print("No matches")


def min_even(main_list):
    check = False
    min_even_num = sys.maxsize
    min_even_index = sys.maxsize
    for index in range(len(main_list)):
        element = int(main_list[index])
        if element <= min_even_num and element % 2 == 0:
            check = True
            min_even_num = element
            min_even_index = index
    if check:
        return min_even_index
    else:
        print("No matches")


def first_count_odd(first_odd_elements_count, main_list):
    first_odd_numbers_list = list()
    main_list_copy = list()
    for counter_copy in range(len(main_list)):
        element = main_list[counter_copy]
        main_list_copy.append(element)
    for counter in range(first_odd_elements_count):
        for index in range(len(main_list_copy)):
            element = main_list_copy[index]
            if int(element) % 2 != 0:
                first_odd_numbers_list.append(int(element))
                main_list_copy.remove(element)
                break
    return first_odd_numbers_list


def first_count_even(first_even_elements_count, main_list):
    first_even_numbers_list = list()
    main_list_copy = list()
    for counter_copy in range(len(main_list)):
        element = main_list[counter_copy]
        main_list_copy.append(element)
    for counter in range(first_even_elements_count):
        for index in range(len(main_list_copy)):
            element = main_list_copy[index]
            if int(element) % 2 == 0:
                first_even_numbers_list.append(int(element))
                main_list_copy.remove(element)
                break
    return first_even_numbers_list


def last_count_odd(last_odd_elements_count, main_list):
    last_odd_numbers_list = list()
    main_list_copy = list()
    for counter_copy in range(len(main_list)):
        element = main_list[counter_copy]
        main_list_copy.append(element)
    for counter in range(last_odd_elements_count):
        for index in range(len(main_list_copy) -1, -1, -1):
            element = main_list_copy[index]
            if int(element) % 2 != 0:
                last_odd_numbers_list.append(int(element))
                main_list_copy.remove(element)
                break
    return last_odd_numbers_list


def last_count_even(last_even_elements_count, main_list):
    last_even_numbers_list = list()
    main_list_copy = list()
    for counter_copy in range(len(main_list)):
        element = main_list[counter_copy]
        main_list_copy.append(element)
    for counter in range(last_even_elements_count):
        for index in range(len(main_list_copy) - 1, -1, -1):
            element = main_list_copy[index]
            if int(element) % 2 == 0:
                last_even_numbers_list.append(int(element))
                main_list_copy.remove(element)
                break
    return last_even_numbers_list


command = input()
while command != "end":

    if "exchange" in command:
        string_exchange_split = command.split()
        string_exchange_split.remove("exchange")
        position_forward = int(string_exchange_split[0])
        if 0 <= position_forward < len(main_list):
            first_index = 0
            left_digits = 0

            zero_list = list()
            for counter in range(len(main_list)):
                zero_list.append(0)

            for index_1 in range(len(main_list)):
                element = main_list[index_1]
                if index_1 + position_forward < len(main_list):
                    zero_list[index_1 + position_forward] = int(element)
                else:
                    left_digits = len(main_list) - index_1
                    first_index = index_1
                    break

            for index_2 in range(left_digits):
                element = main_list[first_index]
                zero_list[index_2] = element
                first_index += 1
            main_list = zero_list
        else:
            print("Invalid index")

    elif "max" in command:
        string_max_split = command.split()
        string_max_split.remove("max")

        if "odd" in string_max_split:
            biggest_odd_index = max_odd(main_list)
            if biggest_odd_index is not None:
                print(biggest_odd_index)
        else:
            biggest_even_index = max_even(main_list)
            if biggest_even_index is not None:
                print(biggest_even_index)

    elif "min" in command:
        string_min_split = command.split()
        string_min_split.remove("min")

        if "odd" in string_min_split:
            min_odd_index = min_odd(main_list)
            if min_odd_index is not None:
                print(min_odd_index)
        else:
            min_even_index = min_even(main_list)
            if min_even_index is not None:
                print(min_even_index)

    elif "first" in command:
        string_first_split = command.split()
        string_first_split.remove("first")

        if "odd" in string_first_split:
            string_first_split.remove("odd")
            int_first_split = int(string_first_split[0])
            if int_first_split > len(main_list):
                print("Invalid count")
            else:
                first_odd_numbers = first_count_odd(int_first_split, main_list)
                print(first_odd_numbers)
        else:
             string_first_split.remove("even")
             int_first_split = int(string_first_split[0])
             if int_first_split > len(main_list):
                 print("Invalid count")
             else:
                first_even_numbers = first_count_even(int_first_split, main_list)
                print(first_even_numbers)

    elif "last" in command:
        string_last_split = command.split()
        string_last_split.remove("last")

        if "odd" in string_last_split:
            string_last_split.remove("odd")
            int_last_split = int(string_last_split[0])
            if int_last_split > len(main_list):
                print("Invalid count")
            else:
                print(last_count_odd(int_last_split, main_list))
        else:
            string_last_split.remove("even")
            int_last_split = int(string_last_split[0])
            if int_last_split > len(main_list):
                print("Invalid count")
            else:
                int_last_split = int(string_last_split[0])
                print(last_count_even(int_last_split, main_list))

    elif "end" == command:
        break
    command = input()
print(main_list)
