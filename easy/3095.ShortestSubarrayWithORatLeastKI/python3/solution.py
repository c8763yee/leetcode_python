class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        size = 2 ** 31 - 1
        num = 0
        left = 0
        maps = [0 for _ in range(33)]
        for right, e in enumerate(nums):
            if e >= k:
                return 1
            
            num |= e
            index = 0
            x = nums[right]
            while x:
                maps[index] += (x%2)
                x //= 2
                index += 1
            

            
            while num >= k and left <= right:
                size = min(size, right - left + 1)
                index = 0
                x = nums[left]
                while x:                       
                    maps[index] -= (x%2)
                    if x%2 and maps[index] == 0:
                        num -= 2 ** index
                    x //= 2
                    index += 1
                left += 1
        return size if size != 2 ** 31 - 1 else -1