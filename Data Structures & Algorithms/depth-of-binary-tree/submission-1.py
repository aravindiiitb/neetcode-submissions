# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # q = deque([root])

        # height = 1
        # while q:
        #     currNode = q.popleft()
        #     if currNode.left:
        #         q.append(currNode.left)                
        #     if currNode.right:
        #         q.append(currNode.right)
            
        #     height += 1
        
        # return height
