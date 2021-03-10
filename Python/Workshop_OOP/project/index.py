class Index:
    @staticmethod
    def _is_index_even(index):
        return index % 2 == 0

    # Checks + Errors / Specific Pattern Name = ?

    @staticmethod
    def _is_index_out_of_range(current_list, index):
        return index > len(current_list)

    @staticmethod
    def out_of_range_error(current_list, index):
        if Index._is_index_out_of_range(current_list, index):
            raise IndexError("The index is greater than the length of the list!")

    @staticmethod
    def _is_int(index):
        return isinstance(index, int)

    @staticmethod
    def index_not_integer_error(index):
        if not Index._is_int(index):
            raise TypeError(f"The index is not 'int' it was '{type(index).__name__}'")

    @staticmethod
    def _does_list_contain_any_elements(current_list):
        return current_list

    @staticmethod
    def empty_list_error(current_list):
        if not Index._does_list_contain_any_elements(current_list):
            raise IndexError("The list doesn't contain any elements!")

    # Facade

    @staticmethod
    def index_checks(current_list, index):
        Index.index_not_integer_error(index)
        Index.empty_list_error(current_list)
        Index.out_of_range_error(current_list, index)
