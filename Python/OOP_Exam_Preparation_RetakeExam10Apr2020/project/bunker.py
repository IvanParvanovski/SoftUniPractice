class Bunker:
    def __init__(self):
        self.survivors = list()
        self.supplies = list()
        self.medicine = list()

    def __does_survivor_already_exist(self, survivor):
        return survivor in self.survivors

    @staticmethod
    def __search_item(collection, searched_type, error_message):
        searched_item = [item
                         for item in collection
                         if type(item).__name__ == searched_type]

        if not searched_item:
            raise IndexError(f'There are no {error_message} left!')

        return searched_item

    @property
    def food(self):
        return Bunker.__search_item(collection=self.supplies,
                                    searched_type='FoodSupply',
                                    error_message='food supplies')

    @property
    def water(self):
        return Bunker.__search_item(collection=self.supplies,
                                    searched_type='WaterSupply',
                                    error_message='water supplies')

    @property
    def painkillers(self):
        return Bunker.__search_item(collection=self.medicine,
                                    searched_type='Painkiller',
                                    error_message='painkillers')

    @property
    def salves(self):
        return Bunker.__search_item(collection=self.medicine,
                                    searched_type='Salve',
                                    error_message='salves')

    def call_food(self):
        return self.food

    def call_water(self):
        return self.water

    def call_painkiller(self):
        return self.painkillers

    def call_salves(self):
        return self.salves

    def add_survivor(self, survivor):
        if Bunker.__does_survivor_already_exist(self, survivor):
            raise ValueError(f'Survivor with name {survivor.name} already exists.')

        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if not survivor.needs_healing:
            return

        pills = {'Painkiller': self.call_painkiller,
                 'painkiller': self.call_painkiller,
                 'Salves': self.call_salves,
                 'salves': self.call_salves}

        pill = pills[medicine_type]()[-1]
        pill_index = self.medicine.index(pill)

        self.medicine.pop(pill_index).apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if not survivor.needs_sustenance:
            return

        supplies = {'FoodSupply': self.call_food,
                    'foodsupply': self.call_food,
                    'WaterSupply': self.call_water,
                    'watersupply': self.call_water}

        supply = supplies[sustenance_type]()[-1]
        supply_index = self.supplies.index(supply)

        self.supplies.pop(supply_index).apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
