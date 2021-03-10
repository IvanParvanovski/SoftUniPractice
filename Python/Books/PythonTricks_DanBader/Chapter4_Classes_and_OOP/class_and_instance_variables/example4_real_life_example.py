class CountedObjects:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

    def __repr__(self):
        return f'{CountedObjects.num_instances}'


CountedObjects()
print(CountedObjects())

CountedObjects()
print(CountedObjects())

CountedObjects()
print(CountedObjects())

CountedObjects()
print(CountedObjects())

CountedObjects()
print(CountedObjects())
