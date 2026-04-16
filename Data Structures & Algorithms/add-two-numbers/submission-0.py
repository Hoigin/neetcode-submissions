# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        point1, point2 = l1, l2
        val1 = val2 = 0
        i = j = 1
        while point1:
            val1 = val1 + point1.val * i
            i *= 10
            point1 = point1.next
        while point2:
            val2 = val2 + point2.val * j
            j *= 10
            point2 = point2.next
        val = val1 + val2
        current = head = ListNode()
        while True:
            res = val % 10
            val = val // 10
            current.val = res
            if val != 0:
                current.next = ListNode()
                current = current.next
            else:
                break
        return head