class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def f(a,b,c,m):
            return (((a ** b) % 10) ** c) % m 
        good = []
        for i, (a,b,c,m) in enumerate(variables):
            if f(a,b,c,m) == target:
                good.append(i)
                
        return good
            