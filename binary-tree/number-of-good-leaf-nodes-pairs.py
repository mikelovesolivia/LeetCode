# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return Counter()
            if not node.left and not node.right:
                return Counter({1: 1})
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.res += left[l] * right[r]
            cnt = Counter()
            for l in left:
                cnt[l+1] += left[l]
            for r in right:
                cnt[r+1] += right[r]
            return cnt
        dfs(root)
        return self.res