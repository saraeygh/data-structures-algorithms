"""Implement DoubleStackQueue

Implemented methods for DoubleStackQueue:
    enqueue: Enqueue new item in queue.
    dequeue: Dequeue new item from queue.
    peek: Just Peek item without dequeue.
    is_empty: Check if queue is empty.
"""
from my_stack import Stack


class DoubleStackQueue:
    def __init__(self):
        self.enq_stack = Stack()
        self.deq_stack = Stack()

    def is_empty(self):
        return self.enq_stack.is_empty() and self.deq_stack.is_empty()

    def enqueue(self, value):
        if self.deq_stack.is_empty():
            self.enq_stack.put(value)
            for _ in range(self.enq_stack.size):
                value = self.enq_stack.get()
                self.deq_stack.put(value)
        else:
            self.enq_stack.put(value)
        return self

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.deq_stack.is_empty():
            for _ in range(self.enq_stack.size):
                self.deq_stack.put(self.enq_stack.get())
            return self.deq_stack.get()
        else:
            return self.deq_stack.get()

    def peek(self):
        if self.is_empty():
            return None
        elif self.deq_stack.is_empty():
            for _ in range(self.enq_stack.size):
                self.deq_stack.put(self.enq_stack.get())
            return self.deq_stack.peek()
        else:
            return self.deq_stack.peek()
