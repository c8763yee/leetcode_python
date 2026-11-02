class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combsum(target, val=0, start=0, size=0):
            if val >= target or start >= size:
                if val == target:
                    dp.append(comb[:])
                return

            for i in range(start, size):
                comb.append(candidates[i])
                combsum(target, val+candidates[i], i, size)
                comb.pop()

        size = len(candidates)
        dp = []
        comb = []
        combsum(target, size=size)
        return dp