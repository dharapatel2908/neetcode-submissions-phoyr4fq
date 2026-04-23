# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            previous = None
            current = head
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous
    
        slow = head
        fast = head
        dummy = ListNode()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        previous = None
        current = temp
        while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
        temp = previous   
        current = head
        current2 = temp
        while current2:
            var = current.next
            var2 = current2.next
            current.next = current2
            current2.next = var
            current = var if var else current2
            current2 = var2
            

    
            
        

        