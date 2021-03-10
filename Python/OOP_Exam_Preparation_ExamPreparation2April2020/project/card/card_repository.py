from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = list()

    @staticmethod
    def __is_name_valid(value):
        return True if value else False

    def __does_card_exist(self, card: Card):
        return card in self.cards

    def add(self, card: Card):
        if CardRepository.__does_card_exist(self, card):
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if not CardRepository.__is_name_valid(card):
            raise ValueError("Card cannot be an empty string!")

        cr = self.find(card)
        self.cards.remove(cr)
        self.count -= 1

    def find(self, name: str):
        return [card for card in self.cards if card.name == name][0]
