class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.definition = None  # Adicionado para armazenar a definição

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, definition):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.definition = definition

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_end_of_word:
            return node.definition
        return None

def build_trie_from_file(file_path):
    trie = Trie()
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Skip header
        for line in file:
            word, definition = line.strip().split(';')
            trie.insert(word.lower(), definition)
    return trie

fileName = "second_output.csv"
word = "Love"

trie = build_trie_from_file(fileName)

definition = trie.search(word)
if definition:
    print(f'A definição da palavra "{word}" é: {definition}')
else:
    print(f'A palavra "{word}" não está na trie.')
