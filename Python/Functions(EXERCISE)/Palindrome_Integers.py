def input_and_operation():

    # user_input, variables and lists
    numbers = input().split(", ")
    positive_numbers = list()

    # functions
    check_if_number_is_positive(numbers, positive_numbers)
    check_if_number_is_palindrome(positive_numbers)


def check_if_number_is_positive(numbers, positive_numbers):
    for elements in numbers:
        if int(elements) > 0:
            positive_numbers.append(elements)
    return positive_numbers


def check_if_number_is_palindrome(positive_numbers):

    for num in positive_numbers:

        num_forwards = ""
        num_backwards = ""

        for forwards_element in num:
            num_forwards += str(forwards_element)
        for index_backwards_element in range(len(num) - 1, -1, -1):
            num_backwards += str(num[index_backwards_element])

        if num_forwards == num_backwards:
            print("True")
        else:
            print("False")


input_and_operation()