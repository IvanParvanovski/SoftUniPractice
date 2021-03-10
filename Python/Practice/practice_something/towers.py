def calculate_tower_range(tower_x, tower_y, tower_radius):
      return  (
                tower_x + tower_radius,
                tower_x - tower_radius,
                tower_y + tower_radius,
                tower_y - tower_radius
              )


towers_count_and_shore_width = list(map(int, input().split()))
towers_count = towers_count_and_shore_width[0]
shore_width = towers_count_and_shore_width[1]

towers_limits = list()
killed_soldiers = 0

for i in range(towers_count):
    tower_data = list(map(int, input().split()))
    tower_x = tower_data[0]
    tower_y = tower_data[1]
    soldiers = tower_data[2]
    tower_radius = soldiers * soldiers

    towers_limits.append(
        (tower_x, tower_y, soldiers, *calculate_tower_range(tower_x, tower_y, tower_radius))
    )

for tower in towers_limits:
    tower_max_x = tower[3]
    tower_min_x = tower[4]

    tower_max_y = tower[5]
    tower_min_y = tower[6]

    if shore_width - (tower_max_x - tower_min_x) <= 0 or \
       shore_width - (tower_max_y - tower_min_y) <= 0:

        towers_limits.append(
            (tower[0],
             tower[1],
             tower[2] - 1,
             *calculate_tower_range(tower[0], tower[1], tower[2] - 1 * tower[2] - 1))
        )
        killed_soldiers += 1

print(killed_soldiers)
