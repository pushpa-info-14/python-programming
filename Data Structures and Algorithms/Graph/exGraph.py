class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]  # Do not use += here. This is not an arithmatic operation

        if start == end:
            return [path]
        if start not in self.graph_dict or end not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                paths = paths + self.get_paths(node, end, path)
        return paths

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]  # Do not use += here. It is not working for arrays

        if start == end:
            return path
        if start not in self.graph_dict or end not in self.graph_dict:
            return []

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_shortest_path(node, end, path)
                if len(new_path) > 0:
                    if shortest_path is None or len(shortest_path) > len(new_path):
                        shortest_path = new_path
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    p1 = "Mumbai"
    p2 = "New York"
    print(f"Paths between {p1} and {p2} : ", route_graph.get_paths(p1, p2))
    print(f"Shortest path between {p1} and {p2} : ", route_graph.get_shortest_path(p1, p2))

    p1 = "Mumbai"
    p2 = "Mumbai"
    print(f"Paths between {p1} and {p2} : ", route_graph.get_paths(p1, p2))
    print(f"Shortest path between {p1} and {p2} : ", route_graph.get_shortest_path(p1, p2))

    p1 = "Mumbai"
    p2 = "USA"
    print(f"Paths between {p1} and {p2} : ", route_graph.get_paths(p1, p2))
    print(f"Shortest path between {p1} and {p2} : ", route_graph.get_shortest_path(p1, p2))
