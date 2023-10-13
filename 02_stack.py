"""Stack using list

Implemented methods:
    min: Return min value in stack, None if stack is empty.
    put: Push in stack.
    get: Pop from stack.
    peek: Pop from stack (keeping value in stack).
    str_reverse: Reverse input string.
    is_balanced_expression: Check if opening and ending symbols match.
"""


class MyStack:
    def __init__(self, stack: list = [], min=None):
        self.stack = stack
        self.min = min

    def min_value(self):
        return self.min

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
