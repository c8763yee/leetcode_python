class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        num = 0
        
        for pivot in nums:
            num += pivot
        
        # [1,1,2,3,5,12,50]
        # total = 74
        for i in range(-1, -len(nums)-1, -1):
            if num > 2 * nums[i]:
                return num
            num -= nums[i]
        return -1