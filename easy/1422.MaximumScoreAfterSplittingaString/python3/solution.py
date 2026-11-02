class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        max_val = 0

        prefix = [0 for _ in s]
        
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            ones += (c == '1')
            prefix[i] = ones

        for i in range(len(s) - 1):
            c = s[i]
            zeros += (c == '0')
            max_val = max(max_val, prefix[i+1]+zeros)
        
        return max_val