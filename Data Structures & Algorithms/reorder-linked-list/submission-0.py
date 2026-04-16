# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 找中点 (快慢指针)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 此时 slow 指向前半段的最后一个节点
        # 2. 反转后半段
        second_half = slow.next
        slow.next = None  # 【关键】断开前后两段的连接，防止成环
        prev = None
        curr = second_half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        # 反转后，prev 指向后半段的头节点
        second_head = prev

        # 3. 合并两段链表
        first = head
        second = second_head
        
        while second:
            # 保存下一步的指针，防止丢失
            temp1 = first.next
            temp2 = second.next
            
            # 交叉连接
            first.next = second
            second.next = temp1
            
            # 移动指针
            first = temp1
            second = temp2