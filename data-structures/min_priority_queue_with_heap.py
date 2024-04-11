"""Implement Min Priority Queue with Heap in python (Stores Tuples as (Key: int, Value: string))

Implemented methods for min priority queue:
    is_empty: True if min priority queue us empty. otherwise False.
    enqueue: Enqueue given value into min priority queue.
    dequeue: Dequeue from min priority queue.
"""

from min_heap import MinHeap


class MinPriorityQueueWithHeap:
    def __init__(self):
        self.priority_queue: MinHeap = MinHeap()

    def is_empty(self):
        return self.priority_queue.is_empty

    def enqueue(self, value: tuple):
        self.priority_queue.insert(value=value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.priority_queue.remove()
