"""Implement Min Heaps in python (Stores Tuples as (Key: int, Value: string))

Implemented methods for min heap:
    is_empty: True if min heap is empty.
    insert: Insert the given value into min heap.
    remove: Remove value (root value) from min heap.
    heap_min: Return heap min value (root value).
    k_th_largest: Return k-th largest value of min heap.
    bubble_up: Move up new inserted value to its right position in min heap.
    bubble_down: After remove, move down new root to its right position in min heap.
"""


class MinHeap:
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

    def __smaller_child_index(self, index):
        if not self.__has_left_child(index):
            return index
        elif not self.__has_right_child(index):
            return self.__get_left_index(index)
        if (
            self.items[self.__get_left_index(index)][0]
            < self.items[self.__get_right_index(index)][0]
        ):
            return self.__get_left_index(index)
        else:
            return self.__get_right_index(index)

    def __is_valid_parent(self, index):
        if not self.__has_left_child(index):
            return True
        elif not self.__has_right_child(index):
            return self.items[index][0] <= self.items[self.__get_left_index(index)][0]
        else:
            return (
                self.items[index][0] <= self.items[self.__get_left_index(index)][0]
                and self.items[index][0] <= self.items[self.__get_right_index(index)][0]
            )

    def __swap(self, first_index, second_index):
        first_index_value = self.items[first_index]
        self.items[first_index] = self.items[second_index]
        self.items[second_index] = first_index_value

    def bubble_up(self):
        index = self.size - 1
        index_value = self.items[index][0]

        parent_index = self.__get_parent_index(index)
        parent_index_value = self.items[parent_index][0]

        while index > 0 and index_value <= parent_index_value:
            self.__swap(index, parent_index)

            index = self.__get_parent_index(index)
            index_value = self.items[index][0]

            parent_index = self.__get_parent_index(index)
            parent_index_value = self.items[parent_index][0]

    def bubble_down(self):
        index = 0
        left_index = self.__get_left_index(index)
        right_index = self.__get_right_index(index)

        while (
            left_index < self.size
            and right_index < self.size
            and not self.__is_valid_parent(index)
        ):
            larger_child_index = self.__smaller_child_index(index)

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

    def insert(self, value: tuple):
        self.items.append(value)
        self.size += 1

        self.bubble_up()

    def heap_min(self):
        if self.is_empty:
            return None

        return self.items[0]

    def k_th_smallest(self, k):
        if self.is_empty or k < 1 or k > self.size:
            return None

        if k == 1:
            return self.heap_min()

        deleted_nodes = []
        for _ in range(k - 1):
            removed_node = self.remove()
            deleted_nodes.append(removed_node)
        k_th_largest = self.heap_min()

        for value in deleted_nodes:
            self.insert(value=value)

        return k_th_largest

    def is_mix_heap(self, input_items: list):
        self.items = input_items
        self.size = len(input_items)

        if self.is_empty:
            return True

        for index, value in enumerate(self.items):
            valid_parent = self.__is_valid_parent(index)
            if not valid_parent:
                return False

        return True
