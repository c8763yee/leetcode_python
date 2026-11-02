class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            left = nums[l]
            right = nums[r]
            if left % 2 != right % 2 and left % 2:
                nums[l], nums[r] = right, left

            if left % 2 == 0:
                l += 1

            if right % 2:
                r -= 1
        return nums