class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if target>nums[right]:
            return right + 1
        if target<nums[left]:
            return 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return left

