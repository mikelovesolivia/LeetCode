# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return False
            left_contains_one = dfs(node.left)
            right_contains_one = dfs(node.right)
            if not left_contains_one:
                node.left = None
            if not right_contains_one:
                node.right = None
            return node.val != 0 or left_contains_one or right_contains_one
        dfs(root)
        if root.left or root.right or root.val != 0:
            return root
        return None