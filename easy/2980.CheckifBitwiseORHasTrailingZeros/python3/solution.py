class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even_nums = list(filter(lambda x: x&1 == 0, nums))
        if even_nums == []:
            return False
        
        return len(even_nums) > 1