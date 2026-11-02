class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        max_count = 0
        max_num = max(nums)

        n = len(nums)
        
        for right in range(n):
            print(max_count, left, right)
            max_count += (nums[right] == max_num)
            while (left<=right and max_count >= k):
                max_count -= (nums[left] == max_num)
                left += 1        

            count += left
    
        return count