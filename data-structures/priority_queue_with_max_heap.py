"""Implement Priority Queue with Max Heap in python

Implemented methods for priority queue:
    is_empty: True if priority queue us empty. otherwise False.
    enqueue: Enqueue given value into priority queue.
    dequeue: Dequeue from priority queue.
"""

from max_heap import MaxHeap


class PriorityQueueWithHeap:
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
