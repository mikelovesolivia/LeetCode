# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def calcSum(node):
            if not node:
                return 0, 0
            left_sum, left_count = calcSum(node.left)
            right_sum, right_count = calcSum(node.right)
            sum_ = left_sum + right_sum + node.val
            count = left_count + right_count + 1
            avg = sum_ // count
            if avg == node.val:
                nonlocal ans
                ans += 1
            return sum_, count 
        calcSum(root)
        return ans