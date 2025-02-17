# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hmap = {}
        def serialize(node, path):
            if not node:
                return "#"
            path = ",".join([str(node.val), serialize(node.left, path), serialize(node.right, path)])
            hmap[path] = hmap.get(path, 0) + 1
            if hmap[path] == 2:
                res.append(node)
            return path
        res = []
        path = serialize(root, "")
        return res