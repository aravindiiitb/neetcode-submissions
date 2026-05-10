# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, diameter):
    if not root:
        return 0
    
    left = dfs(root.left, diameter)
    right = dfs(root.right, diameter)
    
    diameter[0] = max(diameter[0], left+right)

    return 1 + max(left, right)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        diameter = [0]
        dfs(root, diameter)
        return diameter[0]

        