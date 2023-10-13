class MyStack:
    def __init__(self, stack: list = []):
        self.stack = stack

    def put(self, value):
        self.stack.append(value)
        return self

    def get(self):
        return self.stack.pop()

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
