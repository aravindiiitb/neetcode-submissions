# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)

        res = []

        while q:
            level = []
            for i in range(len(q)):
                currNode = q.popleft()
                if currNode:
                    level.append(currNode.val)
                    q.append(currNode.left)
                    q.append(currNode.right)
            if level:
                res.append(level[-1])
        
        return res
        