class ArrayManipulator:
    def __init__(self, text):
        self.numbers = [int(element) for element in text.split(' ')]

    @staticmethod
    def is_command_exchange(command):
        return command == 'exchange'

    @staticmethod
    def is_command_max(command):
        return command == 'max'

    @staticmethod
    def is_command_min(command):
        return command == 'min'

    @staticmethod
    def is_command_first(command):
        return command == 'first'

    @staticmethod
    def is_command_last(command):
        return command == 'last'

    @staticmethod
    def is_command_end(command):
        return command == 'end'

    def get_max_number(self, expression):
        max_num = 0
        max_num_index = 0
        has_number = False

        for i in range(len(self.numbers)):
            num = self.numbers[i]
            if eval(f'{expression}'):
                continue

            if num > max_num:
                max_num = num
                max_num_index = i
                has_number = True

        if has_number:
            return max_num_index
        else:
            return 'No matches'

    def get_min_number(self, expression):
        min_num = 0
        min_num_index = 0
        has_number = False

        for i in range(len(self.numbers)):
            num = self.numbers[i]
            if eval(f'{expression}'):
                continue

            if num < min_num:
                min_num = num
                min_num_index = i
                has_number = True

        if has_number:
            return min_num_index
        else:
            return 'No matches'

    def is_index_out_of_range(self):
        pass

    def operate(self):
        while True:
            user_input = input()

            if self.is_command_end(user_input):
                break

            command_parts = user_input.split()
            command = command_parts[0]

            if self.is_command_exchange(command):
                user_index = int(command_parts[1])
                if user_index > len(self.numbers):
                    print('Invalid index')
                    continue

                index = len(self.numbers) - user_index
                first_list = self.numbers[:index:]
                second_list = self.numbers[index::]
                self.numbers = second_list + first_list

            elif self.is_command_max(command):
                user_index = int(command_parts[1])
                if user_index > len(self.numbers):
                    print('Invalid index')
                    continue

                if second_action == 'odd':
                    print(self.get_max_number('num % 2 == 0'))

                elif second_action == 'even':
                    print(self.get_max_number('num % 2 != 0'))

            elif self.is_command_min(command):
                second_action = command_parts[1]

                if second_action == 'odd':
                    print(self.get_min_number('num % 2 == 0'))

                elif second_action == 'even':
                    print(self.get_min_number('num % 2 != 0'))

            elif self.is_command_first(command):
                pass

            elif self.is_command_last(command):
                pass


array_manipulator = ArrayManipulator(input())
array_manipulator.operate()
