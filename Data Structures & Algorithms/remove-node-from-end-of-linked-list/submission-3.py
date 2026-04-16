# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head.next is None:
        #     return None
        Nullhead = ListNode(next=head)
        point1 = point2 = Nullhead
        for i in range(n):
            point1 = point1.next
        while point1.next:
            point1 = point1.next
            point2 = point2.next
        if point2.next != head:
            point2.next = point2.next.next
        else:
            head = head.next
        return head