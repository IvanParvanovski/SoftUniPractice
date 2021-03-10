class Survivor:
    def __init__(self,
                 name: str,
                 age: int):

        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100

    # ----- Custom + Others

    @staticmethod
    def __invalid_data_error(value, data):
        checks = {'name': Survivor.__is_new_name_value_valid,
                  'age': Survivor.__is_new_age_value_valid,
                  'health': Survivor.__is_new_health_value_valid,
                  'needs': Survivor.__is_new_needs_value_valid}

        if not checks[data](value):
            raise ValueError(f'{data.capitalize()} not valid!')

    # ----- Name Validation

    @staticmethod
    def __is_new_name_value_valid(value):
        return True if value else False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Survivor.__invalid_data_error(value, 'name')

        self._name = value

    # ----- Age Validation

    @staticmethod
    def __is_new_age_value_valid(value):
        return value >= 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        Survivor.__invalid_data_error(value, 'age')

        self._age = value

    # ----- Health Validation

    @staticmethod
    def __is_new_health_value_valid(value):
        return 0 <= value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        Survivor.__invalid_data_error(value, 'health')

        self._health = value
        if self._health > 100:
            self._health = 100

    # ----- Needs Validation

    @staticmethod
    def __is_new_needs_value_valid(value):
        return 0 <= value

    @property
    def needs(self):
        return self._needs

    @needs.setter
    def needs(self, value):
        Survivor.__invalid_data_error(value, 'needs')

        self._needs = value
        if self._needs > 100:
            self._needs = 100

    @property
    def needs_sustenance(self):
        return True if self.needs < 100 else False

    @property
    def needs_healing(self):
        return True if self.health < 100 else False
