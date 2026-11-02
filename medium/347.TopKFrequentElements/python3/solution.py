class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return sorted(
            c,
            reverse=True,
            key=c.get 
            )[:k]
