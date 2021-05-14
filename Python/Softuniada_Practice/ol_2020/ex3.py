def shuffle_deck(deck, shuffle_index):
    first_part = deck[:shuffle_index:]
    second_part = deck[shuffle_index::]
    
    result = list()

    bigger_list = len(first_part) if len(first_part) > len(second_part) else len(second_part)
    for i in range(bigger_list):
        try:
            result.append(first_part.pop(0))
        except IndexError:
            pass

        try:
            result.append(second_part.pop(0))
        except IndexError:
            pass

    return result


cards_in_deck = [card_number for card_number in range(1, int(input()) + 1)]
card_shuffle_numbers = [int(x) for x in input().split()]

for shuffle_num in card_shuffle_numbers:
    cards_in_deck = shuffle_deck(cards_in_deck, shuffle_num)

print(' '.join(map(str,cards_in_deck)))
