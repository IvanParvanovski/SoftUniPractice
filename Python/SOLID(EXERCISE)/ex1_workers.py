from abc import ABC, abstractmethod

# S.O.L.I.D
# Single responsibility
# Open for extensions / Closed for modifications
# Liskov substitution
# Interface segregation
# Dependency inversion


class Employee(ABC):
    @abstractmethod
    def work(self):
        pass


class SuperWorker(Employee):
    def work(self):
        print("I work very hard!!!")


class Worker(Employee):
    def work(self):
        print("I'm working!!")


class Manager:
    def __init__(self):
        self.worker = None

    @staticmethod
    def __is_new_worker_employee(employee):
        # return employee.__class__.__bases__[0].__name__ == "Employee"
        # return employee.__class__.__mro__[1].__name__ == "Employee"
        return "Employee" in [cls.__name__ for cls in employee.__class__.__mro__]

    def set_worker(self, employee):
        if Manager.__is_new_worker_employee(employee):
            self.worker = employee
        else:
            raise AssertionError('`worker` must be of type Employee')

    def manage(self):
        if self.worker:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
