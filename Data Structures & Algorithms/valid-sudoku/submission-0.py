class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            x_row = [x for x in row if x != '.']
            if len(list(set(x_row))) != len(x_row):
                return False
        for i in range(9):
            x_col = [row[i] for row in board if row[i] != '.']
            if len(list(set(x_col))) != len(x_col):
                return False
        for i in range(3):
            for j in range(3):
                x_square = [board[r][c] for r in range(3*i, 3*i+3) for c in range(3*j, 3*j+3) if board[r][c] != '.']
                if len(list(set(x_square))) != len(x_square):
                    return False
        return True