from collections import deque


def food_restaurant_orders(food_quantity, people_que):
    que = deque(map(int, people_que))
    print(max(que))

    while que:
        element = que.popleft()
        if food_quantity - element < 0:
            que.appendleft(element)
            break
        food_quantity -= element

    if len(que) == 0:
        return "Orders complete"
    else:
        return f"Orders left: {' '.join(map(str, que))}"


print(food_restaurant_orders(int(input()), input().split()))