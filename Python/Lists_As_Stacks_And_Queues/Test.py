from collections import deque


def supermarket_que(raw_input):
    people_que = deque()

    while raw_input != "End":
        if raw_input != "Paid":
            people_que.append(raw_input)
        else:
            while people_que:
                print(people_que.popleft())
        raw_input = input()

    return len(people_que)


print(f"{supermarket_que(input())} people remaining.")