class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 3:
            return num
        s = 0
        while num:
            s += 1
            if num%2:
                num -= 1
                continue
            num //=2
        return s
