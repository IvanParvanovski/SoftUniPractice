class Zoo:
    def __init__(self,
                 name,
                 budget,
                 animal_capacity,
                 workers_capacity):

        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget

        self.name = name
        self.animals = list()
        self.workers = list()

    @staticmethod
    def __does_worker_exist(worker):
        return worker

    @staticmethod
    def __certify_object(object_to_certify, object_type):
        return type(object_to_certify).__name__ == object_type

    def __does_zoo_have_free_space_for_new_worker(self):
        return self.__workers_capacity > len(self.workers)

    def __get_worker(self, worker_name):
        return [worker for worker in self.workers if worker.name == worker_name]

    def __does_zoo_have_free_space_for_new_animal(self):
        return self.__animal_capacity > len(self.animals)

    def __is_budget_enough_to_take_care_of_new_animal(self, price):
        return self.__budget - price > 0

    def __is_budget_enough_to_cover_costs(self, expenses):
        return self.__budget >= expenses

    def __separate_animals(self):
        lions = list()
        tigers = list()
        cheetahs = list()

        for animal in self.animals:
            if Zoo.__certify_object(animal, "Lion"):
                lions.append(animal)

            elif Zoo.__certify_object(animal, "Tiger"):
                tigers.append(animal)

            elif Zoo.__certify_object(animal, "Cheetah"):
                cheetahs.append(animal)

        return lions, tigers, cheetahs

    def __separate_workers(self):
        keepers = list()
        caretakers = list()
        vets = list()

        for worker in self.workers:
            if Zoo.__certify_object(worker, "Keeper"):
                keepers.append(worker)

            elif Zoo.__certify_object(worker, "Caretaker"):
                caretakers.append(worker)

            elif Zoo.__certify_object(worker, "Vet"):
                vets.append(worker)

        return keepers, caretakers, vets

    def add_animal(self, animal, price):
        if not self.__is_budget_enough_to_take_care_of_new_animal(price):
            return "Not enough budget"

        if not self.__does_zoo_have_free_space_for_new_animal():
            return "Not enough space for animal"

        self.__budget -= price

        self.animals.append(animal)
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.__does_zoo_have_free_space_for_new_worker():
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, name):
        worker_list = self.__get_worker(name)

        if not Zoo.__does_worker_exist(worker_list):
            return f"There is no {name} in the zoo"

        self.workers.remove(worker_list[0])
        return f"{name} fired successfully"

    def pay_workers(self):
        expenses = sum([worker.salary for worker in self.workers])

        if not self.__is_budget_enough_to_cover_costs(expenses):
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= expenses
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        expenses = sum([animal.get_needs() for animal in self.animals])

        if not self.__is_budget_enough_to_cover_costs(expenses):
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions, tigers, cheetahs = self.__separate_animals()
        starting_separator = '-' * 5

        result += f"\n{starting_separator} {len(lions)} Lions:"
        for lion in lions:
            result += f"\n{lion}"

        result += f"\n{starting_separator} {len(tigers)} Tigers:"
        for tiger in tigers:
            result += f"\n{tiger}"

        result += f"\n{starting_separator} {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            result += f"\n{cheetah}"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        keepers, caretakers, vets = self.__separate_workers()
        starting_separator = '-' * 5

        result += f"\n{starting_separator} {len(keepers)} Keepers:"
        for keeper in keepers:
            result += f"\n{keeper}"

        result += f"\n{starting_separator} {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            result += f"\n{caretaker}"

        result += f"\n{starting_separator} {len(vets)} Vets:"
        for vet in vets:
            result += f"\n{vet}"

        return result
