class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = set()
        perm = []
        length = len(nums)
        visited = [False] * length
        def dfs(idx, size):
            if idx == size:
                dp.add(tuple(perm))
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