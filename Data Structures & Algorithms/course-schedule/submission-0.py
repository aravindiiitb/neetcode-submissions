def dfs(preReqMap, c, visiting):
    if c in visiting:
        return True # cycle detected
    
    if preReqMap[c] == []:
        return False # no pre reqs , safe

    visiting.add(c)

    for course in preReqMap[c]:
        if dfs(preReqMap, course, visiting):
            return True
    
    visiting.remove(c)
    return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReqMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            preReqMap[a].append(b)

        visiting = set()
        for i in range(numCourses):
            if dfs(preReqMap, i, visiting):
                return False
        
        return True

        