# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node, low, high):
            if not node:
                return node 
            if node.val < low:
                return dfs(node.right, low, high)
            if node.val > high:
                return dfs(node.left, low, high)
            node.left = dfs(node.left, low, high)
            node.right = dfs(node.right, low, high)
            return node
        return dfs(root, low, high)
        