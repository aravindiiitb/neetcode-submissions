"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        newGraph = {}
        newGraph[node] = Node(node.val)

        q = deque()
        q.append(node)

        while q:
            currentNode = q.popleft()

            for nei in currentNode.neighbors:
                if nei not in newGraph:
                    newGraph[nei] = Node(nei.val)
                    q.append(nei)
                newGraph[currentNode].neighbors.append(newGraph[nei])
        
        return newGraph[node]