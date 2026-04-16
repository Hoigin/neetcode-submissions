# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True

        def judge(cp, cq):
            if (not cp) and (not cq):
                return
            elif cp is None or cq is None:
                self.result = False
                return
            elif cp.val != cq.val:
                self.result = False
                return
            judge(cp.left, cq.left)
            judge(cp.right, cq.right)
            return
        
        judge(p, q)
        return self.result

        