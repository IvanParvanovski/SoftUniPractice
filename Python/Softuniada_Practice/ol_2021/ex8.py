from collections import deque


class Slope:
    def __init__(self, name):
        self.name = name
        self.stamina = 0
        self.obstacles = 0

    def __repr__(self):
        return f'Slope(' \
               f'{self.name}, {self.stamina}, {self.obstacles})'


player_stamina = int(input())
player_obstacles = 0
slopes = deque()

slopes_names = input().split()
for slope_name in slopes_names:
    slopes.append(Slope(slope_name))

slopes_stamina = tuple(map(int, input().split()))
slopes_obstacles = tuple(map(int, input().split()))

for i in range(len(slopes)):
    current_slope = slopes[i]
    current_slope.stamina = slopes_stamina[i]
    current_slope.obstacles = slopes_obstacles[i]

slopes = deque(sorted(slopes, key=lambda slope: (slope.obstacles, slope.stamina), reverse=True))
solved_slopes = list()
while True:
    slope = slopes.popleft()

    if not slopes:
        break

    if player_stamina - slope.stamina < 0:
        continue

    player_stamina -= slope.stamina
    player_obstacles += slope.obstacles
    solved_slopes.append(slope.name)

print(' '.join(sorted(solved_slopes)))
print(player_obstacles)
print(player_stamina)
