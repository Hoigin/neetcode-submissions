# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        self.swapNode(curr)
        return root
    
    def swapNode(self, curr):
        if not curr:
            return
        # temp = curr.left
        curr.left, curr.right = curr.right, curr.left
        # curr.right = temp
        self.swapNode(curr.left)
        self.swapNode(curr.right)
        return
