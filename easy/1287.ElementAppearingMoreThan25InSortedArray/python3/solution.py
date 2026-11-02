from collections import defaultdict

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        l = len(arr)
        for i in arr:
            counter[i] += 1
            if counter[i] / l > 0.25:
                return i

        return 0

