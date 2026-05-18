class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        count = 0
        ptr = head
        while ptr and count< k:
            ptr = ptr.next
            count+=1
        if count< k:
            return head
        
        prev = None
        curr = head
        next_node = None
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverseKGroup(curr, k)
        return prev