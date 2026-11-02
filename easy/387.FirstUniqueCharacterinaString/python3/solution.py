class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.index(i) for i in set(s) if s.count(i) == 1], default=-1)
        