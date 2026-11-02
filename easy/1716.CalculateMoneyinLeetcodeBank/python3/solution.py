class Solution:
    def totalMoney(self, n: int) -> int:
        val = 0
        for i in range(n):
            val += (i//7) + i%7 + 1

        return val