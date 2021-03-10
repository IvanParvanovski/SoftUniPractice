from abc import ABC, abstractmethod


class Vehicle(ABC):
    CONSUMPTION_INCREASE = 0

    def __init__(self,
                 fuel_quantity,
                 fuel_consumption):

        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def _is_fuel_enough_to_travel(self, needed_fuel):
        return self.fuel_quantity >= needed_fuel

    def _calculate_needed_fuel_consumption(self, distance):
        return (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance


class Car(Vehicle):
    CONSUMPTION_INCREASE = 0.9

    def __init__(self,
                 fuel_quantity,
                 fuel_consumption):

        super().__init__(fuel_quantity, fuel_consumption)

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

        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = self._calculate_needed_fuel_consumption(distance)

        if not self._is_fuel_enough_to_travel(needed_fuel):
            return

        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += 95 / 100 * fuel
