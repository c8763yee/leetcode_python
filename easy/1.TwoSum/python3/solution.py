class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Think out loud as you go!
        hash = {} # k: e; value = i
        for i, e in enumerate(nums): # 
            if e in hash:
                return [i, hash[e]]
            
            hash[target - e] = i
        
        return [-1, -1]
