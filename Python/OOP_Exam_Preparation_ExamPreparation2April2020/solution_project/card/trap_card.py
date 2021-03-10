from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name):
        Card.__init__(self, name, 120, 5)