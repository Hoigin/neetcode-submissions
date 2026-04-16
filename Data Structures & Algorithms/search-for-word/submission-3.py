class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        def dfs(i, r, c):
            if i == n:
                return True
            if r>=ROWS or r<0 or c>=COLS or c<0 or word[i]!=board[r][c] or board[r][c]=="#":
                return False
            board[r][c] = "#"
            res = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)
            board[r][c] = word[i]
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False