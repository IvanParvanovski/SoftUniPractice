from ex7.cities.city import City


class StartCity(City):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def add_destination(self, destination, value):
        City.add_destination(self, destination, value)
        self.trucks += value

    def decrease_trucks(self, value: int) -> None:
        self.trucks -= value

    def increase_trucks(self, value: int) -> None:
        pass
