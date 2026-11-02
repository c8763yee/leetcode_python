class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(n!=1.0):
            if n==0.0 or n<1.0 and n>0.0:
                return False
            n/=3
            
        return True