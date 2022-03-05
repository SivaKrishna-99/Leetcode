# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        self.secondMinimum = float('inf')
        minimum = root.val 
        self.helperdfs(root,minimum)
        
        return self.secondMinimum if self.secondMinimum < float('inf') else -1
        
        
    
    
    
    def helperdfs(self, root,minimum):
        
        if root:
            if minimum < root.val< self.secondMinimum :
                self.secondMinimum = root.val
            elif(root.val == minimum):
                self.helperdfs(root.left,minimum)
                self.helperdfs(root.right,minimum)
        