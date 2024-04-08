"""Implement Heaps in python

Implemented methods for heap:
    is_empty: True if heap is empty.
    insert: Insert the given value into heap.
    remove: Remove value (root value) from heap.
    heap_max: Return heap max value (root value).
    k_th_largest: Return k-th largest value of heap.
    bubble_up: Move up new inserted value to its right position in heap.
    bubble_down: After remove, move down new root to its right position in heap.
"""


class Heap:
    def __init__(self):
        self.items: list = []
        self.size: int = 0

    @property
    def is_empty(self):
        return self.size == 0

    @staticmethod
    def __get_parent_index(index: int):
        return (index - 1) // 2

    @staticmethod
    def __get_left_index(index: int):
        return (index * 2) + 1

    @staticmethod
    def __get_right_index(index: int):
        return (index * 2) + 2

    def __has_left_child(self, index):
        return self.__get_left_index(index) < self.size

    def __has_right_child(self, index):
        return self.__get_right_index(index) < self.size

    def __larger_child_index(self, index):
        if not self.__has_left_child(index):
            return index
        elif not self.__has_right_child(index):
            return self.__get_left_index(index)
        if (
            self.items[self.__get_left_index(index)]
            > self.items[self.__get_right_index(index)]
        ):
            return self.__get_left_index(index)
        else:
            return self.__get_right_index(index)

    def __is_valid_parent(self, index):
        if not self.__has_left_child(index):
            return True
        elif not self.__has_right_child(index):
            return self.items[index] >= self.items[self.__get_left_index(index)]
        else:
            return (
                self.items[index] >= self.items[self.__get_left_index(index)]
                and self.items[index] >= self.items[self.__get_right_index(index)]
            )

    def __swap(self, first_index, second_index):
        first_index_value = self.items[first_index]
        self.items[first_index] = self.items[second_index]
        self.items[second_index] = first_index_value

    def bubble_up(self):
        index = self.size - 1
        index_value = self.items[index]

        parent_index = self.__get_parent_index(index)
        parent_index_value = self.items[parent_index]

        while index > 0 and index_value >= parent_index_value:
            self.__swap(index, parent_index)

            index = self.__get_parent_index(index)
            index_value = self.items[index]

            parent_index = self.__get_parent_index(index)
            parent_index_value = self.items[parent_index]

    def bubble_down(self):
        index = 0
        left_index = self.__get_left_index(index)
        right_index = self.__get_right_index(index)

        while (
            left_index < self.size
            and right_index < self.size
            and not self.__is_valid_parent(index)
        ):
            larger_child_index = self.__larger_child_index(index)

            self.__swap(index, larger_child_index)

            index = larger_child_index

            left_index = self.__get_left_index(index)
            right_index = self.__get_right_index(index)

    def remove(self):
        if self.is_empty:
            return None

        self.size -= 1

        if self.size == 1:
            removed_node = self.items.pop()
            return removed_node

        removed_node = self.items[0]

        self.items[0] = self.items.pop()
        self.bubble_down()

        return removed_node

    def insert(self, value: int):
        self.items.append(value)
        self.size += 1

        self.bubble_up()

    def heap_max(self):
        if self.is_empty:
            return None

        return self.items[0]

    def k_th_largest(self, k):
        if self.is_empty or k < 1 or k > self.size:
            return None

        if k == 1:
            return self.heap_max()

        deleted_nodes = []
        for _ in range(k - 1):
            removed_node = self.remove()
            deleted_nodes.append(removed_node)
        k_th_largest = self.heap_max()

        for value in deleted_nodes:
            self.insert(value=value)

        return k_th_largest
