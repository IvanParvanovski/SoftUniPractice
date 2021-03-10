from project.card.card import Card


class TrapCard(Card):
    def __init__(self,
                 name: str):

        damage_points = 120
        health_points = 5
        super().__init__(name, damage_points, health_points)
