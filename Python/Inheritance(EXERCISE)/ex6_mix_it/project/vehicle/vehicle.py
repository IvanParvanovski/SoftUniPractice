# from ex6_mix_it.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class Vehicle(CapacityMixin):
    def __init__(self, available_seats: int):
        self.available_seats = available_seats
