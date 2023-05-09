class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while True:
            mid = (l + r)//2
            squ = mid * mid
            if squ <= x:
                if x < (mid+1) * (mid+1):
                    return mid
                l = mid + 1
            else:
                r = mid - 1
