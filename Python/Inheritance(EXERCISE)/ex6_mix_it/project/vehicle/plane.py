# from ex6_mix_it.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self,
                 available_seats: int,
                 rows: int,
                 seats_per_row: int):

        Vehicle.__init__(self, available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = dict()

    def __does_row_exist(self, row):
        return row in range(1, self.rows + 1)

    @staticmethod
    def __does_row_have_enough_seats(seats, tickets_count):
        expression = Vehicle.get_capacity(seats, tickets_count)
        return Vehicle.does_expression_return_number(expression)

    def buy_tickets(self, row_number, tickets_count):

        if not self.__does_row_exist(row_number):
            return f"There is no row {row_number} in the plane!"

        seats = self.seats_available[row_number] if row_number in self.seats_available else self.seats_per_row
        if not self.__does_row_have_enough_seats(seats, tickets_count):
            return f"Not enough tickets on row {row_number}!"

        self.seats_available[row_number] = self.seats_per_row - tickets_count
        self.available_seats -= tickets_count
        return tickets_count
