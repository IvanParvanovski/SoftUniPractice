class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = list()

    def does_pokemon_exist(self, pokemon):
        return pokemon in self.pokemon

    def add_pokemon(self, pokemon):
        if self.does_pokemon_exist(pokemon):
            return "This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemons_to_release = [pokemon for pokemon in self.pokemon if pokemon.name == pokemon_name]
        if not pokemons_to_release:
            return "Pokemon is not caught"

        pokemon = pokemons_to_release[0]
        if not self.does_pokemon_exist(pokemon):
            return "Pokemon is not caught"

        self.pokemon.remove(pokemon)
        return f"You have released {pokemon.name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemon)}\n"

        for pokemon in self.pokemon:
            result += f"- {pokemon.pokemon_details()}\n"

        return result
