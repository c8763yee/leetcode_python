class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        o = x
        k = 0
        while x:
            k += x% 10
            x //= 10
        
        if o % k == 0:
            return k
    
        return -1