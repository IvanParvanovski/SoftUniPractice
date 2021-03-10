from collections import deque


def read_input():
    bullet_price = int(input())
    gun_barrel_size = int(input())
    bullets = deque(map(int, input().split()))
    locks = deque(map(int, input().split()))
    intelligence_value = int(input())
    return bullet_price, gun_barrel_size, bullets, locks, intelligence_value


def solve():
    bullet_price, gun_barrel_size, bullets, locks, intelligence_value = read_input()
    bullets_length = len(bullets)
    counter = 0
    while bullets:
        counter += 1
        if counter % (gun_barrel_size + 1) == 0:
            print("Reloading!")
            counter = 1
        bullet = bullets.pop()

        if locks:
            lock = locks.popleft()
        else:
            bullets.append(bullet)
            break

        if bullet > lock:
            print("Ping!")
            locks.appendleft(lock)
        else:
            print("Bang!")

    if not locks:
        ammo_expenses = (bullets_length - len(bullets)) * bullet_price
        return f"{len(bullets)} bullets left. Earned ${intelligence_value - ammo_expenses}"
    elif not bullets:
        return f"Couldn't get through. Locks left: {len(locks)}"


print(solve())
