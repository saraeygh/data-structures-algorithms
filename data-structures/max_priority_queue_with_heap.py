"""Implement Max Priority Queue with Heap in python (Stores Integers!)

Implemented methods for max priority queue:
    is_empty: True if max priority queue us empty. otherwise False.
    enqueue: Enqueue given value into max priority queue.
    dequeue: Dequeue from max priority queue.
"""

from max_heap import MaxHeap


class MaxPriorityQueueWithHeap:
    def __init__(self):
        self.priority_queue: MaxHeap = MaxHeap()

    def is_empty(self):
        return self.priority_queue.is_empty

    def enqueue(self, value: int):
        self.priority_queue.insert(value=value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.priority_queue.remove()
