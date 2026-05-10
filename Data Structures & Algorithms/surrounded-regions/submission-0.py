def dfs(board, x, y, res, rows, cols):
    res[x][y] = 'O'

    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for dx, dy in directions:
        newX, newY = x + dx, y + dy
        if 0<=newX<rows and 0<=newY<cols and board[newX][newY] == 'O' and res[newX][newY] != 'O':
            res[newX][newY] = 'O'
            dfs(board, newX, newY, res, rows, cols)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        resGrid = [['X']*cols for i in range(rows)]

        for r in range(rows):
            if board[r][0] == 'O':
                resGrid[r][0] = 'O'
                dfs(board, r, 0, resGrid, rows, cols)
            elif board[r][cols-1] == 'O':
                resGrid[r][cols-1] = 'O'
                dfs(board, r, cols - 1, resGrid, rows, cols)
        
        for c in range(cols):
            if board[0][c] == 'O':
                resGrid[0][c] = 'O'
                dfs(board, 0, c, resGrid, rows, cols)
            elif board[rows-1][c] == 'O':
                resGrid[rows-1][c] = 'O'
                dfs(board, rows-1, c, resGrid, rows, cols)
        
        for r in range(rows):
            board[r] = resGrid[r]
        
        
        
        