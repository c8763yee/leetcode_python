class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, m, n, target_index):
            if not ((0 <= i < m) and (0 <= j < n)) or (i, j) in visited:
                return False
            if board[i][j] != word[target_index]:
                return False
            if target_index == len(word) - 1:
                return True
            visited.add((i, j))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if dfs(i+dx, j+dy, m, n, target_index + 1):
                    return True
            visited.remove((i, j))
            return False

        for i, e in enumerate(board):
            for j in range(len(e)):
                if dfs(i, j, len(board), len(board[0]), 0):
                    return True

        return False