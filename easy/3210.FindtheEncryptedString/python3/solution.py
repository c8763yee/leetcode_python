class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        c = ''
        for i in range(len(s)):
            c += s[(i+k)%len(s)]
        return c
