class CapacityMixin:
    @staticmethod
    def __is_capacity_reached(capacity, value):
        return value > capacity

    @staticmethod
    def does_expression_return_number(expression_to_check):
        return isinstance(expression_to_check, int)

    @staticmethod
    def get_capacity(capacity, amount):

        if CapacityMixin.__is_capacity_reached(capacity, amount):
            return "Capacity reached!"

        return capacity - amount
