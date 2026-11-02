from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True


        size = len(words)
        c = Counter()
        for i in words:
           c += Counter(i)

        for k, v in c.items():
            if v%size:
                return False

        return True 