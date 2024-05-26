"""Implement Directed Graphs in python

Implemented methods for directed graph:
    add_node: add new node without any neighbors to graph.
    add_edge: add an edge between from_node to to_node if not exists (Singled graph).
    remove_node: remove a node and all its edges from graph.
    remove_edge: remove edge between from_node to to_node if exists.
    print_graph: prints out all nodes and its neighbors in terminal.
    depth_first_traverse_rec: depth first traverse recursively from given node_name.
    depth_first_traverse_iter: same as depth_first_traverse_rec but iterative.
    breadth_first_traverse_rec: breadth first traverse recursively from given node_name.
    breadth_first_traverse_iter: same as breadth_first_traverse_rec but iterative.
    topological_sort_rec: topological sorting, recursively.
    has_cycle: returns True if there is at least one cycle in graph.
"""


class Node:
    def __init__(self, node_name) -> None:
        self.node_name = node_name

    def __str__(self) -> str:
        return self.node_name

    def __repr__(self) -> str:
        return (self.node_name).upper()


class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.neighbors = {}

    def add_node(self, node_name):
        if node_name not in self.nodes:
            new_node = Node(node_name=node_name)
            self.nodes[node_name] = new_node
            self.neighbors[node_name] = list()

    def add_edge(self, from_node, to_node):

        to_node_obj: Node = self.nodes.get(to_node)
        from_node_neighbors: list = self.neighbors.get(from_node)
        if (
            from_node_neighbors is not None
            and to_node_obj is not None
            and to_node_obj not in from_node_neighbors
        ):
            from_node_neighbors.append(to_node_obj)
        else:
            return

    def remove_node(self, node_name):
        rm_node_obj = self.nodes.get(node_name)
        if rm_node_obj is not None:
            for _, node_neighbors in self.neighbors.items():
                if rm_node_obj in node_neighbors:
                    node_neighbors: list = node_neighbors.remove(rm_node_obj)
                    self.neighbors[node_name] = node_neighbors

            del self.nodes[node_name]
            del self.neighbors[node_name]

    def remove_edge(self, from_node, to_node):
        to_node_obj = self.nodes.get(to_node)
        from_node_neighbors = self.neighbors.get(from_node)
        if from_node_neighbors is not None:
            if to_node_obj in from_node_neighbors:
                from_node_neighbors.remove(to_node_obj)
        else:
            return

    def print_graph(self):
        for node_name, node_neighbors in self.neighbors.items():
            print(f"{node_name} is connected to {node_neighbors}")

    def __depth_first_traverse_rec(self, node_name, visited_nodes: set):
        print(node_name)
        visited_nodes.add(node_name)
        node_neighbors = self.neighbors.get(node_name)

        for neighbor in node_neighbors:
            neighbor_name = neighbor.node_name
            if neighbor_name not in visited_nodes:
                self.__depth_first_traverse_rec(neighbor_name, visited_nodes)

    def depth_first_traverse_rec(self, node_name):
        if node_name not in self.nodes:
            return

        visited_nodes = set()
        self.__depth_first_traverse_rec(node_name, visited_nodes)

    def depth_first_traverse_iter(self, node_name):
        if node_name not in self.nodes:
            return

        visited_nodes = {node_name}

        node_list = [node_name]

        while node_list:
            node = node_list.pop()
            print(node)

            neighbors = self.neighbors.get(node)
            for neighbor in neighbors:
                neighbor_name = neighbor.node_name
                if neighbor_name not in visited_nodes:
                    visited_nodes.add(neighbor_name)
                    node_list.append(neighbor_name)

    def __breadth_first_traverse_rec(self, node_queue: list, visited_nodes: set):

        while node_queue:
            node = node_queue.pop()
            print(node)
            node_neighbors = self.neighbors.get(node)
            for neighbor in node_neighbors:
                neighbor_name = neighbor.node_name
                if neighbor_name not in visited_nodes:
                    node_queue.insert(0, neighbor_name)
                    visited_nodes.add(neighbor_name)
            self.__breadth_first_traverse_rec(node_queue, visited_nodes)

    def breadth_first_traverse_rec(self, node_name):
        if node_name not in self.nodes:
            return

        visited_nodes = {node_name}
        node_queue = [node_name]
        self.__breadth_first_traverse_rec(node_queue, visited_nodes)

    def breadth_first_traverse_iter(self, node_name):
        if node_name not in self.nodes:
            return

        visited_nodes = {node_name}
        node_queue = [node_name]

        while node_queue:
            node = node_queue.pop()
            print(node)

            neighbors = self.neighbors.get(node)
            for neighbor in neighbors:
                neighbor_name = neighbor.node_name
                if neighbor_name not in visited_nodes:
                    visited_nodes.add(neighbor_name)
                    node_queue.insert(0, neighbor_name)

    def __topological_sort_rec(self, node_name, visited_nodes: set, node_stack: list):
        if node_name in visited_nodes:
            return

        visited_nodes.add(node_name)

        node_neighbors = self.neighbors.get(node_name)
        for neighbor in node_neighbors:
            neighbor_name = neighbor.node_name
            self.__topological_sort_rec(neighbor_name, visited_nodes, node_stack)

        node_stack.append(node_name)

    def topological_sort_rec(self):
        visited_nodes = set()
        node_stack = list()

        for node_name in self.nodes.keys():
            self.__topological_sort_rec(node_name, visited_nodes, node_stack)

        sorted_nodes = []
        while node_stack:
            sorted_nodes.append(node_stack.pop())

        return sorted_nodes

    def __has_cycle(
        self, node_name, all_nodes: list, visiting_nodes: set, visited_nodes: set
    ):
        if node_name in all_nodes:
            all_nodes.remove(node_name)

        visiting_nodes.add(node_name)
        for neighbor in self.neighbors.get(node_name):
            neighbor_name = neighbor.node_name
            if neighbor_name in visited_nodes:
                continue
            elif neighbor_name in visiting_nodes:
                return True
            else:
                if self.__has_cycle(
                    neighbor_name, all_nodes, visiting_nodes, visited_nodes
                ):
                    return True

        visiting_nodes.remove(node_name)
        visited_nodes.add(node_name)

        return False

    def has_cycle(self):
        all_nodes = set(self.nodes.keys())
        visiting_nodes = set()
        visited_nodes = set()

        while all_nodes:
            node_name = all_nodes.pop()
            if self.__has_cycle(node_name, all_nodes, visiting_nodes, visited_nodes):
                return True

        return False
