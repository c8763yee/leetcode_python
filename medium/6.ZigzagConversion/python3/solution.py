class Solution:
    def convert(self, s: str, rows: int) -> str:
        n = len(s)
        if n <= 1 or rows == 1:
            return s
        # define numColumn
    

        dp = ["" for _ in range(rows)]
        row = 0
        for c in s:
            dp[row] += c
            
            if row == rows-1:
                diff = -1
            elif row == 0:
                diff = 1
            row += diff

        return "".join(dp)

        
