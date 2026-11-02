class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = list(map(lambda x: x*x, nums))
        nums.sort()
        # print(nums)
        lens = len(nums)
        cnt = 0
        for i, e in enumerate(nums):
            cnt += e*(1 if i >= lens//2 else -1)
        return cnt

        
