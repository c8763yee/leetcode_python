class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k

        n = numOnes
        k -= numOnes
        if numZeros >= k:
            return n
        
        k -= numZeros
        return n - min(numNegOnes, k)
