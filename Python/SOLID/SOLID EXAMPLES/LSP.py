from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def senzors_count(self):
        pass


class Android(Robot):
    def senzors_count(self):
        return 4


class Chappie(Robot):
    def senzors_count(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.senzors_count())


# със всички видове наследници трябва да работи кода
# използва се polymorphism + абстракция

r1 = Robot('type')
r2 = Android('type')
r3 = Chappie('type')

robots = [r1, r2, r3]
count_robot_senzors(robots)
