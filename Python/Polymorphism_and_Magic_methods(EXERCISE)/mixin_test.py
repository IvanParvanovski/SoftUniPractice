class MyMixin:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class MyClass(MyMixin):
    def __init__(self, name):
        super().__init__(name)


my_object = MyClass('Default')
username = my_object.get_name()

print(username)