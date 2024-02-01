class Solution:
    def permute(self, nums):
        dp  = []
        perm = []
        length = len(nums)
        visited = [False] * length
        def dfs(idx, size):
            if idx == size:
                dp.append(perm.copy())
                return
            for i, e in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                perm.append(e)
                dfs(idx+1, size)
                visited[i] = False
                perm.pop()


        dfs(0, length)
        return dp
