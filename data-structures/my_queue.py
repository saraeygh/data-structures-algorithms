"""Implement Queue using list

Implemented methods for Queue:
    enqueue: Enqueue new item in queue.
    dequeue: Dequeue new item from queue.
    peek: Just Peek item without dequeue.
    reverse: Reverse queue order.
    reverse_firsk_k: Reverse first k items order.
    is_empty: Check if queue is empty.
"""


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1
        return self

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        self.size -= 1
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[0]

    def reverse(self):
        return self.queue.reverse()

    def reverse_first_k(self, k):
        if k > len(self.queue):
            raise IndexError("Index out of range.")

        first_k = self.queue[:k]
        rest = self.queue[k:]
        first_k_rev = first_k[::-1]
        self.queue = first_k_rev + rest
        return self
