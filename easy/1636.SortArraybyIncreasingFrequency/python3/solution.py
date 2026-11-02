class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return [k for k, v in sorted(Counter(nums).items(), key=lambda pair: (pair[1], -pair[0])) for _ in range(v)]
