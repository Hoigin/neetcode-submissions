# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        point1, point2 = l1, l2
        current = head = ListNode()
        carry = 0
        while True:
            val = (point1.val if point1 else 0) + (point2.val if point2 else 0) + carry
            carry = val // 10
            current.val = val % 10
            if point1:
                point1 = point1.next
            if point2:
                point2 = point2.next
            if point1 or point2 or carry:
                current.next = ListNode()
                current = current.next
            else:
                break
        return head