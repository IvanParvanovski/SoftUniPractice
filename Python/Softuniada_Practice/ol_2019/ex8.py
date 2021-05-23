from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = defaultdict(list)

        for start, end in self.edges:
            self.graph_dict[start].append(end)

    def get_paths(self, start, end, path=list()):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return list()

        paths = list()
        for node in self.graph_dict[start]:
            new_path = self.get_paths(node, end, path)

            for p in new_path:
                paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=list()):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return list()

        shortest_path = list()

        for node in self.graph_dict[start]:
            current_path = self.get_shortest_path(node, end, path)

            if shortest_path:
                if len(current_path) < len(shortest_path):
                    shortest_path = current_path
            else:
                if current_path:
                    shortest_path = current_path

        return shortest_path

    def get_shortest_path_answer(self, start, end, path=list()):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path_answer(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


routes = (
    ('Knezha', 'Bqla Slatina'),
    ('Knezha', 'Pleven'),
    ('Pleven', 'Lovech'),
    ('Pleven', 'Belene'),
    ('Lovech', 'Sofia'),
    ('Belene', 'Sofia'),
    ('Belene', '')
)

routes2 = {
    'Knezha': ['Bqla Slatina', 'Pleven'],
    'Pleven': ['Lovech', 'Belene'],
    'Lovech': ['Sofia'],
    'Belene': ['Sofia', '']
}

route_graph = Graph(routes)

start = 'Knezha'
end = 'Sofia'

print(f'Paths between {start} and {end}:', route_graph.get_paths(start, end))
print(f'Shortest path between {start} and {end}:', route_graph.get_shortest_path_answer(start, end))
