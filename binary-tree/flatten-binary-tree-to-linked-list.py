# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def preorder(node):
            if not node:
                return
            stack.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        n = len(stack)
        for i in range(1, n):
            node = stack[i]
            prevnode = stack[i-1]
            prevnode.left = None
            prevnode.right = node
        return