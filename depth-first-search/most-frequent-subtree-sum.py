# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        subtree_sums = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            subsum = node.val
            left_subsum = dfs(node.left)
            right_subsum = dfs(node.right)
            subsum = subsum + left_subsum + right_subsum
            subtree_sums[subsum] += 1
            return subsum
        dfs(root)
        max_ = max(subtree_sums.values())
        return [k for k, v in subtree_sums.items() if v == max_]