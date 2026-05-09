def dfs(preReqMap, c, visiting, visited, res):
    if c in visiting:
        return True
    
    if c in visited:
        return False
    
    visiting.add(c)

    for pre in preReqMap[c]:
        if dfs(preReqMap, pre, visiting, visited, res):
            return True

    visiting.remove(c)
    visited.add(c)
    res.append(c)
    return False
    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqMap = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            preReqMap[a].append(b)
        
        res = []
        visiting = set()
        visited = set()
        for i in range(numCourses):
            if dfs(preReqMap, i, visiting, visited, res):
                return []
        
        return res
