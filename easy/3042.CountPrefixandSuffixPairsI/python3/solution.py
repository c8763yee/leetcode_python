def isPrefixAndSuffix(word, pattern):
    return word.startswith(pattern) and word.endswith(pattern)

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        size = len(words)
        count = 0
        for i in range(size):
            for j in range(i+1, size):
                count += isPrefixAndSuffix(words[j], words[i])
        return count