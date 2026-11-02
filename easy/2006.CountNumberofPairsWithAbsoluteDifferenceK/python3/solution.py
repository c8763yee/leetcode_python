class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=0
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if abs(nums[i]-nums[j]) == k:
                    n += 1
        return n