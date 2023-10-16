"""Hash table with linear probing for collisions

Implemented methods:
    hash: Return hash or index to be used.
    put: Put new key/value or update value if key already exists.
    get: Return value for given key.
    remove: Remove ke/value pair based on given key.
"""


class HashTable:
    def __init__(self, size: int = 5):
        self.array = []
        self.size = size

        for _ in range(size):
            self.array.append(None)

    def hash(self, key):
        return key % self.size

    def is_slot_empty(self, index):
        return self.array[index] is None

    def put(self, key, value):
        for i in range(self.size):
            index = self.hash(key + i)
            if self.is_slot_empty(index):
                self.array[index] = (key, value)
                return
            continue
        raise ValueError("Hash table is full")

    def get(self, key):
        for i in range(self.size):
            index = self.hash(key + i)
            if self.is_slot_empty(index):
                raise KeyError("Invalid key.")
            elif self.array[index][0] == key:
                return self.array[index][1]
            else:
                continue

    def remove(self, key):
        for i in range(self.size):
            index = self.hash(key + i)
            if self.is_slot_empty(index):
                raise KeyError("Invalid key.")
            elif self.array[index][0] == key:
                self.array[index] = None
                return
            else:
                continue
