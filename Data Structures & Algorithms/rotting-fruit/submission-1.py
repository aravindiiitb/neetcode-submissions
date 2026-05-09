class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        freshFruits = 0

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshFruits += 1
        
        if freshFruits == 0:
            return 0

        mins = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            nxtQueue = deque()
            while q:
                qX, qY = q.popleft()
                for dx ,dy in directions:
                    newX, newY = qX + dx, qY +dy
                    if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        nxtQueue.append((newX, newY))
                        freshFruits -= 1
            q = nxtQueue
            mins += 1

        if freshFruits == 0:
            return mins - 1
        
        return -1
