first_num_range = int(input())
second_num_range = int(input())
magic_num = int(input())
magic_counter = 0
number_one = 0
number_two = 0

for number_one in range(first_num_range,second_num_range + 1):
    for number_two in range(first_num_range, second_num_range + 1):
        if number_one + number_two == magic_num:
            magic_counter += 1
            print(f"Combination N:{magic_counter} ({number_one} + {number_two} = {number_one + number_two})")
            break
        else:
            magic_counter += 1

    if number_one + number_two == magic_num:
        break

if number_one + number_two != magic_num:
    print(f"{magic_counter} combinations - neither equals {magic_num}")