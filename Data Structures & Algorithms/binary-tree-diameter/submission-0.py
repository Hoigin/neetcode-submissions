# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dia(curr):
            if not curr:
                return 0
            l = dia(curr.left)
            r = dia(curr.right)
            self.diameter = max(self.diameter, l+r)
            return max(l, r)+1
        
        dia(root)
        return self.diameter
