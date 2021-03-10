from collections import deque


def solve(people, tosses_count):
    people = deque(people)
    index = 0

    while people:
        index += 1
        person = people.popleft()

        if index == tosses_count:
            index = 0
            if len(people) >= 1:
                print(f"Removed {person}")
            else:
                print(f"Last is {person}")
        else:
            people.append(person)


names = input().split()
step = int(input())
solve(names, step)