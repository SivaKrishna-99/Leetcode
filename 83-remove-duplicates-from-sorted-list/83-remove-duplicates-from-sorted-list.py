# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        curr = head
        prev = None 
        while curr.next :
            
            if curr.val == curr.next.val:
                
                curr.next = curr.next.next
            
            else:
                prev = curr
                curr = curr.next
        return head
            
        