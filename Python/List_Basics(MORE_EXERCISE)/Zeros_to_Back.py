list_string_numbers = input().split(", ")
list_int_numbers = list()
number_list = list()
zero_list = list()


def check_user_input():
    for _ in range(len(list_string_numbers)):
        element = list_string_numbers[_]
        list_int_numbers.append(int(element))


def go_threw_int_elements():
    for index in range(len(list_int_numbers)):
        element = list_int_numbers[index]
        if element != 0:
            number_list.append(element)
        else:
            zero_list.append(element)


def add_zeros():
    for counter in range(len(zero_list)):
        number_list.append(zero_list[counter])


check_user_input()
go_threw_int_elements()
add_zeros()
print(number_list)