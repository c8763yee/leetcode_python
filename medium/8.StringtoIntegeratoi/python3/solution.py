class Solution:
    def myAtoi(self, s: str) -> int:
        x = ''.join(re.findall(r'^[\+\-]?\d+', s.strip()))
        if not x:
            return 0
        return min(2147483647,max(-2147483648, int(x)))