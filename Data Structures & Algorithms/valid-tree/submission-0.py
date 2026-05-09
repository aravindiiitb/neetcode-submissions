def dfs(nodeNeighborMap, x, parent, visited):
    if x in visited:
        return True
    
    visited.add(x)

    for nei in nodeNeighborMap[x]:
        if nei == parent:
            continue

        if dfs(nodeNeighborMap, nei, x,  visited):
            return True

    return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeNeighborMap = {i: [] for i in range(n)}

        for x , y in edges:
            nodeNeighborMap[x].append(y)
            nodeNeighborMap[y].append(x)
        
        visited = set()
        
        if dfs(nodeNeighborMap, 0, -1, visited):
            return False
        
        return len(visited) == n
