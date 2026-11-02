class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        prod = 1
        size = 0
        lens = len(nums)
        for right in range(left, lens):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1

            size += (right - left + 1)
        return size
        
