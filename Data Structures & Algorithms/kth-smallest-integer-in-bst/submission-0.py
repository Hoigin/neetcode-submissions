# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []
        def dfs(curr, l):
            if not curr:
                return
            l.append(curr.val)
            dfs(curr.left, l)
            dfs(curr.right, l)
            return
        dfs(root, self.l)
        self.l.sort()
        print(self.l)
        return self.l[k-1]