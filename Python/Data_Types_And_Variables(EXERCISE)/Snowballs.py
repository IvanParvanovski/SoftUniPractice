import sys
snowballs = int(input())
the_best_snowball_formula = -sys.maxsize
the_best_snowball_snow = 0
the_best_snowball_time = 0
the_best_snowball_quality = 0

for snowballs_counter in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    calculating_snowball_formula = int(snowball_snow / snowball_time) ^ snowball_quality
    if calculating_snowball_formula > the_best_snowball_formula:
        the_best_snowball_snow = snowball_snow
        the_best_snowball_time = snowball_time
        the_best_snowball_quality = snowball_quality
        the_best_snowball = calculating_snowball_formula
print(f"{the_best_snowball_snow} : {the_best_snowball_time} = {the_best_snowball_quality}")