class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        for k, v in Counter(nums).items():
            total += (v * (v-1))//2
        return total