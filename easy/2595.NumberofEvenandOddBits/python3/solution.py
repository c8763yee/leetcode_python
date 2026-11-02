class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bit = [0,0]
        ptr=0
        while n:
            bit[ptr] += n%2
            ptr = (ptr+1)%2
            n >>=1
        return bit