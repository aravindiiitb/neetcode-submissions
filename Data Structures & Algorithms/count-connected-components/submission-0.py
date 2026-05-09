def dfs(nodeNeighborsMap, x, visited):
    visited[x] = True

    for nei in nodeNeighborsMap[x]:
        if not visited[nei]:
            dfs(nodeNeighborsMap, nei, visited)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeNeighborsMap = {i : [] for i in range(n)}

        for a, b in edges:
            nodeNeighborsMap[a].append(b)
            nodeNeighborsMap[b].append(a)
        
        visited = [False]*n

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(nodeNeighborsMap, i, visited)
                count += 1
        
        return count

        