class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def comb(idx=0, target=0):
            if idx == target:
                subsets.append(curr[:])
                return
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                comb(i+1, target)
                curr.pop()
        curr = []
        subsets = []
        for i in range(len(nums)+1):
            comb(target=i)
        return subsets