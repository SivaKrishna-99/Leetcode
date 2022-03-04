# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        self.helper(root,res)
        for i in range(0,k):
            if i == k-1:
                return res[k-1]
        
    
    def helper(self,root,res):
        
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)
            
            