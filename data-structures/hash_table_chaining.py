"""Hash table with chaining for collisions

Implemented methods:
    hash: Return hash or index to be used.
    put: Put new key/value or update value if key already exists.
    get: Return value for given key.
    remove: Remove ke/value pair based on given key.
"""

from my_linked_list import LinkedList


class CustomLinkedList(LinkedList):
    def contains_key(self, key: int):
        node = self.head
        for _ in range(self.length):
            if self.is_empty():
                return None
            elif node.value[0] == key:
                return node

            node = node.after
            if node is None:
                return None

    def remove(self, key: int):
        if self.is_empty():
            raise KeyError("Invalid key.")

        node = self.head
        for _ in range(self.length):
            if node.value[0] == key:
                if node == self.head:
                    self.remove_first()
                    return
                elif node == self.tail:
                    self.remove_last()
                    return
                else:
                    prv_node = self.get_previous(node)
                    prv_node.after = node.after
                    node = None
                    return

            node = node.after
            if node is None:
                raise KeyError("Invalid key.")


class HashTable:
    def __init__(self, size: int = 5):
        self.array = []
        self.size = size

        for _ in range(size):
            new_linked_list = CustomLinkedList()
            self.array.append(new_linked_list)

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash(key)
        linked_list = self.array[index]
        node = linked_list.contains_key(key)
        if node:
            node.value = (key, value)
        else:
            linked_list.add_last((key, value))
        return self

    def get(self, key):
        index = self.hash(key)
        linked_list = self.array[index]
        node = linked_list.contains_key(key)
        if node:
            return node.value
        return None

    def remove(self, key):
        index = self.hash(key)
        linked_list = self.array[index]
        linked_list.remove(key)
        return self
