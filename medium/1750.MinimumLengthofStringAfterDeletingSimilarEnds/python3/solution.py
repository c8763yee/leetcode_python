class Solution:
    def minimumLength(self, s: str) -> int:
        size = len(s)
        left = 0
        right = size - 1

        while left < right:
            if s[left] != s[right]:
                return right - left + 1
            
            prefix_first = s[left]
            while True:
                left += 1
                if s[left] != prefix_first:
                    break
                elif left == right:
                    return 0

            while True:
                right -= 1
                if s[right] != prefix_first or left == right:
                    break
                elif left == right:
                    return 0
        
        return int(left == right)