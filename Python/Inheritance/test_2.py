class Parent:
    @staticmethod
    def get_parent():
        return "Parent"


class Child(Parent):
    @staticmethod
    def get_child():
        return "Child"


class GrandChild(Child):
    @staticmethod
    def get_grand_child():
        return "GrandChild"


print(Parent.get_parent())

print("-" * 15)

print(Child.get_parent())
print(Child.get_child())

print("-" * 15)

print(GrandChild.get_parent())
print(GrandChild.get_child())
print(GrandChild.get_grand_child())
