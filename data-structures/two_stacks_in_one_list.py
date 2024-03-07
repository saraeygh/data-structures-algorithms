"""Use one list to store two stacks

Implemented methods:
    put1: Push in stack1.
    put2: Push in stack2.
    get1: Pop from stack1.
    get2: Pop from stack2.
    is_empty1: Check if stack1 is empty.
    is_empty2: Check if stack2 is empty.
"""


class TwoStackInOneList:
    def __init__(self):
        self.stacks = []
        self.size1 = 0
        self.size2 = 0
        self.top1 = None
        self.top2 = None

    def is_empty1(self):
        return self.top1 is None

    def is_empty2(self):
        return self.top2 is None

    def stacks_size(self):
        return len(self.stacks)

    def put1(self, value):
        if self.stacks_size() == 0:
            self.stacks.append(value)
            self.top1 = 0
        else:
            if self.is_empty1():
                self.stacks.insert(0, value)
                self.top1 = 0
            else:
                self.top1 += 1
                self.stacks.insert(self.top1, value)

        self.size1 += 1
        return self

    def get1(self):
        if self.is_empty1():
            raise IndexError("Stack 1 is empty.")

        value = self.stacks.pop(self.top1)
        self.top1 -= 1
        if self.top1 == -1:
            self.top1 = None

        self.size1 += 1
        return value

    def put2(self, value):
        if self.is_empty2():
            self.stacks.append(value)
            self.top2 = -1
        else:
            self.stacks.append(value)

        self.size2 += 1
        return self

    def get2(self):
        if self.is_empty2():
            raise IndexError("Stack 2 is empty.")

        value = self.stacks.pop(self.top2)

        self.size2 -= 1
        if self.size2 == 0:
            self.top2 = None

        return value
