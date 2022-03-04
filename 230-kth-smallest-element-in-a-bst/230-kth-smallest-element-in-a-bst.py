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
        
        # res = []
        if not root:
            return None
        self.helper(root,k)
        # for i in range(0,k):
        #     if i == k-1:
        #         return res[k-1]
        return self.num
    
    def helper(self,root,k):
        if not root :
            return self.count
        
        self.helper(root.left,k)
        self.count = self.count+1
        if self.count == k:
            self.num = root.val
        # res.append(root.val)
        self.helper(root.right,k)
       
        return self.count
            
            