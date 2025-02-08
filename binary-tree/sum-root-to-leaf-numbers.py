# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node.val)
            if not node.left and not node.right:
                paths.append(res[:])
                return paths
            if node.left:
                dfs(node.left)
                res.pop()
            if node.right:
                dfs(node.right)
                res.pop()
            return paths
        sum_ = 0
        for l in dfs(root):
            sum_ += int("".join(map(str, l)))
        return sum_