# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of it
        #then len - n = N
        #iterate till N-1
        #update N-1.next to N+1
        pointer1= head
        counter =0
        while pointer1:
            counter +=1
            pointer1 =pointer1.next
        difference = counter - n
        if difference == 0:
            return head.next
        pointer =head
        for _ in range(difference -1):
            pointer = pointer.next
        pointer.next = pointer.next.next
        return head