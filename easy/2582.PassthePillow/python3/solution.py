class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time <n:
            return time+1
        val = 0
        factor = 1
        for i in range(time+1):
            val += factor
            if val == n:
                factor = -1
            elif val == 1 and factor == -1:
                factor = 1

        return val