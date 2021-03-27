from types import SimpleNamespace

car1 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)

print(car1)

# Can access attributes with dot

print(car1.color)
car1.color = 'blue'
print(car1.color)
