class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, -2)
            if r < 0:
                n += 1
                r += 2
            nums.append(r)
        nums.reverse()
        return ''.join(map(str, nums))


