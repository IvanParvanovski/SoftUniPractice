class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


print(MangledMethod().call_it())
print(dir(MangledMethod()))
print(MangledMethod().__method())
