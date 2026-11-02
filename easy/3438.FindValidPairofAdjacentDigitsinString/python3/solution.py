class Solution:
    def findValidPair(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i in range(len(s) - 1):
            if (
                s[i] != s[i + 1]
                and count[s[i]] + ord("0") == ord(s[i])
                and count[s[i + 1]] + ord("0") == ord(s[i + 1])
            ):
                return s[i:i+2]

        return ""
