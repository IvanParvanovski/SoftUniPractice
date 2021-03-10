gifts = input().split()
command = input()
out_of_stock = "OutOfStock"
required = "Required"
just_in_case = "JustInCase"

stock = ""

while command != "No Money":

    if out_of_stock in command:
        gifts_without_amount = command.split()
        gifts_without_amount.remove(out_of_stock)

        for index in range(len(gifts_without_amount)):
            element = gifts_without_amount[index]
            while element in gifts:
                gifts.remove(element)
            else:
                continue

    elif required in command:
        replaced_gift = command.split()
        replaced_gift.remove(required)

        element = replaced_gift[0]
        element_index = int(replaced_gift[1])

        if 0 < element_index < len(gifts):
            for index in range(len(gifts)):
                if element_index - 1 == index:
                    gifts[index], element = element, ""
                else:
                    continue

    elif just_in_case in command:
        new_gift = command.split()
        new_gift.remove(just_in_case)
        element = ""

        for index in range(len(new_gift)):
            element = new_gift[index]

        for index in range(len(gifts)):
            if index == len(gifts) - 1:
                gifts[index], element = element, ""
            else:
                continue

    command = input()

for index in range(len(gifts)):
    print(gifts[index], end=" ")