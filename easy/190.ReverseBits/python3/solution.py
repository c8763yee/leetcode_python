class Solution:
    def reverseBits(self, n: int) -> int:
        nums = 0
        for _ in range(32):
            nums = (nums << 1) + (n & 1)
            n >>= 1
        return nums

