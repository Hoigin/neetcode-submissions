# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        curr = root
        return self.searchDepth(curr, depth)
        
    def searchDepth(self, curr, depth):
        if not curr:
            return depth
        depth += 1
        left = self.searchDepth(curr.left, depth)
        right = self.searchDepth(curr.right, depth)
        return max(left, right)