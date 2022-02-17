# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_node = head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        i = 0
        if head.next == None:
            return 
        if count == 2:
            head.next = None
            return head
        curr_node = head
        while i < (count//2)-1:
            curr_node = curr_node.next
            i += 1
            
        curr_node.next = curr_node.next.next
        return head