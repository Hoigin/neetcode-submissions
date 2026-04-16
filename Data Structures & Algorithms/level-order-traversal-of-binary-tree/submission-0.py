# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []
        q = Queue()
        q.put(root)
        while True:
            level = []
            temp = Queue()
            while not q.empty():
                node = q.get()
                if node.left:
                    temp.put(node.left)
                if node.right:
                    temp.put(node.right)
                level.append(node.val)
            q = temp
            if level:
                result.append(level)
            else:
                break
        return result
