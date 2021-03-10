# class food():
#     # init method or constructor
#     def __init__(self, fruit, color):
#         self.fruit = fruit
#         self.color = color
#
#     def show(self):
#         print("fruit is", self.fruit)
#         print("color is", self.color)
#
#
# apple = food("apple", "red")
# grapes = food("grapes", "green")
#
# apple.show()
# grapes.show()


class Math_Operations:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def sum_values(self):
        return self.first_num + self.second_num

    def multiply_values(self):
        return self.first_num * self.second_num

    def divide_values(self):
        return self.first_num / self.second_num


def sum_values(num1, num2):
    return num1 + num2


def multiply_values(num1, num2):
    return num1 * num2


def divide_values(num1, num2):
    return num1 / num2


Gosho = Math_Operations(5, 4)
print(Gosho.sum_values())
print(Gosho.multiply_values())
print(Gosho.divide_values())

print()
print('-' * 30)
print()

n = (5, 4)
print(sum_values(*n))
print(multiply_values(*n))
print(divide_values(*n))

