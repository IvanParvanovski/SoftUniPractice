class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = list()
        self.fishes = list()
        self.birds = list()

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, specie):
        key_word = ""
        output_list = list()
        if specie == "mammal":
            key_word = "Mammals"
            output_list = self.mammals
        elif specie == "fish":
            key_word = "Fishes"
            output_list = self.fishes
        elif specie == "bird":
            key_word = "Birds"
            output_list = self.birds

        output = f"{key_word} in {zoo_name}: {', '.join(output_list)}\n"
        output += f"Total animals: {len(self.mammals) + len(self.fishes) + len(self.birds)}"
        return output


zoo_name = input()
animals_count = int(input())
zoo = Zoo(zoo_name)

for counter in range(animals_count):
    command = input().split()
    species = command[0]
    animal = command[1]
    zoo.add_animal(species, animal)


showed_species = input()
print(zoo.get_info(showed_species))
