"""Implement singly Linked list in python

Implemented methods:
    new_node: Return new Node with given value and 'after' = None.
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
"""


class Node:
    def __init__(self, value: any = None):
        self.value = value
        self.after = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    @staticmethod
    def new_node(value):
        return Node(value=value)

    def is_empty(self):
        return self.head is None and self.tail is None

    def has_one_node(self):
        return (
            self.head == self.tail and self.head is not None and self.tail is not None
        )

    def get_previous(self, node: Node):
        current = self.head
        for _ in range(self.length):
            if current.after == node:
                return current
            current = current.after

    def add_last(self, value: any):
        self.length += 1
        if self.is_empty():
            new_node = self.new_node(value)
            self.head = new_node
            self.tail = new_node
            return self
        elif self.has_one_node():
            new_node = self.new_node(value)
            self.tail = new_node
            self.head.after = new_node
            return self
        else:
            new_node = self.new_node(value)
            self.tail.after = new_node
            self.tail = new_node
            return self

    def add_first(self, value: any):
        self.length += 1
        if self.is_empty():
            new_node = self.new_node(value)
            self.head = new_node
            self.tail = new_node
            return self
        elif self.has_one_node():
            new_node = self.new_node(value)
            self.head = new_node
            self.head.after = self.tail
            return self
        else:
            new_node = self.new_node(value)
            after = self.head
            self.head = new_node
            self.head.after = after
            return self

    def index_of(self, value: any):
        index = 0
        node = self.head
        for _ in range(self.length):
            if self.is_empty():
                return None
            elif node.value == value:
                return index

            node = node.after
            if node is None:
                return None
            index += 1

    def contains(self, value: any):
        if self.index_of(value) is None:
            return False
        return True

    def remove_first(self):
        if self.is_empty():
            return self
        elif self.has_one_node():
            self.head = None
            self.tail = None
            self.length -= 1
            return self
        else:
            new_head = self.head.after
            del self.head
            self.head = new_head
            self.length -= 1
            return self

    def remove_last(self):
        if self.is_empty():
            return self
        elif self.has_one_node():
            self.head = None
            self.tail = None
            self.length -= 1
            return self
        else:
            previous = self.get_previous(self.tail)
            self.tail = previous
            previous.after = None
            self.length -= 1
            return self

    def size(self):
        return self.length

    def to_list(self):
        new_list = []
        if self.is_empty():
            return new_list
        elif self.has_one_node():
            new_list.append(self.head.value)
            return new_list
        else:
            current = self.head
            for _ in range(self.length):
                new_list.append(current.value)
                if current.after is None:
                    return new_list
                current = current.after

    def reverse(self):
        if self.is_empty():
            return self
        elif self.has_one_node():
            return self
        else:
            prs = self.head
            crt = self.head.after
            nxt = crt.after
            self.tail = prs
            self.tail.after = None
            for _ in range(self.length):
                if crt.after is None:
                    crt.after = prs
                    self.head = crt
                    return self

                crt.after = prs
                prs = crt
                crt = nxt
                nxt = nxt.after

    def index_value_from_end(self, index: int):
        if index > self.length or index <= 0:
            raise IndexError("Index out of range.")
        first = self.head
        second = self.head
        for _ in range(index - 1):
            second = second.after

        for _ in range(self.length):
            if second == self.tail:
                return first.value
            else:
                first = first.after
                second = second.after
