# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def judge(curr):
            if not curr:
                return 0
            leftHeight = rightHeight = 0
            if curr.left:
                leftHeight += judge(curr.left)
            if curr.right:
                rightHeight += judge(curr.right)
            if abs(leftHeight-rightHeight) > 1:
                self.isBalanced = False
            return max(leftHeight, rightHeight)+1
        judge(root)
        return self.isBalanced
    