class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums.sort()
        s = dict.fromkeys(nums, False)
        max_num = 1
        for i in nums:
            num = 1
            while i + 1 in s and s[i+1] is False:
                s[i+1] = True
                i += 1
                num += 1

            max_num = max(num, max_num)
                
        return max_num