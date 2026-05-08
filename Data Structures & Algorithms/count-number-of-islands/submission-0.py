def dfs(grid, x, y, visited):
    visited[x][y] = True

    if x+1 < len(grid) and grid[x+1][y] == '1' and not visited[x+1][y]:
        dfs(grid, x+1, y, visited)
    
    if x-1>=0 and grid[x-1][y] == '1' and not visited[x-1][y]:
        dfs(grid, x-1, y, visited)
    
    if y+1 < len(grid[0]) and grid[x][y+1] == '1' and not visited[x][y+1]:
        dfs(grid, x, y+1, visited)
    
    if y-1 >= 0 and grid[x][y-1] == '1' and not visited[x][y-1]:
        dfs(grid, x, y-1, visited)
        

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

