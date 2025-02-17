# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node, parent, low, high):
            if not node:
                return 
            if node.val < low:
                parent.left = node.right
            if node.val > high:
                parent.right = node.left
            dfs(node.left, node, low, high)
            dfs(node.right, node, low, high)
            return 
        dummy_root = TreeNode(val=float('inf'), left=root)
        dfs(root, dummy_root, low, high)
        return dummy_root.left