"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        hash_set = {}
        while curr:
            hash_set[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_curr = hash_set[curr]
            new_curr.next = hash_set.get(curr.next)
            new_curr.random = hash_set.get(curr.random)
            curr = curr.next
        return hash_set[head]
