class Solution:
    def mostPoints(self, questions):
        size = len(questions)
        solved = [0] * size 
        def solve(idx=0):
            if idx >= size:
                return 0
            if solved[idx]:
                return solved[idx]
            solved[idx] = max(
                questions[idx][0] +solve(idx+questions[idx][1]+1),
                solve(idx+1)
            )
            return solved[idx]
        return solve()
