# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def dfs(l, r, indicesMap, preorder, preIdx):
    if l > r:
        return None
    
    root = TreeNode(preorder[preIdx[0]])
    preIdx[0] += 1
    rootIndex = indicesMap[root.val]

    root.left = dfs(l, rootIndex-1, indicesMap, preorder, preIdx)
    root.right = dfs(rootIndex+1, r, indicesMap, preorder, preIdx)

    return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indicesMap = {val: idx for idx, val in enumerate(inorder)}
        preIdx = [0]
        return dfs(0, len(preorder) - 1, indicesMap, preorder, preIdx)
        