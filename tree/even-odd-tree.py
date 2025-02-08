# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 1)]
        prev_val = None
        prev_lv = 0
        while queue:
            node, cur_lv = queue.pop(0)
            if cur_lv == prev_lv:
                if cur_lv % 2 == 1:
                    if not (prev_val > cur_val and cur_val % 2 == 0):
                        return False
                else:
                    if not (prev_val < cur_val and cur_val % 2 == 1):
                        return False
            if cur_lv > prev_lv:
                prev_lv = cur_lv
                if cur_lv % 2 == node.val % 2:
                    return False
            prev_val = node.val
            if node.left:
                queue.append((node.left.val, cur_lv + 1))
            if node.right: 
                queue.append((node.right.val, cur_lv + 1))
        return True