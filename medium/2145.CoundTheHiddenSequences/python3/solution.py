from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = y = x = 0
        for diff in differences:
            cur += diff
            y = max(y, cur)
            x = min(x, cur)
            if (y - x) > (upper - lower):
                return 0

        return (upper - lower + 1) - (y - x)
