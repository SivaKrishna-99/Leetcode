# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        t_sum = targetSum
        curr_sum = 0
        self.helper(root,curr_sum,t_sum)
        return self.helper(root,curr_sum,t_sum)
    
    def helper(self,root,curr_sum,t_sum):
        if not root:
            return False
        
        curr_sum += root.val
        if root.left is None and root.right is None:
            return curr_sum == t_sum
        
        return (self.helper(root.left,curr_sum,t_sum) or 
        self.helper(root.right, curr_sum,t_sum))
        
        
    
        