# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, anc_max, anc_min, max_diff):
            if not node:
                return max_diff
            max_diff = max(abs(node.val - anc_max), abs(node.val - anc_min), max_diff)
            anc_max = max(anc_max, node.val)
            anc_min = min(anc_min, node.val)
            max_diff = max(dfs(node.left, anc_max, anc_min, max_diff), max_diff)
            max_diff = max(dfs(node.right, anc_max, anc_min, max_diff), max_diff)
            return max_diff
        return dfs(root, root.val, root.val, 0)