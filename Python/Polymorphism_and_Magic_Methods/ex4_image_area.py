class ImageArea:
    def __init__(self,
                 width,
                 height):

        self.width = width
        self.height = height

    def __expression(self, other, operator):
        return eval(f"{self.get_area()} {operator} {other.get_area()}")

    def get_area(self):
        return self.width * self.height

    # def __lt__(self, other):
    #     return self.__expression(other, "<")
    #
    # def __gt__(self, other):
    #     return self.__expression(other, ">")
    #
    # def __le__(self, other):
    #     return self.__expression(other, "<=")
    #
    # def __ge__(self, other):
    #     return self.__expression(other, ">=")
    #
    # def __ne__(self, other):
    #     return self.__expression(other, "!=")
    #
    # def __eq__(self, other):
    #     return self.__expression(other, "==")

    def __ge__(self, other):
        return self.__expression(other, ">=")

    def __gt__(self, other):
        return self.__expression(other, ">")

    def __eq__(self, other):
        return self.__expression(other, "==")


im_1 = ImageArea(10, 10) # 100
im_2 = ImageArea(20, 10) # 200

print(im_1 < im_2) # True
print(im_1 > im_2) # False

print('-' * 15)

print(im_1 <= im_2) # True
print(im_1 >= im_2) # False

print('-' * 15)

print(im_1 != im_2) # True
print(im_1 == im_2) # False
