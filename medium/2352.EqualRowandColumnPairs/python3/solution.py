def hash(x):
    return (x * 0x61C88647) & 0xffffffff
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        s = {}
        for i in range(m):
            val = 0
            for j in range(n):
                val = hash(val + grid[i][j])
            s[val] = s.get(val, 0)+1

        for i in range(n):
            val = 0
            for j in range(m):
                val = hash(val + grid[j][i])
            count += s.get(val, 0)
        
        return count
            