class Solution:
    def hammingWeight(self, n: int) -> int:
        if n <= 1:
            return n
        return (n & 1) + self.hammingWeight(n >> 1)