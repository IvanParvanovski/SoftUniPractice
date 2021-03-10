# from ex6_mix_it.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots: int):
        self.parking_lots = parking_lots

    def __does_mall_has_space(self):
        expression = CapacityMixin.get_capacity(self.parking_lots, 1)
        self.parking_lots -= 1
        return CapacityMixin.does_expression_return_number(expression)

    def check_availability(self):
        if not self.__does_mall_has_space():
            return "There are no more parking lots!"

        return f"Parking lots available: {self.parking_lots}"
