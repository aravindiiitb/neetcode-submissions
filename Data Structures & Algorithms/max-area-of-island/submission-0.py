def dfs(grid, x, y, visited): 
    visited[x][y] = True

    area = 1

    directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
    for dx, dy in directions:
        newX = x + dx
        newY = y + dy
        if 0 <= newX and newX < len(grid) and 0 <= newY and newY < len(grid[0]) and grid[newX][newY] == 1 and not visited[newX][newY]:
            area += dfs(grid, newX, newY, visited)
    
    return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False]*len(grid[0]) for i in range(len(grid))]

        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:                    
                    maxArea = max(dfs(grid, i, j, visited), maxArea)
        
        return maxArea