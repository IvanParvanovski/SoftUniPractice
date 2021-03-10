from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name):
        Card.__init__(self, name, 5, 80)
