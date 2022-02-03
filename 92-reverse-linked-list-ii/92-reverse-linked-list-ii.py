# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        bstart = ListNode(0,head)
        curr = head
        prev = None
        lprev = bstart
        for i in range(left-1):
            lprev = curr
            curr = curr.next
            
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
            
        lprev.next.next = curr
        lprev.next = prev  
        
        return bstart.next
        