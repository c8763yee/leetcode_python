class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = int(s[0] != ' ')
        for i in range(1, len(s)):
            if s[i] != ' ':
                if s[i-1] == ' ':
                    length = 1
                else:
                    length += 1

        return max(length, 1)