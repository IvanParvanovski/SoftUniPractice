free_space_width = int(input())
free_space_lenght = int(input())
free_space_height = int(input())

free_space_volume = free_space_width * free_space_lenght * free_space_height
one_cube_volume = 1
total_cube_volume = 0

cubes_number = input()

while cubes_number != "Done":

    integerCubes = int(cubes_number)
    total_cube_volume += one_cube_volume * integerCubes

    if total_cube_volume > free_space_volume:
        break

    cubes_number = input()

if total_cube_volume > free_space_volume:
    deff = total_cube_volume - free_space_volume
    print(f"No more free space! You need {deff} Cubic meters more.")

elif cubes_number == "Done":
    deff = free_space_volume - total_cube_volume
    print(f"{deff} Cubic meters left.")


