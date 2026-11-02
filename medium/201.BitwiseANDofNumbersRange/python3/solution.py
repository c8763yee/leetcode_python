class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        power=0
        while (left or right) and left != right:
            left >>= 1
            right >>= 1
            power +=1

        return left << power
