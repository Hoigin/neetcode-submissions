# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def find(curr, subRoot):
            if not curr:
                return False
            if curr.val == subRoot.val:
                if isSubTree(curr, subRoot):
                    return True
            return find(curr.left, subRoot) or find(curr.right, subRoot)
        
        def isSubTree(curr, subRoot):
            if not curr and not subRoot:
                return True
            if not curr or not subRoot or curr.val != subRoot.val:
                return False 
            else:
                return isSubTree(curr.left, subRoot.left) and isSubTree(curr.right, subRoot.right)

        return find(root, subRoot)
