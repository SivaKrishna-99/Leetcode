# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        if (p.val > root.val and q.val > root.val):
            self.lowestCommonAncestor(root.right,p,q)
        elif(p.val < root.val and q.val < root.val):
            self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
            
            
        
     
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            
    
    
    
    