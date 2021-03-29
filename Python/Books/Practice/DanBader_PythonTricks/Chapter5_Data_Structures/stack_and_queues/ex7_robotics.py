from types import SimpleNamespace


class Robot:
    def __init__(self, name, rest_time):
        self.name = name
        self.execute_time = rest_time
        self.free = True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.execute_time!r})')


class ExecuteProduct:
    def __init__(self, robot_):
        self.robot = robot_
        self.counter = 0

    def __enter__(self):
        self.counter += 1
        return self.robot

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.counter == self.robot.execute_time:
            self.robot.free = True
        else:
            self.robot.free = False


def read_robots():
    robots_data = (
        tuple(robot.split('-'))
        for robot in input().split(';')
    )

    return tuple(
        Robot(name=robot_data[0],
              rest_time=int(robot_data[1]))
        for robot_data in robots_data
    )


def read_products():
    _products = list()
    while True:
        user_input = input()
        if user_input == 'End':
            break
        _product = user_input
        _products.append(_product)

    return _products


def convert_time(time):
    time_data = time.split(':')

    current_time = SimpleNamespace(
        hours=int(time_data[0]),
        minutes=int(time_data[1]),
        seconds=int(time_data[2]),
    )

    if current_time.seconds >= 60:
        current_time.minutes += current_time.seconds // 60
        current_time.seconds %= 60

    if current_time.minutes >= 60:
        current_time.hours += current_time.minutes // 60
        current_time.minutes %= 60

    if current_time.hours >= 24:
        current_time.hours %= 24

    return (f'{current_time.hours:02d}:' 
            f'{current_time.minutes:02d}:' 
            f'{current_time.seconds:02d}')


print(convert_time(input()))

# robots = read_robots()
# start_time = input()
# products = read_products()
#
# for product in products:
#     for robot in robots:
#         with ExecuteProduct(robot) as r:
#
#             if r.free:
#                 print(f'{r.name} - {product} [{start_time}]')
#


# print(robots)

# with ExecuteProduct() as r:
