"""Implement binary search tree in python

Implemented methods for binary search tree:
    size: return number of nodes.
    is_empty: False if at least one node, otherwise True.
    insert: insert new node with given value.
    find: True if value is in tree, otherwise False.
    breadth_first: print tree node values based on breadth first.
    pre_order_depth_first: print tree node values based on pre-order depth first.
    in_order_depth_first: print tree node values based on in-order depth first.
    post_order_depth_first: print tree node values based on post-order depth first.
    height: return tree height.
    tree_min: return minimum value of tree.
    tree_max: return maximum value of tree.
    tree_max: return maximum value of tree.
    is_equal: True if two trees are equal, otherwise False.
    is_binary_search_tree: True if tree is a binary search tree, otherwise False.
    nodes_at_distance: print nodes at given distance/height.
    count_leaves: return number of tree's leaves.
    contains: same as find method, but implemented recursively.
    are_sibiling: True if two given values are sibling, otherwise False.
    get_ancestors: list of a given value ancestors, empty list [] if tree is empty or there is no ancestor.
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.__size = 0

    @property
    def size(self):
        return self.__size

    @staticmethod
    def __new_node(value):
        return Node(value=value)

    @property
    def is_empty(self):
        return self.root is None

    @staticmethod
    def __is_leaf(node: Node):
        if node is None:
            return False

        return node.left_child is None and node.right_child is None

    def insert(self, value: int):
        if self.is_empty:
            self.root = self.__new_node(value=value)
            self.__size += 1
            return

        current = self.root
        while True:
            if value <= current.value:
                if current.left_child is None:
                    current.left_child = self.__new_node(value)
                    return
                current = current.left_child

            else:
                if current.right_child is None:
                    current.right_child = self.__new_node(value)
                    return
                current = current.right_child

            self.__size += 1

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

        if self.is_empty:
            return

        queue = [self.root]
        while queue:
            node = queue[0]
            del queue[0]
            if node.value:
                print(node.value, end=" - ")

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

    def __pre_order_depth_first(self, root: Node):
        if root is None:
            return

        print(root.value, end=" - ")
        self.__pre_order_depth_first(root.left_child)
        self.__pre_order_depth_first(root.right_child)

    def pre_order_depth_first(self):
        self.__pre_order_depth_first(root=self.root)

    def __in_order_depth_first(self, root: Node):
        if root is None:
            return

        self.__in_order_depth_first(root.left_child)
        print(root.value, end=" ")
        self.__in_order_depth_first(root.right_child)

    def in_order_depth_first(self):
        self.__in_order_depth_first(self.root)

    def __post_order_depth_first(self, root: Node):
        if root is None:
            return

        self.__post_order_depth_first(root.left_child)
        self.__post_order_depth_first(root.right_child)
        print(root.value, end=" ")

    def post_order_depth_first(self):
        self.__post_order_depth_first(self.root)

    def __height(self, root: Node):
        if root is None:
            return -1

        if self.__is_leaf(root):
            return 0

        return 1 + max(self.__height(root.left_child), self.__height(root.right_child))

    def height(self):
        return self.__height(self.root)

    def __tree_min(self, root: Node):

        if root is None:
            return

        if self.__is_leaf(root):
            return root.value

        left_min = self.__tree_min(root.left_child)
        right_min = self.__tree_min(root.right_child)

        if left_min is None or right_min is None:
            return root.value
        else:
            return min(left_min, right_min, root.value)

    def tree_min(self):
        return self.__tree_min(self.root)

    def __tree_max(self, node: Node):

        if node is None:
            return

        if self.__is_leaf(node):
            return node.value

        left_max = self.__tree_max(node.right_child)
        right_max = self.__tree_max(node.right_child)

        if left_max is None or right_max is None:
            return node.value
        else:
            return max(left_max, right_max, node.value)

    def tree_max(self):
        return self.__tree_max(self.root)

    def __check_equality(self, node_1: Node, node_2: Node):
        if node_1 is None and node_2 is None:
            return True
        elif node_1 is not None and node_2 is not None:
            return (
                node_1.value == node_2.value
                and (self.__check_equality(node_1.left_child, node_2.left_child))
                and (self.__check_equality(node_1.right_child, node_2.right_child))
            )
        else:
            return False

    def is_equal(self, other_tree):
        if other_tree is None:
            return False

        return self.__check_equality(self.root, other_tree.root)

    def __check_is_binary_search_tree(self, node: Node, min_limit, max_limit):

        if node is None:
            return True

        if node.value < min_limit or node.value > max_limit:
            return False

        return self.__check_is_binary_search_tree(
            node.left_child, min_limit=min_limit, max_limit=node.value - 1
        ) and self.__check_is_binary_search_tree(
            node.right_child, min_limit=node.value + 1, max_limit=max_limit
        )

    def is_binary_search_tree(self):

        return self.__check_is_binary_search_tree(
            self.root, float("-inf"), float("+inf")
        )

    def __print_nodes_at_distance(self, node: Node, distance):
        if distance < 0:
            return

        if node is None:
            return

        if distance == 0:
            print(node.value)

        self.__print_nodes_at_distance(node.left_child, distance - 1)
        self.__print_nodes_at_distance(node.right_child, distance - 1)

    def nodes_at_distance(self, distance):
        return self.__print_nodes_at_distance(self.root, distance=distance)

    def count_leaves(self):
        leaves = 0
        if self.is_empty:
            return -1
        elif self.__is_leaf(self.root):
            leaves += 1
            return leaves
        else:

            queue = [self.root]
            while queue:
                node = queue[0]
                del queue[0]
                if self.__is_leaf(node):
                    leaves += 1
                    continue

                if node.left_child:
                    queue.append(node.left_child)

                if node.right_child:
                    queue.append(node.right_child)

        return leaves

    def __contains(self, node: Node, value: int):

        if node is None:
            print("False")
            return

        if value < node.value:
            self.__contains(node.left_child, value)

        elif value > node.value:
            self.__contains(node.right_child, value)

        else:
            print("True")
            return

    def contains(self, value: int):
        self.__contains(self.root, value)

    def __are_sibiling(self, node: Node, smaller_value: int, greater_value: int):

        queue = [node]
        while queue:
            node = queue[0]
            del queue[0]

            if (
                node.left_child
                and node.right_child
                and node.left_child.value == smaller_value
                and node.right_child.value == greater_value
            ):
                return True

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

        return False

    def are_sibiling(self, value_1: int, value_2: int):
        if self.is_empty:
            return False
        elif value_1 < value_2:
            return self.__are_sibiling(self.root, value_1, value_2)
        elif value_1 > value_2:
            return self.__are_sibiling(self.root, value_2, value_1)
        else:
            return False

    def get_ancestors(self, value: int):
        ancestors_list = []
        is_find = self.find(value)
        if not is_find:
            return ancestors_list
        else:
            if self.is_empty:
                return ancestors_list

            current = self.root
            while current is not None:
                if value < current.value:
                    ancestors_list.append(current.value)
                    current = current.left_child
                elif value > current.value:
                    ancestors_list.append(current.value)
                    current = current.right_child
                else:
                    break

            return ancestors_list
