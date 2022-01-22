class Node:
    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'Node({self.state}, {self.action}, {self.parent})'


class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def contains_state(self, state):
        return any(n.state == state for n in self.frontier)

    def add(self, state):
        self.frontier.append(state)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


cities = {}


def load_data(cities_amount):
    for i in range(cities_amount):
        city, following_city, trucks_str = input().split()
        trucks = int(trucks_str)

        if city not in cities:
            cities[city] = set()

        cities[city].add((following_city, trucks))


def main():
    source = input()
    target = input()
    number_of_cities = int(input())

    load_data(number_of_cities)

    path = shortest_path(source, target)
    print(path)


def shortest_path(source, target):
    """
    Returns the shortest list of (city_name, trucks) pairs
    that connect the source to the target.

    If no possible path, returns "Not Found".
    """

    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    explored = set()
    num_explored = 0

    while True:
        # If nothing left in frontier, then no path
        if frontier.empty():
            return 'Not Found'

        # Choose a node from the frontier
        node = frontier.remove()
        num_explored += 1

        # If node is the goal, then we have a solution
        if node.state == target:
            actions = []
            cells = []

            # Follow parent nodes to find solution
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent

            actions.reverse()
            cells.reverse()
            return actions, cells

        # Mark node as explored
        explored.add(node.state)

        # Add neighbors to frontier
        for state, action in neighbors_for_city(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, action=action, parent=node)
                frontier.add(child)


def neighbors_for_city(city):
    return cities[city]


main()
