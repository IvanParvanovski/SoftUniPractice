class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self,
                 fuel: float,
                 horse_power: int):

        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def _does_vehicle_have_enough_fuel(self, needed_fuel):
        return needed_fuel <= self.fuel

    def drive(self, kilometers):
        needed_fuel = kilometers * self.fuel_consumption

        if self._does_vehicle_have_enough_fuel(needed_fuel):
            self.fuel -= needed_fuel
