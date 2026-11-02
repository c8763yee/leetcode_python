class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        size = l = len(nums)
        result = []

        while size != 0:
            sets = set()
            for index in range(l):
                if nums[index] == 0 or nums[index] in sets:
                    continue
                
                sets.add(nums[index])
                nums[index] = 0
                size -= 1

            result.append(sets)

        return result
            
            