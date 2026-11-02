class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        setnum = set(nums)
        ow = len(nums[0])
        for i in range(2**ow):
            if f'{i:0{ow}b}' not in setnum:
                return f'{i:0{ow}b}'