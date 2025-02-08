"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [(root, 0)]
        prev_lv = -1
        prev_node = None
        while queue:
            node, cur_lv = queue.pop(0)
            if cur_lv == prev_lv and prev_node:
                prev_node.next = node
            if node.left:
                queue.append((node.left, cur_lv + 1))
            if node.right:
                queue.append((node.right, cur_lv + 1))
            prev_lv = cur_lv
            prev_node = node
        return root