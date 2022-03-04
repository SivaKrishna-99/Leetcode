# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    num = float('inf')
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.helper(root,k)
        return self.num
    
    def helper(self,root,k):
        if not root :
            return 
        self.helper(root.left,k)
        self.count = self.count+1
        if self.count == k:
            self.num = root.val
        self.helper(root.right,k)
        
       
            
            