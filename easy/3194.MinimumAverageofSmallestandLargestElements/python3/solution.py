class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        new_arr = set()
        nums.sort()
        nums = deque(nums)
        while nums:
            min_, max_ = nums.popleft(), nums.pop()
            new_arr.add((min_+max_)/2)
        
        return min(new_arr)
