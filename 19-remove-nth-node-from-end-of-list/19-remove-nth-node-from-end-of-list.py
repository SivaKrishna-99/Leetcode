# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         x = head
#         y = head
#         count = 0
#         if head == None:
#             return None
        
#         #Calculate the length
#         while x != None:
#             count += 1
#             x = x.next
            
#         if count == 1:
#             return head.next
#         i = 1
#         prev = head
#         while i <= count-n+1:
#             if i == count-n+1:
#                 #delete operation
#                 prev.next = prev.next.next
                
#             else:
#                 if i == count-n:
#                     prev = y
#                 y = y.next
#             i += 1
#         return head
        p1, p2 = head, head
        for _ in range(n):
            p2 = p2.next
        if not p2:
            return head.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
        