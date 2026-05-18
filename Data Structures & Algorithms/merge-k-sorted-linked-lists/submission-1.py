# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergelist(l1, l2): 
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                elif l1.val == l2.val:
                    next_l1 = l1.next  # save first
                    next_l2 = l2.next  # save first
                    tail.next = l1
                    tail = tail.next
                    tail.next = l2
                    l1 = next_l1       # use saved value
                    l2 = next_l2     
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
        
        if len(lists) == 0:
            return None
            
        for i in range(1, len(lists)):
            lists[i] = mergelist(lists[i-1], lists[i]) 
        return lists[-1]