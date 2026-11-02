class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        _, maximum_element = next(iter(counter.most_common(1)), (None,None))
        frequency = 0
        for k, v in counter.items():
            if v == maximum_element:
                frequency += v
                
        return frequency