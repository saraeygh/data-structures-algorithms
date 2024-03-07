"""Implement binary search tree in python

Implemented methods:
    insert: insert new node with new value to tree.
    find: find node based on given value.
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def new_node(value):
        return Node(value=value)

    @property
    def is_empty(self):
        return self.root is None

    def is_leaf(self, node: Node):
        if node is None:
            return True

        return node.left_child is None and node.right_child is None

    def insert(self, value: int):
        if self.is_empty:
            self.root = self.new_node(value=value)
            return

        current = self.root
        while True:
            if value <= current.value:
                if current.left_child is None:
                    current.left_child = self.new_node(value)
                    return
                current = current.left_child

            if value > current.value:
                if current.right_child is None:
                    current.right_child = self.new_node(value)
                    return
                current = current.right_child

    def find(self, value: int):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:
                return True

        return False

    def breadth_first(self):

        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue[0]
            del queue[0]
            if node.value:
                print(node.value, end=" ")

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

    def pre_order_depth_first(self, root: Node):
        if root is None:
            return

        print(root.value, end=" ")
        self.pre_order_depth_first(root.left_child)
        self.pre_order_depth_first(root.right_child)

    def in_order_depth_first(self, root: Node):
        if root is None:
            return

        self.in_order_depth_first(root.left_child)
        print(root.value, end=" ")
        self.in_order_depth_first(root.right_child)

    def post_order_depth_first(self, root: Node):
        if root is None:
            return

        self.post_order_depth_first(root.left_child)
        self.post_order_depth_first(root.right_child)
        print(root.value, end=" ")

    def height(self, root: Node):
        if root is None:
            return -1

        if self.is_leaf(root):
            return 0

        return 1 + max(self.height(root.left_child), self.height(root.right_child))

    def tree_min(self, root: Node):

        if root is None:
            return

        if self.is_leaf(root):
            return root.value

        left_min = self.tree_min(root.left_child)
        right_min = self.tree_min(root.right_child)

        if left_min is None or right_min is None:
            return root.value
        else:
            return min(left_min, right_min, root.value)

    def equals(self, other_tree):
        if other_tree is None:
            return False

        def is_eqaul(node_1: Node, node_2: Node):
            if node_1 is None and node_2 is None:
                return True
            elif node_1 is not None and node_2 is not None:
                return (
                    node_1.value == node_2.value
                    and (is_eqaul(node_1.left_child, node_2.left_child))
                    and (is_eqaul(node_1.right_child, node_2.right_child))
                )

        return is_eqaul(self.root, other_tree.root)

    def binary_search_tree(self, min, max):
        def is_binary_search_tree(root: Node, min, max):
            if root is None:
                return True

            if root.value < min or root.value > max:
                return False

            return is_binary_search_tree(
                root.left_child, min=min, max=root.value - 1
            ) and is_binary_search_tree(root.right_child, min=root.value + 1, max=max)

        return is_binary_search_tree(self.root, min=min, max=max)

    def nodes_at_distance(self, distance):
        def print_nodes_at_distance(root: Node, distance):
            if root is None:
                return

            if distance == 0:
                print(root.value)

            print_nodes_at_distance(root.left_child, distance - 1)
            print_nodes_at_distance(root.right_child, distance - 1)

        print_nodes_at_distance(self.root, distance=distance)


new_tree_1 = BinaryTree()
new_tree_1.insert(20)
new_tree_1.insert(10)
new_tree_1.insert(30)
new_tree_1.insert(6)
new_tree_1.insert(14)
new_tree_1.insert(24)
new_tree_1.insert(3)
new_tree_1.insert(8)
new_tree_1.insert(26)

new_tree_2 = BinaryTree()
new_tree_2.insert(20)
new_tree_2.insert(10)
new_tree_2.insert(30)
new_tree_2.insert(6)
new_tree_2.insert(14)
new_tree_2.insert(24)
new_tree_2.insert(3)
new_tree_2.insert(8)
new_tree_2.insert(28)

new_tree_1.nodes_at_distance(distance=4)
