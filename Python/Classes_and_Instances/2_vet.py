def does_clinic_have_free_space():
    return Vet.space > 0


class Vet:
    animals = list()
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = list()

    def does_animal_exist(self, animal_name):
        return animal_name in self.animals

    def register_animal(self, animal_name):
        if not does_clinic_have_free_space():
            return "Not enough space"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        Vet.space -= 1
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if not self.does_animal_exist(animal_name):
            return f"{animal_name} not in the clinic"

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        Vet.space += 1
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
