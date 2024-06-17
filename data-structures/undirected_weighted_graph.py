"""Implement Undirected Weighted Graphs in python

Implemented methods for directed graph:
    add_node: add new node without any edges to graph.
    add_edge: add an edge between from_node to to_node with given weight.
    get_shortest_path: get shortest path from from_node to to_node (Dijkstra Algorithm).
    has_cycle: returns True if there is at least one cycle in graph.
    get_min_spanning_tree: get min spanning tree out of a undirected weighted graph.
    print_graph: prints out all nodes and its edges in terminal.
"""


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value_priority_pair):
        self.queue.append(value_priority_pair)

    def dequeue(self):
        most_priority_idx = -1
        for idx, _ in enumerate(self.queue):
            if self.queue[idx][1] < self.queue[most_priority_idx][1]:
                most_priority_idx = idx
        item = self.queue[most_priority_idx]
        del self.queue[most_priority_idx]
        return item


class Node:
    def __init__(self, node_name) -> None:
        self.node_name = node_name
        self.edges = dict()

    def add_edge(self, to_node: "Node", weight):
        new_edge = Edge(from_node=self, to_node=to_node, weight=weight)
        self.edges[to_node.node_name] = new_edge

    def get_edges(self) -> list["Edge"]:
        return list(self.edges.values())

    def __str__(self) -> str:
        return self.node_name

    def __repr__(self) -> str:
        return (self.node_name).upper()


class Edge:
    def __init__(self, from_node: Node, to_node: Node, weight: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.from_node}--{self.to_node} ({self.weight})"

    def __repr__(self) -> str:
        return f"{self.from_node}--{self.to_node} ({self.weight})"


class UndirectedWeightedGraph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, node_name):
        if node_name not in self.nodes:
            new_node = Node(node_name=node_name)
            self.nodes[node_name] = new_node

    def add_edge(self, from_node, to_node, weight):

        from_node_obj: Node = self.nodes.get(from_node)
        to_node_obj: Node = self.nodes.get(to_node)

        if from_node_obj is not None and to_node_obj is not None:
            from_node_obj.add_edge(to_node=to_node_obj, weight=weight)
            to_node_obj.add_edge(to_node=from_node_obj, weight=weight)
        else:
            return

    def __build_shortest_path(self, end_node: Node, prev_nodes: dict):
        path_list = []
        path_list.insert(0, end_node.node_name)

        prev_node: Node = prev_nodes.get(end_node)
        path_list.insert(0, prev_node.node_name)

        while prev_node is not None:
            prev_node: Node = prev_nodes.get(prev_node)
            if prev_node is not None:
                path_list.insert(0, prev_node.node_name)

        return path_list

    def get_shortest_path(self, from_node, to_node):

        from_node_obj: Node = self.nodes.get(from_node)
        to_node_obj: Node = self.nodes.get(to_node)

        if from_node_obj is not None and to_node_obj is not None:
            distances = dict()
            for _, node_obj in self.nodes.items():
                distances[node_obj] = None
            distances[from_node_obj] = 0

            prev_nodes = dict()

            visited = set()

            priority_queue = PriorityQueue()
            priority_queue.enqueue(value_priority_pair=(from_node_obj, 0))

            while not priority_queue.is_empty():
                current: Node = priority_queue.dequeue()[0]
                visited.add(current)

                for edge in current.get_edges():
                    if edge.to_node in visited:
                        continue

                    new_distance = distances.get(current) + edge.weight

                    if distances.get(
                        edge.to_node
                    ) is None or new_distance < distances.get(edge.to_node):
                        distances[edge.to_node] = new_distance
                        prev_nodes[edge.to_node] = current
                        priority_queue.enqueue(
                            value_priority_pair=(edge.to_node, new_distance)
                        )

            shortest_path = self.__build_shortest_path(
                prev_nodes=prev_nodes, end_node=to_node_obj
            )

            return shortest_path
        else:
            return

    def __has_cycle(self, node: Node, parent_node: Node, visited_nodes: set):
        visited_nodes.add(node)

        for edge in node.get_edges():
            if edge.to_node == parent_node:
                continue

            if edge.to_node in visited_nodes or self.__has_cycle(
                node=edge.to_node, parent_node=node, visited_nodes=visited_nodes
            ):
                return True

        return False

    def has_cycle(self):
        all_nodes = set(self.nodes.values())
        visited_nodes = set()

        for node in all_nodes:
            if node not in visited_nodes and self.__has_cycle(
                node=node,
                parent_node="",
                visited_nodes=visited_nodes,
            ):
                return True

        return False

    def get_min_spanning_tree(self):
        tree = UndirectedWeightedGraph()
        least_edge = PriorityQueue()

        if len(self.nodes) == 0:
            return tree

        start_node: Node = list(self.nodes.values())[0]
        for edge in start_node.get_edges():
            least_edge.enqueue(value_priority_pair=(edge, edge.weight))

        if least_edge.is_empty():
            return tree

        tree.add_node(start_node.node_name)

        while len(tree.nodes) < len(self.nodes):
            min_edge: Edge = (least_edge.dequeue())[0]
            next_node: Node = min_edge.to_node

            if next_node.node_name in tree.nodes:
                continue

            tree.add_node(next_node.node_name)
            tree.add_edge(
                min_edge.from_node.node_name, next_node.node_name, min_edge.weight
            )

            for edge in next_node.get_edges():
                if edge.to_node.node_name not in tree.nodes:
                    least_edge.enqueue(value_priority_pair=(edge, edge.weight))

        return tree

    def print_graph(self):
        for node_name, node_obj in self.nodes.items():
            print(f"{node_name} is connected to {node_obj.get_edges()}")
