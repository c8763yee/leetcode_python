class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        a = max(s.split('0'),key=len)
        b = max(s.split('1'), key=len)
        return len(a) > len(b)