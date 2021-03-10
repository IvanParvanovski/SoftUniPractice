user_string = input()
user_count_of_repeating_string = int(input())


def repeating_string(string, count_of_repeating_string):
    for counter in range(count_of_repeating_string):
        print(string, end="")


repeating_string(user_string, user_count_of_repeating_string)


