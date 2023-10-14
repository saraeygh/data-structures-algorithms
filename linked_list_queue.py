"""Implement Linked list in python

Implemented methods:
    is_empty: Check if linked list is empty.
    has_one_node: Check if linked list has just one node.
    get_previous: Return previous node of each given node.
    add_last: Add to the end of linked list.
    add_first: Add to the beginning of linked list.
    index_of: Return index of given value.
    contains: Check if linked list contains given value.
    remove_first: Remove first node.
    remove_last: Remove last node.
    size: Size of linked list.
    to_list: Convert linked list to python list.
    reverse: Reverse linked list.
    index_value_from_end: Value of given index relative to end of linked list.
    middle_node: Return middle node(s) of linked list.
    has_loop: Check if linked list has loop.
"""


class Node:
    """Represent each node of linked list."""

    def __init__(self, value=None, after=None):
        """
        Args:
            value (any, optional): Value stored by node. Defaults to None.
            after (self, optional): Represent next node. Defaults to None.
        """
        self.value = value
        self.after = after


class LinkedListQueue:
    """A singly linked list (There is no previous node)"""

    def __init__(self, head: Node = Node(), tail=None, length: int = 0):
        """
        Args:
            head (Node, optional): First node. Defaults to Node().
            tail (Node, optional): Last node. Defaults to None.
        """
        self.head = head
        self.tail = tail
        self.length = length
        self.tail = self.head

    def is_empty(self):
        return self.head == self.tail and self.head.value is None

    def has_one_node(self):
        return self.head == self.tail and self.head.value is not None

    def enqueue(self, value):
        self.length += 1
        if LinkedListQueue.is_empty(self):
            self.head.value = value
            return self
        elif LinkedListQueue.has_one_node(self):
            new_node = Node(value=value)
            self.head.after = new_node
            self.tail = new_node
            return self
        else:
            new_node = Node(value=value)
            self.tail.after = new_node
            self.tail = new_node
            return self

    def dequeue(self):
        if LinkedListQueue.is_empty(self):
            return None
        elif LinkedListQueue.has_one_node(self):
            value = self.head.value
            self.head.value = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            new_head = self.head.after
            del self.head
            self.head = new_head
            self.length -= 1
            return self

    def size(self):
        print(f"List size is {self.length}.")
        return self.length

    def to_list(self):
        new_list = []
        if LinkedListQueue.is_empty(self):
            return new_list
        elif LinkedListQueue.has_one_node(self):
            new_list.append(self.head.value)
            return new_list
        else:
            current = self.head
            while True:
                if current.after is None:
                    new_list.append(current.value)
                    return new_list
                new_list.append(current.value)
                current = current.after

    def reverse(self):
        if LinkedListQueue.is_empty(self):
            return self
        elif LinkedListQueue.has_one_node(self):
            return self
        else:
            previous = self.head
            current = self.head.after
            next = current.after
            self.tail = previous
            self.tail.after = None
            while True:
                if current.after is None:
                    current.after = previous
                    self.head = current
                    return 1

                current.after = previous
                previous = current
                current = next
                next = next.after
