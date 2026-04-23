# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1 = head
        counter =0
        while pointer1:
            counter +=1
            pointer1= pointer1.next
        difference = counter - n
        pointer = head
        if difference == 0:
            return head.next
        for _ in range(difference - 1):
            pointer = pointer.next
        pointer.next = pointer.next.next
        return head
        

