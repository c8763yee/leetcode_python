class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        def perform(length=1, clipboard=1, count=1, copied=False):
            # method:
            # 0: copy
            # 1: paste
            if length >= n:
                return count if length == n else 1001
            if copied:
                return perform(length+clipboard, clipboard, count+1)
            return min(
                perform(length+clipboard, clipboard, count+1),
                perform(length, length, count+1, copied=True)
                )
        return perform()
            