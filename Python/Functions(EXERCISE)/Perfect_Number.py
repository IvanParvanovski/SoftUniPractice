def input_and_operations():
    number = int(input())

    sum_of_divisors = sum(divisors(number))
    check_if_num_is_perfect(sum_of_divisors, number)


def divisors(number):

    divisors_list = list()
    for counter in range(1, number):
        if number % counter == 0:
            divisors_list.append(counter)
    return divisors_list


def check_if_num_is_perfect(sum_of_divisors, number):
    if sum_of_divisors == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


input_and_operations()