from collections import defaultdict
guests = defaultdict(list)

user_input = input()
disliked_meals = 0

while user_input != "Stop":
    user_input = user_input.split("-")
    like_or_dislike = user_input[0]
    guest = user_input[1]
    meal = user_input[2]

    if like_or_dislike == "Like":
        if meal not in guests[guest]:
            guests[guest].append(meal)

    elif like_or_dislike == "Unlike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        elif meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            disliked_meals += 1
            guests[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")

    user_input = input()

sorted_dict = dict(sorted(guests.items(), key=lambda dict: (-len(dict[1]), dict[0])))
for person in sorted_dict:
    print(f"{person}: {', '.join(sorted_dict[person])}")
print(f"Unliked meals: {disliked_meals}")