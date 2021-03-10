# from ex6_mix_it.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self,
                 available_seats: int,
                 ticket_price: float):

        Vehicle.__init__(self, available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def __does_bus_have_enough_seats(self, tickets_count):
        expression = Vehicle.get_capacity(self.available_seats, self.tickets_sold + tickets_count)
        return expression, Vehicle.does_expression_return_number(expression)

    def get_ticket(self, tickets_count):
        result, check = self.__does_bus_have_enough_seats(tickets_count)

        if not check:
            return result

        self.tickets_sold += tickets_count

    def get_total_profit(self):
        return self.ticket_price * self.tickets_sold
