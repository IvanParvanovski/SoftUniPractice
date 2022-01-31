class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return f'Pizza with {" and ".join(self.toppings)}'

    @classmethod
    def recommend(cls):
        """Recommend some pizza with arbitrary toppings, """
        return cls(['spam', 'ham', 'eggs'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """Use same recommendation as super but add extra spam"""
        recommended = super(VikingPizza).recommend()
        recommended.toppings += ['spam'] * 5
        return recommended
