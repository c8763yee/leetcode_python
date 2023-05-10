class Solution:
    def reverse(self, x):
        def checkWhateverflow(x, a, method=0):
            # method: 0:+, 1: *
            return (
                method == 0 and (
                x > 0 and a > 2147483647-x
                or x < 0 and a < -2147483648+x)
            ) or (
                method == 1 and(
                a > 2147483647//x
                or a < -2147483648//x)
            )
        val = 0
        sign = -1 if x < 0 else 1
        tmp = abs(x)
        while tmp:
            mod = tmp % 10
            if val and checkWhateverflow(val, 10, method=1) or checkWhateverflow(val*10, mod):
                return 0
            val  = val * 10 + tmp%10
            tmp //= 10
        return val * sign
