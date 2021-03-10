n = int(input())
l = int(input())
first_symbol = ""
second_symbol = ""
third_symbol = ""
fourth_symbol = ""
fifth_symbol = ""

for counter in range(4):

    for first_index in range(1,n):
        first_symbol = first_index

        for second_index in range(1,n):
            second_symbol = second_index

            for third_index in range(97, 97 + l):
                third_symbol = chr(third_index)

                for fourth_index in range(97 , 97 + l):
                    fourth_symbol = chr(fourth_index)

                    for fifth_index in range(1, n + 1):
                        if fifth_index > first_index:
                            fifth_symbol = fifth_index

                print(f"{first_symbol}{second_symbol}{third_symbol}{fourth_symbol}{fifth_symbol}")


