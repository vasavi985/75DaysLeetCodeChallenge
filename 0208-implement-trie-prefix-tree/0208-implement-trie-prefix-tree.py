class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.is_end = False  # marks end of a word


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, string: str):
        node = self.root
        for ch in string:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node