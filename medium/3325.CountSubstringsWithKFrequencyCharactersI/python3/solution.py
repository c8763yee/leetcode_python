class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        total = 0
        for i in range(len(s)):
            result = {}
            count = 0
            for j in range(i, len(s)):
                result[s[j]] = result.get(s[j], 0) + 1
                if result[s[j]] >= k:
                    count = 1
                
                total += count

        return total
                