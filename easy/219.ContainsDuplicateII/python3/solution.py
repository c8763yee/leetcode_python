class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        idx=0
        if length <= 1:
            return False
        dic = {}
        flag = False
        min_ = len(nums)
        while idx<length:
            if nums[idx] in dic:
                flag = True
                min_ = min(min_, abs(dic[nums[idx]]-idx))
            dic[nums[idx]] = idx 
            idx+=1
        
        return min_<=k and flag