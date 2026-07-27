# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #reverse the second half of the linked list
        #then put the pointer of the reversed linked list
        #then add the element into first half of the list atlernatively
    #finding the middle for that we being using slow and fast pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    #once we get the middle, break the second half of the linked list after middle
        temp = slow.next
        slow.next = None
        previous = None
        current = temp
        while current:
            temp = current.next
            current.next = previous
            previous =current
            current= temp
            
        
        first = head
        second = previous
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1,temp2


        