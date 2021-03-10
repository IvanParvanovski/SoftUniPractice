_MangledGlobal__mangled = 23


class MangledGlobal:
    def test(self):
        return __mangled


print(MangledGlobal().test())
