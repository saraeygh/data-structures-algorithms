"""Implement Tries in python

Implemented methods for trie:
    insert: Insert the given value into max heap.
    contains: Return True if tree contains given word, otherwise False.
    recursive_contains: Same as "contains" method but implemented recursively.
    pre_order_traverse: Traverse tree as pre-order (Parent -> children).
    post_order_traverse: Traverse tree as post-order (children -> Parent).
    remove: Remove given word from tree if exists.
    found_words: Get a prefix and return list of words starts with that prefix.
    longest_common_prefix: Get a list of words and return longest common prefix of that words.
"""


class TrieNode:
    def __init__(self, letter: str) -> None:
        self.letter: str = letter
        self.children: dict = {}
        self.is_end_of_word: bool = False

    def has_child(self, letter):
        return self.children.get(letter) is not None

    def add_child(self, letter):
        self.children[letter] = TrieNode(letter=letter)

    def get_child(self, letter):
        return self.children.get(letter)

    def get_children(self):
        return self.children.values()

    def has_children(self):
        return self.children

    def remove_child(self, letter):
        del self.children[letter]


class Trie:
    def __init__(self):
        self.root = TrieNode(letter=" ")
        self.__word_count = 0

    @property
    def total_words(self):
        return self.__word_count

    def insert(self, word: str):

        current_node = self.root
        for letter in word:
            if not current_node.has_child(letter):
                current_node.add_child(letter)
            current_node = current_node.get_child(letter)

        current_node.is_end_of_word = True
        self.__word_count += 1

    def contains(self, word: str):

        if not isinstance(word, str):
            return False

        current_node = self.root
        for letter in word:
            current_node = current_node.get_child(letter)
            if not current_node:
                return False

        return current_node.is_end_of_word

    def __recursive_contains(self, node: TrieNode, word: str, index):
        if index == len(word):
            return node.is_end_of_word

        letter = word[index]
        child = node.get_child(letter)

        if child is None:
            return node.is_end_of_word

        return self.__recursive_contains(child, word, index + 1)

    def recursive_contains(self, word: str):
        if not isinstance(word, str):
            return False

        return self.__recursive_contains(self.root, word, 0)

    def __pre_order_traverse(self, node: TrieNode):
        print(node.letter)
        for child in node.get_children():
            self.__pre_order_traverse(child)

    def pre_order_traverse(self):
        self.__pre_order_traverse(self.root)

    def __post_order_traverse(self, node: TrieNode):
        for child in node.get_children():
            self.__post_order_traverse(child)
        print(node.letter)

    def post_order_traverse(self):
        self.__post_order_traverse(self.root)

    def __remove(self, node: TrieNode, word: str, index: int):
        if index == len(word):
            node.is_end_of_word = False
            self.__word_count -= 1
            return

        letter = word[index]
        child = node.get_child(letter)

        if child is None:
            return
        elif child.is_end_of_word and not child.has_children():
            node.remove_child(letter)

        self.__remove(child, word, index + 1)

    def remove(self, word: str):
        if not isinstance(word, str):
            return

        if self.contains(word):
            self.__remove(self.root, word, 0)
        else:
            return

    def __last_node_of(self, prefix: str):

        if not isinstance(prefix, str):
            return False

        current_node = self.root
        for letter in prefix:
            current_node = current_node.get_child(letter)
            if not current_node:
                return False

        return current_node

    def __find_words(self, node: TrieNode, prefix: str, words: list):
        if prefix is None:
            return None

        if not node:
            return

        if node.is_end_of_word:
            words.append(prefix)

        for child in node.get_children():
            self.__find_words(child, prefix + child.letter, words)

    def found_words(self, prefix: str):
        words = []
        last_node = self.__last_node_of(prefix)

        self.__find_words(last_node, prefix, words)

        return words

    @staticmethod
    def longest_common_prefix(word_list: str):
        new_trie = Trie()
        for word in word_list:
            new_trie.insert(word=word)

        current_node = new_trie.root
        longest_prefix = ""
        while True:
            children = list(current_node.get_children())
            if current_node.has_children() and len(children) == 1:
                child: TrieNode = children[0]
                new_letter = child.letter
                longest_prefix += new_letter
                if child.is_end_of_word:
                    break
                current_node = child
            else:
                break

        return longest_prefix
