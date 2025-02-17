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
                return 
            if node.left and node.left.val < low:
                node.left = node.left.right
            if node.right and node.right.val > high:
                node.right = node.right.left
            dfs(node.left, low, high)
            dfs(node.right, low, high)
            return 
        dfs(root, low, high)
        return root 