car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
}

car2 = {
    'color': 'red',
    'mileage': 40231,
    'automatic': False,
}

# Dicts have a nice repr:
print(car2)

# Get mileage:
print(car2['mileage'])

# Dict are mutable
car2['mileage'] = 12
car2['windshield'] = 'broken'
print(car2)
