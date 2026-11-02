class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True] * n
        arr[:2] = [False] * 2
        i=2
        while i*i <= n:
            if arr[i]:
                for multi in range(i*i, n, i):
                    arr[multi] = False
            i+= 1
        return sum(arr)