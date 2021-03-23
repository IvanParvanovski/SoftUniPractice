from types import SimpleNamespace

car1 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)

# The default repr:
print(car1)

# Instances support attribute access and are mutable:
car1.mileage = 12
car1.windshield = 'broken'
del car1.automatic
print(car1)
