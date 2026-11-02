class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        s = ''
        table = '0123456789abcdef'
        if num < 0:
            num = 2**32+num
        while num:
            s += table[num%16]
            num //= 16
        return s[::-1]