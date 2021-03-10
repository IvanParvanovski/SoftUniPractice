spell_book = dict()
user_input = input()

while user_input != "End":
    user_input = user_input.split()
    command = user_input[0]
    hero_name = user_input[1]

    if command == "Enroll":
        if hero_name not in spell_book:
            spell_book[hero_name] = list()
        else:
            print(f"{hero_name} is already enrolled.")

    elif command == "Learn":
        if hero_name not in spell_book:
            print(f"{hero_name} doesn't exist.")
        else:
            spell = user_input[2]
            if spell not in spell_book[hero_name]:
                spell_book[hero_name].append(spell)
            else:
                print(f"{hero_name} has already learnt {spell}.")

    elif command == "Unlearn":
        if hero_name not in spell_book:
            print(f"{hero_name} doesn't exist.")
        else:
            spell = user_input[2]
            if spell in spell_book[hero_name]:
                spell_book[hero_name].remove(spell)
            else:
                print(f"{hero_name} doesn't know {spell}.")

    user_input = input()

sorted_spell_book = dict(sorted(spell_book.items(), key=lambda dict: (-len(dict[1]), dict[0])))

print("Heroes: ")
for hero in sorted_spell_book:
    output = f"== {hero}: {', '.join(sorted_spell_book[hero])}"
    print(output)
