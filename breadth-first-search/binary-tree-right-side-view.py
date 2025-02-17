# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [(root, 0)]
        prev_level = 0
        prev_val = 0
        res = []
        while queue:
            node, level = queue.pop(0)
            if level > prev_level:
                prev_level = level
                res.append(prev_val)
            prev_val = node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        res.append(node.val)
        return res