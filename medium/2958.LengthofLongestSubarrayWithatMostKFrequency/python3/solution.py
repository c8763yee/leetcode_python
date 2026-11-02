class Solution:
    def maxSubarrayLength(self, s: List[int], k: int) -> int:
        left = 0
        size = len(s)
        counter = {s[0]: 1}
        max_size = 1
        for right in range(1, size):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while counter[s[right]] > k and left < right:
                counter[s[left]] -= 1
                left += 1 
            
            max_size = max(max_size, right-left+1)
        return max_size