from project.card.card import Card


class MagicCard(Card):
    def __init__(self,
                 name: str):

        damage_points = 5
        health_points = 80
        super().__init__(name, damage_points, health_points)
