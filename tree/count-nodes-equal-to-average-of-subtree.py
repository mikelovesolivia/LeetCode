# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def calcAvg(node):
            if not node:
                return 0, 0
            left_avg, left_count = calcAvg(node.left)
            right_avg, right_count = calcAvg(node.right)
            sum_ = left_avg * left_count + right_avg * right_count + node.val
            count = left_count + right_count + 1
            avg = sum_ / count 
            return avg, count 

        if not root:
            return 0
        count = 0
        if calcAvg(root)[0] == root.val:
            count += 1
        count += self.averageOfSubtree(root.left) + self.averageOfSubtree(root.right)
        return count