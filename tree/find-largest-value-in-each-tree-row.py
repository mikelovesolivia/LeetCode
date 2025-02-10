# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [(root, 0)]
        max_vals = collections.defaultdict(lambda: -1)
        while queue:
            node, level = queue.pop(0)
            max_vals[level] = max(max_vals.get(level, 0), node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return [v for v in dict(sorted(max_vals.items())).values()]
            

        