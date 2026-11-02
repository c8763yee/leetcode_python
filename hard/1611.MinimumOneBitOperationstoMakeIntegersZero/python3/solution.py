class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        this problem is equivalent as Gray to Binary
        """
        if n == 0:
            return 0
        
        mask = n
        while mask:
            mask >>= 1
            n ^= mask
        
        return n