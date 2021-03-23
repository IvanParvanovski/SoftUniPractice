# Fields: color, mileage, automatic
car1 = ('red', 3812.4, False)
car2 = ('blue', 40231.0, True)

# Tuple instances have a nice repr:
print(car1)
print(car2)

# Get mileage
print(car1[1])

# Tuples are immutable
car1[1] = 'green'
