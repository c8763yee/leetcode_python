class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(start=1, end=1):
            if end <= start:
                if end == start:
                    return end
                return 1
            return (start*end*factorial(start+1, end-1))
        r = n - 1
        c = m - 1
        return (factorial(r+1, c+r) // factorial(end=c))%(2*10**9+1)

# 8!/(2!6!) = factorial(7, 8)/ factorial(2)