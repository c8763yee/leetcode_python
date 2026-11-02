class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            sets = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in sets:
                    return False
                sets.add(board[i][j])

        
        for i in range(9):
            sets = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in sets:
                    return False
                sets.add(board[j][i])
        
        for i in range(3):
            for j in range(3):
                sets = set()
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l] == '.':
                            continue
                        if board[i*3+k][j*3+l] in sets:
                            return False
                        sets.add(board[i*3+k][j*3+l])


        return True