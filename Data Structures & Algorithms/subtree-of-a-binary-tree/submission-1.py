# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def dfs(root, subRoot):
    if not root:
        return False
    
    left = dfs(root.left, subRoot)
    right = dfs(root.right, subRoot)

    return left or right or isSameTree(root, subRoot)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return dfs(root, subRoot)
        