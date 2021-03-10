from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION_INCREASE = 0.9

    def __init__(self,
                 fuel_quantity,
                 fuel_consumption):

        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def _is_fuel_enough_to_travel(self, needed_fuel):
        return self.fuel_quantity >= needed_fuel

    def _calculate_needed_fuel_consumption(self, distance):
        air_consumption = self.fuel_consumption + self.CONSUMPTION_INCREASE
        result = 0
        for _ in range(distance):
            result += air_consumption

        return result

    def drive(self, distance):
        needed_fuel = self._calculate_needed_fuel_consumption(distance)

        if not self._is_fuel_enough_to_travel(needed_fuel):
            return

        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_INCREASE = 1.6

    def __init__(self,
                 fuel_quantity,
                 fuel_consumption):

        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def _is_fuel_enough_to_travel(self, needed_fuel):
        return self.fuel_quantity >= needed_fuel

    def _calculate_needed_fuel_consumption(self, distance):
        air_consumption = self.fuel_consumption + self.CONSUMPTION_INCREASE
        result = 0
        for _ in range(distance):
            result += air_consumption

        return result

    def drive(self, distance):
        needed_fuel = self._calculate_needed_fuel_consumption(distance)

        if not self._is_fuel_enough_to_travel(needed_fuel):
            return

        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += (95 / 100) * fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
