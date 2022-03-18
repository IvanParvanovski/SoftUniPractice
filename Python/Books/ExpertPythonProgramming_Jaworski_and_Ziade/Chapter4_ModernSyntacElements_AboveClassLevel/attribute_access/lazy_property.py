class lazy_property:
    def __init__(self, function):
        self.fget = function

    def __get__(self, instance, owner):
        value = self.fget(instance)
        setattr(instance, self.fget.__name__, value)
        return value

