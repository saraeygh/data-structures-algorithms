"""Implement AVL (Adelson-Velsky and Landis) tree in python

Implemented methods for binary search tree:
    __new_node: Return an AVLNode object with given value.
    is_empty: True if tree is empty, otherwise False.
    __height: Return the height of the given node.
    set_height: Set the height of the given node.
    __balance_factor: Return an integer that shows given node balancing status.
    __is_left_heavy: True if node is left heavy, otherwise False.
    __is_right_heavy: True if node is right heavy, otherwise False.
    __left_rotate: Gives a node an do left rotation on it, returns new root
                   node.
    __right_rotate: Gives a node an do right rotation on it, returns new root
                    node.
    __balance: Return given node if it is already balanced, otherwise make it
               balanced and then return new root of the balanced sub-tree.
    insert: Insert the given value into tree.
"""


class AVLNode:
    def __init__(self, value: int):
        self.value: int = value
        self.height: int = 0
        self.left_child: AVLNode = None
        self.right_child: AVLNode = None


class AVLTree:
    def __init__(self):
        self.root: AVLNode = None

    @staticmethod
    def __new_node(value: int):
        return AVLNode(value=value)

    @property
    def is_empty(self):
        return self.root is None

    @staticmethod
    def __height(node: AVLNode):
        if node is None:
            return -1
        return node.height

    def set_height(self, node: AVLNode):
        node.height = (
            max(
                self.__height(node.left_child),
                self.__height(node.right_child),
            )
            + 1
        )

    def __balance_factor(self, node: AVLNode):
        if node is None:
            return 0
        return self.__height(node.left_child) - self.__height(node.right_child)

    def __is_left_heavy(self, node: AVLNode):
        return self.__balance_factor(node) > 1

    def __is_right_heavy(self, node: AVLNode):
        return self.__balance_factor(node) < -1

    def __left_rotate(self, parent: AVLNode):
        new_root: AVLNode = parent.right_child

        parent.right_child = new_root.left_child
        new_root.left_child = parent

        self.set_height(parent)
        self.set_height(new_root)

        return new_root

    def __right_rotate(self, parent: AVLNode):
        new_root: AVLNode = parent.left_child

        parent.left_child = new_root.right_child
        new_root.right_child = parent

        self.set_height(parent)
        self.set_height(new_root)

        return new_root

    def __balance(self, node: AVLNode):

        if self.__is_left_heavy(node):
            if self.__balance_factor(node.left_child) < 0:
                node.left_child = self.__left_rotate(node.left_child)
            return self.__right_rotate(node)

        elif self.__is_right_heavy(node):
            if self.__balance_factor(node.right_child) > 0:
                node.right_child = self.__right_rotate(node.right_child)
            return self.__left_rotate(node)

        return node

    def __insert(self, parent: AVLNode, value: int):

        if parent is None:
            return self.__new_node(value)

        if value < parent.value:
            parent.left_child = self.__insert(parent.left_child, value=value)
        else:
            parent.right_child = self.__insert(parent.right_child, value=value)

        self.set_height(parent)

        return self.__balance(parent)

    def insert(self, value: int):
        self.root = self.__insert(self.root, value=value)
