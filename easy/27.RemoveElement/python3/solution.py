class Solution:
    def removeElement(self, nums, val):
        idx = 0
        for e in nums:
            if e != val:
                nums[idx] = e
                idx += 1
        return idx

