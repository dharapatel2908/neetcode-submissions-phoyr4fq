# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # None -> 1 -> 2 -> 4 -> None
        #         |
        # None -> 1 -> 3 -> 5- > None
        #         | 
        # result= [1 -> 1 - >2 -> 3-> 4 - > 5]
                    
        result = ListNode()
        result_pt = result
        pointer2 = list2
        pointer1 = list1

        while list1 and list2:
            if list1.val < list2.val:
                result_pt.next = list1
                list1 =list1.next
                
            # elif list2.val < list1.val:
            else:
                result_pt.next = list2
                list2 = list2.next
            result_pt = result_pt.next
        if list1:
            result_pt.next = list1
        else:
            result_pt.next = list2
        return result.next






        