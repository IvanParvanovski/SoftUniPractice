class Person:
    def __init__(self):
        pass


class Worker:
    pass


class SuperWorker:
    def __init__(self, super_power):
        self.super_power = super_power


class Manager:
    def __init__(self, employee):
        self.employee = employee


# Manager е независим
w = Worker()
s_w = SuperWorker("magic")

m1 = Manager(w)
m2 = Manager(s_w)
