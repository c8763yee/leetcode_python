class Solution:
    def isHappy(self, n: int) -> bool:
        val = 0
        while n:
            val += (n%10)**2
            n//=10
        
        if val - 10 <0:
            return val==1 or val == 7
        return self.isHappy(val)