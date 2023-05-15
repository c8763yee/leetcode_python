class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        dp = []
        def dfs(s, idx=0, size=n*2, pate=0):
            if pate < 0:
                return
            if idx == size:
                if pate == 0:
                    dp.append(''.join(temp))
                return

            sign = 1
            for c in s:
                temp.append(c)
                dfs(s, idx+1, size, pate+sign)
                sign *= -1
                temp.pop()
            
        dfs('()')
        return dp
