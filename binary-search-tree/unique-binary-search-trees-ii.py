# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left = generate(start, i-1)
                right = generate(i+1, end)

                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)
            
            return res
        return generate(1, n)