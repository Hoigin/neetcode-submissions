# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current_node = head
        last_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = last_node
            last_node = current_node
            current_node = next_node
        return last_node
