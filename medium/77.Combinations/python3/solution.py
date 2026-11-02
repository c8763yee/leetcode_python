class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        comb = []
        def c(prev=0, num=0):
            if num==k:
                comb.append(curr.copy())
                return
            
            for i in range(prev, n):
                curr.append(i+1)
                c(i+1, num+1)
                curr.pop()
            return comb
        return c()
        

                