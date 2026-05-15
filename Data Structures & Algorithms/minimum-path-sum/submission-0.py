def minCost(grid, dp, r, c, m, n):
    if r == m - 1 and c == n - 1:
        return grid[r][c]

    if r == m or c == n:
        return float('inf')
        
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = grid[r][c] + min(minCost(grid, dp, r + 1, c, m, n), minCost(grid, dp, r, c+1, m, n))
    
    return dp[r][c]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])

        dp = [[-1]*n for _ in range(m)]

        return minCost(grid, dp, 0, 0, m, n)

        