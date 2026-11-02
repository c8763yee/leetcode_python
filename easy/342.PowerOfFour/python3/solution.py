class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # Check if n is a power of 2 and the number of trailing zeros is even
        return (n & (n - 1)) == 0 and (n - 1) % 3 == 0

