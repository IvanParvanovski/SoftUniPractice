def read_people_details():
    people_dict = dict()
    while True:
        raw_input = input()

        if raw_input.isdigit():
            count = int(raw_input)
            break

        person_and_number = raw_input.split('-')
        person = person_and_number[0]
        number = person_and_number[1]
        people_dict[person] = number

    return people_dict, count


def read_phone_calls_and_print(people_dict, count):
    for _ in range(count):
        called_person = input()

        if called_person in people_dict:
            output = f"{called_person} -> {people_dict[called_person]}"
        else:
            output = f"Contact {called_person} does not exist."
        print(output)


def solve():
    people_dict, count = read_people_details()
    read_phone_calls_and_print(people_dict, count)


solve()
