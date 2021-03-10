class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_hero_dead(self, damage):
        return self.health - damage <= 0

    def defend(self, damage):
        if self.is_hero_dead(damage):
            self.health = 0
            return f"{self.name} was defeated"

        self.health -= damage

    def heal(self, amount: int):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
print(hero.heal(50))
print(hero.defend(99))
print(hero.defend(1))
