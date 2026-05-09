class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        INF = 2147483647

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        count = 0
        while q:
            nextQueue = deque()            
            while q:
                x, y = q.popleft()               
                for dx, dy in directions:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == INF:
                        grid[newX][newY] = count + 1
                        nextQueue.append((newX, newY))                                                                
            q = nextQueue
            count += 1
