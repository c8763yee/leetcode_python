class Solution:
    def clumsy(self, n: int) -> int:
        init = [1, 2, 6, 7]
        if n <= 4:
            return init[n-1]
        match n%4:
            case 0:
                return n+1
            case 1|2:
                return n+2

        return n-1