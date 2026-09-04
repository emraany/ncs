# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = node = ListNode()
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summ = x + y + carry
            node.next = ListNode(summ % 10)
            carry = summ // 10
            node = node.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            

        
        return dummy.next