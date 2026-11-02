class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        dp = []
        def dfs(openB=0, closeB=0):
            if openB>n or closeB>n:
                return
            if openB==closeB==n:
                dp.append(''.join(temp))

            if openB < n:
                temp.append('(')
                dfs(openB+1, closeB)
                temp.pop()

            if openB > closeB:
                temp.append(')')
                dfs(openB, closeB+1)
                temp.pop()
        dfs()
        return dp