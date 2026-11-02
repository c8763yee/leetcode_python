class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        target = nums[0]
        for i in range(1, len(nums)):
            if nums[i]!=target:
                target = nums[i]
                nums[k] = target
                k+=1
                
        
        return k