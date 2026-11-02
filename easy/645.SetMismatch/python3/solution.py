class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) 
        duplicated, _ = next(iter(counter.most_common(1))) # assume that the duplicated number is most common number
        n = len(nums)
        missing = next(iter(set(range(1, n+1)).difference(set(counter.keys()))))
        return [duplicated, missing]