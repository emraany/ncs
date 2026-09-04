# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
#0 1 2 3
        while curr:
            temp = curr.next #save the next so save 1
            curr.next = prev # next flips so next is null
            prev = curr # 
            curr = temp

        return prev
