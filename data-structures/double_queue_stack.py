"""Stack using Double queues

Implemented methods for Stack with one list:
    put: Push in stack.
    get: Pop from stack.
    peek: Pop from stack (keeping value in stack).
"""
from my_queue import Queue


class DoubleQueueStack:
    def __init__(self):
        self.push_queue = Queue()
        self.pop_queue = Queue()

    def is_empty(self):
        return self.push_queue.is_empty() and self.pop_queue.is_empty()

    def put(self, value):
        if self.is_empty():
            self.push_queue.enqueue(value)
        else:
            for _ in range(self.push_queue.size):
                self.pop_queue.enqueue(self.push_queue.dequeue())
            self.push_queue.enqueue(value)
        return self

    def get(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        elif self.push_queue.is_empty():
            for _ in range(self.pop_queue.size):
                self.push_queue.enqueue(self.pop_queue.dequeue())
            for _ in range(self.push_queue.size - 1):
                self.pop_queue.enqueue(self.push_queue.dequeue())
            return self.push_queue.dequeue()
        else:
            return self.push_queue.dequeue()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")

        elif self.push_queue.is_empty():
            for _ in range(self.pop_queue.size):
                self.push_queue.enqueue(self.pop_queue.dequeue())
            for _ in range(self.push_queue.size - 1):
                self.pop_queue.enqueue(self.push_queue.dequeue())
            return self.push_queue.peek()
        else:
            return self.push_queue.peek()


new_dqs = DoubleQueueStack()

new_dqs.put(1)
new_dqs.put(2)
new_dqs.put(3)
new_dqs.put(4)
new_dqs.peek()
new_dqs.get()
new_dqs.peek()
new_dqs.peek()
new_dqs.peek()

print(new_dqs)
