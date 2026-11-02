from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num = {*range(1, n**2 + 1)}
        remain = set()
        miss = twice = 0
        for i in grid:
            for j in i:
                if j in remain:
                    twice = j
                remain.add(j)
                num.discard(j)
        miss = num.pop()
        return twice, miss 