def input_and_operations():
    string_number = input()

    even_list, odd_list = go_threw_elements_in_numbers(string_number)
    print(f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}")


def go_threw_elements_in_numbers(string_number):
    even_list = list()
    odd_list = list()
    for element in string_number:
        int_element = int(element)
        if int_element % 2 == 0:
            even_list.append(int_element)
        else:
            odd_list.append(int_element)

    return even_list, odd_list


input_and_operations()