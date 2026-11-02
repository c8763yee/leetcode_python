class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        # loop and insert (c in word) into trie
        for c in word:
            # if c is not next character then insert c into trie
            if c not in node.children:
                node.children[c] = TrieNode()
            # move to next node
            node = node.children[c]
        # set last node as end of word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            # c not in word
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        prefix = ''
        node = trie.root
        while node and node.is_end is False and len(node.children) == 1:
            prefix += next(iter(node.children.keys()))
            node = node.children[prefix[-1]]

        return prefix
