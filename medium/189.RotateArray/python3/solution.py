class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        def reverse(i, j):
            if j <0:
                j += len(nums)
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums): 
            k %= len(nums)
        reverse(0, -1)
        reverse(0, k-1)
        reverse(k, -1)