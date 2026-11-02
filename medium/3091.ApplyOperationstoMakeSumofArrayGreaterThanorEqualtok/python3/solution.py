class Solution:
    def minOperations(self, k: int) -> int:
        def g(k, i):
            return i-1 + k // i - (k%i==0)
        
        if k <= 1:
            return 0
        
        i = int(sqrt(k))
        if i*i == k:
            return (i-1)*2
        
        return min(g(k, i), g(k, i+1))

