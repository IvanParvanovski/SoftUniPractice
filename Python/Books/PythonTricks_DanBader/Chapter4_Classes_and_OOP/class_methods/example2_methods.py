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


print(MyClass.class_method())
print(MyClass.static_method())
print(MyClass.method())