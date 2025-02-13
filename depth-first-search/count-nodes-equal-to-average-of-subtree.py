# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def calcSum(node):
            if not node:
                return 0, 0
            left_sum, left_count = calcSum(node.left)
            right_sum, right_count = calcSum(node.right)
            sum_ = left_sum + right_sum + node.val
            count = left_count + right_count + 1
            return sum_, count 

        def dfs(root):
            if not root:
                return 0
            count = 0
            sub_sum, sub_count = calcSum(root)
            avg = sub_sum // sub_count if sub_sum else 0
            if avg == root.val:
                count += 1
            count += dfs(root.left) + dfs(root.right)
            return count
        
        return dfs(root)