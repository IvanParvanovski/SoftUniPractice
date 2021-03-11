class MyClass:
    # regular instance
    def method(self):
        return 'instance method called', self

    # class method
    @classmethod
    def class_method(cls):
        return 'class method called', cls

    # static method
    @staticmethod
    def static_method():
        return 'static method called'


obj = MyClass()
print(obj.method())
print(MyClass.method(obj))

print()

print(obj.class_method())
print(obj.static_method())
