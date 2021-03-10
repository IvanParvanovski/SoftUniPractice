from collections import defaultdict
cities = defaultdict(list)
user_input = input()

while user_input != "Sail":
    user_input = user_input.split("||")
    city = user_input[0]
    people = int(user_input[1])
    gold = int(user_input[2])
    if city not in cities:
        cities[city].append(people)
        cities[city].append(gold)
    else:
        cities[city][0] += people
        cities[city][1] += gold
    user_input = input()

second_user_input = input()
while second_user_input != "End":
    second_user_input = second_user_input.split("=>")
    command = second_user_input[0]
    town = second_user_input[1]

    if command == "Plunder":
        people = int(second_user_input[2])
        gold = int(second_user_input[3])

        if cities[town][1] - gold == 0:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

        elif cities[town][0] - people == 0:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

        elif cities[town][0] - people > 0 and cities[town][1] > 0:
            cities[town][1] -= gold
            cities[town][0] -= people
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    elif command == "Prosper":
        gold = int(second_user_input[2])

        if gold > -1:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    second_user_input = input()

cities = dict(sorted(cities.items(), key=lambda dict: (-int(dict[1][1]), dict[0])))

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


