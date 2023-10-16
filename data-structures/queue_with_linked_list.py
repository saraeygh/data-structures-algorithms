"""Implement Queue using Linked list

Implemented methods for Queue:
    enqueue: Enqueue new item in queue.
    dequeue: Dequeue new item from queue.
    peek: Just Peek item without dequeue.
    reverse: Reverse queue order.
    is_empty: Check if queue is empty.
"""
from my_linked_list import LinkedList


class LinkedListQueue:
    def __init__(self):
        self.queue = LinkedList()

    def is_empty(self):
        return self.queue.length == 0

    def enqueue(self, value):
        self.queue.add_last(value)
        return self

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")

        value = self.queue.head.value
        self.queue.remove_first()
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")

        return self.queue.head.value

    def reverse(self):
        return self.queue.reverse()
