# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        (head, other) = (list1, list2) if list1.val <= list2.val else (list2, list1)
        current = head
        while current:
            temp = current.next
            if temp:
                if temp.val <= other.val:
                    current = temp
                else:
                    current.next = other
                    current = other
                    other = temp
            else:
                current.next = other
                break
        return head
