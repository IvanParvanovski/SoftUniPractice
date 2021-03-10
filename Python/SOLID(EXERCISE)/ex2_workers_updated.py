from abc import ABCMeta, abstractmethod, ABC
import time

# S.O.L.I.D
# Single responsibility
# Open for extensions / Closed for modifications
# Liskov substitution
# Interface segregation
# Dependency inversion


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable,
             Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable,
                  Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


class Manager(ABC):
    @abstractmethod
    def __init__(self):
        self.worker = None

    @staticmethod
    def __is_new_worker_abstract_worker(new_employee):
        expression = [cls.__name__ for cls in new_employee.__class__.__mro__]
        return 'Workable' in expression

    def set_worker(self, worker):
        if Manager.__is_new_worker_abstract_worker(worker):
            self.worker = worker
        else:
            raise Exception("`worker` must be of type {}")


class WorkManager(Manager):
    def __init__(self):
        super().__init__()

    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def __init__(self):
        super().__init__()

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

print('*' * 20)
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

print('*' * 20)
work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
