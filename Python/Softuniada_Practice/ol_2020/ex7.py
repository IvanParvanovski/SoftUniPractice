import sys
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = list()

    def __repr__(self):
        return (f'{__class__.__name__}'
                f'({self.value!r})')


class Edge:
    def __init__(self,
                 from_,
                 to,
                 is_backwards=False,
                 capacity=0,
                 current_flow=0):

        self.from_ = from_
        self.to = to
        self.is_backwards = is_backwards
        self.capacity = capacity
        self.current_flow = current_flow

    def __repr__(self):
        return (f'Edge('
                f'{self.from_!r}, {self.to!r}, '
                f'{self.is_backwards!r}, {self.capacity!r}, '
                f'{self.current_flow!r})')


def generate_graph(count):
    graph = dict()

    for _ in range(count):
        user_data = input().split()

        # Save the input into variables
        from_ = user_data[0]
        to_ = user_data[1]
        allowed_traffic = int(user_data[2])

        # Add the nodes if they don't exist
        if from_ not in graph:
            graph[from_] = Node(from_)

        if to_ not in graph:
            graph[to_] = Node(to_)

        # Initialize an edge
        edge = Edge(from_=graph[from_],
                    to=graph[to_], )

        # Change edge capacity and add it to the start city / node
        edge.capacity += allowed_traffic
        graph[from_].edges.append(edge)

        # Initialize an edge
        edge = Edge(from_=graph[to_],
                    to=graph[from_],
                    is_backwards=True, )

        # Add the backwards edge
        graph[to_].edges.append(edge)

    #
    # for city_name, node in graph.items():
    #     print(f'--- {node}')
    #     for edge in node.edges:
    #         print(edge)
    #     print()
    #

    return graph


def bfs(graph, start, end, path):
    queue = deque()
    queue.append(graph[start])

    visited = set()
    visited.add(start)

    path[start] = None

    while queue:
        node = queue.popleft()

        for edge in node.edges:
            if edge.capacity - edge.current_flow > 0 and edge.to.value not in visited:

                path[edge.to.value] = node.value
                queue.append(edge.to)
                visited.add(edge.to.value)

    return end in visited


def fulkursen(graph, start, end):
    max_flow = 0
    path = dict()

    while bfs(graph, start, end, path):
        min_flow = sys.maxsize
        current = end

        while path[current] is not None:
            old = current
            current = path[current]

            edge = next(x for x in graph[current].edges if x.to.value == old)

            min_flow = min(min_flow, edge.capacity - edge.current_flow)

        current = end
        while path[current] is not None:
            old = current
            current = path[current]

            edge = next(x for x in graph[current].edges if x.to.value == old)
            edge.current_flow += min_flow

            back_edge = next(x for x in graph[old].edges if x.to.value == current)

            if back_edge is not None and back_edge.is_backwards:
                back_edge.current_flow -= min_flow

        max_flow += min_flow
        path = dict()

    return max_flow


start = input()
end = input()
graph = generate_graph(int(input()))
print(fulkursen(graph, start, end))
