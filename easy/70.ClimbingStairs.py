class Solution:
    def climbStairs(self, n):
        """this problem is similar to tribonacci sequence

        Args:
            n (_type_): _description_

        Returns:
            _type_: _description_
        """
        if n <= 3:
            return n
        a, b, c = 1, 2, 3
        for _ in range(4, n+1):
            a = b
            b = c
            c += a
        return c
