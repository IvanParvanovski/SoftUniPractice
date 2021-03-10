# from ex6_mix_it.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,
                 available_seats: int,
                 fuel_tank: int,
                 fuel_consumption: float,
                 fuel: float):

        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, new_value):
        if self.__does_fuel_exceed_the_fuel_tank(new_value):
            self.__fuel = self.fuel_tank
        else:
            self.__fuel = new_value

    def __does_car_have_enough_fuel_to_travel(self, needed_fuel):
        return self.fuel >= needed_fuel

    def __does_fuel_exceed_the_fuel_tank(self, value):
        return value > self.fuel_tank

    def __does_car_have_free_space_for_fuel(self, liters):
        expression = Vehicle.get_capacity(self.fuel_tank, self.fuel + liters)
        return expression, Vehicle.does_expression_return_number(expression)

    def drive(self, distance):
        needed_fuel = distance * self.fuel_consumption

        if not self.__does_car_have_enough_fuel_to_travel(needed_fuel):
            return

        self.fuel -= needed_fuel
        return "We've enjoyed the travel!"

    def refuel(self, liters):
        result, check = self.__does_car_have_free_space_for_fuel(liters)

        if check:
            self.fuel += liters

        return self.fuel
