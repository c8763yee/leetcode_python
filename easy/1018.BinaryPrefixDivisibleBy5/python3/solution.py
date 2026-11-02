class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary = []
        num = 0
        for i in nums:
            num = (num<<1)+i
            binary.append(num%5==0)
        return binary