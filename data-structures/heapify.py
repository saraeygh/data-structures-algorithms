"""Implement Heapify in python

Implemented heapify method:
    heapify: Heapify given list in-place.
"""


class Heapify:

    def __init__(self) -> None:
        pass

    @staticmethod
    def __swap(items_list, index, larger_index):
        index_value = items_list[index]
        items_list[index] = items_list[larger_index]
        items_list[larger_index] = index_value

    def __heapify(self, items_list, value):
        value_index = items_list.index(value)
        larger_index = value_index

        left_index = value_index * 2 + 1
        if (
            left_index < len(items_list)
            and items_list[left_index] > items_list[larger_index]
        ):
            larger_index = left_index

        right_index = value_index * 2 + 2
        if (
            right_index < len(items_list)
            and items_list[right_index] > items_list[larger_index]
        ):
            larger_index = right_index

        if value_index == larger_index:
            return

        self.__swap(items_list, value_index, larger_index)

        self.__heapify(items_list, value)

    def heapify(self, items_list: list):
        main_list = items_list.copy()
        # iter_num = int(len(main_list) / 2)
        iter_num = len(main_list)

        for _ in range(iter_num):
            value = main_list[0]
            del main_list[0]

            self.__heapify(items_list, value)

        return items_list
