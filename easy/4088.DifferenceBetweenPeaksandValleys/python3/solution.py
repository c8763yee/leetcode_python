class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak = 0
        valleys = 0
        for i in range(1, len(nums)-1):
            left = i-1
            right = i+1
            if nums[i] > max(nums[left], nums[right]): 
                peak += nums[i]
            if nums[i] < min(nums[left], nums[right]): 
                valleys += nums[i]
        print(peak, valleys)
        return peak - valleys