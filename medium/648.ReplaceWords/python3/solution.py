class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end
    
    def startswith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    
    def clear(self):
        self.root = TrieNode()

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        trie = Trie()
        sentence_list = sentence.split()
        for idx, word in enumerate(sentence_list):
            trie.clear()
            trie.insert(word)
            for i in range(len(word)):
                prefix = word[:i+1]
                if prefix in dictionary:
                    sentence_list[idx] = prefix
                    break
        return ' '.join(sentence_list)
