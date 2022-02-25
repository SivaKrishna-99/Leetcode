# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.inorderHelper(root,out)
        return out
    
    def inorderHelper(self,root,out):
        if root:
            self.inorderHelper(root.left,out)
            out.append(root.val)
            self.inorderHelper(root.right,out)
        
        
    

        