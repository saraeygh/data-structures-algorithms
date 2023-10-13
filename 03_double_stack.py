"""Use one list to store two stacks

Implemented methods:
    put1: Push in stack1.
    put2: Push in stack2.
    get1: Pop from stack1.
    get2: Pop from stack2.
    is_empty1: Check if stack1 is empty.
    is_empty2: Check if stack2 is empty.
"""


class DoubleStack:
    def __init__(self, stack: list = [], top1=None, top2=None):
        self.stack = stack
        self.top1 = top1
        self.top2 = top2

    def put1(self, value):
        size = len(self.stack)
        if size == 0:
            self.stack.append(value)
            self.top1 = 0
        else:
            if self.is_empty1():
                self.stack.insert(0, value)
                self.top1 = 0
            else:
                self.stack.insert(self.top1 + 1, value)
                self.top1 += 1

        return self

    def get1(self):
        if self.is_empty1():
            raise BaseException("Empty stack")
        elif self.top1 == 0:
            value = self.stack.pop(self.top1)
            self.top1 = None
            return value
        else:
            value = self.stack.pop(self.top1)
            self.top1 -= 1
            return value

    def put2(self, value):
        size = len(self.stack)
        if size == 0:
            self.stack.append(value)
            self.top2 = -1
        else:
            if self.is_empty2():
                self.stack.append(value)
                self.top2 = -1
            else:
                self.stack.insert(self.top2, value)
                self.top2 -= 1

    def get2(self):
        if self.is_empty2():
            raise BaseException("Empty stack")
        elif self.top2 == -1:
            value = self.stack.pop(self.top2)
            self.top2 = None
            return value
        else:
            value = self.stack.pop(self.top2)
            self.top2 += 1
            return value

    def is_empty1(self):
        return self.top1 is None

    def is_empty2(self):
        return self.top2 is None
