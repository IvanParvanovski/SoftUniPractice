from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            c = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            self.cards.append(card)
            self.count += 1

    # Be careful - here the param card is a string not the
    # card object
    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        c = [c for c in self.cards if c.name == card][0]
        self.cards.remove(c)
        self.count -= 1

    def find(self, name: str):
        c = [c for c in self.cards if c.name == name][0]
        return c


# from project.card.magic_card import MagicCard
#
# p = MagicCard("test")
#
# pr = CardRepository()
# pr.add(p)
# pr.remove("")
# print(pr.count)
#
# print(pr.find("test"))