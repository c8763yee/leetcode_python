class Solution:
    @lru_cache(maxsize=38)
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return int(n>0)

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)