class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        prod = 1
        while n:
            m=n%10
            sum_ += m
            prod *= m
            n//=10
            
        return prod - sum_