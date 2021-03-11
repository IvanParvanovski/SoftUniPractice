class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margarita(cls):
        return cls([
            'mozzarella',
            'tomatoes',
        ])

    @classmethod
    def prosciutto(cls):
        return cls([
            'mozzarella',
            'tomatoes',
            'ham',
        ])

    def __repr__(self):
        return f'Pizza({self.ingredients})'


print(Pizza.margarita())
print(Pizza.prosciutto())
