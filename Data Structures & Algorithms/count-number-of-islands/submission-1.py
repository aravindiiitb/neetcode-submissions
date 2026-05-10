def dfs(grid, x, y, visited):
    visited[x][y] = True

    directions = [[1,0], [0,1], [-1,0], [0,-1]]

    for dx, dy in directions:
        newX, newY = x + dx , y + dy
        if 0<=newX<len(grid) and 0<=newY<len(grid[0]) and grid[newX][newY] == '1' and not visited[newX][newY]:
            dfs(grid, newX, newY, visited)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[False]*len(grid[0]) for i in range(len(grid))]
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    dfs(grid, i , j, visited)
                    islands += 1
        
        return islands

