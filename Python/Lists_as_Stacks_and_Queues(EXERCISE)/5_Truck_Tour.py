from collections import deque


def tour(pumps):
    pumps_que = deque()

    # Append every pump into the que
    for _ in range(pumps):
        pump = list(map(int, input().split()))
        pumps_que.append(pump)

    for i in range(pumps):
        fuel = 0
        is_valid = True

        for _ in range(pumps):
            current = pumps_que.popleft()
            fuel += current[0] - current[1]

            if fuel < 0:
                is_valid = False
            pumps_que.append(current)

        if is_valid:
            print(i)
            break

        pumps_que.append(pumps_que.popleft())


tour(int(input()))