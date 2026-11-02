class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = len(nums)-1
        if l<2:
            return max(nums)
        arr = list(set(nums))
        arr.sort()
        l = len(arr)
        if l <=2:
            return max(arr)
        
        return arr[0] if l==3 else arr[-3]