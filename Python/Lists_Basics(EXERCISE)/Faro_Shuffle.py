card_deck_elements = input().split()
times_cards_swap = int(input())

border = len(card_deck_elements) / 2

for counter in range(times_cards_swap):
    first_part = list()
    second_part = list()
    new_list = list()

    for index in range(len(card_deck_elements)):

        if index < border:
            first_part.append(card_deck_elements[index])
        else:
            second_part.append(card_deck_elements[index])

    for index in range(len(second_part)):
        new_list.append(first_part[index])
        new_list.append(second_part[index])
    card_deck_elements = new_list

print(card_deck_elements)