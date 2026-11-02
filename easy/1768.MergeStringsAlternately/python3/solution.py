class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 = idx2 = 0
        l1 = len(word1)
        l2 = len(word2)
        s = ''
        while idx1 < l1 and idx2 < l2:
            if (idx1+idx2)%2:
                s += word2[idx2]
                idx2 += 1
            else:
                s += word1[idx1]
                idx1 += 1
        return s + word2[idx2:] + word1[idx1:]