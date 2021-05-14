from ex7.cities.city import City


class PrimaryCity(City):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def increase_trucks(self, value: int) -> None:
        self.trucks += value

    def decrease_trucks(self, value: int) -> None:
        self.trucks -= value
