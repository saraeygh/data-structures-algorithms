"""Stack using list

Implemented methods for Stack with one list:
    min: Return min value in stack, None if stack is empty.
    put: Push in stack.
    get: Pop from stack.
    peek: Pop from stack (keeping value in stack).
    str_reverse: Reverse input string.
    is_balanced_expression: Check if opening and ending symbols match.
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.min_value = None

    def minimum(self):
        return self.min_value

    def is_empty(self):
        return len(self.stack) == 0

    def put(self, value):
        self.stack.append(value)

        self.size += 1
        self.min_value = min(self.stack)
        return self

    def get(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")

        value = self.stack.pop()
        if self.is_empty():
            self.min_value = None
        else:
            self.min_value = min(self.stack)
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack[-1]

    def str_reverser(self, input_str: str) -> str:
        if not isinstance(input_str, str):
            raise ValueError("Not a string.")

        for letter in input_str:
            self.put(letter)

        rev_input_str = ""
        for _ in range(len(self.stack)):
            rev_input_str += self.get()

        return rev_input_str

    def is_balanced_expression(self, expression: str) -> bool:
        OPENINGS = ["(", "[", "{", "<"]

        ENDINGS = [")", "]", "}", ">"]

        def is_opening(char):
            return char in OPENINGS

        def is_ending(char):
            return char in ENDINGS

        def match(poped_char, char):
            return OPENINGS.index(poped_char) == ENDINGS.index(char)

        if not isinstance(expression, str):
            raise ValueError("Not a string.")

        for char in expression:
            if is_opening(char):
                self.put(char)
            elif is_ending(char):
                if self.is_empty() or not match(self.get(), char):
                    return False

        return len(self.stack) == 0
