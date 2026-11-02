class Solution:
    def heightChecker(self, r: List[int]) -> int:
        l = sorted(r)
        k = 0
        for i in range(len(r)):
            if l[i]!=r[i]:
                k+=1
        return k