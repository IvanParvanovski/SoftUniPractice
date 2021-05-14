from collections import deque
from copy import copy

from ex7.cities.city import City
from ex7.cities.end_city import EndCity
from ex7.cities.primary_city import PrimaryCity
from ex7.cities.start_city import StartCity


def get_urban(searched_name: str, towns) -> City:
    """
    Iterates threw the collection and compares the name of
    the searched city and the current one.

    - If the searched name matches, the function returns the town
    - If it doesn't find it, the function returns None.

    :param searched_name: str
    :param towns: list, deque, array ...
    :return:
    """
    for town in towns:
        if searched_name == town.name:
            return town


def generate_cities(_home_city_name,
                    _client_city_name,
                    _roadways_count):
    """
    Reads the input from the console and initialize cities

    - StartCity is initialized. (If current city name is equal to home city name)
    - PrimaryCity is initialized (If current city name is not equal to home city name)

    When a city is initialized, the city is being appended to the list and
    the end point is being added to the city collection of destinations.

    When a city already exists, the new end point is being added to the
    city collection.

    :param _home_city_name: str
    :param _client_city_name: str
    :param _roadways_count: int
    :return: list -> StartCity and PrimaryCity objects
    """

    _cities = list()

    for _ in range(_roadways_count):
        data = input().split()

        start_city_name = data[0]
        end_city = data[1]
        road_max = int(data[2])

        city = get_urban(start_city_name, _cities)

        if not city:
            if start_city_name == _home_city_name:
                city = StartCity(home_city_name)
            else:
                city = PrimaryCity(start_city_name)

            _cities.append(city)

        city.add_destination(end_city, road_max)

    _cities.sort(key=lambda x: x.__class__.__name__ == 'StartCity',
                 reverse=True)

    client_city = EndCity(_client_city_name)
    client_city.export = get_urban(_home_city_name, _cities).export

    _cities.append(client_city)

    return _cities


def does_another_city_has_a_course(city_name, cities):
    for city in cities:
        if city_name in city.destinations:
            return True
    return False


home_city_name = input()
client_city_name = input()
roadways_count = int(input())

cities = deque(generate_cities(home_city_name,
                               client_city_name,
                               roadways_count))


while len(cities) != 1:
    start_city = cities.popleft()

    start_city_destinations_copied = copy(start_city.destinations)
    # print(start_city)

    while start_city.trucks > 0 \
            and start_city_destinations_copied:

        end_destination_name, \
        end_destination_road_max = start_city_destinations_copied.popitem()

        end_destination = get_urban(end_destination_name, cities)
        if not end_destination:
            continue

        # print(end_destination)

        counter = 0
        while start_city.trucks > 0 \
                and counter < end_destination_road_max \
                and end_destination.trucks < end_destination.export:

            start_city.decrease_trucks(1)
            end_destination.increase_trucks(1)
            counter += 1

        # print(end_destination)

    # print(start_city)
    # print()

    if does_another_city_has_a_course(start_city.name, cities):
        cities.insert(1, start_city)

print(cities[0].trucks)
