def dfs(heights, x, y, waterSet, rows, cols):
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]

    for dx, dy in directions:
        newX, newY = x + dx, y + dy
        if 0 <= newX < rows and 0<= newY < cols and heights[newX][newY] >= heights[x][y] and (newX, newY) not in waterSet: 
            waterSet.add((newX, newY))
            dfs(heights, newX, newY, waterSet, rows, cols)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        pacificSet = set()
        atlanticSet = set()


        for c in range(cols):
            pacificSet.add((0,c))
            dfs(heights, 0, c, pacificSet, rows, cols)

            atlanticSet.add((rows-1,c))
            dfs(heights, rows -1, c, atlanticSet, rows, cols)
        
        for r in range(rows):
            pacificSet.add((r,0))
            dfs(heights, r, 0, pacificSet, rows, cols)

            atlanticSet.add((r, cols - 1))
            dfs(heights, r, cols -1, atlanticSet, rows, cols)
        
        return [[i, j] for i, j in pacificSet & atlanticSet]
