# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l,r = root,root
        self.helper(root)
        return root
        
    def helper(self,root):
        if root is None:
            return 
        temp = TreeNode
        temp = root.left
        root.left = root.right
        root.right = temp
        l = self.helper(root.left)
        r = self.helper(root.right)
        
        