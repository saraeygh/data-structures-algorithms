"""Stack using list and Double queues

Implemented methods for Stack with one list:
    min: Return min value in stack, None if stack is empty.
    put: Push in stack.
    get: Pop from stack.
    peek: Pop from stack (keeping value in stack).
    str_reverse: Reverse input string.
    is_balanced_expression: Check if opening and ending symbols match.

Implemented methods for Stack with one list:
    put: Push in stack.
    get: Pop from stack.
    peek: Pop from stack (keeping value in stack).
"""


class MyStack:
    def __init__(self, stack: list = [], min=None):
        self.stack = stack
        self.min = min

    def min_value(self):
        return self.min

    def is_empty(self):
        return len(self.stack) == 0

    def put(self, value):
        self.stack.append(value)
        self.min = min(self.stack)
        return self

    def get(self):
        value = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        else:
            self.min = min(self.stack)
        return value

    def peek(self):
        return self.stack[-1]

    def str_reverser(self, input_str: str) -> str:
        if isinstance(input_str, str):
            for letter in input_str:
                self.put(letter)

            rev_input_str = ""
            for i in range(len(self.stack)):
                letter = self.get()
                rev_input_str += letter

            return rev_input_str
        return ValueError

    def is_balanced_expression(self, expression: str) -> bool:
        OPENINGS = ["(", "[", "{", "<"]

        ENDINGS = [")", "]", "}", ">"]

        def is_opening(char):
            return char in OPENINGS

        def is_ending(char):
            return char in ENDINGS

        def match(poped_char, char):
            return OPENINGS.index(poped_char) == ENDINGS.index(char)

        if isinstance(expression, str):
            for char in expression:
                if is_opening(char):
                    self.put(char)
                elif is_ending(char):
                    if len(self.stack) == 0:
                        return False

                    if not match(self.get(), char):
                        return False

            return len(self.stack) == 0

        return ValueError


class DoubleQueueStack:
    push_queue = []
    pop_queue = []

    def put(self, value):
        if self.is_empty():
            self.push_queue.append(value)
        # elif len(self.push_queue) == 0 and len(self.pop_queue) != 0:
        #     self.push_queue.append(value)
        else:
            while len(self.push_queue) != 0:
                self.pop_queue.append(self.push_queue.pop(0))
            self.push_queue.append(value)
        return self

    def get(self):
        if self.is_empty():
            return None
        elif len(self.push_queue) == 0 and len(self.pop_queue) != 0:
            while len(self.pop_queue) != 0:
                self.push_queue.append(self.pop_queue.pop(0))
            while len(self.push_queue) != 1:
                self.pop_queue.append(self.push_queue.pop(0))
            return self.push_queue.pop(0)
        else:
            return self.push_queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        elif len(self.push_queue) == 0 and len(self.pop_queue) != 0:
            while len(self.pop_queue) != 0:
                self.push_queue.append(self.pop_queue.pop(0))
            while len(self.push_queue) != 1:
                self.pop_queue.append(self.push_queue.pop(0))
            return self.push_queue[0]
        else:
            return self.push_queue[0]

    def is_empty(self):
        return len(self.push_queue) == 0 and len(self.pop_queue) == 0
