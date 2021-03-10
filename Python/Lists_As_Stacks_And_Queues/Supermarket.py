from collections import deque


def supermarket_que(raw_input):
    que = deque()
    while raw_input != "End":
        if raw_input != "Paid":
            que.append(raw_input)
        else:
            while que:
                print(que.popleft())
        raw_input = input()
    print(len(que))
    return len(que)


print(supermarket_que(input()))
# print(f"{supermarket_que(input())} people remaining.")