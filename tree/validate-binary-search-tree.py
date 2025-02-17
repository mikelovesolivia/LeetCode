# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.left and not node.right:
                if node.left.val < node.val:
                    return node.val, node.left.val, True
                else:
                    return node.left.val, node.val, False
            if node.right and not node.left:
                if node.right.val > node.val:
                    return node.right.val, node.val, True
                else:
                    return node.val, node.right.val, False
            if not node.left and not node.right:
                return node.val, node.val, True
            flag1 = True
            flag2 = True
            left_max, left_min, _ = dfs(node.left)
            if left_max < node.val:
                flag1 = True
            else:
                flag1 = False
            right_max, right_min, _ = dfs(node.right)
            if right_min > node.val:
                flag2 = True
            else:
                flag2 = False
            return right_max, left_min, flag1 and flag2
        return dfs(root)[-1]