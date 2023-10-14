"""Implement Queue and DoubleStackQueue in python

Implemented methods for Queue:
    enqueue: Enqueue new item in queue.
    dequeue: Dequeue new item from queue.
    peek: Just Peek item without dequeue.
    reverse: Reverse queue order.
    reverse_firsk_k: Reverse first k items order.
    is_empty: Check if queue is empty.

Implemented methods for DoubleStackQueue:
    enqueue: Enqueue new item in queue.
    dequeue: Dequeue new item from queue.
    peek: Just Peek item without dequeue.
    is_empty: Check if queue is empty.
"""


class MyQueue:
    def __init__(self, queue: list = []):
        self.queue = queue

    def enqueue(self, value):
        self.queue.append(value)
        return self

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def reverse(self):
        return self.queue.reverse()

    def reverse_first_k(self, k):
        if k <= len(self.queue):
            first_k = self.queue[:k]
            first_k = first_k[::-1]
            rest = self.queue[k:]
            new_queue = first_k.extend(rest)
            return new_queue
        return IndexError

    def is_empty(self):
        return len(self.queue) == 0


class DoubleStackQueue:
    enq_stack = []
    deq_stack = []

    def enqueue(self, value):
        if len(self.deq_stack) == 0:
            self.enq_stack.append(value)
            while len(self.enq_stack) != 0:
                self.deq_stack.append(self.enq_stack.pop())
        else:
            self.enq_stack.append(value)
        return self

    def dequeue(self):
        if self.is_empty():
            return None
        elif len(self.deq_stack) == 0 and len(self.enq_stack) != 0:
            while len(self.enq_stack) != 0:
                self.deq_stack.append(self.enq_stack.pop())
            value = self.deq_stack.pop()
        else:
            value = self.deq_stack.pop()
        return value

    def peek(self):
        if self.is_empty():
            return None
        elif len(self.deq_stack) == 0 and len(self.enq_stack) != 0:
            while len(self.enq_stack) != 0:
                self.deq_stack.append(self.enq_stack.pop())
            value = self.deq_stack[-1]
        else:
            value = self.deq_stack[-1]
        return value

    def is_empty(self):
        return len(self.enq_stack) == 0 and len(self.deq_stack) == 0
