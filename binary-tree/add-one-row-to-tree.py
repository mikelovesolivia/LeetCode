# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root, right=None)
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if level == depth - 1:
                left = node.left
                right = node.right
                node.left = TreeNode(val=val, left=left, right=None)
                node.right = TreeNode(val=val, left=None, right=right) 

            if level >= depth:
                break
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return root